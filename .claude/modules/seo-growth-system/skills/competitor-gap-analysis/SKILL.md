---
name: competitor-gap-analysis
description: Procedimento para analisar concorrentes e SERP e encontrar lacunas e oportunidades acionáveis — para superar, nunca para copiar. Regista data, localização e dispositivo.
---

# Skill: Competitor Gap Analysis

Procedimento operacional para analisar concorrentes e SERP e identificar gaps e oportunidades acionáveis.

Esta skill é usada principalmente pelo [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) para conduzir análises competitivas estruturadas.

Esta skill não é um agente.  
Esta skill não copia concorrentes.  
Esta skill não inventa dados de backlinks, tráfego ou volume.  
Esta skill não implementa em WordPress.  
Esta skill define o procedimento para analisar a SERP e concorrência de forma consistente.

---

## Objetivo

Analisar o que está a rankear para queries prioritárias — estrutura, conteúdo, prova, schema e UX dos top resultados — e identificar gaps que representam oportunidades reais para criar algo genuinamente melhor.

---

## Quando usar

Usar nos modos:

- `/seo competitor` — modo principal;
- `/seo brief` — para entender o que superar antes de criar brief;
- `/seo audit` — para diagnóstico competitivo;
- `/seo keywords` — para confirmar intenção SERP após cluster map.

---

## Quando não usar

Não usar para:

- keyword research de raiz — usar `keyword-cluster-map`;
- criar brief editorial — usar `content-brief-generation`;
- escrever conteúdo — usar `content-growth` ou `onpage-seo`;
- dados de backlinks ou volume sem ferramenta autorizada — não inventar.

---

## Quem pode usar

Principal:

- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md)

Também pode usar:

- [`keyword-intent`](../../agents/keyword-intent.md) para confirmar intenção;
- [`content-brief`](../../agents/content-brief.md) para informar o brief com dados de concorrência.

---

## Fontes de verdade

1. [`../../project/COMPETITOR_RESEARCH_PLAYBOOK.md`](../../project/COMPETITOR_RESEARCH_PLAYBOOK.md) — processo de pesquisa.
2. [`../../project/STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — tipos de intenção.
3. [`serp-intent-audit`](../serp-intent-audit/SKILL.md) — classificação de intenção SERP.

---

## Inputs necessários

- Queries a analisar;
- mercado/localização/dispositivo;
- data da análise;
- acesso a Browser/Search (obrigatório);
- ferramentas pagas (apenas se autorizadas).

---

## Procedimento

### Passo 1 — Registar contexto obrigatório

Antes de qualquer análise, registar:

- Data: YYYY-MM-DD.
- Mercado/idioma: ex. "Portugal / pt-PT".
- Localização: ex. "Lisboa" (para queries locais).
- Dispositivo: mobile (preferir) ou desktop.

Sem este registo, os dados não são reproduzíveis nem comparáveis no futuro.

---

### Passo 2 — Definir queries a analisar

Confirmar com `keyword-intent` as queries prioritárias.

Agrupar por:
- intenção principal (informacional, comercial, local, transacional);
- cluster a que pertencem.

Analisar no mínimo as queries com maior prioridade comercial.

---

### Passo 3 — Observar SERP por query

Para cada query, registar:

**SERP features:**
- AI Overview? (se visível — observação pontual, não garantia)
- Featured Snippet? Que tipo? (definição, lista, tabela, how-to)
- Local Pack? Quantos resultados?
- People Also Ask? Que perguntas?
- Vídeos, imagens, shopping?

**Intenção dominante:**
- Que tipo de página domina o top 3-5? (serviço, guia, comparativo, FAQ, news)
- Confirmar intenção real vs. intenção literal da query.

---

### Passo 4 — Analisar top 3-5 resultados

Para cada resultado:

**Identificação:**
- URL e domínio.
- Tipo: concorrente comercial / orgânico / autoridade / misto.

**Estrutura:**
- Title e H1.
- Headings H2 visíveis (estrutura geral).
- Comprimento estimado (superficial, médio, aprofundado).
- Secções principais (serviço, como funciona, prova, FAQs, CTA).

**Conteúdo:**
- É específico ou genérico?
- Tem prova (certificações, casos, dados, parcerias)?
- Tem FAQs que respondem a perguntas reais?
- Que diferenciação apresenta?

**Schema / Rich Results:**
- Há schema visível (estrelas, breadcrumb, FAQ, event)?
- Que tipo de schema têm?

**UX:**
- Lê-se bem? Mobile-friendly visível?
- CTA tipo e posição?
- Sinais locais (morada, telefone, GBP)?

**Forças e fraquezas:**
- O que fazem bem?
- O que fazem mal ou em falta?

---

### Passo 5 — Identificar padrões

Após analisar o top 3-5:

- Que é consistente entre os resultados?
- Que formato de conteúdo domina?
- Que comprimento e profundidade são comuns?
- Que tipo de prova é apresentada?
- Que perguntas são respondidas vs ignoradas?

---

### Passo 6 — Identificar gaps

Perguntar:

- Que pergunta real fica sem resposta boa nos top resultados?
- Que proof point está ausente?
- Que formato podia ser melhor (lista, tabela, guia completo)?
- Que intenção secundária não está bem coberta?
- Que localidade, sector ou público está mal servido?

---

### Passo 7 — Definir oportunidades

Para cada gap, definir:

- O que a nossa página pode fazer melhor.
- Que tipo de página recomendada.
- Que estrutura usar.
- Que proof points incluir.
- Como criar algo genuinamente superior — não apenas semelhante.

---

## Output esperado

```md
## Competitor Gap Analysis — [Tema] — YYYY-MM-DD
Mercado: [país/idioma] | Localização: [...] | Dispositivo: [mobile/desktop]

### Queries analisadas
[lista]

### SERP features por query
| Query | AI Overview | Featured Snippet | Local Pack | PAA | Outros |
|---|---|---|---|---|---|

### Intenção dominante
| Query | Intenção | Tipo de página favorecida |
|---|---|---|

### Top concorrentes analisados
| URL | Tipo | Forças | Fraquezas | Schema | Notas |
|---|---|---|---|---|---|

### Padrões identificados
[o que é consistente no top 3-5]

### Gaps identificados
[o que falta nos top resultados]

### Oportunidades
[como ser genuinamente melhor]

### Evidência vs hipótese
[o que foi observado vs inferido]
```

---

## Gates de segurança

- Não copiar estrutura ou texto de concorrentes — observar para superar.
- Não inventar dados de backlinks, DA/DR, volume ou tráfego.
- Registar sempre data, localização e dispositivo.
- Distinguir evidência de hipótese.
- AI Overview observada ≠ garantia de presença futura.
- Ferramentas pagas só com autorização.

---

## Relação com agentes e docs

- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) — agente principal.
- [`keyword-intent`](../../agents/keyword-intent.md) — fornece queries a analisar.
- [`content-brief`](../../agents/content-brief.md) — consome análise para criar brief.
- [`serp-intent-audit`](../serp-intent-audit/SKILL.md) — classifica intenção SERP.
- [`COMPETITOR_RESEARCH_PLAYBOOK.md`](../../project/COMPETITOR_RESEARCH_PLAYBOOK.md) — playbook de concorrência.

---

## Exemplos de pedidos que aceita

- "Aplica o procedimento de gap analysis para estas queries."
- "Analisa os top resultados e identifica o que nos falta."
- "Segue o processo de competitor gap analysis para este serviço."

---

## Exemplos de pedidos que deve encaminhar

- Para `keyword-cluster-map`: "Primeiro preciso das queries — faz o cluster map."
- Para `serp-intent-audit`: "Confirma a intenção desta query na SERP."
- Para `content-brief-generation`: "Transforma os gaps num brief editorial."

---

## Erros comuns a evitar

- Copiar estrutura de concorrentes sem adaptar.
- Não registar data e localização.
- Inventar dados de backlinks ou tráfego.
- Tratar SERP mobile e desktop como equivalentes.
- Confundir concorrente comercial com orgânico.
- Não distinguir evidência de hipótese.

---

## Regra final

Analisar para superar.

O gap não é o que os concorrentes fazem — é o que não fazem e o utilizador ainda precisa.
