# SEO Growth System (Module)

Equipa SEO / crescimento orgânico como **module reutilizável e exportável**.

## O que é
O SEO Growth System é a capacidade de crescimento orgânico, visibilidade, autoridade, conteúdo estratégico, SEO técnico, schema/entidades, local SEO, performance/Core Web Vitals, AI Search e medição — organizada como **um module único**, com SEO Lead e subagentes bem definidos.

**A fonte da verdade é este module/plugin.** Todas as antigas pastas/pontes SEO fora do module foram **removidas** — `.claude/project/seo-growth-system/`, `.claude/skills/seo-growth-system/`, `.claude/commands/seo-growth-system/`, `.claude/agents/seo-growth-system/` e a ponte `.claude/commands/seo.md`. **Não há duplicação:** cada agente/skill/comando existe **uma única vez**, aqui. A descoberta nativa faz-se **instalando o plugin** (ver [`INSTALL.md`](INSTALL.md)).

## Plugin Claude Code
Este module é agora um **plugin Claude Code** propriamente formado: tem `.claude-plugin/plugin.json`, e os `agents/`, `commands/seo.md` e `skills/<n>/SKILL.md` têm **frontmatter** (`name`/`description`). Depois de **instalado** (ver [`INSTALL.md`](INSTALL.md)), os 15 agentes/subagentes, o comando `/seo` e as 11 skills passam a ser **descobertos nativamente** pelo Claude Code.

- Instalar neste repo: `/plugin marketplace add .` → `/plugin install seo-growth-system@previmed-marketplace`.
- Exportar para outro repo: `/plugin marketplace add <git-url>` → `/plugin install ...` (zero cópias manuais).
- Os agentes/skills só são descobertos **após instalação** — não basta os ficheiros existirem.

## Fasquia
Alta. O objetivo é trabalho SEO profissional, não básico — mesmo que gaste mais tokens quando a tarefa o justificar. SEO excelente alinha intenção, qualidade, técnica, autoridade, velocidade, experiência e negócio. Se uma proposta melhora ranking mas piora confiança, UX ou performance, **não está pronta**.

## Como está organizado
- [`manifest.md`](manifest.md) — identidade do module, quando usar, o que inclui, como exportar/ligar a um workspace.
- [`agents/`](agents/) — SEO Lead + 14 subagentes especializados.
- [`commands/seo.md`](commands/seo.md) — comando único `/seo` com modos (fica disponível como `/seo` depois de instalar o plugin).
- [`project/`](project/) — operating system, regras, quality gate e playbooks (fonte de detalhe operacional).
- [`skills/`](skills/) — procedimentos reutilizáveis.

- [`records-templates/`](records-templates/README.md) — templates de records SEO (auditorias, reports, decisões, tasks, go-live). Vivem **dentro do plugin** para virem junto ao exportar. Os **records reais** ficam no projeto-alvo em `.claude/records/`.

## Como é chamado
1. O **supervisor** identifica que o pedido toca web/search/content/WordPress SEO.
2. Encaminha para o **SEO Lead** ([`agents/seo-lead.md`](agents/seo-lead.md)) — o supervisor não faz SEO diretamente.
3. O SEO Lead decide que subagentes/skills/project docs usar (ver "Routing interno SEO" no seu ficheiro).
4. Em trabalhos importantes, passa por **SEO QA** antes da entrega.
5. Análises grandes são persistidas como records (ver `project/REPORTING_MODEL.md`; templates em `records-templates/`).

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
Module operacional — 15 agentes, 11 skills, comando `/seo` com 14 modos, 12 project docs, 5 records templates. Pronto para uso com Claude Code após instalação do plugin.
