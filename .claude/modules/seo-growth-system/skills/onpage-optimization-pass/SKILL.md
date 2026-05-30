---
name: onpage-optimization-pass
description: Procedimento passo a passo para optimizar os elementos on-page de uma página — title, meta description, H1/H2/H3, copy, FAQs, links internos e alt text — mantendo leitura humana e sem keyword stuffing.
---

# Skill: On-page Optimization Pass

Procedimento operacional para optimizar elementos on-page de uma página.

Esta skill é usada principalmente pelo [`onpage-seo`](../../agents/onpage-seo.md) para fazer uma passagem completa de otimização on-page — verificando cada elemento de forma estruturada e produzindo recomendações claras.

Esta skill não é um agente.  
Esta skill não faz estratégia de conteúdo.  
Esta skill não faz keyword research.  
Esta skill não implementa em WordPress.  
Esta skill não publica conteúdo.  
Esta skill define o procedimento para optimizar elementos on-page de forma consistente.

---

## Objetivo

Optimizar os elementos on-page de uma página específica — title, meta description, H1, estrutura de headings, copy, FAQs, links internos e alt text — garantindo alinhamento com intenção de pesquisa, leitura humana natural e ausência de keyword stuffing.

---

## Quando usar

Usar nos modos:

- `/seo content` — parte da análise e optimização de conteúdo;
- `/seo brief` — após brief aprovado, antes de escrever;
- `/seo audit` — como parte da auditoria on-page.

Usar quando:

- o title de uma página precisa de melhorar;
- a meta description está em falta ou é fraca;
- os headings estão desorganizados ou artificiais;
- há keyword stuffing no copy;
- as FAQs não respondem a perguntas reais;
- os links internos na página são insuficientes;
- o alt text das imagens está vazio ou é spam de keyword.

---

## Quando não usar

Não usar para:

- estratégia de conteúdo — usar `content-growth`;
- keyword research — usar `keyword-cluster-map`;
- brief editorial — usar `content-brief-generation`;
- arquitectura global de links — usar `internal-linking`;
- schema semântico — usar `schema-entity-review`;
- diagnóstico técnico — usar `technical-seo-crawl-audit`;
- implementação WordPress — usar `wordpress-seo-implementation`;
- validação final — usar `seo-quality-gate` com `seo-qa`.

---

## Quem pode usar

Principal:

- [`onpage-seo`](../../agents/onpage-seo.md)

Também pode usar:

- [`content-growth`](../../agents/content-growth.md) quando análise de conteúdo inclui on-page;
- [`seo-lead`](../../agents/seo-lead.md) em coordenação de revisões de página.

---

## Fontes de verdade

Consultar por esta ordem:

1. [`../../project/CONTENT_RULES.md`](../../project/CONTENT_RULES.md) — critérios de qualidade, leitura humana, claims.
2. [`../../project/TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — limites técnicos de title/meta.
3. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.

---

## Inputs necessários

Para executar a passagem on-page:

- URL ou conteúdo actual da página;
- keyword principal e intenção de pesquisa;
- brief ou output de `content-brief` (se existir);
- tom de marca;
- contexto de conversão (o que o utilizador deve fazer).

Sem keyword e intenção confirmadas, a optimização é incompleta.

---

## Procedimento

### Passo 1 — Confirmar intenção e keyword

Antes de optimizar qualquer elemento:

- Qual é a keyword principal?
- Qual é a intenção dominante (informacional, comercial, transacional, local)?
- Que tipo de página é (serviço, guia, landing, FAQ, institucional)?
- Qual é o objectivo de conversão?

Sem esta confirmação, qualquer optimização pode estar mal orientada.

---

### Passo 2 — Title tag

**Verificar:**
- Está dentro do limite de ~60 caracteres?
- Inclui a keyword de forma natural (não forçada)?
- É orientado a CTR — cria curiosidade, promete solução ou valor claro?
- É único no site (não duplica outro title)?
- Não é genérico ("Serviços de X" sem diferenciação)?

**Problemas comuns:**
- Title truncado acima de 60 chars.
- Title igual ao H1 palavra a palavra.
- Title genérico sem diferenciação.
- Keyword espremida de forma não natural.

**Output:**
- Title actual (com nº de chars).
- Title recomendado (com nº de chars).
- Justificação.

---

### Passo 3 — Meta description

**Verificar:**
- Está dentro do limite de ~155 caracteres?
- Resume a proposta de valor da página?
- Inclui CTA implícito?
- É diferente do title (complementa, não repete)?
- Não é apenas o primeiro parágrafo da página copiado?
- Não é genérica ("Saiba mais sobre os nossos serviços")?

**Problemas comuns:**
- Meta vazia (Google escolhe o snippet).
- Meta duplicada com outra página.
- Meta que não reflecte o conteúdo real da página.

**Output:**
- Meta actual (com nº de chars).
- Meta recomendada (com nº de chars).
- Justificação.

---

### Passo 4 — H1

**Verificar:**
- Existe exactamente um H1?
- Está alinhado com keyword principal e intenção?
- É diferente do title (mas consistente — podem partilhar keyword)?
- Não repete o title palavra a palavra?
- Não é vago ("Bem-vindo" ou "Sobre Nós" como H1 de página de serviço)?

**Problemas comuns:**
- Página sem H1.
- Múltiplos H1.
- H1 desalinhado com keyword.
- H1 idêntico ao title.

**Output:**
- H1 actual.
- H1 recomendado.
- Justificação.

---

### Passo 5 — Estrutura de headings H2/H3

**Verificar:**
- Hierarquia correcta: H1 → H2 → H3 (sem saltar níveis)?
- Cada H2 cobre uma dimensão lógica e distinta do tema?
- H3 são sub-secções genuínas ou apenas decoração visual?
- Há headings redundantes (mesmo conceito repetido em H2 e H3)?
- Há headings apenas de marketing sem conteúdo ("Porquê escolher-nos?" sem resposta real)?

**Output:**
- Estrutura actual.
- Estrutura recomendada (H2 > H3 se necessário).
- Justificação por cada alteração.

---

### Passo 6 — Copy on-page

**Verificar:**
- Há keyword stuffing? (mesmo termo repetido em excesso, especialmente em posições artificiais)
- O copy é específico desta empresa ou podia ser de qualquer uma?
- Há frases de marketing vazio ("soluções inovadoras", "serviço de excelência") sem substância?
- Parágrafos são curtos e scannable (3-4 linhas max)?
- O copy segue o tom de marca?
- Há afirmações sem prova que podem ser problemáticas?

**Regra de densidade:** a keyword deve aparecer de forma natural, não a cada parágrafo forçosamente. Uma página de 500 palavras com keyword 8+ vezes forçadas tem stuffing.

**Output:**
- Lista de secções com problemas.
- Sugestões de reformulação (não reescrita completa — indicar direcção).

---

### Passo 7 — FAQs

**Verificar:**
- As FAQs respondem a perguntas que utilizadores realmente fazem?
- Ou são FAQs de marketing ("Porquê escolher-nos?")?
- As respostas são directas, concisas e específicas?
- Há conteúdo que merecia ser FAQ mas está escondido em parágrafos?
- FAQPage schema é aplicável? (apenas se FAQs são visíveis no HTML)

**Output:**
- FAQs actuais problemáticas (e porquê).
- FAQs sugeridas (perguntas reais + orientação de resposta).

---

### Passo 8 — Links internos contextuais

**Verificar:**
- A página tem links internos para páginas relacionadas do cluster?
- Os anchors são naturais (não "clique aqui" ou "saiba mais")?
- Há excesso de links (spam de internal links — mais de 10-15 internos numa página simples)?
- Páginas importantes do cluster ou da arquitectura estão ligadas?

**Output:**
- Links internos a adicionar (anchor, URL destino, localização sugerida, motivo).
- Links internos problemáticos a corrigir.

---

### Passo 9 — Alt text de imagens

**Verificar:**
- Imagens têm alt text?
- Alt text é descritivo (não spam de keyword)?
- Imagens decorativas têm alt="" (vazio)?
- Imagem LCP (Hero) está sem lazy load indevido (`loading="lazy"` remove em imagens acima do fold)?

**Output:**
- Imagens sem alt text.
- Alt text problemáticos.
- Alt text sugeridos.
- Nota sobre imagem LCP se aplicável.

---

## Output esperado

```md
## On-page Optimization Pass — [Página/URL]

### Title
- Actual: [...] (X chars)
- Recomendado: [...] (X chars)
- Motivo: [...]

### Meta description
- Actual: [...] (X chars)
- Recomendada: [...] (X chars)
- Motivo: [...]

### H1
- Actual: [...]
- Recomendado: [...]
- Motivo: [...]

### Estrutura de headings recomendada
H1: [...]
  H2: [...]
    H3: [...]
  H2: [...]

### Melhorias de copy
| Secção | Problema | Sugestão |
|---|---|---|

### FAQs
| Actual | Problema | Recomendada |
|---|---|---|

### Links internos sugeridos
| Anchor | URL destino | Posição | Motivo |
|---|---|---|---|

### Alt text
| Imagem | Actual | Sugerido |
|---|---|---|

### Notas de UX/SEO
[observações não bloqueantes]
```

---

## Gates de segurança

**Regras absolutas:**

- Não criar keyword stuffing — densidade natural, não artificial.
- Não criar headings artificiais sem conteúdo real.
- Não duplicar titles entre páginas do mesmo site.
- Não duplicar meta descriptions entre páginas.
- Não usar anchor text spam nos links internos.
- Não colocar keywords em alt text de forma não natural.
- Não recomendar titles que prometem algo que a página não entrega.
- Não recomendar copy com claims não verificados.

**Publicação:**

- Optimização on-page é uma proposta — não vai para produção directamente.
- Implementação passa por `wordpress-seo-implementation` com autorização.
- Publicação passa por `seo-qa` quando relevante.

---

## Relação com agentes e docs

- [`onpage-seo`](../../agents/onpage-seo.md) — agente que usa este procedimento.
- [`content-growth`](../../agents/content-growth.md) — avalia qualidade de conteúdo; on-page aplica a optimização mecânica.
- [`content-brief`](../../agents/content-brief.md) — brief que orienta a optimização.
- [`internal-linking`](../../agents/internal-linking.md) — arquitectura global de links; on-page aplica links contextuais.
- [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md) — implementa os elementos optimizados.
- [`seo-qa`](../../agents/seo-qa.md) — valida antes de publicação.
- [`CONTENT_RULES.md`](../../project/CONTENT_RULES.md) — standards de conteúdo.
- [`TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — limites técnicos.

---

## Exemplos de pedidos que aceita

- "Aplica o procedimento de on-page optimization a esta página."
- "Faz passagem completa on-page antes de publicar."
- "Verifica todos os elementos on-page desta landing page."
- "Revê title, meta, headings e links internos desta página de serviço."

---

## Exemplos de pedidos que deve encaminhar

Encaminhar para `content-growth`:

- "Esta página precisa de melhorar a qualidade e confiança do conteúdo."

Encaminhar para `content-brief-generation`:

- "Precisamos de um brief antes de optimizar."

Encaminhar para `schema-entity-review`:

- "O schema desta página precisa de ser revisto."

Encaminhar para `wordpress-seo-implementation` + Supervisor:

- "Implementa os titles e metas no WordPress."

---

## Erros comuns a evitar

- Criar keyword stuffing tentando "optimizar mais".
- Criar headings H2/H3 sem conteúdo real por baixo.
- Duplicar title ou meta com outra página.
- Usar anchors genéricos nos links internos.
- Escrever alt text como lista de keywords.
- Optimizar sem conhecer intenção de pesquisa.
- Confundir on-page mecânico com revisão de conteúdo.

---

## Regra final

On-page optimizado não é on-page com mais keywords.

É on-page que o Google entende facilmente e o utilizador lê com prazer.

Title claro. Meta honesta. Headings lógicos. Copy específico. Links úteis.
