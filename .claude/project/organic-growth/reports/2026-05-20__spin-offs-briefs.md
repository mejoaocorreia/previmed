# Spin-offs P1 — briefs consolidados — 2026-05-20

## Purpose

Brief curto para cada um dos **15 spin-offs** documentados nos briefs dos 5 pillars. Padrão SEPRI "árvore" (1 pillar + 2-3 spin-offs por cluster) — observado em `reports/2026-05-20__competitor-deep-dive.md` §H1.

**Quando arrancar produção:** aguardar dados de recaptura AIO t+30d (Fase E2 do execution-plan) para priorizar pelos clusters onde os pillars estão a entrar. Cada spin-off custa ~1.25 pd (brief + copy + deploy).

> **Padrões comuns** aplicáveis a todos os spin-offs:
> - **Brand voice**: forma canónica do cluster.
> - **Autor**: mesmo placeholder do pillar pai (até substituição por nome real).
> - **Word count**: 800–1200w body + 6–10 FAQs (mais curto que pillars — focado num sub-tópico).
> - **Citações institucionais**: mínimo 3 por spin-off (subset das do pillar pai).
> - **Schema**: Article + FAQPage; HowTo onde aplicável.
> - **Internal linking**: obrigatório link para o pillar pai + 1 cross-cluster.
> - **URL pattern**: `/recursos/guias/<slug>/`.

## Prioritização global

| # | Spin-off | Cluster | Prioridade | Justificação |
|---|---|---|---|---|
| 1 | Avença vs ato médico | Q5 | **P1-A** | Query comercial pura (BOT funil). Converte direto. |
| 2 | Lei 93/2019 formação | Q4 | **P1-A** | Diferenciador legal único. Conteúdo PT desatualizado em massa. |
| 3 | Ficha de Aptidão | Q1 | **P1-A** | SEPRI tem 1186w neste sub-tópico em AIO. Apropriável. |
| 4 | Relatório Único Anexo D | Q5 | **P1-B** | Critério AIO #4 já citado por Previmed. |
| 5 | HACCP restauração | Q3 | **P1-B** | Vertical maior do cluster HACCP. AHRESP fonte AIO. |
| 6 | Modalidades serviço SST | Q2 | **P1-B** | Traininghouse domina; replicável com tabela. |
| 7 | Crédito de horas formação | Q4 | P2 | Sub-tópico técnico Q4. |
| 8 | Periodicidade exames MT | Q1 | P2 | Snippet target. |
| 9 | Plano prevenção riscos | Q2 | P2 | Follow-up AIO. |
| 10 | Limites críticos temperatura HACCP | Q3 | P2 | Follow-up AIO. |
| 11 | Registos diários HACCP | Q3 | P2 | Follow-up AIO. |
| 12 | Geo Norte MT (ou Porto) | Q1 | P3 | Cobertura geográfica local. |
| 13 | Geo Norte ST | Q2 | P3 | Idem. |
| 14 | Coimas ACT formação | Q4 | P3 | Snippet target compliance. |
| 15 | Geo Norte/Lisboa Q5 | Q5 | P3 | Local SEO. |

---

## P1-A — Atacar primeiro (alto valor, baixo esforço)

### SO-1. "Medicina do Trabalho: avença mensal ou pagamento por ato médico?" (Q5)

- **URL**: `/recursos/guias/medicina-trabalho-avenca-ou-ato-medico/`
- **Query principal**: `medicina trabalho avença ou ato`
- **Queries secundárias**: `quanto custa medicina do trabalho`, `preço medicina trabalho`, `medicina trabalho por trabalhador`
- **Intenção**: TRANS / BOT (comparação comercial)
- **Autor**: Dr. Miguel Henriques (mesmo do Q5)
- **Estrutura**:
  ```
  H1: Avença mensal vs ato isolado em Medicina do Trabalho — guia comparativo
    H2: Como funciona cada modelo
      H3: Avença mensal fixa
      H3: Pagamento por ato isolado
    H2: Comparativo de custos (tabela com cenários)
    H2: Quando escolher avença
    H2: Quando escolher ato isolado
    H2: Custos ocultos a vigiar
    H2: O que está incluído numa avença Previmed
    H2: FAQs
  ```
- **Citações obrigatórias** (3+):
  - pgdlisboa Lei 102/2009 (referência ao serviço obrigatório).
  - Portal ACT.
  - DGS.
- **Diferenciador**: tabela com 3 cenários (PME 10 trab. escritório / PME 30 trab. indústria leve / 100 trab. multi-localização).
- **CTA**: simulação personalizada via `/proposta/?ref=spin-avenca`.
- **Esforço**: 1.25 pd.

### SO-2. "Lei 93/2019 explicada — formação contínua de 35 para 40 horas" (Q4)

- **URL**: `/recursos/guias/lei-93-2019-formacao-trabalhadores/`
- **Query principal**: `Lei 93/2019 formação`
- **Queries secundárias**: `Lei 93/2019 código do trabalho`, `Art.º 131º Código do Trabalho`, `alteração Lei 93/2019`
- **Intenção**: INFO (jurídica pura)
- **Autor**: Dra. Inês Carvalho (mesmo do Q4)
- **Estrutura**:
  ```
  H1: Lei n.º 93/2019 — o que mudou na formação obrigatória
    H2: Contexto — porque é que mudou
    H2: Antes e depois (35h → 40h)
    H2: Art.º 131º do Código do Trabalho atualizado (texto integral comentado)
    H2: Nota Técnica 9 da ACT — como contabilizar
    H2: Implicações práticas para empresas
    H2: Implicações práticas para trabalhadores
    H2: FAQs jurídicas
  ```
- **Citações obrigatórias** (3+):
  - Diário República — Dever de formação contínua (link direto).
  - Nota Técnica 9 ACT (PDF).
  - CGTP-IN — guia direitos.
- **Diferenciador**: texto integral comentado do Art.º 131º + glossário jurídico (acumulação, crédito, proporcionalidade).
- **Esforço**: 1.25 pd.

### SO-3. "Ficha de Aptidão para o Trabalho — guia completo" (Q1)

- **URL**: `/recursos/guias/ficha-de-aptidao-trabalho/`
- **Query principal**: `ficha de aptidão`
- **Queries secundárias**: `ficha de aptidão para o trabalho`, `classificações ficha aptidão`, `apto condicionado`, `inapto definitivo`
- **Intenção**: INFO (RH + trabalhadores procuram explicação)
- **Autor**: Dr. Miguel Henriques
- **Estrutura**:
  ```
  H1: Ficha de Aptidão para o Trabalho — guia completo (Lei 102/2009)
    H2: O que é a Ficha de Aptidão
    H2: Quem a emite (médico do trabalho)
    H2: As 4 classificações possíveis (detalhe)
      H3: Apto
      H3: Apto com Condicionamento (com exemplos reais)
      H3: Inapto Temporário
      H3: Inapto Definitivo
    H2: O que a empresa pode ou não saber (confidencialidade)
    H2: Como contestar uma Ficha de Aptidão
    H2: Validade temporal
    H2: FAQs (10+)
  ```
- **Citações obrigatórias** (3+):
  - pgdlisboa Lei 102/2009 (Art.º 110.º).
  - Portal ACT — médicos do trabalho.
  - SPMT (sociedade científica).
- **Diferenciador**: secção sobre **confidencialidade clínica** — empresa só sabe a classificação binária, não o diagnóstico. SEPRI domina este sub-tópico (1186w) — Previmed pode bater com qualidade superior.
- **Esforço**: 1.25 pd.

---

## P1-B — Segunda onda (médio valor, médio esforço)

### SO-4. "Relatório Único Anexo D — guia de preenchimento SST" (Q5)

- **URL**: `/recursos/guias/relatorio-unico-anexo-d-medicina-trabalho/`
- **Query principal**: `Relatório Único Anexo D`
- **Queries secundárias**: `como preencher relatório único`, `anexo D segurança saúde trabalho`, `Relatório Único SST`
- **Intenção**: INFO + TRANS (RH precisa de cumprir prazo)
- **Autor**: Dr. Miguel Henriques (cross-cluster Eng.ª Sara Vilela em revisão técnica)
- **Estrutura**:
  ```
  H1: Relatório Único Anexo D — guia prático de preenchimento (2026)
    H2: O que é o Relatório Único e o Anexo D
    H2: Quem é obrigado a entregar
    H2: Prazos de entrega (atualizado)
    H2: Dados a recolher durante o ano para evitar correria no fim
    H2: Como exportar dados a partir do portal do prestador SST
    H2: Erros comuns e como evitar
    H2: Coimas por incumprimento
    H2: FAQs
  ```
- **Citações obrigatórias**:
  - Portal ACT (regulamentação Relatório Único).
  - GEP/MTSSS (Gabinete Estratégia Planeamento — gere o sistema do Relatório Único).
  - pgdlisboa.
- **Esforço**: 1.25 pd.

### SO-5. "HACCP para restauração — guia 2026" (Q3)

- **URL**: `/recursos/guias/haccp-restauracao/`
- **Query principal**: `HACCP restauração`
- **Queries secundárias**: `HACCP restaurantes`, `ASAE restauração`, `HACCP cozinha`, `manipulação alimentos restauração`
- **Intenção**: INFO + COMM (proprietários de restaurante)
- **Autor**: Eng.ª Carla Tavares
- **Estrutura**:
  ```
  H1: HACCP para restauração — guia 2026 para restaurantes, cafés e snack-bars
    H2: Porque a restauração é o setor mais fiscalizado pela ASAE
    H2: Os 7 princípios HACCP aplicados a uma cozinha real
      H3-H9: cada princípio com exemplo de restaurante
    H2: PCCs típicos da cozinha (receção / refrigeração / cozedura / arrefecimento / exposição)
    H2: Limites críticos de temperatura para os pratos mais comuns
    H2: Registos diários — exemplo prático
    H2: HACCP digital (AHRESP) vs papel
    H2: Quando chega a ASAE — checklist de 10 itens
    H2: FAQs
  ```
- **Citações obrigatórias**:
  - ASAE (3 URLs específicas).
  - AHRESP (HACCP Digital).
  - Reg CE 852/2004.
- **Diferenciador**: **tabela de temperaturas por prato** (frangos, peixes, sopas, sobremesas) — alto valor prático.
- **Esforço**: 1.5 pd (mais técnico).

### SO-6. "4 Modalidades de Serviço de Segurança no Trabalho — qual escolher" (Q2)

- **URL**: `/recursos/guias/modalidades-servico-seguranca-trabalho/`
- **Query principal**: `modalidades serviço segurança trabalho`
- **Queries secundárias**: `serviços internos seguranca trabalho`, `trabalhador designado SST`, `serviços externos SST`, `serviços comuns segurança`
- **Intenção**: INFO + COMM
- **Autor**: Eng.ª Sara Vilela
- **Estrutura**:
  ```
  H1: 4 Modalidades de Serviço de Segurança no Trabalho — guia comparativo
    H2: O que diz a Lei 102/2009 sobre as modalidades
    H2: Modalidade 1 — Serviços Internos
      H3: Quem é obrigado
      H3: Custos e estrutura típicos
    H2: Modalidade 2 — Serviços Externos
    H2: Modalidade 3 — Serviços Comuns
    H2: Modalidade 4 — Trabalhador Designado
    H2: Tabela comparativa (custos / autonomia / risco / dimensão típica)
    H2: Como mudar de modalidade
    H2: FAQs
  ```
- **Citações obrigatórias**:
  - pgdlisboa Lei 102/2009 (Art.º 73º-81º).
  - ACT — Serviços Internos (obrigatoriedade).
  - ACT — Entidades autorizadas para Serviços Externos.
  - APSEI (Guia organizacional).
- **Diferenciador**: árvore de decisão flowchart "qual modalidade para a minha empresa?".
- **Esforço**: 1.25 pd.

---

## P2 — Terceira onda (priorizar pós-recaptura AIO t+30d)

### SO-7. Crédito de horas formação contínua (Q4)
- URL: `/recursos/guias/credito-horas-formacao-continua/` · Query: `crédito horas formação contínua` · Intenção: INFO · Esforço: 1 pd
- Citações: Diário República, Nota Técnica 9 ACT, CGTP-IN.

### SO-8. Periodicidade dos exames de Medicina do Trabalho (Q1)
- URL: `/recursos/guias/periodicidade-exames-medicina-trabalho/` · Query: `medicina do trabalho periodicidade exames` · Intenção: INFO · Esforço: 1 pd
- Citações: pgdlisboa Lei 102/2009 Art.º 108º, Portal ACT, SPMT.

### SO-9. Plano de Prevenção de Riscos — modelo prático (Q2)
- URL: `/recursos/guias/plano-prevencao-riscos-empresa/` · Query: `plano de prevenção de riscos empresa` · Intenção: INFO + TRANS · Esforço: 1.25 pd
- Citações: Portal ACT, APSEI, pgdlisboa.

### SO-10. Limites críticos de temperatura HACCP (Q3)
- URL: `/recursos/guias/haccp-limites-criticos-temperatura/` · Query: `limites críticos HACCP temperatura` · Intenção: INFO · Esforço: 1 pd
- Citações: ASAE, Codex Alimentarius, DGAV.
- **Diferenciador**: tabela completa por categoria de alimento.

### SO-11. Registos diários HACCP — modelo + checklist (Q3)
- URL: `/recursos/guias/haccp-registos-diarios/` · Query: `registos diários HACCP` · Intenção: INFO + TRANS · Esforço: 1 pd
- Citações: ASAE, AHRESP.
- **Diferenciador**: PDF descarregável com template de registos.

---

## P3 — Quarta onda (geo + compliance long-tail)

### SO-12. Medicina do Trabalho no Norte (ou Porto) (Q1)
- URL: `/recursos/guias/medicina-do-trabalho-norte/` · Query: `medicina do trabalho porto`, `medicina do trabalho norte` · Intenção: COMM local · Esforço: 1 pd
- Reaproveita pillar Q1 + secção sobre cobertura Previmed na região.

### SO-13. Segurança no Trabalho — Norte (Q2)
- URL: `/recursos/guias/seguranca-no-trabalho-norte/` · Query: `segurança no trabalho porto`, `segurança no trabalho norte` · Esforço: 1 pd

### SO-14. Coimas ACT em formação obrigatória (Q4)
- URL: `/recursos/guias/coimas-act-formacao-obrigatoria/` · Query: `coima incumprimento formação`, `coima formação 40 horas` · Intenção: INFO compliance · Esforço: 1 pd
- Citações: Portal ACT, Diário República.
- **Diferenciador**: tabela com valores indicativos de coimas por dimensão de empresa e tipo de falha.

### SO-15. Como escolher empresa MT — Norte/Lisboa (Q5)
- URL: `/recursos/guias/escolher-medicina-do-trabalho-norte/` ou Lisboa · Query: `melhor empresa medicina trabalho porto`, `melhor empresa medicina trabalho lisboa` · Esforço: 1 pd
- Reaproveita pillar Q5 + adapta critério "Infraestrutura" à cobertura regional.

---

## Esforço total se fizermos os 15

| Onda | Spin-offs | Esforço (pd) |
|---|---|---|
| P1-A | SO-1 a SO-3 | ~3.75 |
| P1-B | SO-4 a SO-6 | ~4 |
| P2 | SO-7 a SO-11 | ~5.25 |
| P3 | SO-12 a SO-15 | ~4 |
| **Total** | **15 spin-offs** | **~17 pd** |

## Recomendação para o utilizador

**Não produzir todos antes de validar.** Sequência:

1. **Deploy dos 5 pillars** (Fase D do `execution-plan-90d.md`).
2. **Recaptura AIO t+30d** após pillars publicados.
3. **Priorizar pelos clusters onde os pillars JÁ ESTÃO a entrar em AIO** — esses pillars com spin-offs ganham muito; pillars que ainda não entraram, primeiro melhorar o pillar.
4. **Atacar P1-A em paralelo aos pillars** se houver capacidade editorial (SO-1, SO-2, SO-3 — comerciais/legais diferenciadores).
5. **P1-B e P2** depois de recaptura t+30d.
6. **P3** opcional, conforme dados GSC.

## Backlog Items To Add

A copiar para `../_living/BACKLOG.md`:

- `[Content opportunity] P1` 3 spin-offs P1-A (Avença, Lei 93/2019, Ficha Aptidão) — ~3.75 pd. Origem: `reports/2026-05-20__spin-offs-briefs.md` §P1-A.
- `[Content opportunity] P2` 3 spin-offs P1-B (Relatório Único, HACCP restauração, 4 modalidades) — ~4 pd. Origem: §P1-B.
- `[Content opportunity] P2` 5 spin-offs P2 — ~5.25 pd. Origem: §P2.
- `[Content opportunity] P3` 4 spin-offs P3 (geo + compliance) — ~4 pd. Origem: §P3.

## Last Updated

2026-05-20 por Claude (SEO Lead).
