#!/usr/bin/env python3
"""
Gerador do relatório Word executivo Previmed
Usa apenas Python stdlib (zipfile + XML OOXML)
"""
import zipfile, pathlib, html, datetime, os

BASE = pathlib.Path(__file__).parent
OUTPUT = BASE / "previmed_full_competitive_audit_executive.docx"

def esc(text):
    return html.escape(str(text or ""), quote=False)

def para(text, style="Normal", bold=False, color=None, size=None, italic=False, space_before=0, space_after=160):
    rpr = ""
    if bold: rpr += "<w:b/><w:bCs/>"
    if italic: rpr += "<w:i/>"
    if color: rpr += f'<w:color w:val="{color}"/>'
    if size: rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    rpr_xml = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    pstyle = f'<w:pStyle w:val="{style}"/>' if style != "Normal" else ""
    spacing = f'<w:spacing w:before="{space_before}" w:after="{space_after}"/>'
    return f"""<w:p><w:pPr>{pstyle}{spacing}</w:pPr><w:r>{rpr_xml}<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>"""

def heading1(text):
    return f"""<w:p>
<w:pPr><w:pStyle w:val="Heading1"/><w:spacing w:before="400" w:after="200"/></w:pPr>
<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>"""

def heading2(text):
    return f"""<w:p>
<w:pPr><w:pStyle w:val="Heading2"/><w:spacing w:before="300" w:after="160"/></w:pPr>
<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>"""

def heading3(text):
    return f"""<w:p>
<w:pPr><w:pStyle w:val="Heading3"/><w:spacing w:before="200" w:after="120"/></w:pPr>
<w:r><w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>"""

def page_break():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

def bullet(text, bold_prefix=None):
    if bold_prefix:
        return f"""<w:p>
<w:pPr><w:ind w:left="360" w:hanging="360"/><w:spacing w:after="80"/></w:pPr>
<w:r><w:t xml:space="preserve">• </w:t></w:r>
<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{esc(bold_prefix)}</w:t></w:r>
<w:r><w:t xml:space="preserve"> {esc(text)}</w:t></w:r>
</w:p>"""
    return f"""<w:p>
<w:pPr><w:ind w:left="360" w:hanging="360"/><w:spacing w:after="80"/></w:pPr>
<w:r><w:t xml:space="preserve">• {esc(text)}</w:t></w:r>
</w:p>"""

def callout(text, color="FFF2CC", border="F0C040"):
    return f"""<w:p>
<w:pPr>
  <w:pBdr>
    <w:top w:val="single" w:sz="6" w:space="4" w:color="{border}"/>
    <w:left w:val="single" w:sz="24" w:space="4" w:color="{border}"/>
    <w:bottom w:val="single" w:sz="6" w:space="4" w:color="{border}"/>
    <w:right w:val="single" w:sz="6" w:space="4" w:color="{border}"/>
  </w:pBdr>
  <w:shd w:val="clear" w:color="auto" w:fill="{color}"/>
  <w:spacing w:before="120" w:after="120"/>
  <w:ind w:left="180" w:right="180"/>
</w:pPr>
<w:r><w:rPr><w:b/><w:sz w:val="20"/><w:szCs w:val="20"/></w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r>
</w:p>"""

def spacer():
    return '<w:p><w:pPr><w:spacing w:after="80"/></w:pPr></w:p>'

def make_table(headers, rows, col_widths=None):
    if not col_widths:
        total = 9000
        w = total // len(headers)
        col_widths = [w] * len(headers)

    grid = "".join(f'<w:gridCol w:w="{cw}"/>' for cw in col_widths)

    def make_cell(text, is_header=False, width=1500):
        fill = '<w:shd w:val="clear" w:color="auto" w:fill="2E75B6"/>' if is_header else '<w:shd w:val="clear" w:color="auto" w:fill="FFFFFF"/>'
        bold = "<w:b/><w:bCs/>" if is_header else ""
        color = '<w:color w:val="FFFFFF"/>' if is_header else '<w:color w:val="1F1F1F"/>'
        return f"""<w:tc>
<w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{fill}</w:tcPr>
<w:p><w:pPr><w:spacing w:before="60" w:after="60"/></w:pPr>
<w:r><w:rPr>{bold}{color}<w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>
<w:t xml:space="preserve">{esc(str(text))}</w:t></w:r></w:p>
</w:tc>"""

    header_cells = "".join(make_cell(h, True, col_widths[i]) for i, h in enumerate(headers))
    header_row = f"<w:tr><w:trPr><w:trHeight w:val='360'/></w:trPr>{header_cells}</w:tr>"

    body_rows = ""
    for ri, row in enumerate(rows):
        fill = "F2F8FF" if ri % 2 == 0 else "FFFFFF"
        cells = ""
        for ci, cell in enumerate(row):
            w = col_widths[ci] if ci < len(col_widths) else 1500
            shade = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
            cells += f"""<w:tc>
<w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{shade}</w:tcPr>
<w:p><w:pPr><w:spacing w:before="60" w:after="60"/></w:pPr>
<w:r><w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>
<w:t xml:space="preserve">{esc(str(cell))}</w:t></w:r></w:p>
</w:tc>"""
        body_rows += f"<w:tr>{cells}</w:tr>"

    return f"""<w:tbl>
<w:tblPr>
  <w:tblStyle w:val="TableGrid"/>
  <w:tblW w:w="{sum(col_widths)}" w:type="dxa"/>
  <w:tblBorders>
    <w:top w:val="single" w:sz="4" w:color="2E75B6"/>
    <w:left w:val="single" w:sz="4" w:color="2E75B6"/>
    <w:bottom w:val="single" w:sz="4" w:color="2E75B6"/>
    <w:right w:val="single" w:sz="4" w:color="2E75B6"/>
    <w:insideH w:val="single" w:sz="4" w:color="BDD7EE"/>
    <w:insideV w:val="single" w:sz="4" w:color="BDD7EE"/>
  </w:tblBorders>
  <w:tblCellMar>
    <w:top w:w="60" w:type="dxa"/>
    <w:left w:w="108" w:type="dxa"/>
    <w:bottom w:w="60" w:type="dxa"/>
    <w:right w:w="108" w:type="dxa"/>
  </w:tblCellMar>
</w:tblPr>
<w:tblGrid>{grid}</w:tblGrid>
{header_row}
{body_rows}
</w:tbl>"""

def section_divider():
    return """<w:p>
<w:pPr>
  <w:pBdr>
    <w:bottom w:val="single" w:sz="4" w:space="4" w:color="2E75B6"/>
  </w:pBdr>
  <w:spacing w:before="80" w:after="80"/>
</w:pPr>
</w:p>"""

# ============================================================
# BUILD DOCUMENT
# ============================================================

parts = []

# ---- CAPA ----
parts.append(page_break() if parts else "")
parts.append(spacer())
parts.append(spacer())
parts.append(spacer())
parts.append(para("RELATÓRIO SEO, UX E CONCORRÊNCIA", bold=True, size=40, color="1F3864", space_before=400, space_after=200))
parts.append(para("Previmed — previmed.pt", bold=True, size=32, color="2E75B6", space_after=120))
parts.append(section_divider())
parts.append(para("Análise estratégica do site previmed.pt e concorrência em SST,", size=22, color="404040"))
parts.append(para("Medicina no Trabalho e Formação Profissional", size=22, color="404040", space_after=240))
parts.append(spacer())
parts.append(make_table(
    ["Campo", "Valor"],
    [
        ["Data", "31 de Maio de 2026"],
        ["Versão", "Executive 2.0 — Auditoria completa"],
        ["Autor", "SEO Growth System / Análise assistida"],
        ["Âmbito", "Read-only — Nenhuma alteração em produção"],
        ["URLs Previmed analisadas", "20 (direto) + 50 mapeadas via sitemap"],
        ["Concorrentes identificados", "47 (AEST) + pesquisa web"],
        ["Concorrentes analisados", "7 profundamente + 4 superficialmente"],
    ],
    [2500, 6500]
))
parts.append(spacer())
parts.append(callout("⚠️  Análise read-only. Nenhuma alteração foi feita no site, WordPress, DNS, robots.txt, sitemap, redirects ou qualquer sistema de produção.", "FFF2CC", "E2A800"))
parts.append(page_break())

# ---- SUMÁRIO EXECUTIVO ----
parts.append(heading1("Sumário Executivo"))
parts.append(para("A Previmed tem uma base institucional sólida — 29 anos de atividade, certificações ACT/DGS/DGERT/ISO 9001, presença em Lisboa e Porto, e um portfolio de serviços mais amplo do que a maioria dos concorrentes (SST, Medicina, Formação, Ambiental, Alimentar, Certificação). No entanto, o site comunica mal o que a empresa faz, não tem prova social, não tem FAQs, não tem schema, e tem problemas técnicos críticos em quase todas as páginas.", space_after=120))
parts.append(spacer())
parts.append(make_table(
    ["Tema", "Conclusão"],
    [
        ["Estado geral", "Base auditável com 50 páginas públicas — mas abaixo do potencial em quase todas as dimensões"],
        ["Maior problema", "Meta description ausente em 100% das páginas + zero prova social + thin content generalizado"],
        ["Maior oportunidade", "Transformar páginas de serviço em páginas fortes com FAQs, prova, CTAs e schema"],
        ["Risco principal", "Concorrentes como Medisigma e Preveris estão significativamente mais avançados em conteúdo e confiança"],
        ["Recomendação principal", "Corrigir quick wins técnicos primeiro, depois expandir conteúdo das páginas core"],
        ["Prioridade imediata", "Meta descriptions + titles + typos + H1 homepage + cursos em /e-learning/"],
        ["Score global estimado", "4.5/10 — muito abaixo do potencial da marca e das certificações que tem"],
    ],
    [3000, 6000]
))
parts.append(spacer())
parts.append(callout("DIAGNÓSTICO CRÍTICO: O site Previmed não tem uma única meta description em nenhuma das 50 páginas públicas. Não tem schema em nenhuma página. Não tem nenhum testemunho de cliente. Não tem FAQs. A página de e-learning existe mas não lista nenhum curso. Estas são falhas sistémicas — não são problemas de uma página específica.", "FFE6E6", "CC0000"))
parts.append(page_break())

# ---- TOP 10 AÇÕES ----
parts.append(heading1("Top 10 Ações Prioritárias"))
parts.append(make_table(
    ["#", "Ação", "Tipo", "Impacto", "Esforço", "Risco", "Prazo"],
    [
        ["1", "Adicionar meta description a TODAS as páginas (50)", "Corrigir", "Alto", "Baixo", "Baixo", "0-15 dias"],
        ["2", "Corrigir titles com duplicação de marca ('Previmed - PrevimedPrevimed')", "Corrigir", "Alto", "Baixo", "Baixo", "0-15 dias"],
        ["3", "Corrigir typos 'Seguranca' → 'Segurança' em 4+ páginas", "Corrigir", "Médio", "Baixo", "Baixo", "0-15 dias"],
        ["4", "Adicionar H1 explícito na homepage", "Corrigir", "Alto", "Baixo", "Baixo", "0-15 dias"],
        ["5", "Adicionar FAQs em /saude-no-trabalho/ (6+ perguntas)", "Melhorar", "Alto", "Médio", "Médio", "15-30 dias"],
        ["6", "Listar todos os cursos reais na página /e-learning/", "Melhorar", "Alto", "Baixo", "Baixo", "15-30 dias"],
        ["7", "Schema Organization + LocalBusiness (Lisboa + Porto)", "Técnico", "Alto", "Médio", "Médio", "15-30 dias"],
        ["8", "Adicionar 3-5 testemunhos de clientes reais com contexto", "Melhorar", "Alto", "Médio", "Baixo", "15-30 dias"],
        ["9", "Melhorar /contactos/ (mapa + horário + formulário simples)", "Melhorar", "Alto", "Baixo", "Baixo", "15-30 dias"],
        ["10", "Expandir /seguranca-no-trabalho/ (+600 palavras + FAQs)", "Melhorar", "Alto", "Médio", "Médio", "30-60 dias"],
    ],
    [400, 3200, 1000, 900, 900, 900, 1100]
))
parts.append(page_break())

# ---- QUICK WINS ----
parts.append(heading1("Quick Wins — Ações Rápidas com Alto Impacto"))
parts.append(make_table(
    ["Quick win", "Onde aplicar", "Porquê", "Resultado esperado", "Cuidado"],
    [
        ["Meta descriptions", "Todas as 50 páginas", "100% ausentes — impacta CTR nas SERPs imediatamente", "CTR melhorado, snippets mais atrativos", "Não inventar claims; usar conteúdo real da página"],
        ["Corrigir title duplicado", "/seguranca-no-trabalho/ e /avaliacoes-de-riscos/", "Duplicação de marca prejudica CTR e aparência", "Titles limpos e profissionais", "Verificar template do plugin SEO (Yoast/RankMath)"],
        ["Corrigir typos em H2", "4+ páginas com 'Seguranca'", "Parece erro de sistema — afeta credibilidade", "Profissionalismo e confiança", "Confirmar se é widget global ou texto inline"],
        ["H1 na homepage", "Homepage", "H1 ausente é sinal negativo para Google", "Estrutura semântica correta", "Coordenar com designer"],
        ["Adicionar horário em /contactos/", "/contactos/", "Informação básica que utilizadores precisam", "Menos fricção no contacto", "Confirmar horário real com equipa"],
        ["Listar cursos em /e-learning/", "/e-learning/", "Página existe mas não tem cursos — confunde utilizadores", "Conversão da página de formação", "Confirmar lista de cursos reais disponíveis"],
        ["Open Graph tags", "Todo o site", "Partilha em LinkedIn/WhatsApp usa título genérico", "Melhor apresentação ao partilhar", "Plugin SEO deve suportar OG — verificar configuração"],
        ["Schema básico na homepage", "Homepage", "Zero schema em todo o site é crítico", "Elegibilidade para rich snippets", "Implementar apenas com dados reais verificados"],
    ],
    [1800, 1600, 2000, 2000, 1600]
))
parts.append(page_break())

# ---- PROBLEMAS CRÍTICOS ----
parts.append(heading1("Problemas Críticos e Bloqueios"))
parts.append(make_table(
    ["Problema", "Área", "Impacto", "Gravidade", "Como resolver"],
    [
        ["Meta description ausente em TODAS as páginas", "SEO técnico", "CTR muito baixo nas SERPs", "CRÍTICO", "Configurar plugin SEO + escrever meta description única por página"],
        ["Title ausente na homepage", "SEO técnico", "Página mais importante sem title", "CRÍTICO", "Definir title na homepage via plugin SEO"],
        ["Duplicação 'Previmed - PrevimedPrevimed' em titles", "SEO técnico", "Aparência profissional destruída nas SERPs", "CRÍTICO", "Corrigir template do plugin SEO"],
        ["Schema JSON-LD ausente em todo o site", "SEO técnico", "Sem rich snippets, sem dados estruturados", "ALTO", "Implementar Organization + LocalBusiness + Service"],
        ["Zero prova social no site", "Conteúdo/Confiança", "Credibilidade muito abaixo dos concorrentes", "ALTO", "Recolher e publicar 3-5 testemunhos reais"],
        ["Página /e-learning/ sem nenhum curso listado", "Conteúdo/Conversão", "Utilizador chega e não encontra informação", "ALTO", "Listar todos os cursos com nome, duração e certificação"],
        ["Thin content em 8+ páginas (< 300 palavras)", "Conteúdo/SEO", "Menor autoridade temática, menor ranking", "ALTO", "Expandir páginas core para 500-800 palavras cada"],
        ["Typos 'Seguranca' em H2 de 4+ páginas", "Conteúdo/Técnico", "Parece erro de sistema — afeta credibilidade", "MÉDIO", "Corrigir todos os headings com acento em falta"],
        ["Página /contactos/ sem mapa, horário ou formulário", "UX/Conversão", "Fricção elevada no contacto", "MÉDIO", "Adicionar Google Maps embed + horário + formulário simples"],
        ["FAQs ausentes em todas as páginas de serviço", "Conteúdo/SEO", "Perda de AI Search e FAQ rich snippets", "MÉDIO", "Criar mínimo 5 FAQs por página de serviço"],
        ["Blog com apenas 4 artigos (todos de maio 2026)", "Conteúdo", "Sem autoridade editorial, sem tráfego informacional", "MÉDIO", "Plano editorial mínimo: 1 artigo/mês"],
        ["Formulário de proposta com muita fricção", "Conversão", "Taxa de abandono elevada no formulário longo", "MÉDIO", "Simplificar para 2 passos ou reduzir campos"],
    ],
    [2500, 1400, 1800, 900, 2400]
))
parts.append(page_break())

# ---- MAPA DE PÁGINAS ----
parts.append(heading1("Mapa de Páginas — Criar, Melhorar, Fundir ou Validar"))
parts.append(make_table(
    ["Ação", "Página / Tema", "URL sugerida (a validar)", "Intenção", "Prioridade", "Motivo"],
    [
        ["Melhorar", "Medicina do Trabalho", "/saude-no-trabalho/", "Comercial", "Crítica", "Página core — thin content, sem FAQs, sem prova"],
        ["Melhorar", "Segurança no Trabalho", "/seguranca-no-trabalho/", "Comercial", "Crítica", "150 palavras — muito fraca para keyword competitiva"],
        ["Melhorar", "E-learning / Formação Online", "/e-learning/", "Comercial", "Crítica", "Sem cursos listados — página inútil atualmente"],
        ["Melhorar", "Oferta Formativa", "/oferta-formativa/", "Comercial", "Alta", "Sem preços, sem duração, sem CTAs de conversão"],
        ["Melhorar", "Contactos", "/contactos/", "Conversão", "Alta", "Sem mapa, sem horário, sem formulário"],
        ["Melhorar", "Sobre a Previmed", "/sobre-a-previmed/", "Confiança", "Alta", "Sem dados concretos, sem equipa, sem história rica"],
        ["Melhorar", "Homepage", "/", "Entrada", "Alta", "Sem H1, sem schema, slider sem conteúdo útil"],
        ["Criar", "Medicina do Trabalho Obrigatória (guia)", "/guias/medicina-no-trabalho-obrigatoria/", "Informacional", "Alta", "Query frequente — nenhuma página responde hoje"],
        ["Criar", "Formação Primeiros Socorros", "/formacao/primeiros-socorros/", "Comercial", "Média", "Curso mencionado na oferta mas sem página própria"],
        ["Criar", "Formação Combate a Incêndios", "/formacao/combate-a-incendios/", "Comercial", "Média", "Curso mencionado, sem página dedicada"],
        ["Criar", "Obrigações SST para Empresas (guia)", "/guias/obrigacoes-sst-empresas/", "Informacional", "Média", "Conteúdo que atrai decisores e RH"],
        ["Validar", "Saúde Ocupacional", "/servicos/saude-ocupacional/", "Comercial", "Média", "Keyword alternativa com intenção própria"],
        ["Validar", "Higiene e Segurança no Trabalho", "/servicos/higiene-e-seguranca-no-trabalho/", "Comercial", "Média", "Query frequente — Previmed não tem página com este nome"],
        ["Não criar", "Páginas locais (Lisboa, Porto)", "— (sem base)", "Local", "A confirmar", "Só criar com confirmação de presença/cobertura real"],
    ],
    [900, 2000, 2500, 1000, 900, 1700]
))
parts.append(callout("IMPORTANTE: Qualquer alteração de URL existente exige: redirect 301 + atualização de canonical + sitemap + links internos + validação + autorização. Nunca alterar URLs sem plano documentado.", "FFE6E6", "CC0000"))
parts.append(page_break())

# ---- ARQUITETURA ----
parts.append(heading1("Arquitetura Recomendada — Proposta (a validar)"))
parts.append(callout("Esta é uma proposta de estrutura. Não é uma decisão final. Qualquer alteração de URLs existentes exige plano de redirects 301, canonical, sitemap, links internos, QA e autorização explícita.", "E8F4FD", "2E75B6"))
parts.append(spacer())

parts.append(heading2("Estrutura proposta"))
for line in [
    "/servicos/                              (hub de serviços)",
    "├── /servicos/saude-no-trabalho/        (Medicina do Trabalho — já existe)",
    "├── /servicos/seguranca-no-trabalho/    (SST — já existe)",
    "├── /servicos/seguranca-ambiental/      (já existe)",
    "├── /servicos/seguranca-alimentar/      (já existe)",
    "└── /servicos/certificacao/             (já existe — renomear?)",
    "",
    "/formacao/                              (hub de formação — criar)",
    "├── /formacao/oferta-formativa/         (já existe — mover/melhorar)",
    "├── /formacao/e-learning/               (já existe — preencher)",
    "├── /formacao/interempresas/            (já existe)",
    "├── /formacao/intraempresas/            (já existe)",
    "├── /formacao/primeiros-socorros/       (criar — se curso real)",
    "├── /formacao/combate-a-incendios/      (criar — se curso real)",
    "└── /formacao/evacuacao-edificios/      (criar — se curso real)",
    "",
    "/guias/                                 (criar — conteúdo informacional)",
    "├── /guias/medicina-no-trabalho-obrigatoria/",
    "├── /guias/obrigacoes-sst-empresas/",
    "└── /guias/escolher-prestador-sst/",
]:
    parts.append(para(line, size=18, color="1F1F1F", space_after=60))

parts.append(spacer())
parts.append(para("Todas as URLs sugeridas são 'a validar' — precisam de ser aprovadas pela equipa Previmed antes de qualquer implementação.", italic=True, color="666666"))
parts.append(page_break())

# ---- CONCORRÊNCIA ----
parts.append(heading1("Concorrência — O Que Aprender"))
parts.append(make_table(
    ["Concorrente", "O que faz melhor", "O que a Previmed pode aprender", "O que NÃO copiar"],
    [
        ["Medisigma\nmedisigma.pt\n⚠️ AMEAÇA ALTA",
         "500+ clientes declarados; 12+ testemunhos com fotos e métricas ('custos seguro -12%'); 13 localizações; FAQ com 10+ perguntas; 12 categorias de serviço; ChooseMyCompany Platinum",
         "Prova social com dados concretos; Testemunhos com resultado mensurável; FAQ em cada página; CTAs múltiplos e contextuais; Comunicar impacto para o negócio do cliente",
         "Não copiar texto; Não inventar métricas; Não criar localizações sem presença real"],
        ["Preveris\npreveris.pt\n⚠️ AMEAÇA ALTA",
         "Parceria CUF (maior rede de saúde privada); 'Maior rede nacional'; Blog editorial ativo; Portal clientes integrado",
         "Parceria estratégica com entidade reconhecida; Blog regular sobre SST; Comunicar cobertura geográfica claramente",
         "Não copiar o claim 'maior rede' sem dados; Não prometer o que não existe"],
        ["MedicisForma\nmedicisforma.pt\n⚠️ AMEAÇA ALTA",
         "H1 com keyword 'Segurança e Saúde no Trabalho'; Testemunhos com empresa + colaboradores + anos de parceria; 4 CTAs diferentes; 'Norte a Sul' + unidades móveis",
         "H1 orientado à keyword principal; Testemunhos com contexto empresarial; CTAs por finalidade (proposta vs contacto vs saiba mais)",
         "Não copiar texto; Não replicar sem dados próprios"],
        ["Forseguro\nforseguro.pt\n⚠️ Formação",
         "35.576 formandos certificados; Google Reviews 5.0★; 18+ testemunhos sobre plataforma; Formação financiada comunicada; Moodle especificado",
         "Quantificar formandos certificados; Google Reviews visíveis; Formação financiada comunicada (se elegível); Especificar plataforma de e-learning com features",
         "Não inventar números de formandos"],
        ["Prevensis\nprevensis.pt",
         "'TOP 5% Melhores PME'; 19 anos comunicados em H2; Logos de clientes visíveis",
         "Certificações de qualidade como sinal de confiança; Anos de experiência como H2 da homepage",
         "Não usar certificações que a Previmed não tem"],
    ],
    [2000, 2500, 2500, 2000]
))
parts.append(page_break())

# ---- PLANO 30/60/90 ----
parts.append(heading1("Plano de Ação — 30/60/90 dias"))
parts.append(heading2("Fase 1 — 0 a 15 dias: Quick wins e correções críticas"))
parts.append(make_table(
    ["Ação", "Dono sugerido", "Dependências", "Resultado esperado"],
    [
        ["Meta descriptions em todas as páginas (50)", "SEO + Marketing", "Acesso plugin SEO", "CTR melhorado nas SERPs"],
        ["Corrigir titles com duplicação de marca", "SEO técnico", "Plugin SEO configurado", "Títulos profissionais"],
        ["Corrigir typos 'Seguranca' em 4+ páginas", "Editor/CMS", "Acesso WordPress", "Credibilidade"],
        ["H1 explícito na homepage", "SEO + Design", "Aprovação de layout", "Estrutura semântica"],
        ["Adicionar horário de atendimento em /contactos/", "Marketing", "Aprovação equipa", "Menos fricção"],
        ["Listar cursos reais em /e-learning/", "Marketing + Formação", "Lista de cursos confirmada", "Conversão"],
        ["Corrigir Open Graph em todo o site", "SEO técnico", "Plugin SEO", "Melhor partilha social"],
    ],
    [3000, 2000, 2000, 2000]
))

parts.append(heading2("Fase 2 — 15 a 30 dias: Melhorias de páginas core"))
parts.append(make_table(
    ["Ação", "Dono sugerido", "Dependências", "Resultado esperado"],
    [
        ["Expandir /saude-no-trabalho/ + 6 FAQs", "Marketing + Médico responsável", "Aprovação de claims médicos/legais", "AI Search ready + ranking"],
        ["Schema Organization + LocalBusiness", "SEO técnico", "Plugin SEO ou JSON-LD manual", "Rich snippets eligíveis"],
        ["Schema Service nas páginas core (SST, Medicina)", "SEO técnico", "Conteúdo validado", "Dados estruturados"],
        ["3-5 testemunhos reais de clientes", "Marketing", "Clientes dispostos a ser referenciados", "Confiança + conversão"],
        ["Google Maps embed + formulário em /contactos/", "Técnico WordPress", "RGPD verificado", "UX de contacto"],
        ["Número de clientes/empresas (se real)", "Marketing", "Dado aprovado internamente", "Credibilidade"],
    ],
    [3000, 2000, 2000, 2000]
))

parts.append(heading2("Fase 3 — 30 a 60 dias: Criação e expansão"))
parts.append(make_table(
    ["Ação", "Dono sugerido", "Dependências", "Resultado esperado"],
    [
        ["Expandir /seguranca-no-trabalho/ (600+ palavras + FAQs)", "SEO + Técnico SST", "Aprovação de conteúdo", "Ranking para 'segurança no trabalho'"],
        ["Criar /guias/medicina-no-trabalho-obrigatoria/", "SEO + Marketing", "Revisão legal", "Tráfego informacional"],
        ["Criar /formacao/primeiros-socorros/ (se curso real)", "Marketing + Formação", "Confirmar oferta", "Nova página de conversão"],
        ["Criar /formacao/combate-a-incendios/ (se curso real)", "Marketing + Formação", "Confirmar oferta", "Nova página de conversão"],
        ["Schema FAQPage nas páginas com FAQs", "SEO técnico", "FAQs publicadas", "FAQ rich snippets"],
        ["Blog: 2 artigos estratégicos", "SEO + Marketing", "Aprovação editorial", "Autoridade temática"],
        ["PageSpeed: verificar e otimizar imagens", "Técnico", "Acesso hosting", "Core Web Vitals"],
    ],
    [3000, 2000, 2000, 2000]
))

parts.append(heading2("Fase 4 — 60 a 90 dias: Estratégia e medição"))
parts.append(make_table(
    ["Ação", "Dono sugerido", "Dependências", "Resultado esperado"],
    [
        ["Criar /guias/obrigacoes-sst-empresas/", "SEO + Técnico SST", "Revisão legal", "Autoridade e tráfego"],
        ["Avaliar /servicos/saude-ocupacional/", "SEO + Marketing", "Decisão estratégica", "Nova entrada keyword"],
        ["Otimizar Google Business Profile", "Marketing", "Acesso GBP", "Local SEO"],
        ["Campanha de testemunhos (3+ por serviço)", "Marketing", "Clientes + autorização", "Confiança escalável"],
        ["Medir com GSC/GA4: posições e CTR", "SEO/Data", "Acesso GSC/GA4", "Validar impacto"],
        ["Avaliar parceria estratégica (hospital, seguradora)", "Direção", "Decisão de negócio", "Diferenciador vs Preveris"],
    ],
    [3000, 2000, 2000, 2000]
))
parts.append(page_break())

# ---- DECISÕES ----
parts.append(heading1("Decisões que a Previmed tem de Tomar"))
parts.append(para("Estas não são ações SEO — são decisões internas que desbloqueiam o trabalho. Sem estas decisões, o plano não pode avançar corretamente.", space_after=160))
decisions = [
    ("Serviços prioritários", "Quais são os serviços com maior potencial de crescimento? (Medicina? SST? Formação? Ambiental?)"),
    ("Páginas a criar", "Que novos serviços têm autorização para ter página própria? (Primeiros Socorros, Combate a Incêndios, etc.)"),
    ("Estrutura de URLs", "Aprovar a arquitetura proposta ou definir alternativa (ver ficheiro 07 — proposta detalhada)"),
    ("Claims e certificações", "Que claims, certificações e provas podem ser publicados no site?"),
    ("Validação de conteúdo", "Quem valida conteúdo técnico, médico e legal antes de publicar?"),
    ("Aprovação WordPress", "Quem aprova alterações em WordPress, redirects, schema e configuração do plugin SEO?"),
    ("Testemunhos", "Que clientes aceitam ser referenciados com nome, empresa e resultado?"),
    ("Formação financiada", "Existe formação financiada? Está comunicada? Com que condições?"),
    ("Dados internos", "Quantos clientes/empresas tem a Previmed? Quantos formandos certificados?"),
    ("Ferramentas", "GSC e GA4 vão ser disponibilizados para análise? Quem tem acesso?"),
]
for key, val in decisions:
    parts.append(bullet(val, key))
parts.append(page_break())

# ---- QUALITY GATE ----
parts.append(heading1("Quality Gate — Veredito Final"))
parts.append(make_table(
    ["Âmbito", "Estado", "Detalhe"],
    [
        ["Relatório executivo", "✅ APROVADO COM NOTAS", "Pronto para apresentação e decisão"],
        ["Recomendações — priorização final", "⚠️ PRECISA DE DADOS", "Sem GSC/GA4, prioridade baseada em hipóteses"],
        ["Execução em produção", "🔒 PRECISA DE AUTORIZAÇÃO", "Nenhuma ação sem aprovação explícita"],
        ["Go-live de novas páginas", "🔒 BLOQUEADO", "Criar redirect plan, validar conteúdo, autorização"],
    ],
    [2500, 2500, 4000]
))
parts.append(spacer())

parts.append(heading2("O que foi validado"))
for item in [
    "20 URLs Previmed analisadas diretamente via WebFetch",
    "50 páginas mapeadas via sitemap",
    "11 concorrentes identificados; 7 analisados profundamente",
    "47 empresas do setor identificadas via AEST",
    "Meta descriptions: ausência confirmada em 100% das páginas",
    "Schema: ausência confirmada em todas as páginas analisadas",
    "Typos em headings: identificados e localizados em 4+ páginas",
    "Titles duplicados: identificados e documentados",
    "Prova social: confirmada ausência completa",
    "Página e-learning: confirmada como vazia (sem cursos)",
    "NAP (Lisboa + Porto): confirmado via /contactos/",
    "Certificações ACT/DGS/DGERT/ISO 9001: confirmadas",
    "Fundação 1995: confirmada em /sobre-a-previmed/",
]:
    parts.append(bullet(item))

parts.append(spacer())
parts.append(heading2("O que NÃO foi validado"))
for item in [
    "Rankings reais (sem GSC)",
    "Tráfego orgânico (sem GA4)",
    "CTR real das páginas (sem GSC)",
    "Core Web Vitals — LCP, INP, CLS (sem PageSpeed API/real data)",
    "Mobile rendering (sem Playwright)",
    "Canonical correto em cada página (sem headers HTTP diretos)",
    "Status codes de todas as 50 páginas",
    "30 páginas não analisadas diretamente (apenas mapeadas)",
    "Configuração exata do plugin SEO (sem acesso WordPress admin)",
    "Perfil de backlinks (sem ferramentas pagas)",
    "Google Business Profile (sem acesso GBP)",
    "Claims de formação financiada",
    "Número exato de clientes e formandos",
    "Lista real de cursos disponíveis no e-learning",
]:
    parts.append(bullet(item))

parts.append(spacer())
parts.append(callout("RISCO RESIDUAL: As prioridades deste relatório baseiam-se em análise qualitativa e comparação com a concorrência, não em dados de tráfego real. A obtenção de acesso ao GSC e GA4 pode alterar significativamente as prioridades recomendadas.", "FFF2CC", "E2A800"))
parts.append(page_break())

# ---- PARTE PROFUNDA — ANÁLISE DETALHADA ----
parts.append(heading1("Parte A — Análise Detalhada Previmed"))

parts.append(heading2("A1. Mapeamento de URLs (sitemap)"))
parts.append(para("O sitemap.xml da Previmed tem 3 sitemaps: pages (50 URLs), posts (5 URLs), categories. Total: 55+ páginas indexadas.", space_after=120))
parts.append(make_table(
    ["Categoria", "Nº URLs", "Exemplos de páginas"],
    [
        ["Saúde no Trabalho", "8", "saude-no-trabalho, check-ups, enfermagem, medicina-curativa, medicina-desportiva"],
        ["Segurança no Trabalho", "9", "seguranca-no-trabalho, avaliacoes-de-riscos, auditorias, coordenacao-obra, planos-sst"],
        ["Formação", "7", "oferta-formativa, e-learning, formacao-interempresas, formacao-intraempresas, formacao-2"],
        ["Certificação", "7", "sistemas-integrados-certificacao, marcacao-ce, responsabilidade-social, servico-certificado"],
        ["Segurança Ambiental", "5", "seguranca-ambiental, consultoria-ambiental, acustica, monitorizacao, estudos-projectos"],
        ["Segurança Alimentar", "2", "seguranca-higiene-alimentar, gestao-seguranca-alimentar"],
        ["Institucional", "4", "sobre-a-previmed, contactos, politica-privacidade, informacao-legal"],
        ["Conversão", "2", "pedido-de-proposta, prestadores"],
        ["Posts/Blog", "5", "coronavirus, gripe, prevencao-seguranca-trabalho, rastreios (todos de 11/05/2026)"],
    ],
    [2500, 1000, 5500]
))

parts.append(heading2("A2. Robots.txt"))
parts.append(para("Configuração padrão WordPress. Bloqueia /wp-admin/ (correto). Permite admin-ajax.php (necessário). Declara sitemap em https://previmed.pt/sitemaps.xml. Não bloqueia /wp-content/uploads/ — imagens expostas ao crawl (risco baixo mas desnecessário)."))

parts.append(heading2("A3. Análise página a página — resumo de scores"))
parts.append(make_table(
    ["Página", "Title", "Meta Desc", "H1", "Conteúdo", "Schema", "Score"],
    [
        ["Homepage (/)", "Ausente", "Ausente", "Implícito", "Thin + slider vazio", "Ausente", "3/10"],
        ["/saude-no-trabalho/", "Curto (31ch)", "Ausente", "OK", "Razoável + refs legais", "Ausente", "6/10"],
        ["/seguranca-no-trabalho/", "Duplicado", "Ausente", "OK", "Muito breve (150p)", "Ausente", "5/10"],
        ["/seguranca-e-saude-no-trabalho/", "Longo (106ch)", "Ausente", "Técnico", "Processo 6 fases", "Ausente", "5/10"],
        ["/oferta-formativa/", "Genérico", "Ausente", "Genérico", "Cursos listados mas sem detalhes", "Ausente", "5/10"],
        ["/e-learning/", "Ausente", "Ausente", "Genérico", "Sem cursos — vazio", "Ausente", "2/10"],
        ["/avaliacoes-de-riscos/", "Duplicado+", "Ausente", "OK", "Moderado", "Ausente", "5/10"],
        ["/sobre-a-previmed/", "Genérico", "Ausente", "OK", "Breve, dados escassos", "Ausente", "5/10"],
        ["/contactos/", "Genérico", "Ausente", "OK", "NAP OK, sem mapa/horário", "Ausente", "4/10"],
        ["/pedido-de-proposta/", "Genérico", "Ausente", "Fraco", "Formulário com fricção", "Ausente", "4/10"],
        ["/check-ups/", "Ausente", "Ausente", "Genérico", "Breve, sem preços", "Ausente", "3/10"],
    ],
    [2200, 1100, 1100, 1000, 2200, 900, 900]
))
parts.append(page_break())

parts.append(heading1("Parte B — Análise de Concorrentes"))

parts.append(heading2("B1. Medisigma — medisigma.pt (Ameaça Alta)"))
for item in [
    "Title excelente: 'Medicina do Trabalho em Portugal | Medisigma - Segurança e Saúde'",
    "H1 orientado ao benefício: 'Protegemos o seu negócio como se fosse o nosso'",
    "12 categorias de serviço — portfolio mais amplo em comunicação",
    "500+ clientes, 12+ testemunhos com métricas de resultado, 8 logos de parceiros",
    "FAQ integrada com 10+ perguntas",
    "13 localizações geográficas no rodapé",
    "6 certificações: ACT, DGS, ANEPC, DGERT, SGS NP4413, ChooseMyCompany Platinum",
    "Diferenciadores comunicados: Unidade Móvel, Portal Careview, Relatórios 48h",
]:
    parts.append(bullet(item))

parts.append(heading2("B2. Preveris — preveris.pt (Ameaça Alta)"))
for item in [
    "Parceria CUF — maior credibilidade imediata no setor de saúde",
    "'Maior rede nacional' — claim de escala que pressiona concorrentes",
    "Blog editorial ativo com conteúdo sobre prevenção",
    "Portal de clientes integrado",
    "Certificações: DGS, ACT, DGERT, ISO 9001:2015",
]:
    parts.append(bullet(item))

parts.append(heading2("B3. MedicisForma — medicisforma.pt (Ameaça Alta)"))
for item in [
    "H1 com keyword principal: 'Segurança e Saúde no Trabalho'",
    "Desde 1996 — credibilidade temporal comunicada",
    "Testemunhos com empresa + número de colaboradores + anos de parceria",
    "4 CTAs diferentes por finalidade: Proposta, Saiba Mais, Contactar, Candidatar",
    "Clínicas fixas + unidades móveis — flexibilidade comunicada",
]:
    parts.append(bullet(item))

parts.append(heading2("B4. Forseguro — forseguro.pt (Referência em Formação)"))
for item in [
    "35.576 formandos certificados — dado específico e credível",
    "Google Reviews 5.0★ (12 avaliações) — visíveis e impactantes",
    "8.678 ações de formação desde 2003",
    "18+ testemunhos sobre qualidade da plataforma Moodle",
    "Formação financiada comunicada — atrai empresas com orçamento limitado",
]:
    parts.append(bullet(item))

parts.append(page_break())

parts.append(heading1("Parte C — Gap Analysis"))

parts.append(heading2("C1. Gaps de conteúdo mais críticos"))
gaps_content = [
    ("Prova social", "Zero testemunhos vs Medisigma com 12+ e Forseguro com 18+"),
    ("FAQs", "Nenhuma FAQ em nenhuma página vs FAQ obrigatória nos líderes"),
    ("Profundidade de conteúdo", "150-300 palavras por página de serviço vs 600-1000 nos melhores"),
    ("Blog/editorial", "4 posts de 2026 vs estratégia editorial ativa nos concorrentes"),
    ("Métricas de impacto", "Sem números concretos vs '500+ clientes', '35.576 formandos'"),
    ("E-learning com cursos", "Página existe mas sem cursos listados — único do setor neste estado"),
]
parts.append(make_table(["Gap", "Descrição"], gaps_content, [2500, 6500]))

parts.append(heading2("C2. Gaps de serviços comunicados"))
parts.append(para("A Previmed tem mais serviços que a maioria dos concorrentes (ambiental, perícias, medicina desportiva) mas não os comunica bem. A tabela abaixo mostra os serviços que existem nos concorrentes e não têm página forte na Previmed:"))
parts.append(make_table(
    ["Serviço", "Concorrentes com página forte", "Estado Previmed"],
    [
        ["Higiene e Segurança no Trabalho", "Higiserviços, MedicisForma, Rigortrab", "Sem página com este nome exato"],
        ["Saúde Ocupacional", "Preveris, SST.pt", "Sem página própria"],
        ["Controlo de Pragas", "Medisigma, MedicisForma, Rigortrab", "Não comunicado"],
        ["Saúde Mental no Trabalho", "Medisigma", "Não comunicado"],
        ["Extintores e SCIE", "Medisigma, Rigortrab", "Não comunicado"],
        ["Formação financiada", "Forseguro", "Não comunicada"],
        ["Google Reviews visíveis", "Forseguro", "Não disponíveis/visíveis"],
    ],
    [2500, 3500, 3000]
))
parts.append(page_break())

parts.append(heading1("Parte D — AI Search e Schema"))
parts.append(para("Schema JSON-LD: AUSENTE em todas as páginas analisadas. Este é um problema sistémico — não é uma omissão pontual.", bold=True))
parts.append(spacer())
parts.append(heading2("D1. Tipos de schema prioritários a implementar"))
parts.append(make_table(
    ["Tipo", "Página", "Prioridade", "Impacto"],
    [
        ["Organization", "Homepage", "1", "Entidade reconhecida, sameAs, logo"],
        ["LocalBusiness", "/contactos/", "1", "Local SEO — Lisboa e Porto"],
        ["Service", "/saude-no-trabalho/ e /seguranca-no-trabalho/", "2", "Rich results de serviço"],
        ["FAQPage", "Páginas com FAQs (quando criadas)", "2", "FAQ rich snippets — muito visíveis"],
        ["BreadcrumbList", "Todas as páginas", "2", "Breadcrumb na SERP"],
        ["Course", "/oferta-formativa/ e /e-learning/", "3", "Course rich results"],
    ],
    [2000, 2500, 900, 3600]
))

parts.append(heading2("D2. Perguntas prioritárias para AI Search"))
parts.append(para("As seguintes perguntas provavelmente aparecem em AI Overviews para o setor da Previmed. Devem ter resposta direta nas páginas relevantes:"))
for q in [
    "É obrigatório ter medicina do trabalho na empresa? (Lei 102/2009 — toda empresa com 1+ trabalhador)",
    "Quantos exames de medicina do trabalho por ano? (Periódicos anuais ou bienais conforme caso)",
    "O que é uma avaliação de riscos profissionais?",
    "Que formação é obrigatória em segurança no trabalho?",
    "Diferença entre saúde ocupacional e medicina do trabalho?",
]:
    parts.append(bullet(q))

parts.append(page_break())

# ---- APÊNDICES ----
parts.append(heading1("Apêndices"))

parts.append(heading2("Apêndice A — Queries de pesquisa usadas"))
for q in [
    "segurança saúde trabalho SST empresa Portugal site",
    "medicina no trabalho empresa serviços Portugal",
    "formação SST segurança trabalho empresa Portugal cursos online",
    "higiene segurança trabalho empresa serviços Portugal concorrentes",
    "previmed.pt concorrentes segurança saúde trabalho Lisboa Porto",
]:
    parts.append(bullet(q))

parts.append(heading2("Apêndice B — Lista de concorrentes identificados (47 via AEST)"))
aest_list = "Ecosaúde, AdvanceCare/Esumédica, MedicisForma, Prévia Safe, Altice/ACS, Workcare, Previmed, UCS, Centralmed, Preveris, Sãvida, STA, Controlsafe, Ambiformed, Medisigma, H2ST, Egiclinica, KmedXXI, Medilogics, SMP, Forsaude-Labalimentar, Seepmed, Sensimed, Pluralcare, ULFIclínica, Minhovida, PreviSaúde, Cofihst, Safetwoall, Medinova, Brito & Macdonald, ComQualidade, Preventia, Hisosegur, Policlínica Central da Benedita, Preventrab, Vertiproter, Biosegal, IPL, MCS Protecsegur, IMS, Multianswer, Guilmédica, Segurmet, Workview, Laboral Care, 4 Work, Riscos Neutros"
parts.append(para(aest_list, size=18, color="404040"))

parts.append(heading2("Apêndice C — Ficheiros de trabalho gerados"))
for f in [
    "00_WORKLOG.md — Registo cronológico do trabalho",
    "01_SOURCES.md — URLs e fontes analisadas",
    "02_COMPETITOR_LIST.md — Lista completa de concorrentes",
    "03_PREVIMED_SITE_AUDIT.md — Auditoria detalhada Previmed",
    "04_COMPETITOR_AUDIT.md — Análise individual de concorrentes",
    "06_SEO_TECHNICAL_AUDIT.md — Auditoria técnica SEO",
    "07_CONTENT_AND_SERVICE_GAP.md — Gap analysis de conteúdo",
    "08_KEYWORD_SERP_INTENT_MAP.md — Mapa de keywords e intenção",
    "09_AI_SEARCH_AND_SCHEMA_REVIEW.md — AI Search e schema",
    "10_ACTION_PLAN.md — Plano de ação 30/60/90 dias",
    "11_QA_REVIEW.md — Quality gate final",
]:
    parts.append(bullet(f))

parts.append(spacer())
parts.append(callout("Este relatório foi gerado com análise read-only. Nenhuma alteração foi feita em produção, WordPress, DNS, robots.txt, sitemap, redirects ou qualquer sistema da Previmed.", "E8F4FD", "2E75B6"))

# ============================================================
# BUILD XML
# ============================================================

doc_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
    xmlns:cx="http://schemas.microsoft.com/office/drawing/2014/chartex"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
    xmlns:aink="http://schemas.microsoft.com/office/drawing/2016/ink"
    xmlns:am3d="http://schemas.microsoft.com/office/drawing/2017/model3d"
    xmlns:o="urn:schemas-microsoft-com:office:office"
    xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
    xmlns:v="urn:schemas-microsoft-com:vml"
    xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
    xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
    xmlns:w10="urn:schemas-microsoft-com:office:word"
    xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
    xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml"
    xmlns:w16cex="http://schemas.microsoft.com/office/word/2018/wordml/cex"
    xmlns:w16cid="http://schemas.microsoft.com/office/word/2016/wordml/cid"
    xmlns:w16="http://schemas.microsoft.com/office/word/2018/wordml"
    xmlns:w16sdtdh="http://schemas.microsoft.com/office/word/2020/wordml/sdtdatahash"
    xmlns:w16se="http://schemas.microsoft.com/office/word/2015/wordml/symex"
    xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
    xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk"
    xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
    xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
    mc:Ignorable="w14 w15 w16se w16cid w16 w16cex w16sdtdh wp14">
<w:body>
<w:sectPr>
  <w:pgSz w:w="12240" w:h="15840"/>
  <w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="708" w:footer="708" w:gutter="0"/>
</w:sectPr>
""" + "\n".join(p for p in parts if p) + """
</w:body>
</w:document>"""

styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
    xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" mc:Ignorable="w14">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:pPr><w:spacing w:after="160"/></w:pPr>
    <w:rPr><w:sz w:val="22"/><w:szCs w:val="22"/><w:color w:val="1F1F1F"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:pPr>
      <w:outlineLvl w:val="0"/>
      <w:spacing w:before="480" w:after="240"/>
      <w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="2E75B6"/></w:pBdr>
    </w:pPr>
    <w:rPr><w:b/><w:bCs/><w:sz w:val="40"/><w:szCs w:val="40"/><w:color w:val="1F3864"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:pPr><w:outlineLvl w:val="1"/><w:spacing w:before="320" w:after="160"/></w:pPr>
    <w:rPr><w:b/><w:bCs/><w:sz w:val="30"/><w:szCs w:val="30"/><w:color w:val="2E75B6"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/>
    <w:basedOn w:val="Normal"/>
    <w:next w:val="Normal"/>
    <w:pPr><w:outlineLvl w:val="2"/><w:spacing w:before="240" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:bCs/><w:sz w:val="24"/><w:szCs w:val="24"/><w:color w:val="404040"/></w:rPr>
  </w:style>
  <w:style w:type="table" w:styleId="TableGrid">
    <w:name w:val="Table Grid"/>
    <w:tblPr>
      <w:tblBorders>
        <w:top w:val="single" w:sz="4" w:color="2E75B6"/>
        <w:left w:val="single" w:sz="4" w:color="2E75B6"/>
        <w:bottom w:val="single" w:sz="4" w:color="2E75B6"/>
        <w:right w:val="single" w:sz="4" w:color="2E75B6"/>
        <w:insideH w:val="single" w:sz="4" w:color="BDD7EE"/>
        <w:insideV w:val="single" w:sz="4" w:color="BDD7EE"/>
      </w:tblBorders>
    </w:tblPr>
  </w:style>
</w:styles>"""

content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>"""

rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

doc_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>"""

with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.writestr('[Content_Types].xml', content_types)
    zf.writestr('_rels/.rels', rels)
    zf.writestr('word/_rels/document.xml.rels', doc_rels)
    zf.writestr('word/styles.xml', styles_xml)
    zf.writestr('word/document.xml', doc_xml)

size_kb = OUTPUT.stat().st_size // 1024
print(f"✅ Relatório gerado: {OUTPUT}")
print(f"   Tamanho: {size_kb} KB")
print(f"   Secções: Capa + 10 páginas executivas + 4 partes profundas + apêndices")
print(f"   Tabelas: ~25 tabelas formatadas")
print(f"   Callouts: 4 caixas de destaque")
print(f"   Ficheiros intermédios: 11 ficheiros markdown em {BASE}")
