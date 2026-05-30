# Schema & Entity Model

Fonte de verdade para dados estruturados e entidades do **SEO Growth System**.

Este ficheiro define os standards para schema JSON-LD — tipos, propriedades obrigatórias, regras de sameAs e NAP, limites de schema, e o processo para modelar entidades de forma que ajude motores de pesquisa e sistemas de IA a entender quem é a empresa, o que faz e onde actua.

Este ficheiro não é um agente.  
Este ficheiro não executa alterações.  
Este ficheiro não substitui o `schema-entity`, a skill `schema-entity-review` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que os dados estruturados de qualquer site que use este module representam com precisão as entidades reais, usam tipos adequados, têm propriedades obrigatórias, não estão duplicados e não são enganadores.

---

## Âmbito

Este documento cobre:

- princípios de schema JSON-LD;
- tipos Schema.org mais comuns e quando usar;
- propriedades obrigatórias e recomendadas por tipo;
- regras de sameAs e NAP;
- duplicação entre plugin, tema e markup manual;
- validação;
- limites e proibições.

---

## Fora de âmbito

Este documento não cobre:

- local SEO e GBP — ver `LOCAL_SEO_PLAYBOOK.md`;
- SEO técnico de implementação — ver `TECHNICAL_RULES.md`;
- implementação WordPress — ver `wordpress-seo-implementation`;
- estratégia de conteúdo — ver `CONTENT_RULES.md`.

---

## Responsabilidades por componente

| Componente | Responsabilidade |
|---|---|
| `SCHEMA_ENTITY_MODEL.md` (este ficheiro) | Standard e tipos de schema |
| [`schema-entity`](../agents/schema-entity.md) | Modelação e revisão de schema |
| [`schema-entity-review`](../skills/schema-entity-review/SKILL.md) | Procedimento passo a passo |
| [`technical-seo`](../agents/technical-seo.md) | Validação técnica de schema (duplicação, Rich Results) |
| [`local-seo`](../agents/local-seo.md) | LocalBusiness e NAP no contexto local |
| [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md) | Implementação controlada em WordPress |
| [`seo-qa`](../agents/seo-qa.md) | Validação final antes de implementação ou go-live |

---

## Standards e regras

### Princípios gerais

1. **JSON-LD** é o formato preferido — Google e Schema.org recomendam.
2. **Schema representa conteúdo visível** — nunca marcar conteúdo que não está na página.
3. **Dados reais** — nunca inventar reviews, ratings, preços, moradas ou serviços.
4. **Sem duplicação** — plugin SEO, tema e markup manual não devem gerar o mesmo tipo de schema.
5. **Propriedades obrigatórias primeiro** — preferir schema correcto e simples a schema excessivo e errado.
6. **Validar sempre** — Rich Results Test quando URL acessível; Schema.org validator quando apenas código disponível.

---

### Tipos mais comuns e quando usar

#### Organization

Usar em: homepage, página institucional.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Nome da Empresa",
  "url": "https://www.empresa.pt",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.empresa.pt/logo.png"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+351-...",
    "contactType": "customer service"
  },
  "sameAs": [
    "https://www.linkedin.com/company/...",
    "https://www.facebook.com/...",
    "https://g.page/..."
  ]
}
```

**Obrigatório:** `name`, `url`.  
**Recomendado:** `logo`, `contactPoint`, `sameAs`, `address`.

---

#### LocalBusiness

Usar em: homepage ou página de localização, quando há presença local real.

Subtipos comuns: MedicalOrganization, ProfessionalService, HealthAndBeautyBusiness, etc.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Nome da Empresa",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua X, n.º Y",
    "addressLocality": "Lisboa",
    "postalCode": "1000-000",
    "addressCountry": "PT"
  },
  "telephone": "+351-...",
  "openingHoursSpecification": [...],
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "38.71...",
    "longitude": "-9.14..."
  }
}
```

**Obrigatório:** `name`, `address` (com `PostalAddress`), `telephone`.  
**Recomendado:** `openingHours`, `geo`, `sameAs`, `url`, `image`.

**Regra:** LocalBusiness apenas para localizações reais com presença física ou área de serviço real. Não inventar moradas.

---

#### WebSite

Usar em: homepage.

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Nome do Site",
  "url": "https://www.empresa.pt",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.empresa.pt/?s={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

**Obrigatório:** `name`, `url`.  
`potentialAction` apenas se houver pesquisa interna funcional.

---

#### WebPage

Usar em: qualquer página importante (base que pode ser complementada por outros tipos).

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Título da Página",
  "url": "https://www.empresa.pt/pagina/",
  "description": "Descrição curta.",
  "breadcrumb": { ... }
}
```

**Obrigatório:** `name`, `url`.  
**Recomendado:** `description`, `breadcrumb`, `inLanguage`.

---

#### BreadcrumbList

Usar em: qualquer página com breadcrumb de navegação.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Início",
      "item": "https://www.empresa.pt/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Serviços",
      "item": "https://www.empresa.pt/servicos/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Medicina do Trabalho"
    }
  ]
}
```

**Obrigatório:** `itemListElement` com `position`, `name` e `item` (URL) em cada nível excepto o último.

---

#### Service

Usar em: página de serviço específico.

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Medicina do Trabalho",
  "description": "Descrição do serviço.",
  "provider": {
    "@type": "Organization",
    "name": "Nome da Empresa",
    "url": "https://www.empresa.pt"
  },
  "areaServed": "Portugal"
}
```

**Obrigatório:** `name`, `provider`.  
**Recomendado:** `description`, `areaServed`, `serviceType`, `url`.

---

#### FAQPage

Usar em: páginas com FAQs visíveis no HTML.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Quando é obrigatória a medicina do trabalho?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A medicina do trabalho é obrigatória para..."
      }
    }
  ]
}
```

**Regra crítica:** FAQPage schema **apenas** se as perguntas e respostas estão visíveis no HTML.  
Não criar FAQPage para FAQs escondidas ou em accordions não acessíveis ao Google.

---

#### Article / BlogPosting

Usar em: artigos com data de publicação e autor identificável.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Título do artigo",
  "author": {
    "@type": "Person",
    "name": "Nome do Autor"
  },
  "datePublished": "2024-01-15",
  "dateModified": "2024-03-10",
  "publisher": {
    "@type": "Organization",
    "name": "Nome da Empresa"
  }
}
```

Usar `BlogPosting` em vez de `Article` para posts de blog menos formais.

---

### Regras de sameAs

`sameAs` deve apontar apenas para perfis oficiais verificáveis da empresa:

- LinkedIn (empresa, não pessoal — salvo `Person` schema);
- Facebook (página oficial da empresa);
- Instagram (perfil oficial);
- Twitter/X (perfil oficial);
- Google Business Profile (URL do perfil GBP);
- Wikidata (se existir);
- outras fontes de autoridade relevantes para o sector.

**Nunca:**
- perfis pessoais de colaboradores (excepto em `Person` schema);
- URLs de perfis não activos;
- inventar perfis.

Se não há certeza, não incluir e marcar como "a confirmar pela empresa".

---

### NAP — Name, Address, Phone

NAP deve ser consistente em:

- website (schema + conteúdo visível);
- Google Business Profile;
- diretórios externos;
- schema LocalBusiness.

Qualquer inconsistência de NAP entre website e GBP prejudica credibilidade local.

Para detalhe ver [`LOCAL_SEO_PLAYBOOK.md`](LOCAL_SEO_PLAYBOOK.md).

---

### Duplicação de schema

**Fontes que podem gerar schema em simultâneo:**
- Plugin SEO (Yoast, Rank Math, etc.) — gera automaticamente vários tipos.
- Tema WordPress — alguns geram Organization, WebSite ou WebPage.
- Markup manual — JSON-LD ou RDFa em templates.

**Regra:** apenas uma fonte por tipo em cada página.

**Para resolver duplicação:**
1. Identificar cada fonte via view-source ou Rich Results Test.
2. Decidir qual manter (normalmente plugin SEO é mais configurável).
3. Desactivar ou remover as outras.
4. Handoff para `wordpress-seo-implementation`.

---

## Gates

**Bloquear schema** quando:

- schema marca conteúdo que não está visível na página;
- inventa reviews, ratings, preços, moradas ou serviços;
- usa sameAs para perfis não verificados ou pessoais;
- cria FAQPage para FAQs não visíveis;
- duplica schema sem resolver conflito;
- implementação não tem ambiente seguro e rollback.

---

## Relação com agentes, skills e comandos

- [`schema-entity`](../agents/schema-entity.md) — aplica este standard.
- [`schema-entity-review`](../skills/schema-entity-review/SKILL.md) — procedimento operacional.
- [`technical-seo`](../agents/technical-seo.md) — validação técnica de schema.
- [`local-seo`](../agents/local-seo.md) — LocalBusiness e NAP.
- [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md) — implementação.
- [`seo-qa`](../agents/seo-qa.md) — validação final.
- [`TECHNICAL_RULES.md`](TECHNICAL_RULES.md) — regras técnicas.
- [`LOCAL_SEO_PLAYBOOK.md`](LOCAL_SEO_PLAYBOOK.md) — local SEO e NAP.
- [`/seo schema`](../commands/seo.md) — modo do comando SEO.

---

## Records / Persistência

Recomendar record quando:

- há decisão de schema significativa (novo modelo, mudança de tipo);
- há resolução de duplicação complexa;
- go-live com schema relevante.

Records reais vivem no projeto-alvo em `.claude/records/`.

---

## Regra final

Schema bem feito ajuda. Schema mal feito prejudica.

O Google pode ignorar schema errado — mas schema enganador pode ter consequências.

A regra é simples: apenas schema que representa o que está visível, com dados reais e sem duplicação.
