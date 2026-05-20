# Schema & Entity Model

## Objetivo

Ajudar motores de busca a entender:
- quem é a marca;
- que serviços oferece;
- onde atua;
- que páginas representam que entidades;
- como o site está estruturado.

## Tipos comuns

- Organization
- LocalBusiness, se aplicável
- WebSite
- WebPage
- Service
- BreadcrumbList
- FAQPage, quando conteúdo visível existir
- Article/BlogPosting, se houver artigos
- ContactPoint
- ImageObject, quando relevante

## Regras

- JSON-LD preferido.
- Schema deve representar conteúdo visível.
- Não inventar reviews, ratings, preços ou dados.
- Evitar duplicação com plugin SEO.
- Usar sameAs apenas para perfis oficiais.
- Validar tecnicamente e semanticamente.
