# Decisão — Tool de Keyword Data

> **Lote 2.3 da Fase 2.** Comparativo + recomendação para o tool de dados de keywords/SERPs/competidores.
> Data: 2026-05-20.
> Estado: ✅ **DECIDIDO — Cenário Z (orçamento zero)**. Utilizador descartou todas as opções pagas (A–F). Stack mantém-se apenas com ferramentas gratuitas.
> Decisão completa registada em [`_living/DECISION_LOG.md`](./_living/DECISION_LOG.md).

---

## 1. O que precisamos resolver

A estratégia (Lote 1.5) e o crawl baseline (Lote 2.1) precisam de um data layer externo para:

| Caso de uso | Frequência | Volume estimado |
|---|---|---|
| **Search volume PT** para os ~120 keywords do `strategy/KEYWORDS.md` | Inicial + refresh trimestral | ~500 lookups iniciais, ~100/trimestre |
| **SERP capture** de queries comerciais e informacionais (validação de intent, tracking de top 10) | Mensal | ~50–80 SERPs/mês |
| **Competitor ranked keywords** (que palavras ranqueiam Centralmed, Quadrimed, etc) | Inicial + ad-hoc | ~10 domínios × ~1000 keywords |
| **Keyword ideas / related** para expandir clusters | Esporádico | ~20 seeds/mês |
| **Backlinks** dos 5 top competidores | Inicial + refresh anual | ~10 domínios baseline |
| **SERP features** (AIO, PAA, featured snippets) por query | Contínuo (Fase 2 → Fase 5) | embutido nos SERPs acima |
| **Rank tracking** semanal de ~50 queries-chave Previmed | Semanal | ~50 × 4 = 200/mês |

**Volume total ano 1:** estimado entre **3 000 e 6 000 queries/lookups**, fortemente concentrado nos primeiros 2 meses (auditoria inicial).

---

## 2. Opções avaliadas

| Tool | Modelo | Custo aprox. (USD) | API | UI/Dashboard | Cobertura PT | Notas |
|---|---|---|---|---|---|---|
| **DataForSEO** | Pay-per-query | Min top-up $50; SERP live ~$0.0006-$0.002/query; Search volume ~$0.075/1k keywords; Labs ~$0.01-$0.075/task | ✅ first-class | ❌ próprio (constrói-se) | ✅ google.pt + GA Ads PT | API limpa, docs claros, MCP comunitário existe |
| **SerpAPI** | Tiered (pay por search) | Free 250/mo; Starter $25/mo (1k); Developer $75/mo (5k); $0.025/search Starter | ✅ first-class | ❌ próprio | ✅ google.pt via `gl=pt&hl=pt-PT` | Foco em fidelidade SERP, sem keyword volume nativo |
| **Ahrefs Lite** | SaaS subscription | ~$129/mo ($1 548/ano); API **paga à parte** ~$500/mo | API extra | ✅ excelente | ✅ |  Best-in-class link index e content explorer |
| **Ahrefs Standard** | SaaS | ~$249/mo | API extra | ✅ excelente | ✅ | Para investigação profunda; overkill greenfield |
| **Semrush Pro** | SaaS | ~$139/mo (~$140) | API extra | ✅ excelente | ✅ mas PT historicamente mais fraco que Ahrefs | Mais features no plano base que Ahrefs Lite |
| **SE Ranking** | SaaS | ~$55/mo Essential, ~$110/mo Pro | API limitada | ✅ médio | ✅ | Alternativa low-cost; rank tracking forte |
| **Google Keyword Planner** | Gratuito (com conta Ads ativa) | 0 | ❌ só via Ads API | ✅ via Ads UI | ✅ PT nativo | Bins largos (10-100, 100-1k) se conta sem spend |
| **GSC + GA4** | Gratuito | 0 | ✅ (Search Console API + GA4 Data API) | ✅ próprios | ✅ | **Fonte de verdade** para queries que já trazem cliques. Não substitui keyword research externa. |

---

## 3. Cenários de custo Ano 1

Assumindo ~5 000 queries totais (alvo realista) e ~50 rank tracks semanais (200/mês × 12 = 2 400):

| Cenário | Setup | Mensal | Total ano 1 | Cobre tudo? |
|---|---|---|---|---|
| **A) DataForSEO + GSC + Playwright + Keyword Planner** | $50 top-up | ~$15-25 (média) | **~$250-350** | ✅ sim, requer skills API |
| **B) SerpAPI Starter + GSC + Keyword Planner** | $0 | $25 | **$300** | ⚠️ falta search volume rico, falta link data |
| **C) Ahrefs Lite + GSC** | $0 | $129 | **$1 548** | ✅ mais UI; API pago à parte se quisermos automatizar |
| **D) Semrush Pro + GSC** | $0 | $139 | **$1 668** | ✅ rico em features (rank tracking, audit) |
| **E) SE Ranking Essential + GSC** | $0 | $55 | **$660** | ⚠️ keyword data PT mais fraco |
| **F) DataForSEO + Ahrefs Lite (3 meses)** | $50 + $129 | $15 + $129×3 / depois $15 | **~$650** | ✅ híbrido: trial de link analysis sem subscription anual |

---

## 4. Análise de trade-offs por dimensão

### Custo
DataForSEO ganha por ordem de grandeza para o volume previsto. Ahrefs/Semrush só fazem sentido se houver consumo intensivo de UI (workflows manuais do SEO Lead).

### Qualidade dos dados PT
- **SERPs**: SerpAPI e DataForSEO têm fidelidade comparável (capturam google.pt com `gl=pt&hl=pt-PT`). Ambos retornam SERP features incluindo AIO quando presente.
- **Search volume**: DataForSEO Keywords Data passa por Google Ads API (mesma fonte do Keyword Planner) — buckets agregados se a conta tem spend baixo. Ahrefs/Semrush usam métricas próprias (clickstream + modeling) que diferem em valor absoluto mas mantêm coerência relativa.
- **Backlinks**: Ahrefs é referência da indústria. DataForSEO Backlinks é razoável mas menos profundo. Para Previmed (poucos backlinks, foco em on-page), profundidade extra não é decisiva.

### Integração com Claude / MCP
- DataForSEO: existe MCP comunitário; API REST simples; ideal para automação por agentes.
- SerpAPI: API muito limpa, fácil integrar; sem MCP first-class mas trivial via WebFetch/HTTP.
- Ahrefs/Semrush API: paga adicional ao plano, integração mais pesada, justifica-se com volume.

### UX manual (SEO Lead a explorar dados)
Ahrefs/Semrush ganham por larga margem. Mas o `STRATEGY.md` define que **a equipa SEO neste projeto opera maioritariamente via Claude/agentes** — UX manual é secundária. Quando precisarmos de UI manual, há free trial Ahrefs (7 dias, $7 antigamente) para investigações pontuais.

### Lock-in e reversibilidade
- DataForSEO/SerpAPI: zero lock-in (saldo expira em ~12 meses).
- Ahrefs/Semrush: subscription anual com discount tende a 12 meses; cancelar mensal sai caro proporcionalmente.

### Risco operacional
- DataForSEO: dependência de API estável; mitigado por SerpAPI como fallback se necessário.
- Subscription SaaS: 1 falha de pagamento e perdemos histórico de rank tracking.

---

## 5. Recomendação

**Adotar Cenário A: DataForSEO + GSC + Playwright + Keyword Planner.**

**Justificação:**
1. **Volume real é baixo** (~5k queries/ano). Pagar $1.5k/ano em SaaS para usar 10% das features é desalinhado com a fase greenfield.
2. **Equipa SEO opera via agentes Claude** (decidido em Lote 0.x). DataForSEO é tailor-made para esse padrão; UI Ahrefs/Semrush é desperdiçada.
3. **GSC é fonte de verdade** para tudo o que já tem cliques; reservar dinheiro externo para o que GSC *não* mostra (volume estimado, SERPs ad-hoc, ranked keywords de competidores).
4. **Setup barato e reversível** ($50 top-up que dura meses; saldo não usado expira mas não é assinatura mensal).
5. **Path de escala claro:** se chegarmos a precisar de link analysis profundo, contratamos 1 mês de Ahrefs Lite ad-hoc ($129 one-shot) sem comprometer com anual.

**Tools complementares (sem custo adicional):**
- **Google Search Console** (free, primário) — queries reais com cliques/impressões.
- **GA4** (free) — comportamento pós-clique.
- **Google Keyword Planner** (free com conta Ads ativa) — ground truth de volume PT.
- **Playwright MCP** (free, já configurado) — captura visual de SERPs e Modo IA expandido.
- **PageSpeed Insights API** (free, requer API key) — Core Web Vitals contínuo.

---

## 6. Plano de implementação (próximas ações)

| # | Ação | Responsável | Estado |
|---|---|---|---|
| 1 | Decisão do utilizador (DataForSEO ou alternativa) | João | 🟡 pendente |
| 2 | Criar conta DataForSEO + top-up $50 | João | 🔒 bloqueado por #1 |
| 3 | Guardar credenciais em `.env` (`DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`) — nunca commitar | João + Claude | 🔒 bloqueado por #2 |
| 4 | Activar MCP DataForSEO ou criar wrapper de chamadas | Claude | 🔒 |
| 5 | Smoke test: 1 SERP + 5 search volume lookups | Claude | 🔒 |
| 6 | Pull initial: 120 keywords × search volume + 30 SERPs prioritários | Claude | 🔒 |
| 7 | Adicionar a `MCP_STACK.md` e `_system/TOOLING_MCP_STACK.md` | Claude | 🔒 |
| 8 | Setup GSC + GA4 (Lote 2.4) — independente de #1-#7 | João + Claude | em paralelo |

---

## 7. Alternativas se a recomendação não passar

- **Restrição de orçamento total = $0:** ficar só com GSC + GA4 + Keyword Planner + Playwright. Cobertura limitada (sem SERPs históricas, sem competitor ranked keywords) mas viável para Fase 3 inicial.
- **Preferência por UI manual:** ir para **SE Ranking Essential ($55/mo)** — meio termo entre custo e UX.
- **Necessidade de link audit profundo desde já:** **Ahrefs Lite ($129/mo)**, aceitar custo.

---

## 8. Limitações e riscos

- **Estimativas de volume são exatamente isso — estimativas.** Se o uso explodir (ex.: rank tracking diário em vez de semanal, ou auditoria de 50 competidores), DataForSEO pode chegar a $50-100/mês. Ainda assim, < SaaS.
- **DataForSEO Keywords Data herda buckets do Google Ads.** Se a conta Ads da Previmed estiver inativa ou sem spend, volumes virão em ranges largos (1k-10k em vez de 6 400). Mitigação: ativar conta Ads com €1 de spend mensal para destravar números finos, ou cruzar com Ahrefs num único mês de trial.
- **Sem dashboard pronto** significa que produzimos os relatórios via Claude/docs. Aumenta valor da `SEO_REPORTING_DASHBOARD/SKILL.md` mas exige disciplina.
- **Custos podem variar.** Preços citados são aproximados — verificar nas respectivas páginas oficiais antes de top-up.

---

## 9. Decisão tomada

> ✅ **Cenário Z — Orçamento zero.** Utilizador decidiu em 2026-05-20: *"se não houver nada gratuito, não quero nada"*.
>
> Stack adotada (tudo grátis):
> - **Google Search Console** — queries reais com cliques/impressões (fonte de verdade quando ligado).
> - **GA4** — comportamento pós-clique.
> - **Google Keyword Planner** — volumes em buckets largos (10–100, 100–1k, 1k–10k) via conta Ads ativa.
> - **Playwright MCP** — captura manual de SERPs e Modo IA expandido (já demonstrado nos relatórios de 2026-05-20).
> - **PageSpeed Insights API** — Core Web Vitals (free, requer API key).
>
> ## Trade-offs aceites
>
> - **Sem volumes finos** — Keyword Planner devolve ranges, não números exatos.
> - **Sem competitor ranked keywords automatizadas** — só sabemos o que concorrentes ranqueiam por inspeção manual ou capturas Playwright dirigidas.
> - **Sem rank tracking automatizado** — GSC mostra queries onde Previmed **já** ranqueia; para queries onde não ranqueia, fazemos checks manuais periódicos via Playwright.
> - **Sem backlinks data** — descoberta de backlinks por GSC (links recebidos) + inspeção manual de competidores. Sem índice profundo (Ahrefs).
> - **Sem dashboard SaaS** — relatórios produzidos via Claude/markdown em `reports/`.
>
> ## Quando reavaliar
>
> Reavaliar a decisão se:
> - Volume de queries necessário cresce significativamente (ex. 10+ pillars, rank tracking diário).
> - Briefs precisarem de competitor ranked keywords em massa.
> - Auditoria de backlinks for crítica para compliance / link building.
> - Aparecer free tier de algum tool que cubra parte das lacunas.
>
> ## Plano de implementação (revisto)
>
> Secção 6 acima está obsoleta. Plano atualizado:
>
> | # | Ação | Responsável | Estado |
> |---|---|---|---|
> | 1 | Executar Lote 2.4 (`setup/GSC_GA4_SETUP.md`) — ligar GSC, GA4, Site Kit, criar API key PSI | João | ⏳ pendente |
> | 2 | Garantir conta Google Ads ativa (mesmo sem spend) para destravar Keyword Planner | João | ⏳ pendente |
> | 3 | Atualizar `_system/TOOLING_MCP_STACK.md` para refletir stack zero-cost | Claude | ✅ a fazer agora |
> | 4 | Briefs P1 começam imediatamente — não dependem de keyword data tool para arrancar (estratégia + competitor deep-dive já dão input suficiente) | Claude + João | desbloqueado |
