# Organic Growth / SEO System Index

This folder contains the high-end SEO and organic growth agent system.

Scope includes:
- competitor research;
- keyword and search-intent strategy;
- technical SEO;
- WordPress SEO implementation;
- local SEO;
- schema and entity modelling;
- internal linking;
- content briefs and on-page quality;
- Core Web Vitals and performance SEO;
- AI Search / GEO visibility;
- SEO QA and reporting.

The name **organic-growth** is intentional: this is broader than a narrow SEO checklist.

## Como ler esta pasta

### 1. Operating system (regras de trabalho)

- [`SEO_OPERATING_SYSTEM.md`](./SEO_OPERATING_SYSTEM.md) — workflow, regras, **persistence rule**, **anti-token-waste**. Ler primeiro.
- [`SEO_QUALITY_BAR.md`](./SEO_QUALITY_BAR.md), [`SEO_CONTENT_SYSTEM.md`](./SEO_CONTENT_SYSTEM.md), [`SEO_TECHNICAL_AUDIT.md`](./SEO_TECHNICAL_AUDIT.md), [`SEO_SCHEMA_ENTITY_MODEL.md`](./SEO_SCHEMA_ENTITY_MODEL.md), [`SEO_LOCAL_PLAYBOOK.md`](./SEO_LOCAL_PLAYBOOK.md), [`SEO_KPI_MODEL.md`](./SEO_KPI_MODEL.md), [`SEO_COMPETITOR_RESEARCH_PROTOCOL.md`](./SEO_COMPETITOR_RESEARCH_PROTOCOL.md), [`SEO_TOOLING_MCP_STACK.md`](./SEO_TOOLING_MCP_STACK.md) — playbooks específicos por área.

### 2. Ficheiros vivos (consulta rápida, sempre atualizados)

- [`SEO_CURRENT_STATUS.md`](./SEO_CURRENT_STATUS.md) — estado atual curto + último relatório.
- [`SEO_BACKLOG.md`](./SEO_BACKLOG.md) — tarefas acionáveis priorizadas.
- [`SEO_OPPORTUNITIES.md`](./SEO_OPPORTUNITIES.md) — hipóteses/ideias antes de virarem tarefas.
- [`SEO_DECISION_LOG.md`](./SEO_DECISION_LOG.md) — decisões SEO duradouras.
- [`SEO_GLOSSARY.md`](./SEO_GLOSSARY.md) — glossário plain-language (AIO, E-E-A-T, cluster, etc.). Consultar sempre que aparecer um termo técnico.

### 3. Reports (snapshots datados, históricos)

- [`reports/`](./reports/) — análises completas, datadas (`YYYY-MM-DD__report-type.md`). Não editar depois de publicar.
- [`reports/_TEMPLATE_seo-report.md`](./reports/_TEMPLATE_seo-report.md) — template obrigatório para qualquer relatório novo.
- [`reports/README.md`](./reports/README.md) — explicação completa do formato.

### 4. Estratégia (Fase 1, fechada)

- [`STRATEGY.md`](./STRATEGY.md) — documento mestre da estratégia.
- [`STRATEGY_AUDIENCES.md`](./STRATEGY_AUDIENCES.md), [`STRATEGY_INFORMATION_ARCHITECTURE.md`](./STRATEGY_INFORMATION_ARCHITECTURE.md), [`STRATEGY_KEYWORDS.md`](./STRATEGY_KEYWORDS.md), [`STRATEGY_COMPETITORS.md`](./STRATEGY_COMPETITORS.md) — drill-downs por área.

### 5. Análises da Fase 2 (em curso)

- [`AUDIT_PREVIMED_BASELINE.md`](./AUDIT_PREVIMED_BASELINE.md) — auditoria técnica baseline.
- [`DECISION_KEYWORD_DATA_TOOL.md`](./DECISION_KEYWORD_DATA_TOOL.md) — decisão pendente sobre tool de keyword data.
- [`SETUP_GSC_GA4.md`](./SETUP_GSC_GA4.md) — checklist de ligação GSC/GA4/PSI (lado utilizador).

> Estes 3 ficheiros são da Fase 2 e existem fora de `reports/` por razões históricas. **Análises grandes futuras** devem ir para `reports/YYYY-MM-DD__*.md` conforme a [persistence rule](./SEO_OPERATING_SYSTEM.md#persistence-rule).

### 6. Capturas brutas

- [`aio-captures/`](./aio-captures/) — snapshots Playwright em raw YAML (evidência). Não são análise.

## Regra-chave

> Análise SEO grande sem ficheiro persistente = desperdício de contexto.

Ver [`SEO_OPERATING_SYSTEM.md`](./SEO_OPERATING_SYSTEM.md#anti-token-waste) para detalhe.
