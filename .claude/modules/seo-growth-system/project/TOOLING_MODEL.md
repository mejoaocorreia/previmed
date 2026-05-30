# SEO Tooling Model

Fonte de verdade para ferramentas e MCPs do **SEO Growth System**.

Este ficheiro define que ferramentas o module pode usar, com que cuidados, a política de orçamento e o que nunca assumir sobre disponibilidade ou autorização de ferramentas.

Este ficheiro não é um agente.  
Este ficheiro não acede a ferramentas.  
Este ficheiro não substitui o `seo-data-analyst`, o `technical-seo` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que qualquer agente do module usa ferramentas de forma responsável — sem assumir que estão instaladas, sem assumir autenticação, sem inventar dados quando a ferramenta não está disponível, e com autorização explícita para ferramentas pagas ou com acesso a dados reais.

---

## Âmbito

Este documento cobre:

- política de orçamento;
- ferramentas gratuitas disponíveis;
- ferramentas pagas e quando usar;
- regras de segurança transversais;
- o que nunca assumir sobre ferramentas;
- o que fazer quando uma ferramenta não está disponível.

---

## Fora de âmbito

- procedimento de análise passo a passo — ver skills individuais;
- KPIs e métricas — ver `KPI_MODEL.md`;
- persistência de resultados — ver `REPORTING_MODEL.md`.

---

## Política de orçamento

**Padrão: ferramentas gratuitas.**

Este module opera por defeito com ferramentas gratuitas.

Ferramentas pagas (Ahrefs, Semrush, DataForSEO, SerpAPI, Screaming Frog paid, etc.) **requerem autorização explícita** antes de ser usadas.

Sem autorização explícita:

- não usar ferramentas pagas;
- não inventar os dados que essas ferramentas dariam (volumes finos, backlinks, rank tracking, site audit automático);
- declarar claramente "dados indisponíveis sem ferramenta autorizada".

**Nota de exportabilidade:** a decisão de orçamento é por-projecto. Cada repo que usa este module define a sua política. Este module assume zero até autorização em contrário.

---

## Regras de segurança transversais

**Válidas para todas as ferramentas:**

- **Read-only por defeito.** Nenhuma ferramenta deve ser usada para alterar dados externos sem autorização.
- **Sem tokens no repo.** Nunca guardar API keys, tokens ou credenciais em ficheiros do repo. Usar `.env` ou sistema de secrets do ambiente.
- **Sem alteração de GSC/GBP sem aprovação.** Search Console e Google Business Profile só em leitura. Qualquer alteração exige Supervisor.
- **Sem deploy.** Nenhuma ferramenta executa deploy ou publicação automática.
- **Sem instalar plugins/dependências sem autorização.** Qualquer adição a WordPress ou ambiente requer aprovação.
- **Preferir staging/preview.** Validar em ambiente seguro antes de produção.

---

## Stack de ferramentas gratuitas

### Análise e dados

| Ferramenta | Função | Cuidados |
|---|---|---|
| Google Search Console | Queries, clicks, impressões, CTR, posição, indexação, cobertura, CWV field | Read-only; amostragem em propriedades grandes; posição média ≠ ranking fixo |
| GA4 | Sessões orgânicas, conversões, engagement, landing pages | Read-only; dados agregados; verificar modelo de atribuição activo |
| URL Inspection Tool/API | Estado de indexação, canonical escolhido, cobertura | Só em propriedades geridas; respeitar quotas da API |
| PageSpeed Insights API | Lighthouse (lab data), CWV/CrUX, SEO checks | Read-only; distinguir lab de field; CrUX indisponível para URLs de baixo tráfego |
| CrUX API | Field data de CWV por origem ou URL | Indisponível para URLs de baixo tráfego |
| Keyword Planner | Volumes em buckets | Requer conta Google Ads; valores são em bucket, não exactos |

### SERP e pesquisa

| Ferramenta | Função | Cuidados |
|---|---|---|
| Browser/Search (Playwright MCP) | SERPs ad-hoc, AI Mode/AI Overview, auditoria competitiva, render mobile/desktop, crawling leve | Read-only; sem scraping agressivo; registar data, localização e dispositivo |
| Rich Results Test | Validação de schema (UI Google) | Read-only; URL deve ser acessível |
| Schema.org validator | Validação de markup schema | Read-only; apenas valida estrutura, não semântica business |

### WordPress e técnico

| Ferramenta | Função | Cuidados |
|---|---|---|
| Chrome DevTools MCP | Performance, network, rendering, DOM, debug | Read-only; não alterar nada |
| Filesystem MCP | Ler ficheiros de tema/plugin; criar records | Read-only para tema/plugin; escrita para records autorizada |
| Git/GitHub | Criar branch, PR, verificar histórico | Alterações de código requerem autorização |
| Bing Webmaster Tools | Cobertura Bing/assistentes | Avaliar por projecto; similar ao GSC |

### Local SEO

| Ferramenta | Função | Cuidados |
|---|---|---|
| Google Business Profile API | Local SEO, verificação de perfil | Read-only; qualquer alteração exige autorização do Supervisor |

---

## Mapeamento Por Area / Agente

Este mapa ajuda o `seo-lead` e o comando [`/seo`](../commands/seo.md) a escolher ferramentas sem assumir disponibilidade.

| Area | Ferramentas possiveis | Usos | Requer autorizacao? | Riscos |
|---|---|---|---|---|
| Technical SEO | Playwright, Chrome DevTools, Lighthouse, PageSpeed Insights, CrUX, GSC, URL Inspection, filesystem read-only | crawl leve, render, indexacao, canonical, robots, sitemap, CWV, templates | GSC/URL Inspection e filesystem fora do repo exigem autorizacao; escrita sempre exige autorizacao | alterar URLs/indexacao/producao sem plano; confundir lab data com field data |
| Content | Browser/Search, GSC, filesystem read-only | SERP, intencao, pagina existente, gaps, queries reais | GSC e leitura de repos privados exigem autorizacao | inventar claims, copiar concorrentes, publicar sem revisao |
| Keywords/SERP | Browser/Search, GSC, Keyword Planner, Ahrefs/Semrush/DataForSEO/SerpAPI | clusters, intencao, concorrentes, volumes, SERP features | ferramentas pagas e contas autenticadas exigem autorizacao explicita | inventar volumes/rankings; scraping agressivo |
| Schema | Rich Results Test, Schema.org validator, Browser/Playwright, filesystem read-only | validar JSON-LD, entidades, duplicacao, conteudo visivel | leitura externa normalmente read-only; implementar exige autorizacao | schema enganador, dados nao visiveis, duplicacao por plugin/tema |
| Local SEO | Google Business Profile, Browser/Search, NAP/citation checks, Schema.org validator | GBP, NAP, reviews, paginas locais, LocalBusiness | GBP sempre requer autorizacao; escrita nunca sem Supervisor | doorway pages, moradas falsas, NAP inconsistente |
| Performance | PageSpeed Insights, CrUX, Lighthouse, Chrome DevTools, Playwright | LCP, INP, CLS, mobile, render, network | ferramentas publicas read-only; alteracoes exigem autorizacao | otimizar destruindo UX/design; assumir field data inexistente |
| Data | GSC, GA4, CrUX, PageSpeed, exports agregados | insights, KPIs, brand/non-brand, landing pages, conversoes | sempre confirmar autorizacao e propriedade | dados pessoais, conclusoes sem periodo/comparacao, exports excessivos |
| AI Search / GEO | Browser/Search, Playwright, SERP observation, schema validators | observar AI Overviews/AI Mode quando disponivel, entidades, conteudo citavel | browser read-only; ferramentas pagas/autenticadas exigem autorizacao | prometer presenca em AI Overviews; criar conteudo para bots |
| WordPress | filesystem read-only, Git/GitHub, Playwright, WordPress admin, GSC | descobrir plugin/tema, planear implementacao, PR, validar staging | WordPress admin, escrita, Git/GitHub write e producao exigem autorizacao | quebrar producao, expor credenciais, instalar plugin sem aprovacao |
| Records/reporting | filesystem, Git/GitHub, templates de records | criar records, ligar reports/tasks/decisions | escrita em repo exige autorizacao conforme contexto | guardar dados sensiveis, tokens ou exports desnecessarios |

Regras deste mapa:

- nunca assumir ferramenta autenticada;
- nunca assumir dados reais;
- dados reais so em read-only e com autorizacao;
- ferramentas pagas so com autorizacao explicita;
- WordPress admin so com autorizacao explicita;
- sem credenciais em records;
- sem inventar dados quando a ferramenta nao existe.

---

## Ferramentas pagas — apenas com autorização

Exemplos de ferramentas pagas que requerem autorização explícita:

- **Ahrefs:** backlinks, site audit, rank tracking, keywords.
- **Semrush:** keywords, SERP, site audit, backlinks, position tracking.
- **DataForSEO:** keywords, SERP, rank tracking programático.
- **SerpAPI / ValueSERP:** SERP automático em escala.
- **Screaming Frog (paid):** crawl avançado.
- **Moz:** DA, backlinks, keywords.

Se não há autorização:

- declarar claramente que estes dados não estão disponíveis;
- não estimar valores que dependeriam destas ferramentas;
- trabalhar com as fontes gratuitas disponíveis.

---

## Comportamento quando ferramenta não está disponível

Para cada ferramenta indisponível:

1. **Declarar a indisponibilidade** explicitamente na análise.
2. **Propor alternativa gratuita** quando existir.
3. **Marcar como hipótese** qualquer conclusão que dependeria dessa ferramenta.
4. **Não inventar** dados que a ferramenta daria.

Exemplo:

> "Volumes de pesquisa não estão disponíveis sem ferramenta paga autorizada. Priorizando clusters por intenção comercial estimada e dados de GSC."

---

## Autenticação e acesso

**Quando uma ferramenta requer autenticação:**

- Confirmar que há autorização antes de aceder.
- Usar as credenciais do ambiente (não hardcoded no repo).
- Confirmar que é a propriedade/conta correcta.
- Usar apenas em leitura salvo autorização explícita para escrita.

**Nunca:**

- guardar API keys ou tokens em ficheiros do repo;
- usar credenciais pessoais sem autorização do dono da conta;
- aceder a propriedades GSC/GA4 sem confirmar que pertencem ao projecto.

---

## Gates

**Bloquear ou declarar limitação** quando:

- ferramenta paga necessária sem autorização;
- autenticação necessária sem confirmação;
- acesso a dados de produção sem autorização;
- ferramenta não disponível e análise depende dela.

---

## Relação com agentes, skills e comandos

- Todos os agentes consultam este ficheiro quando precisam de dados externos.
- [`seo-data-analyst`](../agents/seo-data-analyst.md) — principal utilizador de GSC/GA4/CrUX.
- [`technical-seo`](../agents/technical-seo.md) — GSC, URL Inspection, Playwright, PageSpeed.
- [`cwv-performance-seo`](../agents/cwv-performance-seo.md) — PageSpeed, CrUX, DevTools.
- [`serp-competitor-analyst`](../agents/serp-competitor-analyst.md) — Browser/Playwright, Rich Results.
- [`schema-entity`](../agents/schema-entity.md) — Rich Results Test, Schema.org validator.
- [`local-seo`](../agents/local-seo.md) — GBP API (read-only).

---

## Regra final

Nunca assumir que uma ferramenta está disponível.

Nunca assumir que há autenticação activa.

Nunca inventar dados que dependem de ferramenta não autorizada.

Declarar sempre fonte, limitações e o que ficou por confirmar.
