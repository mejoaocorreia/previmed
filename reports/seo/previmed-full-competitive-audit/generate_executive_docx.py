from pathlib import Path
from datetime import datetime
from html import escape
import json
import re
import struct
import zipfile

ROOT = Path("reports/seo/previmed-full-competitive-audit")
DATA = ROOT / "data" / "audit-results.json"
OUT = ROOT / "previmed_full_competitive_audit_executive.docx"


def clean(text):
    return re.sub(r"\s+", " ", str(text or "")).strip()


def limit(text, n=180):
    text = clean(text)
    return text if len(text) <= n else text[: n - 1].rstrip() + "..."


def png_size(path):
    with open(path, "rb") as handle:
        sig = handle.read(24)
    if sig[:8] != b"\x89PNG\r\n\x1a\n":
        return 1200, 800
    return struct.unpack(">II", sig[16:24])


class Docx:
    def __init__(self):
        self.body = []
        self.media = []
        self.rel_index = 10
        self.docpr = 1

    def paragraph(self, text="", style=None, bold=False, color=None):
        text = escape(clean(text))
        if not text:
            self.body.append("<w:p/>")
            return
        style_xml = f'<w:pStyle w:val="{style}"/>' if style else ""
        color_xml = f'<w:color w:val="{color}"/>' if color else ""
        bold_xml = "<w:b/>" if bold else ""
        self.body.append(
            f"<w:p><w:pPr>{style_xml}</w:pPr><w:r><w:rPr>{bold_xml}{color_xml}</w:rPr>"
            f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
        )

    def bullet(self, text):
        self.paragraph("• " + clean(text))

    def page_break(self):
        self.body.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def callout(self, title, text, fill="EAF2F8"):
        self.table([[title], [text]], widths=[9000], header=False, fill=fill)

    def table(self, rows, widths=None, header=True, fill="D9EAF7"):
        if not rows:
            return
        cols = max(len(r) for r in rows)
        widths = widths or [int(9000 / cols)] * cols
        xml = ['<w:tbl><w:tblPr><w:tblW w:w="0" w:type="auto"/><w:tblBorders>'
               '<w:top w:val="single" w:sz="4" w:space="0" w:color="B7C9D6"/>'
               '<w:left w:val="single" w:sz="4" w:space="0" w:color="B7C9D6"/>'
               '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="B7C9D6"/>'
               '<w:right w:val="single" w:sz="4" w:space="0" w:color="B7C9D6"/>'
               '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D7E1E8"/>'
               '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="D7E1E8"/>'
               '</w:tblBorders></w:tblPr>']
        for r_idx, row in enumerate(rows):
            xml.append("<w:tr>")
            for c_idx in range(cols):
                text = escape(limit(row[c_idx] if c_idx < len(row) else "", 420))
                shade = f'<w:shd w:fill="{fill}"/>' if header and r_idx == 0 else ""
                bold = "<w:b/>" if header and r_idx == 0 else ""
                width = widths[min(c_idx, len(widths) - 1)]
                xml.append(
                    f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{shade}</w:tcPr>'
                    f"<w:p><w:r><w:rPr>{bold}</w:rPr><w:t>{text}</w:t></w:r></w:p></w:tc>"
                )
            xml.append("</w:tr>")
        xml.append("</w:tbl>")
        self.body.append("".join(xml))

    def image(self, path, caption=None, width_inches=5.8):
        path = Path(path)
        if not path.exists():
            return
        rid = f"rId{self.rel_index}"
        self.rel_index += 1
        media_name = f"image{len(self.media) + 1}.png"
        self.media.append((rid, media_name, path))
        w_px, h_px = png_size(path)
        cx = int(width_inches * 914400)
        cy = int(cx * h_px / max(w_px, 1))
        docpr = self.docpr
        self.docpr += 1
        self.body.append(f"""
<w:p><w:r><w:drawing>
<wp:inline distT="0" distB="0" distL="0" distR="0" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">
<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{docpr}" name="{escape(media_name)}"/>
<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:nvPicPr><pic:cNvPr id="{docpr}" name="{escape(media_name)}"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip r:embed="{rid}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>
""")
        if caption:
            self.paragraph(caption, style="Caption")

    def save(self, path):
        document = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            "<w:body>"
            + "".join(self.body)
            + '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="900" w:right="900" w:bottom="900" w:left="900"/></w:sectPr>'
            "</w:body></w:document>"
        )
        styles = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:b/><w:sz w:val="44"/><w:color w:val="163B57"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:rPr><w:sz w:val="24"/><w:color w:val="5C6F7C"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:rPr><w:b/><w:sz w:val="30"/><w:color w:val="163B57"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:rPr><w:b/><w:sz w:val="24"/><w:color w:val="1F4E79"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:rPr><w:b/><w:sz w:val="20"/><w:color w:val="1F4E79"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Caption"><w:name w:val="Caption"/><w:rPr><w:i/><w:sz w:val="18"/><w:color w:val="666666"/></w:rPr></w:style>
</w:styles>"""
        rels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>']
        docrels = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
        for rid, media_name, _ in self.media:
            docrels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/{media_name}"/>')
        docrels.append("</Relationships>")
        types = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>']
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("[Content_Types].xml", types[0])
            archive.writestr("_rels/.rels", rels[0])
            archive.writestr("word/_rels/document.xml.rels", "".join(docrels))
            archive.writestr("word/document.xml", document)
            archive.writestr("word/styles.xml", styles)
            for _, media_name, media_path in self.media:
                archive.write(media_path, f"word/media/{media_name}")


def issue_counts(pages):
    counts = {"Alto": 0, "Medio": 0, "Baixo": 0}
    for page in pages:
        for issue in page.get("issues", []):
            counts[issue.get("severity")] = counts.get(issue.get("severity"), 0) + 1
    return counts


def page_score(page):
    severity = {"Alto": 3, "Medio": 2, "Baixo": 1}
    return sum(severity.get(i.get("severity"), 0) for i in page.get("issues", []))


def page_label(page):
    title = page.get("title") or "Sem title"
    return f"{limit(title, 55)} — {page.get('finalUrl') or page.get('requestedUrl')}"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    pages = data.get("previmed_pages", [])
    competitors = data.get("competitors", [])
    screenshots = [Path(p) for p in data.get("screenshots", []) if Path(p).exists()]
    counts = issue_counts(pages)
    risky_pages = sorted(pages, key=page_score, reverse=True)[:12]
    service_pages = [p for p in pages if p.get("serviceTerms")]
    thin_pages = [p for p in pages if p.get("wordCount", 0) < 300][:10]

    doc = Docx()
    today = datetime.now().strftime("%d/%m/%Y")

    doc.paragraph("Relatório SEO, UX e Concorrência — Previmed", style="Title")
    doc.paragraph("Análise estratégica do site previmed.pt e concorrência em SST, Medicina no Trabalho e Formação", style="Subtitle")
    doc.paragraph(f"Data: {today}")
    doc.paragraph("Versão: Executive 1.0")
    doc.paragraph("Análise read-only, sem alterações em produção")
    doc.paragraph("Autor: SEO Growth System / Análise assistida")
    doc.callout("Âmbito", f"Baseado na investigação já recolhida: {data.get('previmed_urls_analyzed')} URLs Previmed, {data.get('competitors_discovered')} concorrentes, {data.get('screenshots') and len(data.get('screenshots'))} screenshots Playwright e auditorias intermédias.", "EAF2F8")
    if screenshots:
        doc.image(screenshots[0], "Exemplo de evidência visual recolhida com Playwright.", width_inches=5.6)
    doc.page_break()

    doc.paragraph("Página 1 — Sumário executivo", style="Heading1")
    doc.callout("Leitura rápida", "A Previmed tem uma base institucional importante, mas o site deve comunicar melhor os serviços principais, reforçar páginas comerciais, organizar a arquitetura SEO e tornar a proposta mais clara face à concorrência.", "E2F0D9")
    doc.table([
        ["Tema", "Conclusão executiva"],
        ["Estado geral", f"Base auditável e com várias páginas públicas; foram analisadas {len(pages)} URLs, com {data.get('previmed_ok_urls')} respostas OK/parciais."],
        ["Maior problema", "As páginas de maior valor comercial precisam de estrutura mais clara por serviço, prova validada, CTAs e ligação interna."],
        ["Maior oportunidade", "Transformar serviços principais em páginas fortes: intenção clara, FAQs úteis, conteúdo específico, schema honesto e percurso de contacto."],
        ["Risco principal", "Avançar com alterações de URLs, schema, claims ou páginas locais sem validação técnica/humana."],
        ["Recomendação principal", "Melhorar páginas comerciais prioritárias antes de expandir conteúdos novos."],
        ["Prioridade imediata", "Homepage, Medicina no Trabalho, Segurança no Trabalho, Formação SST, CTAs, titles/metas e internal linking."],
    ], widths=[2200, 6800])
    doc.page_break()

    doc.paragraph("Página 2 — Top 10 ações prioritárias", style="Heading1")
    doc.table([
        ["Prioridade", "Ação", "Tipo", "Impacto", "Esforço", "Risco", "Prazo"],
        [1, "Melhorar homepage como entrada clara para serviços, contacto e confiança.", "Melhorar", "Alto", "Médio", "Baixo", "0-15 dias"],
        [2, "Criar/melhorar página forte para Medicina no Trabalho.", "Criar/Melhorar", "Alto", "Médio", "Médio", "15-30 dias"],
        [3, "Melhorar ou criar página de Segurança no Trabalho/SST.", "Melhorar", "Alto", "Médio", "Médio", "15-30 dias"],
        [4, "Criar cluster de Formação SST se os cursos forem reais e aprovados.", "Criar", "Médio/Alto", "Médio", "Médio", "30-60 dias"],
        [5, "Rever CTAs: contacto, telefone, pedido de proposta e próximo passo.", "Melhorar", "Alto", "Baixo", "Baixo", "0-15 dias"],
        [6, "Rever titles, meta descriptions, H1 e H2 das páginas prioritárias.", "Corrigir", "Médio/Alto", "Baixo", "Baixo", "0-15 dias"],
        [7, "Adicionar FAQs úteis e específicas nas páginas de serviço.", "Melhorar", "Médio", "Baixo/Médio", "Médio", "15-30 dias"],
        [8, "Melhorar internal linking entre serviços, formação, guias e contacto.", "Reestruturar", "Médio/Alto", "Médio", "Médio", "15-30 dias"],
        [9, "Validar schema Organization/Service/FAQ/Breadcrumb com conteúdo visível.", "Validar", "Médio", "Baixo/Médio", "Alto", "30-60 dias"],
        [10, "Definir arquitetura aprovada antes de alterar slugs ou URLs.", "Validar", "Alto", "Médio", "Alto", "0-30 dias"],
    ], widths=[900, 3300, 1100, 1100, 1000, 1000, 1200])
    doc.page_break()

    doc.paragraph("Página 3 — Quick wins", style="Heading1")
    doc.table([
        ["Quick win", "Onde aplicar", "Porquê", "Resultado esperado", "Cuidado"],
        ["Rever titles/metas", "Páginas prioritárias", "Melhora clareza em SERP e intenção.", "Mais relevância e CTR potencial.", "Não inventar claims."],
        ["Clarificar H1", "Páginas com H1 fraco/ausente", "Ajuda utilizador e motores a perceberem o tema.", "Melhor leitura e foco.", "Um H1 principal por página."],
        ["CTAs visíveis", "Homepage e serviços", "Facilita pedido de contacto/proposta.", "Menos fricção comercial.", "Validar telefone/formulários reais."],
        ["FAQs úteis", "Serviços principais", "Responde dúvidas reais e ajuda AI Search.", "Conteúdo mais completo.", "Não inventar legislação."],
        ["Links internos", "Menus, blocos e texto", "Ajuda descoberta de serviços.", "Melhor rastreabilidade.", "Evitar links forçados."],
        ["Prova/confiança", "Páginas comerciais", "Aumenta credibilidade.", "Mais confiança.", "Só usar prova validada."],
        ["Texto do hero", "Homepage/serviços", "Primeiro ecrã deve explicar oferta.", "Mais clareza imediata.", "Não usar frases genéricas."],
        ["Schema básico", "Homepage/serviços/FAQ", "Ajuda entidades e elegibilidade.", "Dados mais estruturados.", "Só com conteúdo visível."],
    ], widths=[1500, 1700, 2300, 1900, 1600])
    doc.page_break()

    doc.paragraph("Página 4 — Problemas críticos e bloqueios", style="Heading1")
    doc.table([
        ["Problema", "Área", "Impacto", "Gravidade", "Como resolver"],
        ["Páginas comerciais sem estrutura suficientemente forte.", "Conteúdo/Conversão", "Menor capacidade de captar intenção de serviço.", "Alto", "Reestruturar páginas prioritárias por serviço, prova, FAQs e CTA."],
        ["Alterações de URL ainda não aprovadas.", "Técnico", "Risco de perda de indexação se forem feitas sem redirects/canonical/sitemap.", "Crítico", "Criar plano URL/redirects e validar antes de qualquer mudança."],
        ["Dados de GSC/GA4 ausentes.", "Dados", "Não permite priorizar por tráfego, CTR ou conversão real.", "Médio", "Dar acesso read-only e cruzar com esta auditoria."],
        ["Claims legais/médicos/certificações a validar.", "Confiança/Compliance", "Risco reputacional e factual.", "Alto", "Criar lista de claims permitidos e fonte de prova."],
        ["Páginas locais sem prova seriam arriscadas.", "Local SEO", "Risco de doorway/thin local pages.", "Alto", "Só criar páginas locais com presença/cobertura real validada."],
        ["Schema não deve ser aplicado sem validação.", "Schema", "Risco de dados estruturados enganadores.", "Médio/Alto", "Mapear conteúdo visível e validar com QA."],
    ], widths=[2600, 1300, 2300, 1000, 2500])
    doc.paragraph(f"Contagem automática na auditoria: {counts.get('Alto', 0)} issues altas, {counts.get('Medio', 0)} médias e {counts.get('Baixo', 0)} baixas nas URLs Previmed.")
    doc.page_break()

    doc.paragraph("Página 5 — Oportunidades de páginas", style="Heading1")
    doc.table([
        ["Ação", "Página / Tema", "URL sugerida", "Intenção", "Prioridade", "Motivo", "Observações"],
        ["Melhorar/Criar", "Medicina no Trabalho", "/servicos/medicina-no-trabalho/ (a validar)", "Comercial", "Alta", "Tema core com intenção de serviço.", "Validar serviço, claims e URL final."],
        ["Melhorar/Criar", "Segurança no Trabalho", "/servicos/seguranca-no-trabalho/ (a validar)", "Comercial", "Alta", "Cluster central de SST.", "Exige conteúdo específico e prova."],
        ["Validar", "Saúde Ocupacional", "/servicos/saude-ocupacional/ (a validar)", "Comercial/Informacional", "Média/Alta", "Pode capturar intenção complementar.", "Evitar sobreposição com Medicina no Trabalho."],
        ["Validar", "Higiene e Segurança no Trabalho", "/servicos/higiene-e-seguranca-no-trabalho/ (a validar)", "Comercial", "Média", "Tema relacionado com SST.", "Decidir se página própria ou secção."],
        ["Criar", "Formação SST", "/formacao/seguranca-e-saude-no-trabalho/ (a validar)", "Comercial", "Média/Alta", "Pode organizar ofertas de formação.", "Só se cursos forem reais."],
        ["Criar/Validar", "Primeiros Socorros", "/formacao/primeiros-socorros/ (a validar)", "Comercial", "Média", "Possível subpágina de formação.", "Confirmar oferta e certificação."],
        ["Criar/Validar", "Combate a Incêndios", "/formacao/combate-a-incendios/ (a validar)", "Comercial", "Média", "Possível procura formativa.", "Confirmar serviço real."],
        ["Criar", "Guias práticos SST", "/guias/obrigacoes-sst-empresas/ (a validar)", "Informacional", "Média", "Apoia autoridade e internal linking.", "Revisão técnica/legal obrigatória."],
        ["Não criar sem prova", "Páginas locais", "/servicos/.../lisboa/ (não aprovar sem prova)", "Local", "A confirmar", "Risco doorway se não houver base real.", "Validar área de atuação/presença."],
    ], widths=[1000, 1600, 1900, 1300, 1000, 2100, 2100])
    doc.page_break()

    doc.paragraph("Página 6 — Arquitetura recomendada", style="Heading1")
    doc.callout("Proposta, não decisão final", "Qualquer alteração de URLs existentes exige plano de redirects 301, canonical, sitemap, links internos, Search Console e QA antes de produção.", "FFF2CC")
    for line in [
        "/servicos/",
        "/servicos/medicina-no-trabalho/",
        "/servicos/seguranca-no-trabalho/",
        "/servicos/saude-ocupacional/",
        "/servicos/higiene-e-seguranca-no-trabalho/",
        "/formacao/",
        "/formacao/seguranca-e-saude-no-trabalho/",
        "/formacao/primeiros-socorros/",
        "/formacao/combate-a-incendios/",
        "/guias/",
        "/guias/obrigacoes-sst-empresas/",
        "/guias/medicina-no-trabalho-obrigatoria/",
    ]:
        doc.bullet(line + " — sugerida / a validar")
    doc.page_break()

    doc.paragraph("Página 7 — Concorrência: o que aprender", style="Heading1")
    comp_rows = [["Concorrente", "O que faz melhor", "O que a Previmed pode aprender", "O que não copiar"]]
    for comp in competitors:
        summary = comp.get("summary", {})
        services = ", ".join(summary.get("services", [])[:4]) or "Serviços a confirmar pela análise pública."
        strengths = "; ".join(summary.get("strengths", [])[:2])
        comp_rows.append([
            comp.get("name"),
            strengths or "Comunicação/estrutura a rever visualmente.",
            f"Clarificar oferta e percurso comercial; observar serviços comunicados: {services}.",
            "Não copiar texto, claims, estrutura legal, certificações ou páginas locais sem base própria.",
        ])
    doc.table(comp_rows, widths=[1300, 2600, 3100, 2200])
    doc.page_break()

    doc.paragraph("Página 8 — Plano 30/60/90 dias", style="Heading1")
    doc.table([
        ["Fase", "Ação", "Dono sugerido", "Dependências", "Resultado esperado"],
        ["0-15 dias", "Quick wins: titles/metas, H1, CTAs, hero copy, links internos básicos.", "Marketing + SEO", "Acesso CMS e aprovação copy.", "Mais clareza e melhor percurso comercial."],
        ["15-30 dias", "Melhorar páginas principais de serviço.", "Marketing + especialista técnico", "Serviços/claims validados.", "Páginas comerciais mais fortes."],
        ["30-60 dias", "Criar briefs e páginas novas prioritárias.", "SEO + Conteúdo", "Arquitetura aprovada.", "Cluster de serviços organizado."],
        ["30-60 dias", "Validar schema e internal linking.", "SEO técnico", "Conteúdo visível e URLs finais.", "Melhor estrutura sem risco."],
        ["60-90 dias", "Expandir guias, FAQs e formação.", "Conteúdo + área técnica", "Revisão humana/legal.", "Autoridade e cobertura temática."],
        ["60-90 dias", "Medir com GSC/GA4 e ajustar.", "SEO/Data", "Acessos read-only.", "Priorização por dados reais."],
    ], widths=[1200, 3100, 1600, 2300, 2200])
    doc.page_break()

    doc.paragraph("Página 9 — Decisões que a Previmed deve tomar", style="Heading1")
    for item in [
        "Quais são os serviços prioritários para crescimento comercial?",
        "Que páginas devem ser comerciais e que páginas devem ser informativas?",
        "Que estrutura de URLs pode ser aprovada?",
        "Que páginas têm autorização para ser criadas ou reestruturadas?",
        "Que claims, certificações, provas e dados podem ser publicados?",
        "Quem valida conteúdo técnico, médico, legal ou de segurança?",
        "Quem aprova alterações em WordPress, slugs, redirects e schema?",
        "Que ferramentas/dados serão disponibilizados: GSC, GA4, PageSpeed, Search Console?",
    ]:
        doc.bullet(item)
    doc.page_break()

    doc.paragraph("Página 10 — Quality Gate resumido", style="Heading1")
    doc.table([
        ["Estado", "Aplicação"],
        ["Aprovado com notas", "O relatório executivo está pronto para ser usado em decisão e planeamento."],
        ["Precisa de dados", "Prioridades finais precisam de GSC, GA4, Search Console, PageSpeed/CrUX e dados comerciais."],
        ["Precisa de autorização", "Qualquer alteração em WordPress, URLs, redirects, canonical, schema, robots ou sitemap."],
        ["Bloqueado para produção", "Go-live ou alterações técnicas sem validação e autorização final."],
    ], widths=[2200, 6800])
    doc.paragraph("Validado: análise pública read-only, DOM renderizado por Playwright, screenshots, URLs Previmed, concorrentes e relatórios intermédios.")
    doc.paragraph("Não validado: rankings, volumes, tráfego, conversões, GSC/GA4, WordPress admin, claims legais/médicos/certificações e field data Core Web Vitals.")
    doc.page_break()

    doc.paragraph("Auditoria profunda", style="Heading1")
    doc.paragraph("Metodologia", style="Heading2")
    doc.bullet("Uso dos ficheiros intermédios já gerados, sem nova recolha externa.")
    doc.bullet("Dados principais: audit-results.json, relatórios markdown, CSV de concorrentes e screenshots Playwright.")
    doc.bullet("Classificação separa evidência, hipótese e recomendação.")
    doc.bullet("Alterações de produção permanecem fora do âmbito.")

    doc.paragraph("Análise detalhada da Previmed", style="Heading2")
    doc.table([["Métrica", "Resultado"], ["URLs analisados", data.get("previmed_urls_analyzed")], ["URLs OK/parciais", data.get("previmed_ok_urls")], ["Páginas com termos de serviço", len(service_pages)], ["Páginas com conteúdo curto (<300 palavras)", len(thin_pages)], ["Screenshots referenciados", len(screenshots)]], widths=[3500, 5500])
    doc.paragraph("Páginas a rever primeiro", style="Heading3")
    rows = [["URL/Página", "Status", "Word count", "Issues", "Recomendação"]]
    for page in risky_pages:
        issues = "; ".join(limit(i.get("issue"), 80) for i in page.get("issues", [])[:3])
        recs = "; ".join(limit(r, 80) for r in page.get("recommendations", [])[:2])
        rows.append([page_label(page), page.get("status"), page.get("wordCount", 0), issues or "Sem issue forte", recs or "Rever manualmente"])
    doc.table(rows, widths=[2700, 800, 900, 2700, 2700])

    doc.paragraph("Análise técnica", style="Heading2")
    doc.bullet("Canonical, robots, sitemap, redirects e status codes foram observados publicamente; confirmar antes de qualquer alteração.")
    doc.bullet("Mudanças de URL exigem redirect 301, canonical, sitemap, links internos, validação e rollback.")
    doc.bullet("Schema deve ser implementado só quando representar conteúdo visível e validado.")

    doc.paragraph("Análise de conteúdo e UX", style="Heading2")
    doc.bullet("Páginas de serviço devem responder rapidamente a: o que é, para quem é, quando é necessário, como funciona, que prova existe e como contactar.")
    doc.bullet("Evitar páginas genéricas que qualquer concorrente poderia publicar.")
    doc.bullet("CTAs e contactos devem ser visíveis, consistentes e úteis em mobile.")

    doc.paragraph("Concorrência — detalhe", style="Heading2")
    rows = [["Concorrente", "Páginas", "OK", "Serviços observados", "Gaps/oportunidades"]]
    for comp in competitors:
        summary = comp.get("summary", {})
        rows.append([
            comp.get("name"),
            len(comp.get("pages", [])),
            sum(1 for page in comp.get("pages", []) if page.get("ok")),
            ", ".join(summary.get("services", [])[:6]) or "A confirmar",
            "; ".join(summary.get("gaps", [])[:3]),
        ])
    doc.table(rows, widths=[1300, 800, 700, 3100, 3100])

    doc.paragraph("AI Search e schema", style="Heading2")
    doc.bullet("Oportunidade: respostas completas e citáveis nas páginas de serviço.")
    doc.bullet("FAQPage apenas quando perguntas/respostas estiverem visíveis.")
    doc.bullet("Organization, Service e BreadcrumbList devem usar dados reais e consistentes.")

    doc.paragraph("Apêndice — screenshots selecionados", style="Heading1")
    selected = []
    names = ["previmed-01-desktop", "previmed-01-mobile", "medisigma-01-desktop", "preslaboral-01-desktop", "gral-01-desktop", "stahp-01-desktop"]
    for wanted in names:
        match = next((shot for shot in screenshots if wanted in shot.name), None)
        if match:
            selected.append(match)
    for shot in selected[:6]:
        doc.image(shot, f"Screenshot Playwright: {shot.name}", width_inches=5.8)

    doc.paragraph("Apêndice — lista completa de evidências", style="Heading1")
    doc.paragraph("Os screenshots completos e dados brutos estão nas pastas:")
    doc.bullet(str(ROOT / "screenshots"))
    doc.bullet(str(ROOT / "data" / "audit-results.json"))
    doc.bullet(str(ROOT / "notes" / "full-report.md"))

    doc.save(OUT)
    print(json.dumps({
        "docx": str(OUT),
        "bytes": OUT.stat().st_size,
        "previmed_urls": len(pages),
        "competitors": len(competitors),
        "screenshots_available": len(screenshots),
        "screenshots_embedded": len(selected[:6]),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
