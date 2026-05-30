# SEO Go-Live Checklist — [Pagina/Site] — YYYY-MM-DD

> **Template.** Copiar para o sitio de records do projeto consumidor e preencher. Operado por `seo-qa` + `technical-seo` + `wordpress-seo-implementation`.

## Contexto

- Modo: [`/seo go-live`](../commands/seo.md)
- Ambiente: [local / staging / preview / producao]
- Paginas/URLs afetadas:
- Owner:
- Data prevista:

## Pre-Requisitos

- [ ] Preview/staging validado
- [ ] Rollback definido e testado
- [ ] Autorizacao explicita para go-live
- [ ] Ambiente confirmado (nao assumir producao sem evidencia)
- [ ] Sem credenciais/tokens/dados sensiveis no record

## Crawl / Index

- [ ] Paginas importantes em status 200
- [ ] robots.txt nao bloqueia o que deve indexar
- [ ] Sem noindex indevido
- [ ] Canonical correto
- [ ] Sitemap inclui as paginas certas
- [ ] Sitemap submetido/validado quando aplicavel
- [ ] Redirects 301 mapeados
- [ ] Sem cadeias/loops de redirects
- [ ] Internal links rastreaveis
- [ ] Sem novas orphan pages

## On-page

- [ ] Titles unicos e adequados
- [ ] Meta descriptions presentes
- [ ] H1 unico + hierarquia correta
- [ ] Conteudo visivel/indexavel
- [ ] CTAs e formularios testados
- [ ] Claims sensiveis revistos por humano quando aplicavel

## Schema

- [ ] Schema representa conteudo visivel
- [ ] Sem duplicacao por plugin/tema
- [ ] Validado (Rich Results / Schema.org)
- [ ] sameAs/NAP conferidos quando aplicavel

## Performance / Mobile / A11y

- [ ] LCP, INP e CLS revistos em mobile
- [ ] Lab vs field data distinguidos
- [ ] Mobile renderiza corretamente
- [ ] Acessibilidade basica ok
- [ ] Mudancas de performance nao degradam UX/design

## URL Changes (Se Aplicavel)

- [ ] Motivo confirmado
- [ ] Trafego/indexacao/backlinks internos verificados
- [ ] 301 testado
- [ ] Internal links atualizados
- [ ] Sitemap atualizado
- [ ] Canonical testado
- [ ] Validacao no Search Console planeada

## Dados / Tracking

- [ ] GA4 validado quando aplicavel
- [ ] GSC/URL Inspection planeado quando aplicavel
- [ ] Eventos/conversoes essenciais testados
- [ ] Limites de dados registados

## Pos-Go-Live

- [ ] Verificar indexacao/cobertura (URL Inspection)
- [ ] Monitorizar GSC/GA4 em periodo comparavel
- [ ] Monitorizar erros 404/redirects
- [ ] Registar record final
- [ ] Atualizar status/backlog/decisions

## Handoff

- WordPress Engineering:
- Visual Experience:
- System Safety:
- SEO QA:

## Veredito

Estado: [Aprovado / Aprovado com notas / Bloqueado / Precisa de dados / Precisa de autorizacao]

- Validacao feita:
- Nao validado / a confirmar:
- Bloqueios:
- Risco residual:
- Autorizacao necessaria:
- Proximo passo:
