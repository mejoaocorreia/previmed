---
name: content-brief-generation
description: Procedimento passo a passo para gerar um brief editorial SEO acionável — transforma intenção de pesquisa, análise SERP e contexto de negócio numa especificação que permite criar uma página superior à concorrência.
---

# Skill: Content Brief Generation

Procedimento operacional para gerar briefs editoriais SEO.

Esta skill é usada principalmente pelo [`content-brief`](../../agents/content-brief.md) para produzir briefs completos e acionáveis a partir de pesquisa de keywords, análise SERP e contexto de negócio.

Esta skill não é um agente.  
Esta skill não faz keyword research de raiz.  
Esta skill não faz análise SERP/concorrência de raiz.  
Esta skill não escreve a página final.  
Esta skill não implementa em WordPress.  
Esta skill não aprova publicação.  
Esta skill define o procedimento para transformar inputs em brief editorial.

---

## Objetivo

Transformar pesquisa de keywords, análise de intenção SERP e contexto de negócio num brief editorial completo — suficientemente específico para que o resultado seja uma página superior à concorrência, não apenas semelhante.

---

## Quando usar

Usar antes de:

- criar uma página de raiz;
- reescrever profundamente uma página importante;
- transformar um cluster de keywords numa página dedicada;
- garantir alinhamento entre SEO, negócio e editorial antes de avançar para redacção.

Usar nos modos:

- `/seo brief` — modo principal;
- parte de `/seo audit` quando são identificadas páginas em falta;
- parte de `/seo keywords` quando um cluster precisa de página.

---

## Quando não usar

Não usar esta skill para:

- rever conteúdo já existente sem criar de raiz — usar `content-growth`;
- optimizar apenas titles/metas de página existente — usar `onpage-optimization-pass`;
- fazer keyword research de raiz — usar `keyword-cluster-map`;
- escrever a página final — usar `content-growth` ou `onpage-seo`;
- validar conteúdo antes de publicar — usar `seo-quality-gate` com `seo-qa`.

---

## Quem pode usar

Principal:

- [`content-brief`](../../agents/content-brief.md)

Também pode usar:

- [`content-growth`](../../agents/content-growth.md) quando precisa de estrutura antes de rever;
- [`seo-lead`](../../agents/seo-lead.md) para coordenar criação de brief em auditorias grandes.

---

## Fontes de verdade

Consultar por esta ordem:

1. [`../../project/CONTENT_RULES.md`](../../project/CONTENT_RULES.md) — critérios de qualidade, E-E-A-T, claims.
2. [`../../project/STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — intenção, arquitetura, tipos de página.
3. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.
4. [`keyword-cluster-map`](../keyword-cluster-map/SKILL.md) — output de keywords que alimenta o brief.
5. [`serp-intent-audit`](../serp-intent-audit/SKILL.md) — análise de intenção SERP.

---

## Inputs necessários

Para um brief de qualidade:

- keyword principal e variações (do `keyword-intent`);
- intenção de pesquisa confirmada ou a confirmar;
- contexto SERP: tipo de página que rankeia, padrões, gaps (de `serp-competitor-analyst`);
- objetivo comercial da página;
- público-alvo;
- serviço, produto ou tema;
- factos reais da empresa: serviços, certificações, processos, provas, diferenciais;
- restrições de compliance ou marca;
- arquitectura actual: páginas existentes no mesmo cluster.

Se inputs faltarem, trabalhar com o disponível e marcar lacunas explicitamente.

---

## Procedimento

### Passo 1 — Confirmar intenção de pesquisa

Antes de qualquer estrutura:

- Confirmar intenção dominante: informacional, comercial, transacional, local.
- Confirmar tipo de página que a SERP favorece (via `serp-intent-audit` se disponível):
  - Serviço: a página deve apresentar o serviço e conduzir a contacto/proposta.
  - Guia/informacional: a página deve educar, estruturar e ser citável.
  - Comparativo: a página deve comparar opções e ajudar a decidir.
  - Local: a página deve reflectir presença local real.
  - FAQ: a página deve responder directamente a perguntas.

**Decisão:** o tipo de página determina a estrutura. Não criar estrutura de guia se a SERP favorece serviço, e vice-versa.

---

### Passo 2 — Verificar arquitetura

Antes de avançar:

- Esta página já existe no site? (pode ser refresh, não criação)
- Existe outra página que cobre a mesma intenção? (canibalização)
- Qual é o papel desta página na arquitectura? (pilar, suporte, serviço, guia)
- De que páginas deve receber links? Para que páginas deve linkar?

Se houver canibalização, parar e devolver ao `seo-lead` para decisão de arquitectura.

---

### Passo 3 — Definir título, meta e tipo de página

**Título sugerido (H1):**
- Alinhado com a keyword principal e a intenção.
- Claro, específico, orientado ao utilizador.
- Não genérico ("Serviços de X" sem mais contexto).
- Dentro de limite razoável para uso como H1 (~70 chars).

**Meta description sugerida:**
- ~155 chars.
- Resume proposta de valor e inclui CTA implícito.
- Diferente do H1 mas alinhada.
- Não é copy do H1 repetida.

**Tipo de página:**
- Confirmado com base na intenção SERP.
- Usado para definir estrutura.

---

### Passo 4 — Criar outline H1/H2/H3

Para cada secção, definir:

- o que deve estar nela;
- que objetivo cumpre para o utilizador;
- que prova ou conteúdo específico é necessário.

**Estrutura padrão para página de serviço:**

```
H1: [serviço + proposta de valor ou diferencial]
  H2: O que é / para quem é / quando usar
  H2: Como funciona [processo específico]
    H3: Passo 1
    H3: Passo 2
  H2: O que inclui / O que entregamos
  H2: Porquê [empresa] / Diferenciais
    H3: [diferencial 1]
    H3: [diferencial 2]
  H2: Perguntas frequentes
  H2: [CTA section]
```

**Estrutura padrão para guia/informacional:**

```
H1: [tópico + complemento que sinaliza utilidade]
  H2: O que é [X] — definição clara
  H2: Para quem se aplica / Quando é obrigatório
  H2: Como funciona / Processo
    H3: [componente 1]
    H3: [componente 2]
  H2: O que devo ter/fazer
  H2: Erros comuns / O que evitar
  H2: Perguntas frequentes
  H2: Próximo passo [CTA]
```

Adaptar sempre à realidade do tema e do negócio.

---

### Passo 5 — Definir must-answer questions

Listar 5-10 perguntas que a página deve responder obrigatoriamente:

- Que perguntas alguém com esta intenção teria?
- Que objecções surgem nesta fase da jornada?
- Que dúvidas são recorrentes (People Also Ask, FAQs de concorrentes)?
- Que perguntas de compliance ou saúde surgem neste tema?

Estas perguntas devem estar cobertas na página, não necessariamente como H2 mas como conteúdo visível.

---

### Passo 6 — Definir FAQs estratégicas

FAQs estratégicas são perguntas reais que clientes fazem.

Não são:
- "Porque escolher [empresa]?"
- "O que é [serviço]?" (se o H2 já responde)
- Perguntas óbvias sem valor.

São:
- "Quanto tempo demora o processo?"
- "É obrigatório por lei?"
- "Que documentos preciso?"
- "Qual é o custo?"
- "Posso fazer online ou presencialmente?"

Para cada FAQ sugerida, indicar orientação de resposta (não escrever a resposta completa — isso é papel do `content-growth`).

---

### Passo 7 — Definir prova e trust elements

Identificar o que é necessário para que a página seja confiável:

- Certificações reais que a empresa tem (se aplicável).
- Anos de experiência (real, verificável).
- Sectores ou tipos de clientes servidos (sem inventar).
- Processo específico da empresa (não genérico).
- Parcerias ou reconhecimentos (verificáveis).
- Dados ou estudos internos (se existirem).

Marcar como "a preencher pela empresa" o que não for conhecido.

Bloquear se o brief exigir claims que a empresa não pode verificar.

---

### Passo 8 — Definir CTAs e links internos

**CTA principal:**
- Tipo: contacto, proposta, pedido de orçamento, download, chamada, formulário.
- Posição: acima do fold (após proposta de valor), após prova, no final.
- Linguagem: específica ao serviço, não genérica ("Pedir proposta de medicina do trabalho" vs "Contacte-nos").

**CTA secundário** (se aplicável):
- Guia relacionado, simulador, checklist, exemplo.

**Links internos:**
- De que páginas esta deve receber links? (serviços relacionados, homepage, guias)
- Para que páginas esta deve linkar? (serviços complementares, contacto, guias)

---

### Passo 9 — Definir schema potencial

Indicar tipos de schema aplicáveis:

- Service: se for página de serviço.
- FAQPage: se houver FAQs visíveis no HTML.
- LocalBusiness: se houver dimensão local.
- BreadcrumbList: se a estrutura de navegação suportar.
- Article/BlogPosting: se for artigo editorial.

Passar para `schema-entity` para desenho completo se for schema complexo.

---

### Passo 10 — Definir critério de aceitação

Definir explicitamente:

- O que torna esta página publicável?
- O que a tornaria genérica ou abaixo do standard?
- Que elementos são obrigatórios vs desejáveis?
- Há compliance ou revisão humana obrigatória?

---

## Output esperado

```md
## Content Brief — [Título sugerido]

### Objectivo
[negócio + SEO]

### Público-alvo
[quem, necessidade, fase]

### Intenção de pesquisa
[dominante + tipo de página SERP]

### Keyword principal + variações
[...]

### Tipo de página
[serviço / guia / comparativo / local / FAQ]

### Papel na arquitectura
[pilar / suporte / serviço / guia]

### Título sugerido (H1)
[...]

### Meta description sugerida
[...]

### Outline
[estrutura H1/H2/H3 com indicações por secção]

### Must-answer questions
[5-10 perguntas obrigatórias]

### FAQs estratégicas
[perguntas reais + orientação de resposta]

### Prova e trust elements necessários
[o que a empresa precisa de fornecer]

### Internal links
[receber de + linkar para]

### CTA principal
[tipo, posição, linguagem]

### Schema potencial
[tipos + indicação para schema-entity]

### O que superar na concorrência
[2-3 pontos específicos]

### Critério de aceitação
[o que torna a página publicável]

### Claims ou áreas de revisão humana
[lista com risco]

### Próximo passo
[content-growth / seo-qa / etc.]
```

---

## Gates de segurança

Read-only (brief é documento de planeamento, não de implementação).

Bloquear ou marcar como incompleto quando:

- intenção de pesquisa não confirmada;
- canibalização com página existente não resolvida;
- brief exige claims que a empresa não pode verificar;
- conteúdo é YMYL sensível sem identificar revisão humana;
- trust elements necessários são desconhecidos e decisivos.

---

## Relação com agentes e docs

- [`content-brief`](../../agents/content-brief.md) — agente que usa este procedimento.
- [`content-growth`](../../agents/content-growth.md) — consome o brief para escrever/rever.
- [`keyword-intent`](../../agents/keyword-intent.md) — fornece cluster e intenção.
- [`serp-competitor-analyst`](../../agents/serp-competitor-analyst.md) — fornece contexto SERP.
- [`schema-entity`](../../agents/schema-entity.md) — aprofunda schema quando brief identifica tipos aplicáveis.
- [`onpage-seo`](../../agents/onpage-seo.md) — aplica otimização on-page depois do brief.
- [`CONTENT_RULES.md`](../../project/CONTENT_RULES.md) — standards de qualidade.
- [`STRATEGY_RULES.md`](../../project/STRATEGY_RULES.md) — intenção e arquitetura.

---

## Exemplos de pedidos que aceita

- "Usa este procedimento para gerar um brief para a página de medicina do trabalho."
- "Segue o processo de brief generation para este cluster de keywords."
- "Gera o brief antes de avançarmos para a redacção."
- "Transforma esta pesquisa de keywords num brief acionável."

---

## Exemplos de pedidos que deve encaminhar

Encaminhar para `keyword-cluster-map`:

- "Primeiro precisamos das keywords — faz o cluster map."

Encaminhar para `serp-intent-audit`:

- "Primeiro precisamos de saber que tipo de página rankeia para esta query."

Encaminhar para `content-growth`:

- "A página já existe — preciso de a rever, não de criar de raiz."

Encaminhar para `seo-quality-gate` com `seo-qa`:

- "O conteúdo está escrito — valida antes de publicar."

---

## Erros comuns a evitar

- Criar outline genérico sem confirmar intenção SERP.
- Criar estrutura de guia quando a SERP favorece página de serviço.
- Criar brief sem identificar prova necessária.
- Não definir must-answer questions específicas.
- Não identificar canibalização com páginas existentes.
- Inventar certificações ou dados para enriquecer o brief.
- Confundir brief com copy final — o brief orienta, não escreve.
- Não definir critério de aceitação.

---

## Regra final

Um brief de qualidade transforma pesquisa em direcção clara.

O redactor que recebe o brief deve saber exactamente o que escrever, que prova usar, que perguntas responder, que tom manter e o que é inaceitável.

Se o brief não define isso — não está pronto.
