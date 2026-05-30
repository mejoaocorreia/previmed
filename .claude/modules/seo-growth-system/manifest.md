# Manifest — SEO Growth System

Identidade e contrato do module.

## Nome

`seo-growth-system`

## Versao

`1.1.0`

## Objetivo

Fornecer uma equipa SEO profissional, reutilizavel e exportavel: SEO Lead + subagentes, comando oficial `/seo`, regras/playbooks, skills e templates de records para crescimento organico de qualidade alta.

## Quando Usar

Quando o pedido tocar:

- SEO, pesquisa organica, ranking ou trafego organico;
- web content / conteudo indexavel;
- Google / SERP / Search Console / GA4;
- schema / entidades;
- performance SEO / Core Web Vitals;
- AI Search / AI Overviews / GEO;
- WordPress SEO;
- arquitetura de informacao;
- internal linking;
- local SEO;
- concorrencia organica;
- reporting e KPIs SEO.

## Quando Nao Usar

- Tarefas que nao sao web/search/content.
- Operacoes internas sem impacto SEO.
- Dados de saude, dados pessoais, credenciais, producao, rollback ou decisoes criticas sem Supervisor/System Safety.
- Implementacao WordPress de risco sem autorizacao e handoff apropriado.

## Uso No Repo Atual

Este repo usa o module como capacidade SEO. O module, contudo, e generico e exportavel. Dados especificos do projeto consumidor ficam no workspace/records desse projeto, nao dentro do module.

## Agents Incluidos (15)

`seo-lead` · `technical-seo` · `keyword-intent` · `content-brief` · `content-growth` · `onpage-seo` · `internal-linking` · `schema-entity` · `local-seo` · `serp-competitor-analyst` · `seo-data-analyst` · `cwv-performance-seo` · `ai-search-visibility` · `wordpress-seo-implementation` · `seo-qa`.

## Command Incluido

- `commands/seo.md` — comando oficial `/seo` com modos: `audit`, `technical`, `content`, `brief`, `keywords`, `local`, `schema`, `competitor`, `data`, `performance`, `ai-search`, `wordpress`, `go-live`, `qa`.

## Project Docs Incluidos (12)

`README` · `OPERATING_SYSTEM` · `STRATEGY_RULES` · `TECHNICAL_RULES` · `CONTENT_RULES` · `QUALITY_GATE` · `TOOLING_MODEL` · `KPI_MODEL` · `REPORTING_MODEL` · `SCHEMA_ENTITY_MODEL` · `LOCAL_SEO_PLAYBOOK` · `COMPETITOR_RESEARCH_PLAYBOOK`.

## Skills Incluidas (11)

`technical-seo-crawl-audit` · `content-brief-generation` · `keyword-cluster-map` · `schema-entity-review` · `onpage-optimization-pass` · `seo-quality-gate` · `competitor-gap-analysis` · `local-seo-review` · `cwv-performance-seo-review` · `gsc-ga4-analysis` · `serp-intent-audit`.

Skills deferidas por design:

- `ai-search-visibility-review` — coberta por `ai-search-visibility` + `CONTENT_RULES`/`STRATEGY_RULES`;
- `internal-linking-architecture` — coberta por `internal-linking` + `onpage-optimization-pass`;
- `wordpress-seo-implementation` — coberta por agente proprio + `TECHNICAL_RULES`;
- `seo-reporting-dashboard` — coberta por `REPORTING_MODEL` + `KPI_MODEL`.

## Records Templates

O plugin inclui templates em [`records-templates/`](records-templates/README.md):

- `SEO_AUDIT_TEMPLATE`
- `SEO_TASK_TEMPLATE`
- `SEO_REPORT_TEMPLATE`
- `SEO_DECISION_TEMPLATE`
- `SEO_GO_LIVE_CHECKLIST`

Sao templates, nao records reais. Records reais ficam no projeto consumidor em `.claude/records/`.

## Ferramentas / MCPs Possiveis

O module nao assume ferramentas instaladas ou autenticadas. Ver [`project/TOOLING_MODEL.md`](project/TOOLING_MODEL.md).

Possiveis ferramentas:

- Browser/Search;
- Playwright;
- Chrome DevTools;
- Lighthouse/PageSpeed/CrUX;
- Google Search Console;
- URL Inspection;
- GA4;
- Rich Results Test;
- Schema.org validator;
- Google Business Profile;
- Bing Webmaster Tools / IndexNow;
- Filesystem;
- Git/GitHub;
- Ahrefs/Semrush/DataForSEO/SerpAPI apenas com autorizacao explicita.

## Como Exportar / Reutilizar

1. Copiar ou instalar este module como plugin no repo destino.
2. Instalar via marketplace/plugin.
3. Garantir que o Supervisor do destino encaminha SEO para `/seo` ou `seo-lead`.
4. Manter o module generico: dados especificos ficam no projeto consumidor.
5. Ajustar tooling/autorizacoes no projeto consumidor.

## Estado Atual

Module operacional v1.1. Agentes, skills, comando, project docs e templates alinhados para uso real com Claude Code/plugin.
