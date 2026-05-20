# SEO Tooling & MCP Stack

Este ficheiro lista ferramentas e MCPs úteis para um SEO Lead de alto nível.

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

## Muito úteis

- Sitemap crawler
- Broken link checker
- Rich Results Test / Schema validator
- Screaming Frog / Sitebulb, se disponível
- Ahrefs/Semrush/DataForSEO/SerpAPI, se autorizado
- Google Business Profile API, se aplicável
- Bing Webmaster Tools
- Figma MCP, se design/tokens forem relevantes

## Segurança

- não guardar tokens no repo;
- usar `.env`;
- read-only por defeito;
- não alterar Search Console/GBP sem aprovação;
- não fazer deploy;
- não instalar plugins sem aprovação;
- usar staging/preview.
