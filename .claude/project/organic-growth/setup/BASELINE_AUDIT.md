# Auditoria Técnica Baseline — previmed.pt

> **Lote 2.1 da Fase 2.** Captura do estado técnico do site atual antes de qualquer alteração ou reinstalação.
> Data: 2026-05-20.
> Método: HEAD/GET via PowerShell + regex (HTML cru, sem execução JS). PSI via API pública (rate-limited).
> Amostra: 11 páginas-chave (homepage + 5 hubs de serviço + sobre + contactos + 2 formação + proposta) + checks de redirect e infraestrutura.

---

## 1. Sumário executivo

**Sinal forte:**
- HTTPS forçado, canonical consistente, redirects 301 para versão preferida (non-www, com trailing slash).
- Schema JSON-LD presente em todas as páginas (Organization + WebSite + WebPage + BreadcrumbList + SearchAction).
- Sitemap index estruturado em 3 ficheiros (pages 50 URLs, posts 5 URLs, categories 1 URL).
- WordPress 6.9.4 (versão atual em 2026-05).
- Cloudflare como CDN/edge.
- `lang="pt-PT"`, viewport meta correcto, robots `index, follow`.

**Bloqueadores SEO críticos:**

| # | Problema | Severidade | Impacto |
|---|---|---|---|
| 1 | `<title>` corrompido com "Previmed - PrevimedPrevimed" em **todas** as páginas | 🔴 Crítico | CTR SERP, perceção de qualidade, ranking |
| 2 | Homepage `<title>` = literalmente "Previmed" (8 chars) | 🔴 Crítico | Nenhuma keyword na homepage |
| 3 | Homepage `<h1>` = "Notícias Previmed" | 🔴 Crítico | H1 deveria refletir o que a empresa faz, não o feed |
| 4 | Meta descriptions geradas auto a partir do primeiro parágrafo, com `[…]` truncado e 274–485 chars (limite 150–160) | 🟡 Alto | CTR; Google trunca/re-escreve |
| 5 | 17/36 imagens da homepage **sem `alt`** (47%) | 🟡 Alto | A11y + image SEO |
| 6 | **Zero conteúdo informacional** (5 posts datados de 2026-05-11, todos thin: coronavirus, gripe, dia da prevenção, rastreios) | 🔴 Crítico | Sem hub editorial, confirma tese estratégica |
| 7 | Sem `Service`, `MedicalBusiness`, `MedicalOrganization` ou `LocalBusiness` schema nas service pages | 🟡 Alto | Perde elegibilidade a rich results e classificação semântica |
| 8 | `Cache-Control: max-age=0` no HTML (sem cache de browser, depende de Cloudflare edge) | 🟢 Médio | Performance |
| 9 | `X-Powered-By: PHP/8.4.20` exposto | 🟢 Baixo | Info disclosure menor |
| 10 | `http://www.previmed.pt/` → 2-hop redirect (http→https→non-www) | 🟢 Baixo | Pequena perda de crawl budget |
| 11 | Meta description de `/pedido-de-proposta/` com HTML entities não decodificadas (`&iacute;`, `&atilde;`) | 🟡 Médio | SERP mostra texto partido |

**Diagnóstico de fundo:**
O site técnico-base é decente (HTTPS, schema base, sitemap, canonical, Cloudflare, WP recente). O que o mata em orgânico não é infraestrutura — é **conteúdo + metadata**: titles partidos, sem hub editorial, sem schema rico por entidade de serviço, descriptions geradas por defeito. Confirma a tese estratégica do Lote 1.5: a alavanca é editorial/semântica, não infra.

---

## 2. Infraestrutura

| Item | Valor |
|---|---|
| Server | Cloudflare (edge) |
| Backend | PHP/8.4.20 (`X-Powered-By` exposto) |
| WordPress | 6.9.4 (generator meta exposto) |
| Lang | `pt-PT` |
| Viewport | `width=device-width, initial-scale=1` ✓ |
| Hreflang | nenhum (OK enquanto só PT) |
| Robots.txt | `User-agent: *`, `Disallow: /wp-admin/`, `Allow: /wp-admin/admin-ajax.php`, `Sitemap: https://previmed.pt/sitemaps.xml` ✓ |
| WP REST API | não exposta no HTML (não confirma se está aberta em `/wp-json/`) |
| Plugins detetados (homepage) | `cookieadmin`, `cookieadmin-pro`, `contact-form-7` |
| Plugin SEO detetado | **nenhum dos conhecidos** (Yoast/RankMath/AIOSEO/SEOPress/Squirrly). Schema e meta provavelmente gerados pelo tema ou por código custom. **Investigar.** |
| Page builder detetado | nenhum (sem Elementor/Divi/WPBakery) |
| JS scripts (homepage) | 7 `<script src>` |
| CSS links (homepage) | 3 `<link rel=stylesheet>` |
| HTML size (homepage) | ~124KB |

---

## 3. Redirects e canonical

| Origem | Status | Destino |
|---|---|---|
| `http://previmed.pt/` | 301 | `https://previmed.pt/` ✓ |
| `https://www.previmed.pt/` | 301 | `https://previmed.pt/` ✓ |
| `http://www.previmed.pt/` | 301 | `https://www.previmed.pt/` ⚠️ (depois 2.º hop) |
| `https://previmed.pt/saude-no-trabalho` | 301 | `https://previmed.pt/saude-no-trabalho/` ✓ |
| `https://previmed.pt/nao-existe-12345` | 404 ✓ | — |
| `https://previmed.pt/wp-admin/` | 302 | `https://previmed.pt/acesso-negado/` (provável plugin segurança) |

**Recomendação:** ajustar regra HTTPS para fazer `http://www.*` → `https://previmed.pt/*` em **uma só hop**.

---

## 4. Inventário de URLs

| Sitemap | URLs | Última atualização |
|---|---|---|
| `page-sitemap1.xml` | **50** páginas (serviços + institucional) | 2026-05-11 |
| `post-sitemap1.xml` | **5** posts (coronavirus, gripe, dia da prevenção, rastreios) | 2026-05-11 |
| `category-sitemap1.xml` | **1** categoria (`/category/previmed/`) | 2026-05-20 |

**Total: 56 URLs indexáveis.** Para um site B2B nacional com 5 áreas de serviço e 30+ anos de empresa, esta cobertura é **estruturalmente sub-crítica** — confirma o argumento "hub editorial é a alavanca principal" do `STRATEGY.md`.

---

## 5. Amostra de páginas (11 URLs)

| URL | Title | Title Len | Meta Desc Len | H1 | JSON-LD @types |
|---|---|---|---|---|---|
| `/` | `Previmed` | 8 | 174 | `Notícias Previmed` 🔴 | Organization, WebSite, WebPage, BreadcrumbList, SearchAction |
| `/saude-no-trabalho/` | `Medicina No Trabalho - Previmed  -  PrevimedPrevimed` | 52 | 350 | `Medicina No Trabalho` | mesma stack |
| `/seguranca-no-trabalho/` | `Segurança no Trabalho - Previmed  -  PrevimedPrevimed` | 53 | 465 | `Segurança no Trabalho` | mesma stack |
| `/seguranca-higiene-alimentar/` | `Serviços de Segurança e Higiene Alimentar - Previmed  -  PrevimedPrevimed` | 73 | 427 | `Serviços de Segurança e Higiene Alimentar` | mesma stack |
| `/seguranca-ambiental/` | `Segurança Ambiental - Previmed  -  PrevimedPrevimed` | 51 | 450 | `Segurança Ambiental` | mesma stack |
| `/consultoria-formacao/` | `Formação profissional - Previmed  -  PrevimedPrevimed` | 53 | 356 | `Formação profissional` | mesma stack |
| `/sobre-a-previmed/` | `Sobre a Previmed - Previmed  -  PrevimedPrevimed` | 48 | 377 | `Sobre a Previmed` | mesma stack |
| `/contactos/` | `Contactos - Previmed  -  PrevimedPrevimed` | 41 | 485 | `Contactos` | mesma stack |
| `/oferta-formativa/` | `Oferta Formativa - Previmed  -  PrevimedPrevimed` | 48 | 274 | `Oferta Formativa` | mesma stack |
| `/e-learning/` | `E-Learning - Previmed  -  PrevimedPrevimed` | 42 | 432 | `E-Learning` | mesma stack |
| `/pedido-de-proposta/` | `Pedido de proposta - Previmed  -  PrevimedPrevimed` | 50 | 159 (com HTML entities partidas) | `Pedido de proposta` | mesma stack |

**Padrão consistente em 10/11 páginas:** sufixo " - Previmed  -  PrevimedPrevimed" no `<title>` — bug claro de tema ou filtro de plugin SEO custom que está a concatenar a brand 3x.

**Homepage é o outlier:** apenas "Previmed" como title (provavelmente porque a regra de concatenação só atua quando há title custom da página).

---

## 6. Schema atual (homepage)

JSON-LD presente:

```
Organization
  + ImageObject (logo?)
  + WebSite
    + WebPage
      + BreadcrumbList
        + ListItem × 3
        + SearchAction
```

**Ausências críticas:**
- `LocalBusiness` ou `MedicalOrganization` (Previmed é centro de medicina ocupacional — devia declarar-se como tal).
- `Service` schema nas service pages (`/saude-no-trabalho/`, `/seguranca-no-trabalho/`, etc).
- `Person` ou `MedicalProfessional` para a equipa clínica.
- `Course` ou `EducationalOccupationalProgram` nas páginas `/oferta-formativa/`, `/e-learning/`, `/formacao-*`.
- `FAQPage` em qualquer lado.
- `Review` / `AggregateRating` (sem testemunhos estruturados).
- `PostalAddress` rica em `/contactos/` com `geo`, `openingHoursSpecification`.

---

## 7. Performance e Core Web Vitals

**Status:** PSI API devolveu 429 (rate limit sem API key). Reagendar após:
- registar API key Google em `.env` (`GOOGLE_PSI_API_KEY=…`), OU
- correr manualmente `https://pagespeed.web.dev/analysis?url=https://previmed.pt/` no browser.

**Pendente — alvo de medição:**
- LCP mobile (alvo < 2.5s) e desktop.
- INP mobile (alvo < 200ms).
- CLS (alvo < 0.1).
- Comparar lab vs CrUX field (28d).

Sinal indireto observado: HTML 124KB sem optimizações agressivas, 7 scripts + 3 stylesheets, Cloudflare a fazer edge cache → presumivelmente "OK mas não rápido". Confirmar empírico antes de tirar conclusões.

---

## 8. Backlog técnico priorizado

### P0 — fix imediato (pré-redesign WP)

1. **Reparar `<title>` duplicado.** Origem provável: filtro no `functions.php` do tema ou plugin custom de SEO que concatena `get_bloginfo('name')` múltiplas vezes. Auditar.
2. **Definir `<title>` e meta description próprios da homepage** (não autogerados). Title alvo ~55–60 chars com keyword + brand.
3. **Substituir H1 da homepage** de "Notícias Previmed" para algo que descreva a empresa.
4. **Reescrever meta descriptions** de todas as 50 pages para 150–160 chars, com proposta de valor + CTA.
5. **Decodificar HTML entities** na meta description de `/pedido-de-proposta/`.
6. **Adicionar `alt` text** às 17 imagens sem alt na homepage (extrapolar para todo o site num crawl completo).

### P1 — antes de Fase 3 (briefs P1)

7. **Adicionar `MedicalOrganization` + `LocalBusiness`** ao schema da homepage e `/contactos/`.
8. **Adicionar `Service` schema** a cada service hub (5 áreas + subserviços).
9. **Adicionar `Course` / `EducationalOccupationalProgram`** a `/oferta-formativa/` e às páginas de curso.
10. **Investigar e documentar** que plugin/código gera schema e meta tags actualmente — input crítico para a decisão de plugin SEO da Fase 4.

### P2 — durante redesign WP (Fase 4)

11. Ajustar regra de redirect HTTPS para `http://www.*` → `https://previmed.pt/*` em 1 hop.
12. Remover `X-Powered-By` header e `generator` meta (security hygiene).
13. Definir `Cache-Control` no HTML (ex.: `max-age=300, s-maxage=3600`) para reduzir TTFB repetido em Cloudflare miss.
14. Confirmar `/wp-json/` está disabled para utilizadores anónimos.

### P3 — depois da migração

15. Auditoria de orphan pages (cruzar sitemap × internal links extraídos por crawl).
16. Verificar pagination e arquivos `category/` / `tag/` / `author/`.
17. Implementar PSI com API key para medição contínua.

---

## 9. Limitações desta auditoria

- **Sem render JS.** HTML extraído via HEAD/GET cru. Se houver conteúdo crítico injetado por JS (improvável neste site), não foi capturado.
- **Amostra de 11/56 páginas.** As 45 não amostradas podem ter padrões diferentes — alargar quando possível.
- **PSI rate-limited.** Métricas de Core Web Vitals pendentes.
- **Sem acesso GSC.** Não conhecemos queries reais, CTR real, pages com impressões nem erros de cobertura. Resolve-se em 2.4.
- **Sem crawl interno completo.** Não há mapa de internal links — orphan pages, redirect chains internas, anchor text distribution ficam por mapear.
- **Não testado se schema valida no Rich Results Test.** Marcar para validar em fase posterior.

---

## 10. Próximos passos imediatos

- Concluir 2.2 (auditoria AIO).
- 2.3: produzir doc de decisão tool keyword data.
- 2.4: setup GSC + GA4 (ação do utilizador).
- Re-correr PSI quando tiver API key.
- Investigar origem dos titles duplicados (auditoria do `functions.php` do tema ou do plugin SEO custom) — bloqueia decisão de "manter tema atual" vs "tema novo" em Fase 4.
