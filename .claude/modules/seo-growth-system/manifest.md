# Manifest — SEO Growth System

Identidade e contrato do module.

## Nome
`seo-growth-system`

## Objetivo
Fornecer uma equipa SEO profissional, reutilizável e exportável: SEO Lead + subagentes, comando único `/seo`, regras/playbooks, skills e templates de records — para crescimento orgânico de qualidade alta.

## Quando usar
Quando o pedido tocar:
- SEO, pesquisa orgânica, ranking, tráfego orgânico;
- web content / conteúdo indexável;
- Google / SERP / Search Console / GA4;
- schema / entidades;
- performance SEO / Core Web Vitals;
- AI Search / AI Overviews / GEO;
- WordPress SEO;
- arquitetura de informação, internal linking, local SEO, concorrência orgânica.

## Quando NÃO usar
- Tarefas que não são web/search/content (ex.: operações internas, comercial puro, dados de saúde) — o SEO não deve contaminar esses contextos.
- Decisões de segurança, RGPD, produção, rollback — são do supervisor / system-safety; o SEO recomenda dentro desses limites.
- Implementação WordPress de risco sem WordPress Engineering e autorização.

## Workspaces atuais relacionados
- `departments/web/previmed_pt/` — principal consumidor (site Previmed.pt).
- `departments/operations/careview/` — pode usar capacidades web pontuais, mas não é o foco SEO.

## Departments relacionados
- `web` (dono da capacidade SEO);
- `communications` (conteúdo/linguagem);
- `commercial` (conversão/páginas comerciais);
- `compliance` (transversal — dados, claims, RGPD);
- `health_safety` (conteúdo técnico, quando aplicável ao workspace).

## Agents incluídos (15)
`seo-lead` (coordenador) · `technical-seo` · `keyword-intent` · `content-brief` · `content-growth` · `onpage-seo` · `internal-linking` · `schema-entity` · `local-seo` · `serp-competitor-analyst` · `seo-data-analyst` · `cwv-performance-seo` · `ai-search-visibility` · `wordpress-seo-implementation` · `seo-qa`.

## Commands incluídos
- `commands/seo.md` — comando único `/seo` com modos (`audit`, `technical`, `content`, `brief`, `keywords`, `local`, `schema`, `competitor`, `data`, `performance`, `ai-search`, `wordpress`, `go-live`, `qa`). Disponível como `/seo` após instalar o plugin.

## Project docs incluídos (12)
`README` · `OPERATING_SYSTEM` · `STRATEGY_RULES` · `TECHNICAL_RULES` · `CONTENT_RULES` · `QUALITY_GATE` · `TOOLING_MODEL` · `KPI_MODEL` · `REPORTING_MODEL` · `SCHEMA_ENTITY_MODEL` · `LOCAL_SEO_PLAYBOOK` · `COMPETITOR_RESEARCH_PLAYBOOK`.

## Skills incluídas (11)
`technical-seo-crawl-audit` · `content-brief-generation` · `keyword-cluster-map` · `schema-entity-review` · `onpage-optimization-pass` · `seo-quality-gate` · `competitor-gap-analysis` · `local-seo-review` · `cwv-performance-seo-review` · `gsc-ga4-analysis` · `serp-intent-audit`.

Skills avaliadas e **deferidas** (capacidade coberta por agente/project doc, para evitar selva de skills): `ai-search-visibility-review` (→ agente `ai-search-visibility` + `CONTENT_RULES`/`STRATEGY_RULES`), `internal-linking-architecture` (→ agente `internal-linking` + `onpage-optimization-pass`), `wordpress-seo-implementation` (→ agente `wordpress-seo-implementation` + `TECHNICAL_RULES`), `seo-reporting-dashboard` (→ `REPORTING_MODEL` + `KPI_MODEL`).

## Records templates usados
O plugin **inclui** os templates SEO em [`records-templates/`](records-templates/README.md) — `SEO_AUDIT_TEMPLATE` · `SEO_TASK_TEMPLATE` · `SEO_REPORT_TEMPLATE` · `SEO_DECISION_TEMPLATE` · `SEO_GO_LIVE_CHECKLIST`. São **templates** (não records reais) e vivem dentro do plugin para serem autossuficientes ao exportar. Os **records reais** ficam no projeto-alvo em `.claude/records/`.

## Dependências opcionais futuras
- Ferramentas gratuitas Google (Search Console, GA4, PageSpeed/CrUX, Keyword Planner) — ver `project/TOOLING_MODEL.md`.
- MCPs: Playwright, Chrome DevTools, Lighthouse/PageSpeed, Filesystem, Git/GitHub.
- Ferramentas pagas (Ahrefs/Semrush/DataForSEO/SerpAPI) — **só com autorização explícita**; por defeito o module assume orçamento zero.

## MCPs / ferramentas futuras possíveis
Search/Browser, Search Console API, URL Inspection API, GA4 Data API, PageSpeed Insights API, Rich Results Test, Schema validator, Google Business Profile API, Bing Webmaster Tools/IndexNow. Nenhuma é assumida como instalada; o agente propõe alternativa se faltar.

## Como exportar / reutilizar noutro repo
1. Copiar a pasta `.claude/modules/seo-growth-system/` para o repo destino.
2. Instalar o plugin no destino via `/plugin marketplace add <git-url>` + `/plugin install` (ver `INSTALL.md`). **Não** são precisas pontes manuais — a descoberta de agentes/comando/skills é nativa após a instalação.
3. Garantir que o supervisor do destino encaminha SEO para o SEO Lead do module.
4. Manter o module **genérico**: dados específicos do projeto ficam no workspace/records do destino, não dentro do module.
5. Ajustar `TOOLING_MODEL.md` à realidade de ferramentas do destino.

## Como ligar a um workspace
1. No workspace, criar/atualizar `modules.md` a listar `seo-growth-system` (ver `departments/web/previmed_pt/modules.md`).
2. O workspace referencia o module; **não** copia agentes para dentro de si.
3. Dados/decisões específicas do workspace ficam no workspace e em records reais.

## Estado atual
Module operacional. Todos os agentes, skills, comandos e project docs completos e validados. Pronto para uso após instalação do plugin.
