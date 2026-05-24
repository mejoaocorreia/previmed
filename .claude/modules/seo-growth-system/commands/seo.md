# Command: /seo

Comando único de entrada do module **SEO Growth System**. Em vez de um ficheiro por microação, há **um comando com modos**.

## Como funciona
1. O comando encaminha sempre para o **SEO Lead** ([`../agents/seo-lead.md`](../agents/seo-lead.md)).
2. O SEO Lead lê o modo, decide os subagentes/skills/project docs e coordena.
3. Em trabalhos importantes, passa por **SEO QA** antes de entregar.
4. Análises grandes são persistidas como records (ver [`../project/REPORTING_MODEL.md`](../project/REPORTING_MODEL.md); templates em [`.claude/records/templates/seo/`](../../../records/templates/seo/README.md)).

## Regras transversais (todos os modos)
- Não alterar o site, WordPress, indexação ou URLs sem autorização do supervisor.
- Read-only por defeito; ferramentas pagas só com autorização.
- Distinguir evidência, hipótese e recomendação. Sem dados reais → hipótese.
- Governação (segurança, RGPD, produção, rollback) vence sempre — é do supervisor/system-safety.

## Modos

### /seo audit
- **Quando:** auditoria/revisão SEO ampla.
- **Agentes:** technical-seo, content-growth, serp-competitor-analyst, seo-data-analyst, cwv-performance-seo, schema-entity, seo-qa.
- **Skills/docs:** `technical-seo-crawl-audit`, `OPERATING_SYSTEM`, `REPORTING_MODEL`.
- **Output:** diagnóstico, evidência, prioridades, riscos, plano por fases, record datado.

### /seo technical
- **Quando:** crawl/index, canonical, redirects, sitemap, robots, render, WordPress técnico.
- **Agentes:** technical-seo (+ cwv-performance-seo, wordpress-seo-implementation se aplicável).
- **Skills/docs:** `technical-seo-crawl-audit`, `TECHNICAL_RULES`.
- **Output:** Technical SEO Review (problemas, impacto, risco, validação).

### /seo content
- **Quando:** rever/criar conteúdo, E-E-A-T, páginas de serviço, refresh.
- **Agentes:** content-growth (+ onpage-seo).
- **Skills/docs:** `seo-quality-gate`, `CONTENT_RULES`.
- **Output:** Content Growth Review (intenção, lacunas, prova, estrutura, riscos).

### /seo brief
- **Quando:** preparar um brief editorial antes de escrever.
- **Agentes:** keyword-intent, content-brief, content-growth.
- **Skills/docs:** `content-brief-generation`, `keyword-cluster-map`, `CONTENT_RULES`.
- **Output:** brief completo acionável.

### /seo keywords
- **Quando:** pesquisa/cluster de keywords e mapeamento de intenção.
- **Agentes:** keyword-intent (+ serp-competitor-analyst).
- **Skills/docs:** `keyword-cluster-map`, `serp-intent-audit`, `STRATEGY_RULES`.
- **Output:** clusters com intenção, página alvo, prioridade, risco de canibalização.

### /seo local
- **Quando:** SEO local, GBP, NAP, páginas locais.
- **Agentes:** local-seo (+ content-brief).
- **Skills/docs:** `local-seo-review`, `LOCAL_SEO_PLAYBOOK`.
- **Output:** oportunidades locais, páginas necessárias, GBP/NAP, citations.

### /seo schema
- **Quando:** dados estruturados e entidades.
- **Agentes:** schema-entity (+ technical-seo).
- **Skills/docs:** `schema-entity-review`, `SCHEMA_ENTITY_MODEL`.
- **Output:** tipos recomendados, propriedades, fonte, páginas, validação.

### /seo competitor
- **Quando:** análise de concorrência/SERP.
- **Agentes:** serp-competitor-analyst.
- **Skills/docs:** `competitor-gap-analysis`, `serp-intent-audit`, `COMPETITOR_RESEARCH_PLAYBOOK`.
- **Output:** concorrentes, padrões SERP, gaps, oportunidades, recomendação (datada).

### /seo data
- **Quando:** análise de Search Console/GA4/PageSpeed.
- **Agentes:** seo-data-analyst.
- **Skills/docs:** `gsc-ga4-analysis`, `KPI_MODEL`.
- **Output:** insight, evidência, hipótese, ação, métrica a monitorizar.

### /seo performance
- **Quando:** Core Web Vitals / performance SEO.
- **Agentes:** cwv-performance-seo (+ wordpress-seo-implementation; Visual Experience se visual).
- **Skills/docs:** `cwv-performance-seo-review`, `TECHNICAL_RULES`.
- **Output:** métrica, causa, recomendação, impacto SEO/UX, teste.

### /seo ai-search
- **Quando:** visibilidade em AI Overviews / AI Mode / GEO.
- **Agentes:** ai-search-visibility, content-growth, schema-entity.
- **Skills/docs:** `STRATEGY_RULES`, `CONTENT_RULES`.
- **Output:** perguntas-alvo, entidades, conteúdo citável, lacunas, estrutura.

### /seo wordpress
- **Quando:** implementar SEO em WordPress.
- **Agentes:** wordpress-seo-implementation, technical-seo.
- **Skills/docs:** `TECHNICAL_RULES`.
- **Output:** onde implementar, ficheiros/configs, risco, teste, rollback.

### /seo go-live
- **Quando:** preparar go-live SEO seguro.
- **Agentes:** seo-qa, technical-seo, wordpress-seo-implementation.
- **Skills/docs:** [`SEO_GO_LIVE_CHECKLIST.md`](../../../records/templates/seo/SEO_GO_LIVE_CHECKLIST.md), `QUALITY_GATE`.
- **Output:** checklist validada, riscos, autorização necessária.

### /seo qa
- **Quando:** revisão final antes de entregar/publicar.
- **Agentes:** seo-qa.
- **Skills/docs:** `seo-quality-gate`, `QUALITY_GATE`.
- **Output:** aprovado/bloqueado, problemas, correções, risco residual.

## Notas de consolidação
Consolida num único comando com modos os vários comandos SEO que antes existiam separados (auditoria, conteúdo, brief, concorrência, dados, local, schema, go-live, estratégia, técnico). As pontes em `.claude/commands/seo-growth-system/` encaminham os nomes antigos para os modos correspondentes.
