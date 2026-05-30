---
name: schema-entity-review
description: Procedimento para rever ou modelar dados estruturados e entidades — garantindo correspondência com conteúdo visível, propriedades obrigatórias, ausência de duplicação e validação técnica.
---

# Skill: Schema & Entity Review

Procedimento operacional para rever ou modelar schema JSON-LD e entidades de um site ou página.

Esta skill é usada principalmente pelo [`schema-entity`](../../agents/schema-entity.md) para conduzir revisões de schema de forma estruturada e consistente.

Esta skill não é um agente.  
Esta skill não implementa schema em WordPress.  
Esta skill não inventa dados.  
Esta skill define o procedimento para rever e modelar schema de forma consistente.

---

## Objetivo

Rever ou modelar dados estruturados e entidades de uma página ou site — garantindo que cada schema representa conteúdo visível real, tem propriedades obrigatórias, não está duplicado e pode ser validado.

---

## Quando usar

Usar nos modos:

- `/seo schema` — modo principal;
- `/seo audit` — componente de schema na auditoria;
- `/seo go-live` — validação de schema antes de go-live;
- `/seo technical` — quando auditoria técnica inclui schema.

Usar quando:

- há schema a criar para nova página;
- há schema existente a rever;
- há duplicação de schema entre plugin, tema e markup manual;
- há dúvida sobre que tipos ou propriedades usar;
- há validação de schema necessária antes de go-live.

---

## Quando não usar

Não usar para:

- implementar schema no WordPress — usar `wordpress-seo-implementation`;
- diagnóstico técnico geral — usar `technical-seo-crawl-audit`;
- schema para conteúdo invisível ou inventado.

---

## Quem pode usar

Principal:

- [`schema-entity`](../../agents/schema-entity.md)

Também pode usar:

- [`technical-seo`](../../agents/technical-seo.md) para validação técnica de schema;
- [`seo-qa`](../../agents/seo-qa.md) para validação antes de go-live.

---

## Fontes de verdade

1. [`../../project/SCHEMA_ENTITY_MODEL.md`](../../project/SCHEMA_ENTITY_MODEL.md) — tipos, propriedades, standards.
2. [`../../project/TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — regras técnicas de schema.
3. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.

---

## Inputs necessários

- Conteúdo visível da página;
- dados reais da entidade (nome, morada, contactos, perfis);
- schema actualmente presente (view-source ou Rich Results Test);
- plugin SEO activo e o que gera;
- tema activo e se gera schema.

---

## Procedimento

### Passo 1 — Identificar entidades e tipos

Para cada página ou secção, identificar:

- Que entidade representa? (organização, serviço, localização, FAQ, artigo, pessoa)
- Que tipo Schema.org é mais adequado?

**Tipos mais comuns:**

| Tipo | Quando usar |
|---|---|
| Organization | Homepage, página institucional |
| LocalBusiness | Quando há localização física real ou área de serviço |
| WebSite | Homepage (com SearchAction se houver pesquisa interna) |
| WebPage | Qualquer página (base para outros tipos) |
| Service | Página de serviço específico |
| BreadcrumbList | Qualquer página com breadcrumb de navegação |
| FAQPage | Apenas com FAQ visível no HTML |
| Article / BlogPosting | Artigos com data e autor real |
| Person | Página de autor com informação real |
| ContactPoint | Contactos (telefone, email, horário) |

---

### Passo 2 — Verificar correspondência com conteúdo visível

Para cada propriedade do schema proposto:

- A informação está visível no HTML renderizado da página?
- Não é conteúdo escondido em modal, accordion não expandido ou fora do viewport?
- A propriedade representa dados reais (não inventados)?

**Regra:** se a informação não está visível na página, não pode estar no schema.

---

### Passo 3 — Verificar propriedades obrigatórias

**Organization:**
- Obrigatório: `name`, `url`.
- Recomendado: `logo` (com `ImageObject`), `contactPoint`, `sameAs`, `address`.

**LocalBusiness:**
- Obrigatório: `name`, `address` (com `PostalAddress`), `telephone`.
- Recomendado: `openingHours`, `geo` (com `GeoCoordinates`), `priceRange`, `servesCuisine` se aplicável.

**WebSite:**
- Obrigatório: `name`, `url`.
- Recomendado: `potentialAction` com `SearchAction` (se houver pesquisa interna).

**WebPage:**
- Obrigatório: `name`, `url`.
- Recomendado: `description`, `breadcrumb`.

**BreadcrumbList:**
- Obrigatório: `itemListElement` com `ListItem`: `position` (número), `name`, `item` (URL).

**FAQPage:**
- Obrigatório: `mainEntity` com múltiplos `Question`: `name` (pergunta), `acceptedAnswer` com `Answer` e `text`.
- Apenas usar se FAQ está visível no HTML.

**Service:**
- Obrigatório: `name`, `provider`.
- Recomendado: `description`, `areaServed`, `serviceType`.

---

### Passo 4 — Verificar sameAs

Para cada URL em `sameAs`:

- É um perfil oficial real da empresa?
- A URL está correcta e acessível?
- É verificável (LinkedIn, Facebook, Instagram, Twitter/X, Google Business Profile, Wikidata)?
- Não há perfis pessoais ou desactualizados?

Se não há certeza sobre um perfil, não incluir e marcar como "a confirmar pela empresa".

---

### Passo 5 — Verificar e resolver duplicação

**Fontes de schema a verificar:**

- Plugin SEO (Yoast SEO, Rank Math, etc.) — ver o que gera automaticamente.
- Tema WordPress — alguns temas geram schema próprio.
- Markup manual — JSON-LD ou RDFa no tema ou em plugins específicos.

**Verificar via:**
- view-source da página → procurar `application/ld+json`;
- Rich Results Test.

**Para cada conflito:**
- Identificar qual fonte deve ser mantida.
- Identificar qual deve ser desactivada.
- Recomendar handoff para `wordpress-seo-implementation` para resolver.

**Regra:** só deve existir uma fonte de schema por tipo em cada página.

---

### Passo 6 — Identificar riscos

**Schema enganador:**
- Reviews com rating sem reviews reais na página.
- Preços sem preço real ou apenas preço base não representativo.
- Morada falsa ou inventada.
- Áreas de serviço inventadas.
- FAQPage para FAQs não visíveis.

**Qualquer schema enganador deve ser bloqueado.**

---

### Passo 7 — Validar

Quando possível:
- Rich Results Test para URLs acessíveis.
- Schema.org validator para código disponível.

Registar resultado:
- "Validado com Rich Results Test — sem erros."
- "Validado parcialmente — [limitações]."
- "Não validado — URL não acessível / ferramenta não disponível."

---

## Output esperado

```md
## Schema & Entity Review — [Página/Entidade]

### Entidades identificadas
| Entidade | Tipo Schema.org | Página aplicável |
|---|---|---|

### Schema proposto por página

#### [Página / URL]
**Tipo:** [...]
**JSON-LD:**
```json
{
  "@context": "https://schema.org",
  "@type": "...",
  ...
}
```
**Propriedades em falta:** [lista]
**Fonte dos dados:** [conteúdo visível / dados confirmados / a preencher]

### sameAs
[lista de URLs verificadas]

### Duplicação identificada
[fonte A vs. fonte B — recomendação]

### Validação
[resultado de Rich Results Test ou Schema.org validator]

### Riscos
[schema enganador, dados inventados, duplicação]

### Handoff para wordpress-seo-implementation
[o que implementar, onde, como]
```

---

## Gates de segurança

- Nunca criar schema para conteúdo invisível.
- Nunca inventar reviews, ratings, preços, moradas ou serviços.
- Nunca usar sameAs para perfis não oficiais.
- Nunca criar FAQPage para FAQs não visíveis no HTML.
- Nunca duplicar schema sem resolver conflito.
- Bloquear e pedir autorização para implementação WordPress.

---

## Relação com agentes e docs

- [`schema-entity`](../../agents/schema-entity.md) — agente que usa este procedimento.
- [`technical-seo`](../../agents/technical-seo.md) — valida dimensão técnica de schema.
- [`local-seo`](../../agents/local-seo.md) — aprofunda LocalBusiness e NAP.
- [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md) — implementa schema aprovado.
- [`seo-qa`](../../agents/seo-qa.md) — valida antes de go-live.
- [`SCHEMA_ENTITY_MODEL.md`](../../project/SCHEMA_ENTITY_MODEL.md) — tipos e propriedades.
- [`TECHNICAL_RULES.md`](../../project/TECHNICAL_RULES.md) — regras técnicas.

---

## Exemplos de pedidos que aceita

- "Revê o schema desta página usando o procedimento."
- "Modela o schema Organization para a homepage."
- "Verifica se há duplicação de schema neste site."
- "Valida se o FAQPage schema é correcto para esta página."
- "Identifica propriedades obrigatórias em falta no LocalBusiness."

---

## Exemplos de pedidos que deve encaminhar

- Para `wordpress-seo-implementation`: "Implementa o schema no WordPress."
- Para `technical-seo-crawl-audit`: "O schema não está a ser lido pelo Google — diagnostica."
- Para `seo-quality-gate` com `seo-qa`: "Valida o schema antes de go-live."

---

## Erros comuns a evitar

- Criar schema para conteúdo não visível.
- Inventar reviews ou dados não reais.
- Usar sameAs sem verificar os perfis.
- Esquecer de verificar duplicação entre plugin e tema.
- Dizer "schema válido" sem validar com ferramenta.
- Confundir schema correcto com schema completo.

---

## Regra final

Schema correcto e simples vale mais que schema excessivo e errado.

O que não está na página não deve estar no schema.  
O que está no schema deve ser verificável.
