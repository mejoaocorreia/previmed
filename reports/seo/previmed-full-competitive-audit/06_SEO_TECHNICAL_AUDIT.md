# Auditoria Técnica SEO — Previmed.pt

**Data:** 2026-05-31  
**Tipo:** Read-only. Nada alterado.  
**Nota:** Sem acesso GSC, sem crawl completo, sem PageSpeed API autenticado.

---

## 1. Robots.txt

**URL:** https://previmed.pt/robots.txt

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Sitemap: https://previmed.pt/sitemaps.xml
```

**Análise:**
- ✅ Bloqueia /wp-admin/ (correto)
- ✅ Permite admin-ajax.php (necessário para WordPress AJAX)
- ✅ Sitemap declarado
- ⚠️ Sitemap aponta para `sitemaps.xml` (com "s") — confirmar que está correto e acessível
- ❌ Não bloqueia: /wp-content/uploads/ (imagens expostas ao crawl)
- Nota: Configuração padrão WordPress — adequada mas sem otimização

---

## 2. Sitemap

**URL:** https://previmed.pt/sitemaps.xml (sitemap index)

| Sitemap | URLs | Última modificação |
|---------|------|--------------------|
| page-sitemap1.xml | 50 páginas | 11/05/2026 |
| post-sitemap1.xml | 5 posts | 11/05/2026 |
| category-sitemap1.xml | categorias | 31/05/2026 |

**Análise:**
- ✅ Sitemap index funciona
- ✅ Inclui páginas e posts separados
- ⚠️ Apenas 5 posts — blog muito fraco
- ⚠️ category-sitemap: categorias indexadas podem criar thin content
- ❓ Não confirmado se sitemap está submetido no GSC
- ❓ Não confirmado se todas as 50 páginas devem ser indexadas (algumas podem ser thin content)

**URLs questionáveis no sitemap (possível thin content):**
- /formacao-2/ — slug genérico, conteúdo desconhecido
- /previmed/ — pode ser thin content (só sobre a marca)
- /instalacoes-do-cliente/ — conteúdo provavelmente breve

---

## 3. Title tags — análise completa

| Página | Title atual | Problemas | Score |
|--------|------------|-----------|-------|
| Homepage | **Não detetado** | Crítico — title ausente | ❌ |
| /saude-no-trabalho/ | "Medicina No Trabalho - Previmed" (31 chars) | Curto, falta diferenciador | ⚠️ |
| /seguranca-no-trabalho/ | "Segurança no Trabalho - Previmed - Previmed" | **Duplicação de marca** | ❌ |
| /seguranca-e-saude-no-trabalho/ | 106 chars — "Implementação e Manutenção..." | **Demasiado longo (>65 chars)** | ❌ |
| /oferta-formativa/ | "Oferta Formativa - Previmed" (39 chars) | Genérico | ⚠️ |
| /e-learning/ | **Não detetado** | Crítico — title ausente | ❌ |
| /avaliacoes-de-riscos-profissionais/ | "...Previmed - PrevimedPrevimed" | **Duplicação grave** | ❌ |
| /sobre-a-previmed/ | "Sobre a Previmed - Previmed" | Genérico | ⚠️ |
| /contactos/ | "Contactos - Previmed" | Genérico | ⚠️ |
| /pedido-de-proposta/ | "Pedido de proposta - Previmed" | Genérico | ⚠️ |
| /check-ups/ | **Não detetado** | Crítico — title ausente | ❌ |
| /sistemas-integrados-de-certificacao/ | "Sistemas Integrados de Certificação - Previmed" | OK comprimento, sem diferenciador | ⚠️ |

**Padrão de problema:** Vários títulos com duplicação de "Previmed" — indica erro na configuração do plugin SEO (provavelmente Yoast ou Rank Math com template mal configurado)

---

## 4. Meta descriptions — análise completa

| Página | Estado |
|--------|--------|
| Homepage | ❌ **AUSENTE** |
| /saude-no-trabalho/ | ❌ **AUSENTE** |
| /seguranca-no-trabalho/ | ❌ **AUSENTE** |
| /seguranca-e-saude-no-trabalho/ | ❌ **AUSENTE** |
| /oferta-formativa/ | ❌ **AUSENTE** |
| /e-learning/ | ❌ **AUSENTE** |
| /avaliacoes-de-riscos-profissionais/ | ❌ **AUSENTE** |
| /sobre-a-previmed/ | ❌ **AUSENTE** |
| /contactos/ | ❌ **AUSENTE** |
| /pedido-de-proposta/ | ❌ **AUSENTE** |
| /check-ups/ | ❌ **AUSENTE** |

**Conclusão:** Meta description ausente em TODAS as páginas analisadas.  
Isto é uma falha sistémica — provavelmente o plugin SEO não está configurado para gerar meta descriptions automáticas, e nenhuma foi definida manualmente.  
**Impacto:** Google gera snippets automáticos (muitas vezes pouco atrativos) → CTR baixo.

---

## 5. H1 e estrutura de headings

| Página | H1 | Problema |
|--------|-----|---------|
| Homepage | Não explícito | ❌ Crítico |
| /saude-no-trabalho/ | "Medicina No Trabalho" | ✅ OK |
| /seguranca-no-trabalho/ | "Segurança no Trabalho" | ✅ OK |
| /seguranca-e-saude-no-trabalho/ | "Implementação e Manutenção do Sistema de Gestão SST" | ⚠️ Demasiado técnico |
| /oferta-formativa/ | "Oferta Formativa" | ⚠️ Genérico |
| /e-learning/ | "E-Learning" | ⚠️ Genérico |
| /avaliacoes-de-riscos-profissionais/ | "Avaliação de Riscos Profissionais" | ✅ OK |

**Typos encontrados em H2/H3 (sem acento em "Segurança"):**
- "Seguranca No Trabalho" — em /seguranca-no-trabalho/, /avaliacoes-de-riscos-profissionais/, /informacao-formacao/, /auditorias-e-inspeccoes/
- "Consultoria Formacao" — em /oferta-formativa/, /e-learning/
- "Servico Certificado" — em /seguranca-e-saude-no-trabalho/, /sistemas-integrados-de-certificacao/

**Causa provável:** Widget ou bloco WordPress com texto hardcoded sem acentuação correta.

---

## 6. Schema/dados estruturados

**Estado: AUSENTE em todas as páginas analisadas.**

Nenhuma página tem schema JSON-LD visível.

**Tipos recomendados por página:**

| Página | Schema recomendado |
|--------|-------------------|
| Homepage | Organization + WebSite + BreadcrumbList |
| /sobre-a-previmed/ | Organization + LocalBusiness |
| /contactos/ | LocalBusiness (2 localizações: Lisboa + Porto) |
| /saude-no-trabalho/ | Service + FAQPage |
| /seguranca-no-trabalho/ | Service + FAQPage |
| /oferta-formativa/ | ItemList (cursos) |
| /e-learning/ | Course (quando cursos forem listados) |
| Todas | BreadcrumbList |

---

## 7. Indexação aparente

**Nota:** Sem GSC não é possível confirmar o estado real de indexação.

**Observações baseadas em análise pública:**
- Sitemap existe e está funcional
- robots.txt não bloqueia conteúdo público
- URLs têm estrutura limpa (slugs descritivos em português)
- Nenhum noindex detectado nas páginas analisadas
- Confirmado via sitemap que 55+ páginas estão mapeadas

**Riscos identificados:**
- Categoria-sitemap pode indexar páginas de arquivo thin content
- Slugs de blog com datas: /2026/05/11/coronavirus/ — formato não ideal para SEO
- /formacao-2/ — slug genérico, pode indicar página duplicada

---

## 8. Performance — estimativa (sem PageSpeed real)

**Nota:** Análise baseada em observações estruturais. Sem PageSpeed/CrUX.

**Indicadores de risco de performance:**
- Slider com 7 imagens na homepage → risco de LCP alto se imagens não forem otimizadas
- Imagem principal na /saude-no-trabalho/ descrita como "1024x710px" sem menção de compressão
- Site WordPress com theme + plugins → risco de JS/CSS excessivo
- E-learning e portais em domínios externos → não afetam performance do site principal

**A confirmar com PageSpeed Insights (gratuito):**
- https://pagespeed.web.dev/report?url=https://previmed.pt/
- LCP, INP, CLS para mobile e desktop

---

## 9. Canonical

**Estado:** Não analisado diretamente (WebFetch não devolve headers HTTP).

**Riscos identificados:**
- /saude-no-trabalho/ vs /medicina-no-trabalho/ — se houver alias, canonical pode estar errado
- /formacao-2/ vs /oferta-formativa/ — risco de duplicação de conteúdo
- Categorias WordPress indexadas podem criar duplicação com páginas de arquivo

**Recomendação:** Verificar canonical com ferramenta (Rich Results Test ou URL Inspection no GSC).

---

## 10. Open Graph

**Analisado:** Não encontrado em nenhuma página.

**Impacto:** Partilha nas redes sociais usa título genérico e imagem automática → má apresentação no LinkedIn, Facebook, WhatsApp.

---

## 11. WordPress — observações técnicas visíveis

**CMS:** WordPress (confirmado via robots.txt e estrutura de URLs)  
**Plugin SEO:** Provavelmente Yoast ou Rank Math (não confirmado — configuração deficiente)

**Problemas WordPress visíveis:**
- Title tags com duplicação "Previmed - PrevimedPrevimed" → template de title mal configurado no plugin SEO
- Slugs de posts com formato /ano/mes/dia/slug → formato antigo, não ideal para SEO
- Imagens WordPress: /wp-content/uploads/ — não bloqueado em robots (crawl de imagens exposto)
- Categorias no sitemap: risco de thin content indexado

---

## 12. Checklist técnica — estado atual

| Item | Estado | Prioridade |
|------|--------|-----------|
| Title tags presentes | ❌ Problemas em 5+ páginas | Crítica |
| Meta descriptions | ❌ Ausentes em TODAS | Crítica |
| H1 presente em todas as páginas | ⚠️ Ausente na homepage | Alta |
| Schema JSON-LD | ❌ Ausente | Alta |
| Sitemap funcional | ✅ OK | — |
| robots.txt funcional | ✅ OK | — |
| HTTPS | ✅ Confirmado | — |
| Slugs descritivos | ✅ OK (pages) | — |
| Slugs de posts | ⚠️ Formato /ano/mes/dia/ | Média |
| Typos em headings | ❌ Múltiplos | Alta |
| Open Graph | ❌ Ausente | Média |
| Mobile | ❓ A confirmar | Alta |
| Core Web Vitals | ❓ A confirmar | Alta |
| Canonical | ❓ A confirmar | Alta |
| Páginas thin content | ⚠️ Suspeitas (/formacao-2/) | Média |
