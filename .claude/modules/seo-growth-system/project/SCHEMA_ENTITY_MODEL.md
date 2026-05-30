# Schema & Entity Model

## Objetivo
Ajudar motores de busca e IA a entender quem é a marca, que serviços oferece, onde atua, que páginas representam que entidades e como o site está estruturado.

## Quando usar
Modelar/rever dados estruturados e entidades de um site.

## Regras principais
- JSON-LD preferido.
- Schema deve representar conteúdo **visível**.
- Não inventar reviews, ratings, preços ou dados.
- Evitar duplicação com plugin SEO/tema.
- `sameAs` apenas para perfis oficiais.
- Validar técnica e semanticamente.

## Processo
1. Identificar entidades principais (organização, serviços, localizações, autores). 2. Mapear página↔entidade↔tipo. 3. Escolher tipos. 4. Preencher propriedades obrigatórias a partir de conteúdo visível e dados reais. 5. Verificar duplicação com plugin/tema. 6. Validar (Rich Results / Schema.org).

## Tipos comuns
Organization · LocalBusiness (se aplicável) · WebSite · WebPage · Service · BreadcrumbList · FAQPage (com FAQ visível) · Article/BlogPosting (se houver artigos) · ContactPoint · ImageObject (quando relevante) · Person (autor) quando aplicável.

## Inputs
Conteúdo visível, dados reais da entidade (nome, morada, contactos, perfis oficiais), schema atual.

## Outputs
Tipos recomendados · propriedades · fonte dos dados · páginas aplicáveis · riscos · validação.

## Agentes relacionados
[`schema-entity`](../agents/schema-entity.md), [`technical-seo`](../agents/technical-seo.md), [`local-seo`](../agents/local-seo.md), [`wordpress-seo-implementation`](../agents/wordpress-seo-implementation.md).

## Skills relacionadas
[`schema-entity-review`](../skills/schema-entity-review/SKILL.md).

## Ferramentas/MCPs possíveis
Rich Results Test, Schema.org validator, Browser. Read-only.

## Critérios de qualidade
Schema = conteúdo visível; propriedades obrigatórias presentes; sem duplicação; sameAs só oficiais; validado.

