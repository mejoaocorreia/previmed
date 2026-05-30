# SEO Go-Live Checklist — [Página/Site] — YYYY-MM-DD

> **Template.** Copiar para o sítio de records do projeto e preencher. Operado pelo `seo-qa` + `technical-seo` + `wordpress-seo-implementation`.

## Pré-requisitos
- [ ] Preview/staging validado
- [ ] Rollback definido e testado
- [ ] Autorização explícita para go-live
- [ ] Ambiente confirmado (não assumir produção sem evidência)

## Crawl / Index
- [ ] Páginas importantes em status 200
- [ ] robots.txt não bloqueia o que deve indexar
- [ ] Sem noindex indevido
- [ ] Canonical correto
- [ ] Sitemap inclui as páginas certas e foi submetido
- [ ] Redirects 301 mapeados (sem cadeias/loops)
- [ ] Internal links rastreáveis; sem novas orphan pages

## On-page
- [ ] Titles únicos e dentro do limite
- [ ] Meta descriptions presentes
- [ ] H1 único + hierarquia correta
- [ ] Conteúdo visível/indexável (não escondido por JS)

## Schema
- [ ] Schema representa conteúdo visível
- [ ] Sem duplicação por plugin/tema
- [ ] Validado (Rich Results / Schema.org)

## Performance / Mobile / A11y
- [ ] LCP ≤ 2.5s / INP < 200ms / CLS estável (mobile)
- [ ] Mobile renderiza corretamente
- [ ] Acessibilidade básica ok

## URL changes (se aplicável)
- [ ] Motivo confirmado · tráfego/indexação verificados
- [ ] 301 + internal links + sitemap + canonical testados
- [ ] Validação no Search Console planeada

## Pós-go-live
- [ ] Verificar indexação/cobertura (URL Inspection)
- [ ] Monitorizar GSC/GA4 (período comparável)
- [ ] Registar record + atualizar estado

## Veredito

Estado: [Aprovado / Aprovado com notas / Bloqueado / Precisa de dados / Precisa de autorização]

Riscos residuais:

Próximo passo:
