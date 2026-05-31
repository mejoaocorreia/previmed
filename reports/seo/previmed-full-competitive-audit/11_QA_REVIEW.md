# Quality Gate — Auditoria Previmed

**Data:** 2026-05-31  
**Aplicado por:** SEO Growth System / seo-qa  
**Procedimento:** QUALITY_GATE.md do SEO Growth System

---

## Veredito

### Relatório de auditoria: **APROVADO COM NOTAS**

### Recomendações do relatório: **PRECISA DE DADOS** (para priorização final por tráfego/posições)

### Execução em produção: **PRECISA DE AUTORIZAÇÃO** (para qualquer alteração)

---

## O que foi validado

| Item | Estado |
|------|--------|
| Homepage analisada | ✅ |
| Robots.txt analisado | ✅ |
| Sitemap analisado (index + 2 sitemaps) | ✅ |
| 20 páginas Previmed analisadas individualmente | ✅ |
| 50 páginas mapeadas via sitemap | ✅ |
| 11 concorrentes identificados | ✅ |
| 7 concorrentes analisados profundamente | ✅ |
| AEST: 47 empresas do setor identificadas | ✅ |
| Schema: ausência confirmada | ✅ |
| Meta descriptions: ausência confirmada em todas | ✅ |
| Typos em headings: identificados e localizados | ✅ |
| Title duplicados: identificados | ✅ |
| Prova social: ausência confirmada | ✅ |
| E-learning vazio: confirmado | ✅ |
| NAP (Lisboa + Porto): confirmado | ✅ |
| Certificações (ACT/DGS/DGERT/ISO): confirmadas | ✅ |
| Fundação 1995: confirmada | ✅ |
| Problemas de conversão: identificados | ✅ |
| Gap de conteúdo vs concorrência: documentado | ✅ |
| Plano de ação 30/60/90 dias: criado | ✅ |

---

## O que NÃO foi validado

| Item | Motivo | Como validar |
|------|--------|-------------|
| Rankings reais em SERP | Sem GSC, sem ferramenta de ranking | GSC → Desempenho → Queries |
| Tráfego orgânico | Sem GA4 | GA4 → Aquisição → Orgânico |
| CTR real das páginas | Sem GSC | GSC → Desempenho por página |
| Core Web Vitals (LCP/INP/CLS) | Sem PageSpeed API | PageSpeed Insights gratuito |
| Mobile rendering | Sem Playwright | Google Mobile-Friendly Test |
| Canonical correto em cada página | Sem acesso headers | URL Inspection no GSC |
| Canonical de /saude-no-trabalho/ vs /medicina-no-trabalho/ | — | Verificar no browser |
| Status codes de todas as páginas | WebFetch não expõe todos | Screaming Frog ou GSC |
| Links quebrados internos | Sem crawl completo | Screaming Frog ou GA4 |
| Orphan pages | Sem crawl completo | Screaming Frog |
| Configuração exata do plugin SEO | Sem acesso WordPress admin | Dashboard WordPress |
| Schema implementado (se existir em pages não analisadas) | Analisadas apenas 20/50 | Validar com Rich Results Test |
| Perfil de backlinks | Sem Ahrefs/Semrush | Ferramentas pagas |
| Google Business Profile | Sem acesso GBP | Google Maps + GBP dashboard |
| Claims de formação financiada | Sem confirmação interna | Equipa Previmed |
| Número exato de clientes/empresas | Sem dados internos | Dados internos Previmed |
| Dados reais de cursos e-learning | Plataforma externa | Acesso previmed-academia.careview.pt |

---

## Evidência usada

- WebFetch: 20 URLs Previmed + 11 URLs concorrentes
- WebSearch: 5 pesquisas de descoberta de concorrentes
- Sitemap XML: mapeamento de 50+ páginas
- robots.txt: análise de configuração
- AEST: lista pública de 47 associados

---

## Risco residual

| Risco | Nível | Descrição |
|-------|-------|-----------|
| Dados de tráfego ausentes | Médio | Priorização baseada em hipóteses de volume, não dados reais |
| Core Web Vitals desconhecidos | Médio | Slider de 7 imagens na homepage pode ter LCP alto |
| Canonical desconhecido | Médio | Possível duplicação não confirmada |
| Performance mobile não testada | Médio | WordPress com plugins pode ter problemas |
| Conteúdo de 30 páginas não analisadas | Baixo | 20 de 50 páginas foram analisadas — as mais importantes |
| Configuração plugin SEO não confirmada | Baixo | Typos sugerem configuração deficiente |

---

## Dados ainda necessários (para completar a auditoria)

Para elevar o veredito de "Aprovado com notas" para "Aprovado":

1. **GSC read-only:** queries, posições, CTR, cobertura, erros
2. **GA4 read-only:** tráfego orgânico, conversões, bounce rate
3. **PageSpeed URL:** Core Web Vitals de homepage e páginas core
4. **Lista real de cursos e-learning:** para completar análise de /e-learning/
5. **Número real de clientes:** para recomendar com dados reais
6. **Confirmar slug correto de medicina do trabalho:** /saude-no-trabalho/ ou /medicina-no-trabalho/?

---

## Gates de segurança — o que precisa de autorização antes de avançar

| Ação | Autorização necessária | Por quem |
|------|----------------------|---------|
| Alterar meta descriptions/titles | ✅ WordPress admin | Marketing + Técnico |
| Alterar qualquer URL/slug | ✅ Supervisor + plano redirect | Direção + SEO |
| Adicionar/alterar schema JSON-LD | ✅ Plugin SEO ou código | Técnico WordPress |
| Publicar novos conteúdos | ✅ Revisão humana de claims | Editor + Área responsável |
| Alterar formulários | ✅ RGPD verificado | Compliance |
| Alterar homepage | ✅ Design + Marketing + Direção | — |
| Otimizar Google Business Profile | ✅ Acesso GBP | Marketing |
| Criar páginas novas | ✅ Serviço confirmado + URL aprovada | Marketing + SEO |

---

## Notas obrigatórias ao usar este relatório

1. **Não executar nenhuma ação em produção sem autorização**
2. **Não inventar dados:** todos os claims do relatório baseiam-se em evidência pública observada
3. **Não criar páginas locais** sem confirmar presença/cobertura real (Lisboa, Porto, etc.)
4. **Não criar schema** para conteúdo que não existe na página
5. **Não alterar URLs** sem plano de redirect documentado, aprovado e testado
6. **Validar claims legais/médicos** com profissional responsável antes de publicar
7. **Medir antes e depois** — obter acesso GSC/GA4 antes de iniciar mudanças para poder medir impacto

---

## Próximo passo recomendado

1. Reunião de alinhamento: apresentar este relatório à equipa/direção
2. Obter acesso read-only ao GSC e GA4
3. Confirmar lista de cursos e-learning reais
4. Aprovar arquitetura de URLs (ficheiro 07)
5. Iniciar Fase 1 (quick wins) com autorização
