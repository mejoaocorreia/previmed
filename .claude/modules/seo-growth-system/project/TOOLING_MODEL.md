# SEO Tooling Model

## Objetivo
Definir que ferramentas/MCPs o module pode usar, com que cuidados, e a política de orçamento.

## Quando usar
Sempre que um agente precisa de dados/validação externos.

## Regras principais

### Política de orçamento (padrão: zero)
Por defeito, o module opera com **ferramentas gratuitas**. Ferramentas pagas (Ahrefs, Semrush, DataForSEO, SerpAPI, Screaming Frog paid) **requerem autorização explícita** — se não houver, não inventar os dados que elas dariam (volumes finos, backlinks profundos, rank tracking automatizado).

> Nota de exportação: a decisão de orçamento é por-projeto. Cada repo/destino define a sua. Este module assume zero até autorização em contrário.

### Segurança (transversal)
Read-only por defeito; não guardar tokens no repo (usar `.env`); não alterar Search Console/GBP sem aprovação; não fazer deploy; não instalar plugins/dependências sem autorização; preferir staging/preview.

## Stack de referência (gratuita)
| Ferramenta | Função |
|---|---|
| Google Search Console | Queries reais (cliques/impressões) — fonte de verdade |
| GA4 | Comportamento pós-clique |
| Google Site Kit (WP) | Bridge GSC/GA4 no admin WordPress |
| Keyword Planner | Volumes em buckets (requer conta Ads) |
| Playwright MCP | SERPs ad-hoc, AI Mode, auditoria competitiva, render/mobile |
| Chrome DevTools MCP | Performance, network, debug |
| PageSpeed Insights API | Lighthouse, Core Web Vitals, CrUX |
| Rich Results Test / Schema validator | Validação de schema (UI Google) |
| URL Inspection API | Estado de indexação (via GSC) |
| Bing Webmaster Tools | Cobertura Bing/assistentes (avaliar) |

## Uso por ferramenta (resumo)
- **Search Console:** queries, páginas, CTR, impressões, posição, indexação. Read-only; cuidado com amostragem; posição média ≠ ranking fixo.
- **URL Inspection:** indexação, canonical escolhido, cobertura. Só em propriedades geridas; respeitar quotas.
- **GA4:** sessões orgânicas, conversões, engagement, landing pages. Dados agregados; evitar somas incorretas.
- **PageSpeed/Lighthouse:** performance, CWV/CrUX, SEO checks.
- **Chrome DevTools:** tracing, network, rendering, DOM, debug.
- **Playwright:** screenshots, mobile/desktop, navegação, validação visual, crawling leve. Sem scraping agressivo.
- **Google Business Profile API:** local SEO; não alterar sem autorização.

## Inputs / Outputs
Input: necessidade de dados + autorização. Output: dados com fonte e limitações declaradas.

## Agentes relacionados
Principalmente [`seo-data-analyst`](../agents/seo-data-analyst.md), [`technical-seo`](../agents/technical-seo.md), [`cwv-performance-seo`](../agents/cwv-performance-seo.md), [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md).

## Skills relacionadas
[`gsc-ga4-analysis`](../skills/gsc-ga4-analysis/SKILL.md), [`technical-seo-crawl-audit`](../skills/technical-seo-crawl-audit/SKILL.md).

## Critérios de qualidade
Nunca assumir ferramenta instalada; propor alternativa se faltar; declarar fonte e limitações; nada de tokens no repo.

## Notas de consolidação
Consolidado do tooling/MCP stack da versão anterior do pacote SEO. **Generalizado:** decisões específicas de orçamento e estados de ligação de ferramentas são dados de projeto — vão para records reais do workspace. Aqui fica o modelo reutilizável.
