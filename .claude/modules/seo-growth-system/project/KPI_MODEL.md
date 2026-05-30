# SEO KPI Model

Fonte de verdade para métricas de SEO do **SEO Growth System**.

Este ficheiro define que métricas acompanhar, como interpretá-las correctamente, como organizá-las por fase de projecto e que limitações reconhecer — para que análise de dados SEO gere insights reais, não conclusões apressadas.

Este ficheiro não é um agente.  
Este ficheiro não acede a dados.  
Este ficheiro não substitui o `seo-data-analyst`, a skill `gsc-ga4-analysis` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que o acompanhamento SEO foca as métricas certas para a fase certa do projecto, com períodos comparáveis, separação brand/non-brand e interpretação honesta — sem avaliar SEO apenas por ranking, sem inventar dados e sem tirar conclusões sem evidência suficiente.

---

## Âmbito

Este documento cobre:

- princípios de medição SEO;
- KPIs por fase de projecto;
- métricas de Search Console, GA4 e CrUX;
- regras de comparação de períodos;
- separação brand/non-brand;
- limitações e armadilhas comuns.

---

## Fora de âmbito

- ferramentas e autorização para aceder a dados — ver `TOOLING_MODEL.md`;
- procedimento de análise passo a passo — ver skill `gsc-ga4-analysis`;
- reporting e persistência de records — ver `REPORTING_MODEL.md`.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `KPI_MODEL.md` (este ficheiro) | Standard de KPIs e interpretação |
| [`seo-data-analyst`](../agents/seo-data-analyst.md) | Análise de dados e insights |
| [`gsc-ga4-analysis`](../skills/gsc-ga4-analysis/SKILL.md) | Procedimento de análise |
| [`seo-lead`](../agents/seo-lead.md) | Priorização com base em dados |
| [`REPORTING_MODEL.md`](REPORTING_MODEL.md) | Persistência de análises |

---

## Princípios de medição

**Nunca avaliar SEO apenas por ranking:**
- Ranking varia por localização, dispositivo, histórico de pesquisa e SERP features.
- Ranking sem clicks, impressões ou conversões é uma métrica incompleta.
- Preferir clicks, impressões e conversões orgânicas como métricas primárias.

**Separar sempre brand de non-brand:**
- Brand: queries com nome da empresa. Alta CTR, fácil de dominar.
- Non-brand: queries sem nome da empresa. Representa visibilidade real no mercado.
- Misturar distorce a análise de crescimento orgânico real.

**Comparar períodos equivalentes:**
- Ano-a-ano (YoY) é o mais fiável para sazonalidade.
- Mês-a-mês (MoM) para tendências de curto prazo.
- Evitar comparar Dezembro com Janeiro ou períodos de feriados diferentes.
- Sempre indicar o período exacto.

**Relacionar métricas com acções:**
- Uma subida de tráfego sem acção associada pode ser sazonalidade.
- Uma queda após migração técnica tem causa identificável.
- Sempre tentar ligar variação a acção realizada ou evento externo.

**Sem dados reais → hipótese:**
- Sem GSC ou GA4, não inventar métricas.
- Declarar como hipótese qualquer estimativa sem ferramenta real.

---

## KPIs por fase de projecto

### Fase 1 — Fundamentos

Objectivo: garantir que o site está tecnicamente correcto e tem conteúdo publicado.

**KPIs prioritários:**

| KPI | Fonte | O que medir | Alvo inicial |
|---|---|---|---|
| Páginas indexadas | GSC → Cobertura | Quantas páginas indexadas? | Todas as prioritárias |
| Erros de indexação | GSC → Cobertura | Quantos erros críticos? | 0 erros críticos |
| Sitemap submetido | GSC | Sitemap presente e sem erros? | Sim |
| Titles/metas presentes | Crawl / GSC | Páginas sem title/meta? | 0 páginas críticas sem |
| CWV — LCP mobile | PSI / CrUX | LCP homepage/principais | ≤ 2.5s |
| CWV — CLS | PSI / CrUX | CLS homepage/principais | ≤ 0.1 |
| Páginas prioritárias publicadas | Filesystem/GSC | Serviços principais indexados? | Sim |

**Foco:** resolver bloqueios técnicos antes de olhar para tráfego.

---

### Fase 2 — Crescimento

Objectivo: aumentar visibilidade orgânica e começar a atrair tráfego qualificado.

**KPIs prioritários:**

| KPI | Fonte | O que medir | Meta direcção |
|---|---|---|---|
| Impressões non-brand | GSC | Visibilidade na SERP | Crescimento |
| Clicks non-brand | GSC | Tráfego real | Crescimento |
| CTR médio non-brand | GSC | Eficácia de titles/metas | ≥ 3-5% páginas key |
| Posição média non-brand | GSC | Posicionamento médio | Melhorar para top 20→top 10 |
| Páginas com impressões | GSC | Quantas páginas visíveis | Crescimento |
| Novas queries (MoM) | GSC | Novos tópicos a aparecer | Crescimento |
| Internal links implementados | Crawl | Orphan pages resolvidas? | 0 orphan pages críticas |

**Foco:** conteúdo a ganhar visibilidade, primeiras queries a aparecer.

---

### Fase 3 — Conversão

Objectivo: transformar tráfego orgânico em leads e conversões.

**KPIs prioritários:**

| KPI | Fonte | O que medir | Meta direcção |
|---|---|---|---|
| Leads/conversões orgânicas | GA4 | Formulários, chamadas, chats de origem orgânica | Crescimento |
| Taxa de conversão orgânica | GA4 | Sessões → conversão por landing page | Melhorar |
| CTR para CTAs | GA4 / GSC | Clicks em CTAs de páginas orgânicas | Crescimento |
| Páginas de serviço com melhor retorno | GA4 | Quais convertem mais? | Identificar e priorizar |
| Organic session duration / engagement | GA4 | Qualidade do tráfego | Melhorar |
| Revenue orgânico (se rastreado) | GA4 | Contribuição orgânica para receita | Crescimento |

**Foco:** qualidade do tráfego e impacto em negócio.

---

## KPIs de diagnóstico

**Úteis para identificar problemas específicos:**

| KPI | Quando usar |
|---|---|
| CTR por posição | Detectar titles/metas fracos em posições boas |
| Posição média por query | Identificar oportunidades (posição 4-20) |
| Impressões sem clicks | SERP feature a roubar clicks (AI Overview, snippet) |
| Páginas com queda YoY | Identificar páginas a refrescar ou com problema técnico |
| Cobertura GSC: excluídas | Detectar noindex acidental, canonical issues |
| CrUX por URL | Detectar páginas com mau CWV em campo real |

---

## Armadilhas comuns

| Armadilha | Descrição | Como evitar |
|---|---|---|
| Posição média ≠ ranking | Posição média é a média de todas as impressões (posições 1+80+90 = média 57) | Segmentar por query específica e analisar posições individuais |
| Brand vs non-brand | CTR médio inflacionado por brand (CTR 60%+) esconde fraqueza non-brand | Sempre separar |
| Sazonalidade | Comparar Dezembro com Janeiro dá variações artificiais | Usar YoY ou indicar período exacto |
| Amostragem GSC | Propriedades com muito tráfego têm dados amostrados | Verificar aviso no GSC e declarar |
| GA4 "not provided" | GSC não passa query para GA4 | Usar GSC directamente para análise de queries |
| CrUX indisponível | URLs com pouco tráfego não têm field data | Usar lab data declarando limitação |
| Atribuição GA4 | Last click vs data-driven mudam atribuição | Verificar modelo de atribuição activo |

---

## Métricas a não usar como proxy de sucesso

| Métrica | Porquê não usar sozinha |
|---|---|
| Ranking "número 1" | Varia por utilizador, localização, dispositivo |
| Traffic total | Inclui brand que pode subir por PR sem SEO |
| PageSpeed Score | Score sem CWV reais não é garantia de performance real |
| Domain Authority | Métrica de ferramentas pagas, não do Google |
| Backlinks count | Quantidade ≠ qualidade |

---

## Relação com agentes, skills e comandos

- [`seo-data-analyst`](../agents/seo-data-analyst.md) — usa este modelo para análises.
- [`gsc-ga4-analysis`](../skills/gsc-ga4-analysis/SKILL.md) — procedimento que aplica estes KPIs.
- [`seo-lead`](../agents/seo-lead.md) — usa KPIs para priorizar.
- [`cwv-performance-seo`](../agents/cwv-performance-seo.md) — usa KPIs de CWV.
- [`REPORTING_MODEL.md`](REPORTING_MODEL.md) — persistência de análises.
- [`/seo data`](../commands/seo.md) — modo do comando SEO.

---

## Records / Persistência

Recomendar record quando:

- análise de dados relevante (trimestral, semestral, anual);
- baseline de KPIs definida;
- análise de queda/subida com impacto significativo;
- relatório de KPIs para decisão estratégica.

Records reais vivem no projeto-alvo em `.claude/records/`.

---

## Regra final

SEO bom melhora clicks, conversões e negócio.

Não se mede apenas por ranking.  
Não se mede apenas por tráfego total.  
Mede-se por tráfego qualificado que converte, em páginas que servem intenções reais.
