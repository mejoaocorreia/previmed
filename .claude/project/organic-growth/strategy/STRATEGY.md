# Strategy — Síntese mestre (Fase 1)

> **Documento "north star" do Organic Growth da Previmed.**
> Última atualização: 2026-05-20.
> Fecha o Lote 1.5 e consolida Lotes 1.1–1.4.
> Base: `strategy/AUDIENCES.md`, `strategy/INFORMATION_ARCHITECTURE.md`, `strategy/KEYWORDS.md`, `strategy/COMPETITORS.md`.

---

## 1. Executive summary

A Previmed é uma empresa de SST/HSST B2B nacional, fundada em 1995 (razão social: *Previmed - Centro de Medicina Ocupacional Lda*). Cobre 5 áreas — Medicina do Trabalho, Segurança no Trabalho, Higiene e Segurança Alimentar, Ambiente, Formação Profissional. O site atual `previmed.pt` é WordPress, sub-otimizado, sem hub editorial e sem páginas dedicadas a audiências distintas. **Esta estratégia é greenfield: define a arquitetura SEO antes da reinstalação WP**.

**Tese central:** o mercado HSST português é **estruturalmente fragmentado em orgânico** (nenhum player ocupa mais do que 1-2 posições por SERP) mas tem um líder claro em SEO+SEM combinados — **Centralmed**. Previmed entra no top 10 apenas em 2 de 9 queries comerciais não-brand e está ausente de todos os clusters informacionais. A oportunidade não é "ranquear melhor" — é **construir o hub editorial que ninguém construiu**, captar long-tail informacional onde institucionais dominam mas convertem mal, e abrir um diferenciador comercial (transparência de preço) que nenhum concorrente assume.

**Cinco decisões estratégicas:**

1. **Hub editorial é a alavanca principal.** Pillars legais + comparativos + verticais por setor são onde existe assimetria (concorrentes não os têm; institucionais têm conteúdo bruto sem CTA).
2. **Três audiências, três tratamentos distintos.** Cliente Empresa = 65% esforço; Formando = 25%; Trabalhador = 10% (retenção/UX, não aquisição).
3. **Formação como sub-hub no mesmo domínio** (não subdomínio), portal trabalhador em `portal.previmed.pt` (sub).
4. **Sem páginas regionais doorway-style.** Uma página `/cobertura/` com mapa interativo, revisitar pós-GSC.
5. **AI Overview é o jogo novo.** AIO ativo em 12/12 queries em 2026-05 — conteúdo precisa de ser estruturalmente citável (definições, listas, schema, factos com fonte).

---

## 2. Audiências (síntese; detalhe em `strategy/AUDIENCES.md`)

| Audiência | % esforço SEO | Triggers principais | Hubs | Sucesso = |
|---|---|---|---|---|
| **Cliente Empresa** (decisor HSST) | ~65% | Nova obrigação, contrato a expirar, inspeção ACT, certificação ISO, crescimento, M&A | `/servicos/`, `/recursos/guias/`, `/cobertura/` | Lead qualificado em `/proposta/` |
| **Formando** (B2C/B2B2C) | ~25% | Obrigação legal (HACCP, CAP, 35h), transição carreira | `/formacao/` | Inscrição em curso |
| **Trabalhador** (utente) | ~10% | Convocatória, recuperação acesso, ver resultados | `portal.previmed.pt` (subdomínio) | Friction = 0 |

**Princípio:** nunca tratar como audiência única. Páginas para Trabalhador não devem ranquear em queries comerciais (canibalização); páginas para Empresa não devem distrair com login.

**Pontes válidas entre audiências:**
- Empresa → Formando (cliente que precisa de formar trabalhadores)
- Formando → Empresa (pessoa qualificada em CAP TST pode trabalhar para cliente)
- Empresa → Trabalhador (demo do portal na página comercial)
- ❌ Trabalhador → Empresa (objetivos opostos; não pontear)

---

## 3. Arquitetura de informação (síntese; detalhe em `strategy/INFORMATION_ARCHITECTURE.md`)

### URL spine

```
/                                                       Homepage
├── /servicos/                                          Hub serviços (Empresa)
│   ├── /servicos/medicina-trabalho/
│   ├── /servicos/seguranca-trabalho/
│   ├── /servicos/higiene-seguranca-alimentar/
│   ├── /servicos/ambiente/
│   ├── /servicos/pericias-medico-legais/
│   ├── /servicos/exames-serologicos/
│   ├── /servicos/exames-seguradoras/
│   └── /servicos/certificacao/
├── /formacao/                                          Hub formação
│   ├── /formacao/catalogo/
│   ├── /formacao/{curso-slug}/
│   ├── /formacao/dgert/
│   ├── /formacao/modalidades/online/ ¦ /presencial/
│   └── /formacao/para-empresas/                        Ponte B2B
├── /cobertura/                                         Mapa nacional + locator
├── /recursos/
│   ├── /recursos/guias/{pillar-slug}/                  Pillars (P1)
│   ├── /recursos/faq/
│   └── /recursos/noticias/
├── /sobre/{certificacoes, equipa, historia}
├── /recrutamento/
├── /contactos/
├── /proposta/                                          Form pedido (noindex)
└── [legal]

[subdomínios]
portal.previmed.pt              Portal Trabalhador (noindex áreas auth)
elearning.previmed.pt           E-learning (decisão Fase 4: sub vs sub-folder)
```

**Regras-chave:**
- Profundidade ≤ 3 cliques da home para qualquer página de conversão.
- Slugs PT, lowercase, hifens, sem acentos, sem prefixos `/category/` ou `/page/`.
- Páginas conversão (`/proposta/`) = `noindex, follow`.
- LMS Previmed corre hoje em `previmed-academia.careview.pt` (white-label Careview/mediaview) — **decisão Fase 4** sobre integrar em `/formacao/elearning/` (WP-native) ou manter em `elearning.previmed.pt` (subdomínio externo).

### Schema map (alto nível)

| Tipo de página | Schema principal |
|---|---|
| Home | `Organization` + `WebSite` (`SearchAction`) |
| Hub `/servicos/` | `WebPage` + `BreadcrumbList` |
| Página de serviço | `Service` + `FAQPage` (quando aplicável) |
| Hub `/formacao/` | `EducationalOrganization` |
| Página de curso | `Course` + `CourseInstance` + `EducationalOccupationalCredential` (DGERT) |
| Pillar | `Article` + `FAQPage` |
| Sobre | `Organization` com `hasCredential` (ACT, DGS, DGERT, ISO 9001) |
| Cobertura | `Organization` com `areaServed: Country: PT` |

**Não usar `LocalBusiness`** — Previmed não tem morada única comercial (rede de parceiros + sede). Usar `Organization` com `areaServed`.

---

## 4. Estratégia de keywords (síntese; detalhe em `strategy/KEYWORDS.md`)

### 16 clusters mapeados, organizados em 3 camadas

**Camada 1 — Serviços (Empresa, P1)**
- Cluster 1: Medicina do Trabalho
- Cluster 2: Segurança do Trabalho
- Cluster 3: HACCP / Higiene e Segurança Alimentar
- Cluster 4: Ambiente
- Cluster 5: Perícias Médico-Legais
- Cluster 6: Exames Serológicos
- Cluster 7: Exames Seguradoras
- Cluster 8: Certificação (ISO)

**Camada 2 — Formação (Formando + Empresa, P1)**
- Cluster 9: Formação 35h obrigatória
- Cluster 10: CAP TST/TSST
- Cluster 11: Formação HACCP
- Cluster 12: Outras DGERT

**Camada 3 — Hub editorial + brand (P1 para pillars; P1-3 para brand)**
- Cluster 13: Brand (Previmed)
- Cluster 14: Trabalhador (portal/suporte)
- Cluster 15: Pillars informacionais legais
- Cluster 16: Comparativos / "Como escolher"

### Pillars prioritários (P1)

| Pillar | Slug | Volume info | Concorrência | Oportunidade |
|---|---|---|---|---|
| Lei 102/2009 explicada | `/recursos/guias/lei-102-2009-medicina-trabalho/` | Alto | Alta (DRE, PGDL bruto; só Twind explica) | **Alta** — entrar com calculadora obrigações + tabela multas |
| HACCP restauração | `/recursos/guias/haccp-restauracao/` | Alto | Média (Kaizen, Infraspeak, AHRESP) | **Média-Alta** — verticalizar por sub-setor |
| Formação 35h obrigatória | `/recursos/guias/formacao-35-horas-obrigatoria/` | Alto | Média (blogs jurídicos, Infeira, Doutor Finanças) | **Alta** — clarificar 35h vs 40h pós Lei 93/2019 |
| Como escolher empresa MT | `/recursos/guias/escolher-medicina-do-trabalho/` | Médio | Baixa (Centralmed/Sepri lideram com posts thin) | **Quick win** — Previmed já entra #10 só com página de serviço |
| Acidente trabalho: procedimento | `/recursos/guias/acidente-trabalho-procedimento/` | Médio | Média | Média |
| ISO 45001 vs OHSAS | `/recursos/guias/iso-45001-seguranca/` | Baixo | Média | Sinergia com `/servicos/certificacao/` |

### Canibalizações vigiar

| Query | Páginas em conflito | Resolução |
|---|---|---|
| "medicina do trabalho" | `/servicos/medicina-trabalho/` ↔ pillar Lei 102/2009 | Title do pillar começa por "Lei 102/2009" |
| "formação 35 horas" | `/formacao/catalogo/` ↔ pillar 35h | Pillar = "obrigatória explicada"; catálogo = "inscrição" |
| "HACCP" | `/servicos/higiene-seguranca-alimentar/` ↔ `/formacao/curso-haccp/` ↔ pillar HACCP | Serviço=consultoria; curso=formação; pillar=guia |

### Limitação a registar

Volumes e dificuldades são **estimativas qualitativas** (A/M/B) — não baseadas em GSC/Ahrefs. Re-calibrar na **Fase 2** com GSC ativo + (idealmente) DataForSEO/Ahrefs.

---

## 5. Cenário competitivo (síntese; detalhe em `strategy/COMPETITORS.md`)

### Concorrentes núcleo (5 a vigiar)

| # | Concorrente | Posição estratégica | Ameaça principal |
|---|---|---|---|
| 1 | **Centralmed** | Líder absoluto SEO+SEM+GMB. Conteúdo blog multi-cluster (medicina trabalho, HACCP, "como escolher"). | Bate Previmed em tudo o que se possa pagar + em conteúdo de quick wins |
| 2 | **Sepri** | Blog ativo, subdomínio dedicado para B2B (`empresassaudaveis.sepri.pt`), ads em head queries | Tenta mesmos ângulos editoriais |
| 3 | **Preveris** | Claim "maior rede nacional de clínicas autorizadas DGS" | Domina narrativa de escala/cobertura |
| 4 | **Hospital da Luz** | Força bruta de marca; **detém Featured Snippet** em "medicina do trabalho" | Difícil de bater em head term sem autoridade equivalente |
| 5 | **Seepmed** | Pequeno mas combina ads + blog "como escolher" | Mostra que tática é replicável |

### Padrões SERP (12 queries-âncora capturadas em 2026-05-20)

- **AI Overview ativo em 12/12 queries.** Conteúdo precisa de ser citável.
- **Ads escassos** (3 de 12 queries). Mercado SST PT não é PPC-heavy.
- **Local pack ativa** em queries com intenção comercial implícita. Centralmed domina Lisboa.
- **Featured snippet** só em head term genérica → Hospital da Luz.
- **Mercado fragmentado** em orgânico — ninguém domina > 2 posições por SERP.

### Posicionamento atual da Previmed (baseline 2026-05-20)

| Query | Posição | URL |
|---|---|---|
| `previmed` (brand) | #1 + sitelinks | `/` |
| `previmed e-learning` | #1 | `/e-learning/` |
| `previmed portal trabalhador` | — (homepage genérica) | — (gap UX/SEO) |
| `empresa medicina do trabalho` | **#9** | `/saude-no-trabalho/` |
| `como escolher empresa medicina trabalho` | **#10** | `/saude-no-trabalho/` |
| Restantes 7 não-brand | fora do top 10 | — |

**Leitura:** brand defendida; entrada em 2 queries comerciais com a mesma URL genérica; **zero presença em queries informacionais e de formação**.

### Lacunas → oportunidades (priorizadas)

**P1 — Quick wins (entrar top 5 em <90 dias):**
- L1. Blog "Como escolher empresa medicina do trabalho" → pillar dedicado.
- L2. Landing `/portal-trabalhador/` (não existe URL pública para o produto).
- L3. Tabela de preço B2B (decisão comercial; só GPmedicos+UACS expõem hoje).

**P2 — Hubs estruturais (3–6 meses):**
- L4. Pillar Lei 102/2009 com calculadora.
- L5. Hub "Formação 35h obrigatória".
- L6. Hub HACCP por setor (restauração, hotelaria, distribuição).

**P3 — Defensivo/médio prazo:**
- L7. Reforço GMB nacional (Centralmed tem múltiplos).
- L8. Identidade SEO para "Previforma" (sub-brand sem presença orgânica autónoma).
- L9. Citation building com SPMT, Ordem dos Médicos, ACT.

### Ângulos de diferenciação possíveis

1. **Transparência de preço** (decisão comercial — ninguém B2B SST PT expõe).
2. **Profundidade legal/regulatória** com clareza prática + CTA contextual.
3. **Verticalização por setor** em HACCP e segurança no trabalho.
4. **Mapa real de cobertura** (sem inflar — diferenciador vs Preveris).
5. **Integração Previforma** (formação 35h + medicina do trabalho num pacote único).

---

## 6. Roadmap (Fase 2+)

### Fase 2 — Infraestrutura de dados (próximas semanas, **antes** de produção de conteúdo)

| Tarefa | Responsável | Bloqueador para |
|---|---|---|
| Configurar Google Search Console em previmed.pt actual | utilizador | Re-calibrar volumes/dificuldades em `strategy/KEYWORDS.md` |
| (Opcional) Avaliar DataForSEO/Ahrefs (custo vs valor) | utilizador | Análise competitiva quantitativa |
| Capturar AIO expandido em 5 queries de teste (clicar "Modo IA") | SEO Lead | Estratégia de conteúdo AIO-friendly |
| Crawl técnico de previmed.pt actual | SEO Lead + WP impl. | Tabela redirects 301 para Fase 6 |
| GA4 setup + eventos conversão | utilizador | Medir lead value |

### Fase 3 — Briefs de conteúdo (Lote 1.5+ ou 2.x)

- Briefs detalhados para os 6 pillars P1.
- Briefs para as 3 quick wins (L1, L2, L3).
- Templates de página de serviço (`/servicos/{x}/`) com schema, FAQ, CTA.
- Templates de página de curso (`/formacao/{x}/`) com `Course` schema.

### Fase 4 — Decisões técnicas WordPress

- Stack: vanilla WP + Yoast/Rank Math (decisão SEO plugin).
- Page builder: nativo (Gutenberg blocks custom) ou Bricks/Cwicly (decisão).
- LMS: integrar em `/formacao/elearning/` (LearnDash/LifterLMS) OU manter `previmed-academia.careview.pt` externo.
- Portal Trabalhador: confirmar `portal.previmed.pt` com noindex em áreas auth.
- Form `/proposta/`: ferramenta (Gravity Forms / WP Forms / custom).

### Fase 5 — Produção de conteúdo

- Build dos hubs `/servicos/`, `/formacao/`, `/recursos/`.
- Build dos 6 pillars P1.
- Build de páginas individuais de serviço + curso.
- Internal linking matrix preenchida.

### Fase 6 — Go-live + migração

- Crawl final do site antigo → tabela redirects 301.
- Migrar conteúdo legacy útil.
- Switch DNS / preview → produção.
- Validação técnica pós-go-live (sitemap, robots, schema, Core Web Vitals).

### Fase 7+ — Iteração

- Medição mensal (GSC + GA4): queries que entram top 10, páginas com decay, AIO citations.
- Expansão long-tail conforme GSC mostrar.
- Decisão de páginas regionais (sim/não) com dados reais.

---

## 7. Questões em aberto / decisões a tomar

| # | Questão | Decisor | Quando |
|---|---|---|---|
| Q1 | Publicar tabela de preços B2B? Risco comercial vs ganho SEO. | Negócio (utilizador) | Antes de Fase 5 |
| Q2 | E-learning: WP-native (`/formacao/elearning/`) ou manter Careview externo? | utilizador + WP impl. | Fase 4 |
| Q3 | Páginas regionais por distrito (sim/não)? | SEO Lead | Pós-GSC, Fase 7 |
| Q4 | Sub-brand "Previforma": URL própria ou apenas marketing? | utilizador | Fase 4 |
| Q5 | DataForSEO/Ahrefs: investir? | utilizador | Fase 2 |
| Q6 | AIO: estratégia de citação (ser citado vs cliques)? | SEO Lead | Pós-Fase 2 (depende do que AIO mostra) |
| Q7 | Plugins SEO: Yoast vs Rank Math vs SEOPress? | SEO Lead + WP impl. | Fase 4 |

---

## 8. Riscos & mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Estimativas de volume erradas → priorização errada | Alta | Médio | Recalibrar Fase 2 com GSC; tratar strategy/KEYWORDS.md como hipótese |
| Centralmed responde com ads agressivos | Média | Médio | Diferenciar em conteúdo, não em SEM; long-tail informacional |
| AIO captura cliques sem driver tráfego | Alta | Alto | Foco em queries onde AIO ainda não domina + brand authority |
| Decisão "abrir preços" rejeitada | Média | Baixo | L1+L2 são quick wins independentes; L3 não bloqueia |
| Migração WP perde redirects | Média | Alto | Crawl + tabela 301 obrigatórios Fase 6 |
| Conteúdo legal sem validação jurídica | Baixa | Alto | Pillar 102/2009 e participação acidente trabalho devem ser revistos por advogado/SST sénior |

---

## 9. Handover para implementação WordPress (checklist Fase 4)

Quando se entrar na fase WP, o implementador deve receber:

- [ ] `STRATEGY.md` (este documento) + 4 docs filhas
- [ ] Mapa de URLs final (§3) com regras de slug
- [ ] Tabela schema por tipo de página (§3)
- [ ] Tabela `robots`/indexabilidade por área
- [ ] Lista de pillars P1 com briefs (Fase 3, ainda não produzido)
- [ ] Decisão Q2 (LMS local vs externo)
- [ ] Decisão Q7 (plugin SEO)
- [ ] Lista de campos custom necessários para `Service`/`Course`/`Article` schema
- [ ] Internal linking matrix
- [ ] Tabela redirects 301 (Fase 6)
- [ ] Plano de medição (KPIs por hub)

---

## 10. KPIs (Fase 7+)

Definição completa em `_system/KPI_MODEL.md` (já existe). Resumo das métricas estrela:

| Métrica | Target Fase 7 (mês 3 pós go-live) | Fonte |
|---|---|---|
| Queries onde Previmed está no top 10 (não-brand) | ≥ 15 | GSC |
| Leads `/proposta/` orgânicos / mês | linha de base + medição | GA4 |
| Inscrições `/formacao/` orgânicas / mês | linha de base + medição | GA4 |
| Pillars com tráfego orgânico > 100/mês | ≥ 3 | GSC + GA4 |
| Core Web Vitals (LCP/INP/CLS) em verde | 100% das páginas conversão | PSI/CrUX |
| AIO citations da Previmed | tracking manual mensal | Captura SERP |

---

## 11. Princípios não-negociáveis

1. **Não construir páginas para SEO que não sirvam o utilizador.** Cada URL tem de ter razão de existir além do ranking.
2. **Não fazer doorway pages regionais.**
3. **Não duplicar conteúdo entre serviço e pillar.** Title/H1/intent distintos.
4. **Não esconder o portal do trabalhador.** Mesmo que não convertido, é UX nuclear.
5. **Não publicar conteúdo legal sem validação.** Pillars 102/2009, acidente trabalho, formação 35h precisam de revisão jurídica.
6. **Não copiar Centralmed.** Diferenciar — ser mais profundo, mais claro, mais útil.
7. **Não ignorar AIO.** Conteúdo estruturado, citável, com schema.

---

## 12. Estado dos documentos da Fase 1

| Lote | Documento | Estado |
|---|---|---|
| 1.1 | `strategy/AUDIENCES.md` | ✅ Fechado |
| 1.2 | `strategy/INFORMATION_ARCHITECTURE.md` | ✅ Fechado |
| 1.3 | `strategy/KEYWORDS.md` | ✅ Fechado (com caveat de volumes qualitativos) |
| 1.4 | `strategy/COMPETITORS.md` | ✅ Fechado |
| 1.5 | `STRATEGY.md` (este) | ✅ Fechado |

**Fase 1 = COMPLETA.** Próxima decisão: arrancar Fase 2 (GSC + crawl) ou Fase 3 (briefs de conteúdo P1).
