# SEO Growth System (Module)

Equipa SEO / crescimento orgânico como **module reutilizável e exportável**.

## O que é
O SEO Growth System é a capacidade de crescimento orgânico, visibilidade, autoridade, conteúdo estratégico, SEO técnico, schema/entidades, local SEO, performance/Core Web Vitals, AI Search e medição — organizada como **um module único**, com SEO Lead e subagentes bem definidos.

Deixou de estar espalhado por `.claude/agents|commands|project|skills/seo-growth-system/`. **A fonte da verdade é este module.** Os caminhos antigos são pontes para o Claude Code descobrir/invocar o module.

## Fasquia
Alta. O objetivo é trabalho SEO profissional, não básico — mesmo que gaste mais tokens quando a tarefa o justificar. SEO excelente alinha intenção, qualidade, técnica, autoridade, velocidade, experiência e negócio. Se uma proposta melhora ranking mas piora confiança, UX ou performance, **não está pronta**.

## Como está organizado
- [`manifest.md`](manifest.md) — identidade do module, quando usar, o que inclui, como exportar/ligar a um workspace.
- [`agents/`](agents/) — SEO Lead + 14 subagentes especializados.
- [`commands/seo.md`](commands/seo.md) — comando único `/seo` com modos. Ponte global em `.claude/commands/seo.md`.
- [`project/`](project/) — operating system, regras, quality gate e playbooks (fonte de detalhe operacional).
- [`skills/`](skills/) — procedimentos reutilizáveis.

Os **templates de records SEO** não ficam dentro do module — vivem em [`.claude/records/templates/seo/`](../../records/templates/seo/README.md). Os records reais vivem em `.claude/records/`.

## Como é chamado
1. O **supervisor** identifica que o pedido toca web/search/content/WordPress SEO.
2. Encaminha para o **SEO Lead** ([`agents/seo-lead.md`](agents/seo-lead.md)) — o supervisor não faz SEO diretamente.
3. O SEO Lead decide que subagentes/skills/project docs usar (ver "Routing interno SEO" no seu ficheiro).
4. Em trabalhos importantes, passa por **SEO QA** antes da entrega.
5. Análises grandes são persistidas como records (ver `project/REPORTING_MODEL.md`; templates em `.claude/records/templates/seo/`).

## Limites (governação vence sempre)
Segurança, RGPD/dados pessoais, produção, WordPress safety, rollback e escopo são do **supervisor / system-safety**. O SEO recomenda; não passa por cima destes limites. SEO não deve contaminar workspaces que não são web/search/content.

## Referências externas base (fonte única)
Para evitar repetição, as referências oficiais ficam **só aqui**. Os agentes e project docs apontam para esta secção em vez de repetir a lista.

- Google Search Essentials — https://developers.google.com/search/docs/essentials
- Google SEO Starter Guide — https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Helpful, reliable, people-first content — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- AI features and your website — https://developers.google.com/search/docs/appearance/ai-features
- Structured data general guidelines — https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Structured data introduction — https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Core Web Vitals and Google Search — https://developers.google.com/search/docs/appearance/core-web-vitals
- URL Inspection API — https://developers.google.com/search/blog/2022/01/url-inspection-api
- URL Inspection Tool — https://support.google.com/webmasters/answer/9012289
- Search spam policies — https://developers.google.com/search/docs/essentials/spam-policies
- Google Business Profile local ranking — https://support.google.com/business/answer/7091
- Schema.org — https://schema.org

## Generalidade / exportabilidade
Este module é **genérico**. Não contém dados específicos da Previmed (serviços, leis, entidades, clusters). Esses dados vivem no workspace que usa o module e/ou em records reais. Assim, o module pode ser exportado para outros projetos (ver `manifest.md` → "Como exportar/reutilizar").

## Estado atual
Module estruturado e consolidado (estrutura final). Sem código funcional, sem comandos automáticos.
