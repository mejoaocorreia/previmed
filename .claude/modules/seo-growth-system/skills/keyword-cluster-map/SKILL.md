---
name: keyword-cluster-map
description: Procedimento para construir um mapa de clusters de keywords com intenção, hierarquia e mapeamento a páginas — evitando canibalização e priorizando por intenção comercial.
---

# Skill: Keyword Cluster Map

Procedimento operacional para construir mapas de keywords com intenção e estrutura semântica.

Esta skill é usada principalmente pelo [`keyword-intent`](../../agents/keyword-intent.md) para produzir cluster maps completos e acionáveis a partir de pesquisa de keywords e análise de intenção.

Esta skill não é um agente.  
Esta skill não escreve conteúdo.  
Esta skill não implementa em WordPress.  
Esta skill não inventa volumes de pesquisa.  
Esta skill define o procedimento para mapear keywords a intenção e páginas de forma consistente.

---

## Objetivo

Construir um mapa de clusters de keywords com intenção classificada, hierarquia semântica definida, mapeamento a páginas e identificação de canibalização — para que cada esforço editorial sirva uma intenção real de pesquisa.

---

## Quando usar

Usar nos modos:

- `/seo keywords` — modo principal;
- `/seo audit` — quando auditoria identifica gaps de keyword ou canibalização;
- `/seo brief` — para confirmar intenção antes de criar brief.

Usar quando:

- é necessário estruturar o universo de keywords de um serviço ou área;
- há suspeita de canibalização entre páginas;
- há nova área de serviço a cobrir;
- é necessário mapear intenção antes de criar briefs.

---

## Quando não usar

Não usar para:

- análise SERP aprofundada — usar `serp-intent-audit`;
- análise de concorrência — usar `competitor-gap-analysis`;
- criar briefs — usar `content-brief-generation`;
- escrever conteúdo — usar `content-growth` ou `onpage-seo`;
- dados confirmados de volume sem ferramenta paga — declarar hipótese.

---

## Quem pode usar

Principal:

- [`keyword-intent`](../../agents/keyword-intent.md)

Também pode usar:

- [`content-brief`](../../agents/content-brief.md) para confirmar intenção antes de brief;
- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) em conjunto para validar na SERP.

---

## Fontes de verdade

Consultar por esta ordem:

1. [`../../project/STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — tipos de intenção, arquitetura, clusters.
2. [`../../project/CONTENT_RULES.md`](../../project/CONTENT_RULES.md) — critérios para criar páginas.
3. [`serp-intent-audit`](../serp-intent-audit/SKILL.md) — classificação de intenção SERP.

---

## Inputs necessários

- Tema/serviço ou área de negócio;
- mercado e idioma;
- localização (nacional, regional, local?);
- páginas existentes no site;
- dados de GSC (queries actuais, se autorizados);
- concorrentes conhecidos (opcional, mas útil);
- restrições de negócio (serviços não prestados, áreas não servidas).

---

## Procedimento

### Passo 1 — Construir universo de keywords

**Head keywords:** termos amplos com maior volume estimado.  
Exemplo: "medicina do trabalho", "segurança no trabalho".

**Mid-tail:** mais específicos, intenção mais clara.  
Exemplo: "empresa de medicina do trabalho", "consultas de medicina do trabalho".

**Long-tail:** muito específicos, volume baixo, conversão alta.  
Exemplo: "medicina do trabalho obrigatória número de trabalhadores", "o que inclui exame de medicina do trabalho".

**Locais:** queries com localização.  
Exemplo: "medicina do trabalho Lisboa", "medicina do trabalho Porto".

**Perguntas:** PAA, FAQs implícitas.  
Exemplo: "quando é obrigatória a medicina do trabalho?", "quanto custa medicina do trabalho?".

**Brand vs non-brand:** separar sempre.

Fontes sem ferramentas pagas:
- Browser/Search autocompletar.
- People Also Ask na SERP.
- Buscas relacionadas no fundo da SERP.
- Estrutura de sites de concorrentes.
- GSC queries actuais (quando autorizado).

---

### Passo 2 — Classificar intenção por keyword

Para cada keyword, classificar intenção dominante:

| Intenção | O utilizador quer... | Exemplos |
|---|---|---|
| Informacional | Entender ou aprender | "o que é X", "como funciona X", "quando é obrigatório X" |
| Comercial | Comparar opções ou fornecedores | "empresa de X", "serviço de X Lisboa", "melhor X" |
| Transacional | Agir, contratar, comprar | "contratar X", "pedir orçamento X", "preço de X" |
| Local | Solução numa zona geográfica | "X Lisboa", "X perto de mim", "X [cidade]" |
| Navegacional | Encontrar marca específica | "[marca] X", "[nome da empresa]" |

Quando a intenção não é clara, verificar na SERP (usar `serp-intent-audit`).

---

### Passo 3 — Agrupar em clusters semânticos

Regra: 1 cluster = 1 intenção específica = 1 página alvo.

Cluster é um grupo de keywords que:
- respondem à mesma intenção principal;
- podem coexistir na mesma página sem confundir o utilizador;
- não competem por intenções diferentes.

Exemplo de cluster correcto:
- Cluster "Medicina do trabalho Lisboa" → keywords: "medicina do trabalho Lisboa", "consultas medicina do trabalho Lisboa", "empresa medicina do trabalho Lisboa"
- Todas têm intenção local + comercial → mesmo cluster.

Exemplo de split necessário:
- "o que é medicina do trabalho" (informacional) → cluster separado de "contratar medicina do trabalho" (transacional).

---

### Passo 4 — Mapear clusters a páginas

Para cada cluster, determinar:

**Existe:** há página existente que satisfaz bem a intenção?
- Se sim: marcar como "Existe" e verificar se está optimizada.

**Em falta:** não há página para este cluster?
- Marcar como "Em falta" e classificar prioridade.

**Canibalização:** dois ou mais URLs competem pela mesma intenção?
- Identificar qual deve ser a página principal.
- Recomendar acção (redirect, noindex, consolidação, diferenciação).

**Não criar:** volume existe mas não há serviço real ou a empresa não actua nessa área?
- Marcar como "Não criar — sem serviço/intenção real".

---

### Passo 5 — Identificar e resolver canibalização

**Identificar:** várias páginas com keywords sobrepostas e intenção idêntica.

**Como verificar:** pesquisar a keyword alvo no Browser e ver se aparecem múltiplas URLs do mesmo domínio.

**Recomendar acção** (sem executar — escalar para `technical-seo`):
- Consolidar: fundir páginas numa só mais forte.
- Redirecionar: 301 da página mais fraca para a mais forte.
- Diferenciar: se as páginas têm intenções ligeiramente diferentes, clarificar essa diferença.
- Noindex: em casos muito específicos de páginas que não devem indexar.

Não implementar redirects ou noindex — handoff para `technical-seo`.

---

### Passo 6 — Priorizar clusters

Factores de priorização:

1. **Intenção comercial/transacional** — maior impacto em conversão.
2. **Relevância para os serviços reais** — a empresa pode converter este tráfego?
3. **Volume estimado** — marcado como hipótese sem ferramenta paga.
4. **Dificuldade estimada** — SERP simples ou muito competitiva?
5. **Gap actual** — página em falta vs página fraca vs página boa.
6. **Quick wins** — keywords com impressões GSC mas CTR baixo (quando disponível).

Prioridade alta: intenção comercial forte + serviço real + gap real.  
Prioridade baixa: intenção informacional pura + cluster já coberto adequadamente.

---

## Output esperado

```md
## Keyword Cluster Map — [Tema] — YYYY-MM-DD

### Resumo
- Clusters identificados: X
- Páginas existentes: X
- Páginas em falta: X
- Canibalização detectada: X casos
- Prioridades principais: [1-3 itens]

### Clusters

| # | Cluster | Keyword principal | Variações (top 3) | Intenção | Página alvo | Estado | Tipo de página recomendado | Prioridade | Notas |
|---|---|---|---|---|---|---|---|---|---|

### Canibalização detectada
| Keywords | URLs conflituosas | Recomendação |
|---|---|---|

### Páginas a criar (prioritárias)
[lista ordenada por prioridade]

### Clusters sem criação de página
[keywords com volume mas sem serviço real para a empresa]

### Limitações de dados
- Volume: [confirmado via GSC / estimado via Browser / hipótese]
- SERP: [verificado / não verificado]
- Ferramentas pagas: [disponíveis / não autorizadas]
```

---

## Gates de segurança

**Regras absolutas:**

- Não inventar volumes de pesquisa — marcar sempre como hipótese se não há ferramenta confirmada.
- Não criar clusters para serviços que a empresa não presta.
- Não criar clusters para localizações onde a empresa não actua.
- Não recomendar páginas locais vazias para capturar volume.
- Não confundir intenção informacional com comercial.
- Não implementar redirects ou noindex — handoff para `technical-seo`.
- Ferramentas pagas exigem autorização explícita.

---

## Relação com agentes e docs

- [`keyword-intent`](../../agents/keyword-intent.md) — agente principal que usa este procedimento.
- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) — valida intenção na SERP real.
- [`serp-intent-audit`](../serp-intent-audit/SKILL.md) — skill de classificação de intenção SERP.
- [`content-brief`](../../agents/content-brief.md) — consome clusters para criar briefs.
- [`internal-linking`](../../agents/internal-linking.md) — consome arquitectura de clusters.
- [`technical-seo`](../../agents/technical-seo.md) — resolve canibalização técnica.
- [`STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — intenção e arquitetura.

---

## Exemplos de pedidos que aceita

- "Constrói o cluster map para os serviços de medicina do trabalho."
- "Usa este procedimento para mapear keywords a páginas existentes."
- "Identifica canibalização entre estas páginas usando o procedimento de cluster map."
- "Mapeia estas keywords com intenção classificada."

---

## Exemplos de pedidos que deve encaminhar

Encaminhar para `serp-intent-audit`:

- "Confirma a intenção desta query na SERP real."

Encaminhar para `competitor-gap-analysis`:

- "Analisa que páginas os concorrentes têm para estas queries."

Encaminhar para `content-brief-generation`:

- "Transforma este cluster num brief editorial."

Encaminhar para `technical-seo`:

- "Há canibalização — como resolver os redirects."

---

## Erros comuns a evitar

- Priorizar por volume puro sem considerar intenção.
- Criar clusters que canibalizam páginas existentes sem identificar isso.
- Ignorar intenção informacional vs comercial.
- Inventar volumes sem ferramenta ("esta keyword tem 5.000 pesquisas/mês").
- Criar clusters para serviços que a empresa não presta.
- Marcar volume como dado confirmado quando é hipótese.

---

## Regra final

Um cluster map sem intenção classificada é apenas uma lista de palavras.

Cada cluster deve responder: para quem é? que intenção tem? que página satisfaz? — antes de gerar qualquer trabalho editorial.
