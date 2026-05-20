# SEO Tooling & MCP Stack

Este ficheiro lista ferramentas e MCPs úteis para um SEO Lead de alto nível.

## Política orçamental — orçamento zero

> **Decisão 2026-05-20** (ver [`_living/DECISION_LOG.md`](./_living/DECISION_LOG.md)): toda a stack SEO opera com ferramentas **gratuitas**. Sem subscrições pagas. Sem APIs com top-up.
>
> As 6 opções pagas avaliadas (DataForSEO, SerpAPI, Ahrefs, Semrush, SE Ranking, híbrido) foram rejeitadas. Detalhe completo em [`setup/KEYWORD_DATA_DECISION.md`](./setup/KEYWORD_DATA_DECISION.md).
>
> **Trade-offs aceites**: sem volumes finos (Keyword Planner em buckets), sem competitor ranked keywords automatizadas, sem rank tracking automatizado, sem backlinks data profunda, sem dashboard SaaS.
>
> Qualquer proposta de uso de ferramenta paga **requer reavaliação explícita** desta decisão.

## Stack atual (todas grátis)

| Ferramenta | Função | Estado |
|---|---|---|
| Google Search Console | Queries reais com cliques/impressões — fonte de verdade | ⏳ a ligar (Lote 2.4) |
| GA4 | Comportamento pós-clique | ⏳ a ligar (Lote 2.4) |
| Google Site Kit (WP) | Bridge GSC/GA4 no admin WordPress | ⏳ a ligar (Lote 2.4) |
| Google Keyword Planner | Volumes em buckets (requer conta Ads ativa) | ⏳ a ligar (Lote 2.4) |
| Playwright MCP | SERPs ad-hoc + Modo IA + auditoria competitiva | ✅ ativo (já usado em 2 relatórios) |
| Chrome DevTools MCP | Performance, network, debug | ✅ ativo |
| PageSpeed Insights API | Lighthouse, Core Web Vitals, CrUX | ⏳ API key por criar (Lote 2.4) |
| Rich Results Test | Validação de schema (UI Google) | ✅ disponível (UI manual) |
| Schema.org Validator | Validação de schema (UI) | ✅ disponível (UI manual) |
| URL Inspection API | Estado de indexação | ⏳ ligada via GSC |
| Bing Webmaster Tools | Cobertura Bing/ChatGPT | ⏳ por avaliar |

## Stack rejeitada (paga)

Não usar sem reabrir a decisão de 2026-05-20:

- DataForSEO (~$300/ano)
- SerpAPI (~$300/ano)
- Ahrefs Lite/Standard (~$1 548–$2 988/ano)
- Semrush Pro (~$1 668/ano)
- SE Ranking (~$660/ano)
- Screaming Frog paid licence (~£200/ano)

## Essenciais

### Browser/Search MCP
Uso:
- pesquisar concorrentes;
- recolher SERP features;
- observar titles/descriptions;
- verificar intenção.

Cuidados:
- não scraping agressivo;
- respeitar limites;
- preferir APIs quando possível.

### Google Search Console API/MCP
Uso:
- queries;
- páginas;
- CTR;
- impressões;
- posição média;
- datas;
- dispositivo;
- país;
- comparação antes/depois.

Regras:
- read-only por defeito;
- cuidado com limitações e amostragem/linhas;
- não confundir posição média com ranking fixo.

### URL Inspection API/MCP
Uso:
- estado de indexação;
- canonical escolhido;
- cobertura;
- última indexação;
- problemas de crawl.

Regras:
- usar apenas em propriedades geridas;
- respeitar quotas.

### GA4 Data API/MCP
Uso:
- sessões orgânicas;
- conversões;
- engagement;
- landing pages;
- device/country;
- funil pós-clique.

Regras:
- dados são agregados;
- evitar somas incorretas;
- BigQuery só se existir.

### PageSpeed Insights API/MCP
Uso:
- Lighthouse;
- performance;
- accessibility;
- SEO checks;
- Core Web Vitals/CrUX quando disponível.

### Chrome DevTools MCP
Uso:
- performance tracing;
- network;
- rendering;
- console;
- DOM;
- debug de problemas reais.

### Playwright MCP
Uso:
- screenshots;
- mobile/desktop;
- navegação;
- validação visual;
- snapshots de acessibilidade;
- crawling leve.

## Muito úteis (avaliar individualmente — preferir versão grátis)

- Sitemap crawler (UI grátis ou Screaming Frog free tier — 500 URLs)
- Broken link checker (ferramenta browser grátis)
- Rich Results Test / Schema validator (Google UI, grátis)
- Screaming Frog **free tier** (até 500 URLs — suficiente para Previmed greenfield)
- Google Business Profile API (gratuita, se aplicável)
- Bing Webmaster Tools (gratuita)
- Figma MCP (uso indireto — design/tokens)

**Bloqueado por decisão 2026-05-20** (não usar sem reabrir decisão): Ahrefs, Semrush, DataForSEO, SerpAPI, Screaming Frog paid.

## Segurança

- não guardar tokens no repo;
- usar `.env`;
- read-only por defeito;
- não alterar Search Console/GBP sem aprovação;
- não fazer deploy;
- não instalar plugins sem aprovação;
- usar staging/preview.
