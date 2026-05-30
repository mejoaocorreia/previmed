---
name: serp-intent-audit
description: Procedimento para classificar a intenção dominante de uma SERP e o tipo de conteúdo que favorece — registando data, localização e dispositivo, e distinguindo evidência de hipótese.
---

# Skill: SERP Intent Audit

Procedimento operacional para classificar a intenção dominante de uma SERP e determinar que tipo de página e conteúdo a satisfaz melhor.

Esta skill é usada pelo [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) e pelo [`keyword-intent`](../../agents/keyword-intent.md) para confirmar intenção real antes de decidir que página criar ou optimizar.

Esta skill não é um agente.  
Esta skill não inventa dados de SERP sem acesso real.  
Esta skill não assume que SERP mobile = SERP desktop.  
Esta skill não assume que intenção literal da query = intenção real do utilizador.

---

## Objetivo

Classificar a intenção dominante de uma SERP — com base no que realmente aparece, não no que a query literalmente diz — e determinar que formato, tipo de página e profundidade de conteúdo a SERP favorece.

---

## Quando usar

Usar:

- antes de criar uma página nova (confirmar intenção);
- antes de criar brief (confirmar tipo de página a criar);
- antes de optimizar página existente (confirmar alinhamento com intenção actual);
- quando há dúvida sobre se uma query é informacional vs comercial;
- como parte de `competitor-gap-analysis`;
- nos modos `/seo keywords` e `/seo competitor`.

---

## Quando não usar

Não usar quando:

- não há acesso a SERP real — trabalhar com hipótese e declarar;
- o pedido é apenas keyword research — usar `keyword-cluster-map`;
- o pedido é análise de concorrentes completa — usar `competitor-gap-analysis`.

---

## Quem pode usar

Principal:

- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md)
- [`keyword-intent`](../../agents/keyword-intent.md)

Também pode usar:

- [`content-brief`](../../agents/content-brief.md) para confirmar intenção antes de brief;
- [`seo-lead`](../../agents/seo-lead.md) para verificação rápida de intenção.

---

## Fontes de verdade

1. [`../../project/STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — tipos de intenção.
2. [`../../project/COMPETITOR_RESEARCH_PLAYBOOK.md`](../../project/COMPETITOR_RESEARCH_PLAYBOOK.md) — processo de análise.

---

## Inputs necessários

- Query (ou queries) a auditar;
- mercado/idioma;
- localização (para queries locais);
- dispositivo (preferir mobile);
- acesso a Browser/Search (obrigatório para evidência real).

Se não houver acesso a SERP real, declarar limitação e trabalhar com hipótese.

---

## Procedimento

### Passo 1 — Registar contexto

Obrigatório antes de qualquer observação:

- Data: YYYY-MM-DD.
- Query exacta pesquisada.
- Mercado/idioma: ex. "Portugal / pt-PT".
- Localização: "Nacional" ou ex. "Lisboa" (para queries locais).
- Dispositivo: mobile (preferir sempre — Google usa mobile-first).

Sem este registo, a observação não é reproduzível.

---

### Passo 2 — Observar SERP

Pesquisar a query e registar:

**Posições 1-5:**
- Que tipo de URLs aparecem? (domínio, tipo de página)
- São de negócios? Guias? Notícias? Reguladores? Marketplaces?

**SERP features presentes:**
- AI Overview? (se visível) → sugere intenção informacional ou de resposta directa.
- Featured Snippet? Que tipo? (definição, lista numerada, tabela, how-to)
- Local Pack? → sugere intenção local.
- People Also Ask? Que perguntas associadas?
- Vídeos? → sugere conteúdo explicativo/demonstrativo.
- Imagens? → sugere conteúdo visual.
- Shopping? → sugere intenção de compra.

---

### Passo 3 — Classificar intenção dominante

Baseado no que a SERP mostra (não no que a query diz literalmente):

| Intenção | Sinais na SERP |
|---|---|
| Informacional | Guias, artigos, FAQs dominam; AI Overview provável; PAA activa |
| Comercial | Misto de serviços e guias; páginas de empresa a rankear mas também guias comparativos |
| Transacional | Páginas de serviço, preços, formulários de contacto dominam |
| Local | Local Pack presente; páginas com localização específica no título |
| Navegacional | A marca ou entidade específica domina; top results são o site oficial |

**Cuidados:**
- "empresa de medicina do trabalho" → literal parece comercial, mas SERP pode mostrar guias informativos = intenção mista.
- "segurança no trabalho" → literal parece informacional, mas SERP local pode mostrar empresas = intenção comercial/local.
- Sempre verificar: o que a SERP mostra é a verdade, não o que a query aparenta.

---

### Passo 4 — Identificar tipo de página favorecida

Com base nos resultados observados:

| Tipo de página | Quando a SERP favorece |
|---|---|
| Página de serviço | Top resultados são páginas comerciais com CTA |
| Guia educativo | Top resultados são artigos longos, how-to ou explicações |
| FAQ/Resposta directa | Featured Snippet de lista ou definição; PAA activa |
| Comparativo | Top resultados comparam opções ou fornecedores |
| Página local | Local Pack; top resultados têm localização no título |
| Blog/artigo | Mix de news e artigos recentes; freshness parece importante |

---

### Passo 5 — Observar formato e profundidade

- Que comprimento têm os top resultados? (curto, médio, aprofundado)
- Há FAQs visíveis nos top resultados?
- Há schema estruturado (rich results)?
- Que secções de conteúdo são comuns?
- Que proof points aparecem?

---

### Passo 6 — Concluir

Produzir:
- Intenção dominante (com base na SERP observada).
- Intenção secundária (se houver mix).
- Tipo de página recomendada.
- Formato e profundidade recomendados.
- O que a página deve responder.
- Limitações da observação.

---

## Output esperado

```md
## SERP Intent Audit — [Query] — YYYY-MM-DD
Mercado: [país/idioma] | Localização: [...] | Dispositivo: [mobile/desktop]

### Query analisada
[...]

### SERP features observadas
- AI Overview: [sim/não/parcialmente]
- Featured Snippet: [sim — tipo: ... / não]
- Local Pack: [sim — X resultados / não]
- PAA: [sim — exemplos: ... / não]
- Outros: [...]

### Tipo de resultados top 3-5
| Posição | URL/domínio | Tipo de página | Notas |
|---|---|---|---|

### Intenção dominante
[informacional / comercial / transacional / local / mista — com justificação]

### Tipo de página que a SERP favorece
[serviço / guia / FAQ / comparativo / local / blog]

### Formato e profundidade recomendados
[...]

### O que a página deve responder
[...]

### Evidência vs hipótese
[o que foi observado vs inferido]
```

---

## Gates de segurança

- Não dizer "a intenção é X" sem SERP real — marcar como hipótese.
- Não assumir que SERP mobile = SERP desktop — são frequentemente diferentes.
- Não assumir que SERP num país = SERP noutro.
- Não tratar AI Overview como estável ou garantida — é observação pontual.
- Registar sempre data — SERPs mudam, especialmente com AI features.

---

## Relação com agentes e docs

- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) — usa em conjunto com `competitor-gap-analysis`.
- [`keyword-intent`](../../agents/keyword-intent.md) — usa para confirmar intenção de clusters.
- [`content-brief`](../../agents/content-brief.md) — recebe intenção confirmada para orientar brief.
- [`STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — tipos de intenção.
- [`COMPETITOR_RESEARCH_PLAYBOOK.md`](../../project/COMPETITOR_RESEARCH_PLAYBOOK.md) — processo de pesquisa.

---

## Exemplos de pedidos que aceita

- "Classifica a intenção desta query na SERP."
- "Que tipo de página favorece esta SERP?"
- "Confirma se esta query é informacional ou comercial."
- "Observa a SERP para 'medicina do trabalho Lisboa' e classifica."

---

## Exemplos de pedidos que deve encaminhar

- Para `competitor-gap-analysis`: "Analisa os top resultados em detalhe."
- Para `keyword-cluster-map`: "Mapeia este universo de keywords com intenção."

---

## Erros comuns a evitar

- Assumir intenção pela query literal sem verificar SERP.
- Ignorar SERP features na classificação.
- Confundir intenção comercial com transacional.
- Não registar data ou localização.
- Dizer "intenção confirmada" sem ter visto a SERP real.

---

## Regra final

A intenção real está na SERP, não na query.

O utilizador que pesquisa "medicina do trabalho obrigatória" pode querer entender (informacional) ou pode querer contratar (comercial) — a SERP diz qual.

Nunca assumir. Sempre observar.
