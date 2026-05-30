---
name: gsc-ga4-analysis
description: Procedimento para analisar dados de Search Console e GA4 — períodos comparáveis, separação brand/non-brand, limitações explícitas e sem dados inventados. Requer autorização para dados reais.
---

# Skill: GSC / GA4 Analysis

Procedimento operacional para analisar dados de Search Console, GA4 e CrUX.

Esta skill é usada principalmente pelo [`seo-data-analyst`](../../agents/seo-data-analyst.md) para conduzir análises de dados SEO de forma estruturada.

Esta skill não é um agente.  
Esta skill não inventa métricas.  
Esta skill não acede a dados sem autorização.  
Esta skill define o procedimento para analisar dados SEO de forma consistente e honesta.

---

## Objetivo

Analisar dados de Google Search Console, GA4 e CrUX para transformar números em insights accionáveis — com períodos comparáveis, separação brand/non-brand, limitações declaradas e sem conclusões sem evidência.

---

## Quando usar

Usar nos modos:

- `/seo data` — modo principal;
- `/seo audit` — componente de dados na auditoria;
- análise de queda/subida de tráfego;
- definição de KPIs baseline.

---

## Quando não usar

Não usar sem autorização para aceder a dados reais.  
Sem dados, declarar limitação — não inventar.

---

## Quem pode usar

Principal:

- [`seo-data-analyst`](../../agents/seo-data-analyst.md)

---

## Fontes de verdade

1. [`../../project/KPI_MODEL.md`](../../project/KPI_MODEL.md) — KPIs e fases.
2. [`../../project/REPORTING_MODEL.md`](../../project/REPORTING_MODEL.md) — records e persistência.
3. [`../../project/TOOLING_MODEL.md`](../../project/TOOLING_MODEL.md) — ferramentas e autorização.

---

## Inputs necessários

- Acesso autorizado a GSC e/ou GA4;
- pergunta a responder;
- períodos a comparar;
- páginas ou queries de interesse;
- objectivo da análise.

---

## Procedimento

### Passo 1 — Confirmar acesso e autorização

Antes de qualquer análise:

- GSC: propriedade correcta confirmada? Leitura autorizada?
- GA4: propriedade correcta? Leitura autorizada?
- CrUX: URL pública disponível (não requer autorização)?

Se não há autorização → declarar e não aceder.

---

### Passo 2 — Definir pergunta e período

Definir claramente:

- O que queremos descobrir? (queda de tráfego, CTR baixo, oportunidade de optimização, baseline)
- Período primário: ex. "últimos 28 dias" ou "mês de março 2025".
- Período de comparação: mesmo período do ano anterior (para sazonalidade) ou período imediatamente anterior.

**Regras de período:**
- Mínimo 28 dias para estabilidade estatística.
- Evitar comparar Dezembro com Janeiro (sazonalidade diferente).
- Ano-a-ano é mais fiável para maioria das análises.
- Comparar antes/depois de evento específico quando relevante.

---

### Passo 3 — Separar brand de non-brand

**Brand:** queries que incluem nome da empresa, domínio ou variações.  
**Non-brand:** todas as outras.

Misturar brand e non-brand distorce análise de visibilidade orgânica real porque:
- Brand queries têm CTR muito alto (utilizador já quer a marca) → inflaciona CTR médio.
- Subida de brand queries (por acção de PR/marketing) mascara queda de non-brand.

Sempre reportar separadamente:
- Performance de brand.
- Performance de non-brand.
- Total (opcional, como contexto).

---

### Passo 4 — Análise GSC

**Performance report:**

Para cada período definido:

| Métrica | O que mede | Armadilhas comuns |
|---|---|---|
| Clicks | Visitas a partir de resultados orgânicos | Apenas clicks em resultados orgânicos; excluir GSC para Google Ads |
| Impressões | Vezes que apareceu na SERP | Uma query pode gerar múltiplas impressões por sessão |
| CTR | Clicks / Impressões | Posição média muito alta distorce CTR |
| Posição média | Média de todas as impressões | ≠ ranking fixo; depende de query, localização, dispositivo |

**Identificar:**
- Top queries por clicks (non-brand).
- Queries com posição 4-20 e alta impressão → oportunidade de CTR.
- Queries com queda de clicks YoY.
- Queries com subida de impressões mas queda de CTR → title/meta fraco ou SERP feature.

**Páginas:**
- Top páginas por clicks orgânicos.
- Páginas com queda significativa.
- Páginas com impressões altas mas CTR baixo.

---

### Passo 5 — Análise GA4 (quando disponível)

**Sessões orgânicas:**
- Canal: "Organic Search".
- Comparar períodos.
- Segmentar por landing page.
- Segmentar por dispositivo (mobile vs desktop).

**Conversões orgânicas:**
- Definir eventos de conversão relevantes (formulários, chamadas, downloads).
- Taxa de conversão orgânica por página.
- Jornada até conversão: quantas sessões antes de converter?

**Engagement:**
- Session engagement rate (≥ 10s, ou conversão, ou 2+ páginas).
- Scroll depth em páginas de conteúdo.
- Pages per session para landing pages específicas.

**Limitações GA4 comuns:**
- Dados agregados — não por utilizador identificado.
- Conversões podem não estar bem configuradas → declarar se há incerteza.
- "Not provided" para dados de query orgânica no GA4 → usar GSC para queries.

---

### Passo 6 — CrUX / PageSpeed (quando relevante)

**Field data CrUX:**
- Disponível para URLs com tráfego suficiente (> ~1000 sessões/mês tipicamente).
- LCP, INP, CLS por origem ou URL.
- Separar mobile de desktop.
- Se indisponível: declarar — não usar lab data como field data.

---

### Passo 7 — Formular hipóteses

Para cada variação significativa, formular hipótese:

| Observação | Hipótese | Evidência de suporte | Grau de certeza |
|---|---|---|---|
| Queda de clicks em março | Mudança de algoritmo | GSC + outros sites confirmam no mesmo período | Média |
| Queda de CTR na homepage | Title/meta menos relevante ou AI Overview a roubar clicks | Impressões mantiveram, CTR desceu | Média-alta |

**Graus de certeza:**
- Alta: evidência directa confirma hipótese.
- Média: evidência correlacionada mas não confirma directamente.
- Baixa: possível mas sem evidência suficiente.
- Hipótese: inferência sem evidência.

---

### Passo 8 — Recomendar acções

Para cada insight:

- Acção específica e acionável.
- Agente recomendado para executar.
- Prioridade.
- Métrica a monitorizar para confirmar melhoria.

---

### Passo 9 — Declarar limitações

Declarar explicitamente:

- Período analisado.
- Amostras: GSC amostras para propriedades grandes ou queries long-tail.
- Disponibilidade: campo "data disponível desde" em GSC.
- O que ficou por analisar.
- Que dados não estavam disponíveis.

---

## Output esperado

```md
## GSC / GA4 Analysis — [Tema/Período]
Data: YYYY-MM-DD | Período: [A] vs [B]

### Acesso e autorização
- GSC: [confirmado / não disponível]
- GA4: [confirmado / não disponível]
- CrUX: [disponível / não disponível]

### Limitações
[amostragem, disponibilidade, lacunas]

### GSC — Performance orgânica
| Métrica | Período A | Período B | Variação |
|---|---|---|---|

Non-brand performance: [separada]
Brand performance: [separada]

### Top queries (non-brand)
[tabela]

### Páginas com maior impacto
[tabela de variações]

### GA4 — Orgânico (se disponível)
[sessões, conversões, engagement]

### CrUX (se disponível)
[LCP, INP, CLS field data]

### Hipóteses
[observação → hipótese → evidência → certeza]

### Recomendações
| Acção | Agente | Prioridade |
|---|---|---|

### Métricas a monitorizar
[lista]
```

---

## Gates de segurança

- Não aceder a dados sem autorização.
- Não inventar métricas ou posições.
- Separar sempre brand de non-brand.
- Declarar limitações de amostragem.
- Não guardar dados de utilizadores identificáveis em records.
- Posição média ≠ ranking fixo.

---

## Relação com agentes e docs

- [`seo-data-analyst`](../../agents/seo-data-analyst.md) — agente principal.
- [`technical-seo`](../../agents/technical-seo.md) — usa dados de cobertura GSC.
- [`cwv-performance-seo`](../../agents/cwv-performance-seo.md) — usa field data CrUX.
- [`content-growth`](../../agents/content-growth.md) — usa insights de CTR/conversão.
- [`KPI_MODEL.md`](../../project/KPI_MODEL.md) — métricas e fases.
- [`REPORTING_MODEL.md`](../../project/REPORTING_MODEL.md) — records e persistência.

---

## Exemplos de pedidos que aceita

- "Aplica o procedimento de análise GSC/GA4 a este projecto."
- "Analisa os últimos 90 dias de dados Search Console."
- "Segue o processo de análise para identificar causas de queda de tráfego."

---

## Erros comuns a evitar

- Misturar brand e non-brand.
- Comparar períodos sazonalmente diferentes.
- Confundir posição média com ranking fixo.
- Ignorar amostragem do GSC.
- Inventar dados quando não há acesso.
- Não declarar limitações.

---

## Regra final

Análise sem limitações declaradas não é análise — é ficção.

Períodos comparáveis. Brand separado. Limitações explícitas. Conclusões baseadas em evidência.
