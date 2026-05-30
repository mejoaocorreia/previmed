---
name: local-seo-review
description: Procedimento para rever a presença local de um site — GBP, NAP, páginas locais, reviews, citations e schema LocalBusiness — apenas para localizações reais. Nunca inventa moradas ou áreas.
---

# Skill: Local SEO Review

Procedimento operacional para rever a presença local de um site ou negócio.

Esta skill é usada principalmente pelo [`local-seo`](../../agents/local-seo.md) para conduzir revisões de local SEO de forma estruturada.

Esta skill não é um agente.  
Esta skill não altera o Google Business Profile.  
Esta skill não inventa moradas ou áreas de serviço.  
Esta skill não cria páginas locais vazias.  
Esta skill define o procedimento para rever presença local de forma consistente.

---

## Objetivo

Rever a presença local de um negócio — GBP, NAP, páginas locais, service areas, reviews, citations e schema — e identificar gaps, inconsistências e oportunidades, sempre com base em presença ou intenção local real.

---

## Quando usar

Usar nos modos:

- `/seo local` — modo principal;
- `/seo audit` — componente de local SEO;
- `/seo go-live` — validação local antes de go-live.

---

## Quando não usar

Não usar para:

- alterar GBP — requer autorização do Supervisor;
- criar páginas locais sem intenção real;
- análise técnica geral — usar `technical-seo-crawl-audit`;
- schema LocalBusiness completo — usar `schema-entity-review`.

---

## Quem pode usar

Principal:

- [`local-seo`](../../agents/local-seo.md)

Também pode usar:

- [`schema-entity`](../../agents/schema-entity.md) para verificação de schema LocalBusiness.

---

## Fontes de verdade

1. [`../../project/LOCAL_SEO_PLAYBOOK.md`](../../project/LOCAL_SEO_PLAYBOOK.md) — processo e standard de local SEO.
2. [`../../project/SCHEMA_ENTITY_MODEL.md`](../../project/SCHEMA_ENTITY_MODEL.md) — LocalBusiness e NAP.
3. [`../../project/QUALITY_GATE.md`](../../project/QUALITY_GATE.md) — critérios de aprovação.

---

## Inputs necessários

- Localizações ou service areas reais;
- dados NAP: nome exacto, morada, telefone;
- acesso ao GBP (leitura, se autorizado);
- URL do website e páginas locais existentes;
- queries locais prioritárias.

---

## Procedimento

### Passo 1 — Confirmar presença local real

Antes de qualquer análise:

- A empresa tem localização física?
- A empresa tem service areas confirmadas?
- Há queries locais com intenção real?

Se não há presença ou intenção local real, declarar e não criar páginas ou schema local sem base.

---

### Passo 2 — Verificar GBP

Quando autorizado:

- GBP activo e verificado?
- Categorias corretas para o negócio?
- Descrição completa e actualizada?
- Fotos presentes (interior, exterior, equipa, serviços)?
- Service areas definidas correctamente?
- Reviews visíveis e respondidas?
- Horário correcto?
- Q&A actualizado?

Se não há acesso ao GBP, declarar como "a confirmar".

**Não alterar GBP sem autorização explícita.**

---

### Passo 3 — Verificar NAP

Para cada fonte:

| Fonte | Nome | Morada | Telefone | Consistente? |
|---|---|---|---|---|
| Website (footer, contacto) | | | | |
| Google Business Profile | | | | |
| Facebook | | | | |
| LinkedIn | | | | |
| Diretórios principais | | | | |

Identificar cada inconsistência e impacto potencial.

**Inconsistências NAP prejudicam ranking local.**

---

### Passo 4 — Verificar páginas locais

Para cada página local existente:

- Tem conteúdo útil e específico para a localização?
- Ou é doorway page (conteúdo genérico com cidade trocada)?
- Tem intenção local real justificada?
- Tem schema LocalBusiness?

Para páginas locais a criar:

- Há intenção local real (queries locais activas)?
- Haverá conteúdo específico (não genérico)?
- A empresa actua realmente nessa área?

Se não há conteúdo útil possível → não criar.

---

### Passo 5 — Verificar service areas

- Que áreas a empresa serve realmente?
- Correspondem às service areas no GBP?
- Correspondem ao website?
- Há áreas relevantes em falta?

---

### Passo 6 — Verificar reviews

- Quantas reviews no GBP?
- Qual é o rating médio?
- Reviews estão a ser respondidas (positivas e negativas)?
- Há padrões problemáticos?
- Há estratégia activa de solicitação?

Recomendar: responder sempre a reviews negativas, solicitar reviews após entrega de serviço (sem incentivo indevido).

---

### Passo 7 — Verificar citations

- A empresa está nos principais diretórios locais relevantes?
- NAP é consistente nesses diretórios?
- Há diretórios sectoriais importantes em falta?

---

### Passo 8 — Verificar schema LocalBusiness

- Schema LocalBusiness existe?
- Propriedades obrigatórias presentes (name, address, telephone)?
- Morada é real e correcta?
- sameAs aponta para perfis oficiais?
- Handoff para `schema-entity-review` para especificação completa.

---

## Output esperado

```md
## Local SEO Review — [Empresa] — YYYY-MM-DD

### Presença local confirmada
[localizações, service areas, intenção local]

### GBP
- Estado: [activo / incompleto / inexistente / a confirmar]
- Categorias: [corretas / a rever]
- Completude: [score estimado]
- Oportunidades: [lista]

### NAP
| Fonte | Consistente? | Problemas |
|---|---|---|

### Páginas locais
| Página | Estado | Recomendação |
|---|---|---|

### Service Areas
[mapeamento real vs. declarado]

### Reviews
[volume, rating, estado, estratégia]

### Citations
[presença, inconsistências, oportunidades]

### Schema LocalBusiness
[estado + handoff para schema-entity-review]

### Riscos
[doorway pages, NAP inconsistente, GBP sem autorização]

### Próximo passo
[ação imediata]
```

---

## Gates de segurança

- Nunca criar doorway pages ou páginas locais vazias.
- Nunca inventar moradas, telefones ou áreas de serviço.
- Nunca alterar GBP sem autorização.
- Nunca criar schema LocalBusiness com dados falsos.
- Nunca solicitar reviews com incentivo indevido.

---

## Relação com agentes e docs

- [`local-seo`](../../agents/local-seo.md) — agente principal.
- [`schema-entity`](../../agents/schema-entity.md) — schema LocalBusiness.
- [`schema-entity-review`](../schema-entity-review/SKILL.md) — procedimento de schema.
- [`wordpress-seo-implementation`](../../agents/wordpress-seo-implementation.md) — implementação.
- [`seo-qa`](../../agents/seo-qa.md) — validação final.
- [`LOCAL_SEO_PLAYBOOK.md`](../../project/LOCAL_SEO_PLAYBOOK.md) — standard local.
- [`SCHEMA_ENTITY_MODEL.md`](../../project/SCHEMA_ENTITY_MODEL.md) — LocalBusiness e NAP.

---

## Exemplos de pedidos que aceita

- "Aplica o procedimento de local SEO review a este negócio."
- "Revê a presença local usando este processo."
- "Verifica NAP e GBP seguindo o procedimento."

---

## Erros comuns a evitar

- Criar páginas locais sem intenção real.
- Ignorar inconsistências NAP.
- Não registar o que ficou por confirmar (GBP sem acesso).
- Confundir schema Local com estratégia local completa.

---

## Regra final

Local SEO real começa com presença real.

NAP consistente, GBP completo, pages locais com conteúdo útil — nunca inventado.
