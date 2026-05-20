# Strategy — Universo de Keywords

> Lote 1.3 da Fase 1.
> Última atualização: 2026-05-19.
> Autor: SEO Lead + Keyword & Intent agent.
> Base: `strategy/AUDIENCES.md` + `strategy/INFORMATION_ARCHITECTURE.md`.

## Limitações desta análise

**Não há dados próprios** nesta fase:

- ❌ Sem Google Search Console (não configurado).
- ❌ Sem ferramenta de volume (Ahrefs/Semrush/DataForSEO) configurada.
- ❌ Sem dados de PPC/Google Ads.

**O que esta análise é**: hipóteses estruturadas com base em:
- conhecimento do mercado HSST português (vocabulário regulatório real);
- padrões SERP previsíveis para B2B regulado;
- vocabulário identificado em previmed.pt e em sites institucionais (ACT, DGS, DGERT).

**O que esta análise não é**: lista priorizada por volume real. Volume e dificuldade são **estimativas qualitativas** marcadas A/M/B (Alto/Médio/Baixo).

**Validação obrigatória na Fase 2**: assim que GSC + (idealmente) DataForSEO ou Ahrefs estiverem disponíveis, esta tabela é refeita com volumes reais e re-priorizada. O `keyword-intent` agent recebe esse trabalho.

---

## Notação

**Intenção:**
- `INFO` — informacional (aprender)
- `COMM` — comercial (avaliar/comparar)
- `TRANS` — transacional (comprar/contactar)
- `NAV` — navegacional/brand
- `LOCAL` — intenção local explícita

**Funil:** TOP / MID / BOT

**Volume estimado:** A=Alto, M=Médio, B=Baixo, MB=Muito Baixo (long-tail)

**Dificuldade estimada:**
- ALTA — institucional (ACT/DGS) ou marcas estabelecidas dominam
- MÉDIA — 5–10 concorrentes comerciais, fragmentado
- BAIXA — ninguém faz bem, oportunidade

**Prioridade (P1–P5):**
- **P1** — captura crítica (alto ROI esperado)
- **P2** — forte oportunidade
- **P3** — cobertura útil
- **P4** — long-tail / nice-to-have
- **P5** — monitorizar apenas

---

## Cluster 1 — Medicina do Trabalho

**Target hub:** `/servicos/medicina-trabalho/`
**Pillar de suporte:** `/recursos/guias/lei-102-2009-medicina-trabalho/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| medicina do trabalho | INFO+COMM | TOP/MID | A | ALTA | P1 | `/servicos/medicina-trabalho/` | Termo head, ambíguo — página tem de servir informacional e comercial. |
| o que é medicina do trabalho | INFO | TOP | M | MÉDIA | P2 | pillar 102/2009 | Featured snippet target. |
| medicina do trabalho obrigatória | INFO | TOP | M | MÉDIA | P2 | pillar 102/2009 | Forte intenção pré-comercial. |
| quem precisa medicina do trabalho | INFO | TOP | M | MÉDIA | P2 | pillar 102/2009 | PAA candidate. |
| lei 102/2009 | INFO | TOP | M | ALTA | P2 | pillar 102/2009 | Concorre com ACT/Diário Repúb. — ganhar com clareza prática. |
| lei medicina do trabalho | INFO | TOP | M | ALTA | P2 | pillar 102/2009 | Sinónimo do anterior. |
| ficha de aptidão | INFO | TOP | M | MÉDIA | P3 | sub-página ou secção pillar | Termo técnico, alta intenção de compliance. |
| ficha de aptidão modelo | INFO | TOP | M | BAIXA | P3 | secção pillar | Long-tail; oportunidade. |
| exame de admissão medicina trabalho | INFO | TOP | M | MÉDIA | P3 | secção pillar | Q informacional típica de HR. |
| periodicidade exames medicina trabalho | INFO | TOP | M | BAIXA | P2 | secção pillar | Resposta factual, snippet-friendly. |
| obrigações empregador medicina trabalho | INFO | TOP | M | MÉDIA | P2 | pillar 102/2009 | Alto fit comercial. |
| medicina do trabalho preço | COMM | MID | M | MÉDIA | P1 | `/servicos/medicina-trabalho/` (secção preços) | Q comercial pura — não evitar; dar faixa indicativa + CTA proposta. |
| preço medicina do trabalho por trabalhador | COMM | MID | M | BAIXA | P1 | `/servicos/medicina-trabalho/` | Sub-pergunta de cima, especifica. |
| empresa medicina do trabalho | COMM | MID | A | ALTA | P1 | `/servicos/medicina-trabalho/` | Q comercial principal do cluster. |
| empresas medicina do trabalho portugal | COMM | MID | M | ALTA | P2 | `/servicos/medicina-trabalho/` + `/cobertura/` | Concorrência forte: nacionais grandes. |
| como escolher empresa medicina do trabalho | INFO+COMM | MID | M | BAIXA | P1 | `/recursos/guias/escolher-medicina-do-trabalho/` | **Oportunidade ouro** — ninguém faz bem. |
| serviços externos medicina trabalho | COMM | MID | B | MÉDIA | P3 | `/servicos/medicina-trabalho/` | Vocabulário B2B. |
| medicina trabalho online | INFO+COMM | MID | B | BAIXA | P3 | `/servicos/medicina-trabalho/` | Tendência crescente; FAQ obrigatório. |
| rede clínicas medicina trabalho | COMM | MID | B | BAIXA | P2 | `/cobertura/` | Diferenciador Previmed. |
| pedido proposta medicina do trabalho | TRANS | BOT | B | MÉDIA | P1 | `/proposta/?ref=medicina-trabalho` | Conversion query. |
| orçamento medicina trabalho | TRANS | BOT | B | MÉDIA | P1 | `/proposta/` | Sinónimo. |

**Resumo:** cluster grande, com forte mistura informacional + comercial. Estratégia: dominar long-tail informacional para alimentar conversão na página de serviço.

---

## Cluster 2 — Segurança do Trabalho

**Target hub:** `/servicos/seguranca-trabalho/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| segurança no trabalho | INFO+COMM | TOP/MID | A | ALTA | P1 | `/servicos/seguranca-trabalho/` | Head term. |
| segurança e saúde no trabalho | INFO+COMM | TOP/MID | A | ALTA | P1 | `/servicos/seguranca-trabalho/` | Termo formal regulatório. |
| HST higiene segurança trabalho | INFO | TOP | M | MÉDIA | P3 | `/servicos/seguranca-trabalho/` | Termo de profissionais. |
| HSST | INFO | TOP | M | MÉDIA | P3 | hub `/servicos/` | Abreviatura sector. |
| técnico de segurança no trabalho | INFO | TOP | A | ALTA | P2 | secção pillar | Carreira; pode atrair candidatos a TST (não cliente). |
| TST funções | INFO | TOP | M | MÉDIA | P3 | pillar carreira ou DGERT | Cuidado com intenção: aspirantes a TST não convertem. |
| avaliação de riscos no trabalho | INFO | TOP | M | MÉDIA | P2 | secção pillar | Serviço típico Previmed. |
| plano de prevenção empresa | INFO | TOP | B | BAIXA | P3 | secção pillar | Compliance query. |
| EPI equipamento proteção | INFO | TOP | M | ALTA | P4 | — | Volume alto mas intenção é compra de EPI, não serviço. **Excluir**. |
| consultoria segurança trabalho | COMM | MID | M | MÉDIA | P1 | `/servicos/seguranca-trabalho/` | Q comercial directa. |
| serviços externos segurança trabalho | COMM | MID | B | MÉDIA | P2 | `/servicos/seguranca-trabalho/` | B2B vocabulário. |
| empresa segurança no trabalho | COMM | MID | M | ALTA | P1 | `/servicos/seguranca-trabalho/` | Comercial principal. |
| serviços segurança trabalho preço | COMM | MID | B | MÉDIA | P2 | `/servicos/seguranca-trabalho/` | Mesma regra: dar faixa. |
| contratar técnico segurança | TRANS | BOT | B | BAIXA | P2 | `/proposta/` | Sinal de necessidade imediata. |

---

## Cluster 3 — Higiene e Segurança Alimentar (HACCP)

**Target hub:** `/servicos/higiene-seguranca-alimentar/`
**Pillar:** `/recursos/guias/haccp-restauracao/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| HACCP | INFO+COMM | TOP/MID | A | ALTA | P1 | `/servicos/higiene-seguranca-alimentar/` | Head term — restauração toda procura. |
| o que é HACCP | INFO | TOP | M | MÉDIA | P2 | pillar HACCP | Snippet target. |
| princípios HACCP | INFO | TOP | M | MÉDIA | P2 | pillar HACCP | Os 7 princípios — resposta estruturada. |
| HACCP restauração | INFO+COMM | TOP/MID | M | MÉDIA | P1 | pillar + serviço | Vertical principal. |
| HACCP padaria | INFO+COMM | TOP/MID | B | BAIXA | P3 | pillar (secção) | Long-tail vertical. |
| HACCP escolar | INFO+COMM | MID | B | BAIXA | P3 | pillar (secção) | Cantinas escolares — verticais. |
| manual HACCP | INFO+COMM | MID | M | MÉDIA | P2 | secção serviço | Forte intenção pré-comercial. |
| manual HACCP modelo | INFO | TOP | M | BAIXA | P3 | secção serviço | Pode oferecer template gratuito como lead magnet. |
| ASAE inspeção | INFO | TOP | M | ALTA | P3 | secção pillar | Pânico/curiosidade → leva a serviço. |
| regulamento 852/2004 | INFO | TOP | B | ALTA | P3 | pillar | Vocabulário técnico. |
| segurança alimentar restaurante | COMM | MID | M | MÉDIA | P2 | `/servicos/higiene-seguranca-alimentar/` | Comercial directa. |
| consultoria HACCP | COMM | MID | M | MÉDIA | P1 | `/servicos/higiene-seguranca-alimentar/` | Q comercial principal. |
| implementação HACCP preço | COMM | MID | B | MÉDIA | P2 | `/servicos/higiene-seguranca-alimentar/` | Dar faixa indicativa. |
| empresa HACCP | COMM | MID | B | MÉDIA | P2 | `/servicos/higiene-seguranca-alimentar/` | Lookup B2B. |

---

## Cluster 4 — Ambiente

**Target hub:** `/servicos/ambiente/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| gestão ambiental empresa | INFO+COMM | TOP/MID | M | MÉDIA | P2 | `/servicos/ambiente/` | Termo de compliance. |
| ISO 14001 | INFO | TOP | M | ALTA | P3 | secção pillar | Pillar dedicado se houver tempo. |
| consultoria ambiental | COMM | MID | M | ALTA | P2 | `/servicos/ambiente/` | Comercial. |
| licenciamento ambiental | INFO+COMM | TOP/MID | M | ALTA | P3 | `/servicos/ambiente/` | Verticais industriais. |
| APA | NAV | — | A | ALTA | P5 | — | Brand público — não capturar. |
| responsabilidade ambiental empresa | INFO | TOP | B | MÉDIA | P3 | secção pillar | Compliance. |
| resíduos perigosos empresa | INFO | TOP | B | MÉDIA | P3 | secção | Vertical. |

---

## Cluster 5 — Perícias Médico-Legais

**Target hub:** `/servicos/pericias-medico-legais/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| perícia médico-legal | INFO+COMM | TOP/MID | M | ALTA | P2 | `/servicos/pericias-medico-legais/` | Head term. |
| acidente de trabalho perícia | INFO+COMM | MID | M | MÉDIA | P2 | pillar acidente trabalho | Cruza com pillar. |
| junta médica acidente trabalho | INFO | TOP | M | MÉDIA | P3 | pillar | Compliance Q. |
| participação acidente trabalho | INFO | TOP | M | MÉDIA | P2 | pillar `/recursos/guias/acidente-trabalho-procedimento/` | Prazos, formulário. |
| prazo participação acidente trabalho | INFO | TOP | B | BAIXA | P2 | secção pillar | Snippet directo. |
| código do trabalho acidente | INFO | TOP | M | ALTA | P3 | pillar | Concorre com Diário Repúb. |

---

## Cluster 6 — Exames Serológicos

**Target hub:** `/servicos/exames-serologicos/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| exames serológicos | INFO+COMM | TOP/MID | M | MÉDIA | P2 | `/servicos/exames-serologicos/` | Termo técnico. |
| análises serológicas | INFO | TOP | M | MÉDIA | P3 | `/servicos/exames-serologicos/` | Sinónimo. |
| serologia o que é | INFO | TOP | M | MÉDIA | P3 | secção página | Snippet. |
| testes serológicos empresa | COMM | MID | B | BAIXA | P2 | `/servicos/exames-serologicos/` | B2B vertical. |
| serologia covid empresa | COMM | MID | MB | BAIXA | P4 | — | Volume caiu pós-pandemia. |

---

## Cluster 7 — Exames Seguradoras

**Target hub:** `/servicos/exames-seguradoras/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| exame médico seguradora | INFO+COMM | TOP/MID | M | MÉDIA | P3 | `/servicos/exames-seguradoras/` | Pessoa singular: pode não ser audiência B2B; rever. |
| exames médicos seguro vida | INFO | TOP | M | MÉDIA | P3 | `/servicos/exames-seguradoras/` | Pessoa singular. |
| exame médico empresa seguradora | COMM | MID | B | BAIXA | P2 | `/servicos/exames-seguradoras/` | Mais B2B. |

**Nota:** este serviço tem audiência mista (B2C + B2B). Página deve clarificar logo no H1 a quem se dirige.

---

## Cluster 8 — Certificação (ISO, etc.)

**Target hub:** `/servicos/certificacao/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| certificação ISO 9001 | INFO+COMM | TOP/MID | M | ALTA | P2 | `/servicos/certificacao/` | Concorre com SGS, Bureau Veritas. |
| certificação ISO 45001 | INFO+COMM | TOP/MID | M | ALTA | P2 | `/servicos/certificacao/` + pillar ISO 45001 | Sinergia HSST. |
| consultoria ISO | COMM | MID | M | ALTA | P2 | `/servicos/certificacao/` | Comercial. |
| ajuda implementação ISO | COMM | MID | B | MÉDIA | P3 | `/servicos/certificacao/` | Sub-pergunta. |
| ISO 45001 vs OHSAS 18001 | INFO | TOP | B | BAIXA | P3 | pillar ISO 45001 | Migração; snippet target. |

---

## Cluster 9 — Formação contínua obrigatória (35h legado → 40h atual)

**Target hub:** `/formacao/` + `/recursos/guias/formacao-obrigatoria-40-horas/`

> ⚠️ **Nota legal — atualização 2026-05-20.** A Lei 93/2019 alterou o Art.º 131.º do Código do Trabalho: o mínimo de formação contínua obrigatória passou de **35 para 40 horas anuais** por trabalhador. A AIO do Google já corrige automaticamente a query "35 horas" para "40 horas". Decisão registada em `_living/DECISION_LOG.md` 2026-05-20.
>
> **Política para este cluster:**
> 1. Manter slug/título da pillar com "40 horas" como referencial atual.
> 2. Manter a query "35 horas" trackeada por volume residual e por ser a forma popular.
> 3. Cada peça de conteúdo deste cluster abre com correção 35→40 explícita + citação Lei 93/2019 + Nota Técnica 9 da ACT.
> 4. Conteúdo "35 horas" antigo deve ser auditado (404, 301 ou refresh) — ver `_living/BACKLOG.md` cluster `[Technical blocker]`.

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| formação 35 horas | INFO+TRANS | TOP/BOT | A | ALTA | P1 | pillar 40h (com nota correção) | Head term legado, ainda popular. Pillar tem de corrigir para 40h logo no H2 inicial. |
| formação 35 horas obrigatória | INFO | TOP | A | ALTA | P1 | pillar 40h | "Sou obrigado?" — Q crítica de RH. AIO corrige automaticamente. |
| formação 35 horas online | TRANS | BOT | A | ALTA | P1 | `/formacao/modalidades/online/` | Forte intenção compra; head term comercial. |
| formação 35 horas preço | TRANS | BOT | M | MÉDIA | P1 | `/formacao/catalogo/` | Dar preço. |
| formação 35 horas DGERT | TRANS | BOT | M | MÉDIA | P2 | `/formacao/dgert/` | Validação certificação. |
| **formação 40 horas obrigatória** | INFO | TOP | M | MÉDIA | P1 | pillar 40h | **Variante atualizada.** Volume previsivelmente menor que "35h" mas crescerá. |
| **formação contínua 40 horas** | INFO | TOP | B | MÉDIA | P2 | pillar 40h | Variante formal. |
| **Lei 93/2019 formação** | INFO | TOP | B | BAIXA | P2 | pillar 40h (secção legal) | Q jurídica precisa. Snippet target. |
| **Art.º 131.º Código do Trabalho** | INFO | TOP | B | BAIXA | P3 | pillar 40h (secção legal) | Q jurídica precisa. |
| formação contínua trabalhadores | INFO | TOP | M | MÉDIA | P3 | pillar 40h | Sinónimo formal. |
| formação 35 horas quem precisa | INFO | TOP | M | BAIXA | P2 | pillar 40h (secção) | Snippet. |
| isenção formação 35 horas | INFO | TOP | M | BAIXA | P3 | pillar 40h (secção) | Long-tail compliance. |
| **40 horas formação obrigatória empresas** | INFO+COMM | TOP/MID | B | MÉDIA | P2 | pillar 40h | Q empresa-side (RH). |
| **coima incumprimento formação obrigatória** | INFO | TOP | B | BAIXA | P3 | pillar 40h (secção consequências) | Long-tail compliance/risco. |

---

## Cluster 10 — CAP / TST / TSST

**Target:** `/formacao/{slug}/` para cada CAP + pillar carreira

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| CAP segurança trabalho | INFO+TRANS | TOP/BOT | A | ALTA | P1 | página curso CAP TSST | Concorrência alta (escolas profissionais, IEFP). |
| CAP TST | INFO+TRANS | TOP/BOT | M | ALTA | P1 | página curso CAP TST | Aspirante a TST. |
| CAP TSST | INFO+TRANS | TOP/BOT | M | MÉDIA | P1 | página curso CAP TSST | Aspirante a TSST. |
| CAP segurança trabalho online | TRANS | BOT | M | MÉDIA | P1 | página curso (online) | Forte intenção. |
| CAP TST preço | TRANS | BOT | M | MÉDIA | P1 | página curso | Dar preço. |
| curso técnico superior segurança trabalho | INFO+TRANS | TOP/BOT | M | ALTA | P2 | página curso TSST | Sinónimo. |
| CAP segurança trabalho duração | INFO | TOP | B | BAIXA | P2 | secção página curso | Snippet. |

---

## Cluster 11 — Formação HACCP

**Target:** `/formacao/{slug}/` (curso HACCP) + cruza com `/recursos/guias/haccp-restauracao/`

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| formação HACCP | INFO+TRANS | TOP/BOT | A | ALTA | P1 | página curso HACCP | Head term formação. |
| curso HACCP online | TRANS | BOT | M | MÉDIA | P1 | página curso HACCP online | Modalidade preferida. |
| formação higiene segurança alimentar | INFO+TRANS | TOP/BOT | M | MÉDIA | P1 | página curso | Sinónimo formal. |
| formação manipulador alimentos | INFO+TRANS | TOP/BOT | M | MÉDIA | P2 | página curso | Termo público comum. |
| curso HACCP preço | TRANS | BOT | M | MÉDIA | P1 | página curso | Dar preço. |
| curso HACCP DGERT | TRANS | BOT | B | BAIXA | P2 | página curso | Validação. |

---

## Cluster 12 — Outras formações DGERT

**Target:** `/formacao/dgert/` + páginas curso específicas

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| formação DGERT | INFO | TOP | M | MÉDIA | P2 | `/formacao/dgert/` | Validação. |
| formação DGERT online | TRANS | BOT | M | MÉDIA | P2 | `/formacao/dgert/` + catálogo | Conversão. |
| entidade formadora DGERT | INFO | TOP | M | MÉDIA | P3 | `/formacao/dgert/` | Lookup credencial. |
| formação certificada online | INFO+TRANS | TOP/BOT | M | ALTA | P3 | `/formacao/` | Genérico, ambíguo. |

---

## Cluster 13 — Brand (Previmed)

**Target:** múltiplas — depende da query

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| previmed | NAV | — | A (brand) | BAIXA | P1 | `/` | Tem de ser sempre #1. |
| previmed.pt | NAV | — | M | BAIXA | P1 | `/` | Brand+TLD. |
| previmed contacto | NAV | — | M | BAIXA | P1 | `/contactos/` | Direct. |
| previmed pedido proposta | NAV+TRANS | BOT | B | BAIXA | P1 | `/proposta/` | Direct. |
| previmed avaliações | NAV+INFO | — | B | BAIXA | P2 | `/sobre/` ou página dedicada | Reputação. |
| previmed lisboa | NAV+LOCAL | — | B | BAIXA | P2 | `/cobertura/` | Brand + geo. |
| previmed porto | NAV+LOCAL | — | B | BAIXA | P2 | `/cobertura/` | Brand + geo. |
| previmed clínicas | NAV | — | B | BAIXA | P2 | `/cobertura/` | Rede. |
| previmed recrutamento | NAV | — | B | BAIXA | P3 | `/recrutamento/` | Mantém. |

---

## Cluster 14 — Trabalhador (suporte/portal)

**Target:** `portal.previmed.pt` ou `/portal-trabalhador/` (decisão Fase 4)

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Target | Notas |
|---|---|---|---|---|---|---|---|
| previmed portal trabalhador | NAV | — | M | BAIXA | P1 | landing portal | Resposta imediata. |
| previmed login | NAV | — | M | BAIXA | P1 | landing portal | — |
| previmed marcação | NAV | — | B | BAIXA | P2 | landing portal (FAQ) | Suporte. |
| previmed resultados | NAV | — | B | BAIXA | P2 | landing portal | Suporte. |
| esqueci password previmed | NAV | — | MB | BAIXA | P2 | landing portal (FAQ recuperação) | Friction zero. |
| previmed clínica perto | NAV+LOCAL | — | B | BAIXA | P2 | `/cobertura/` | Locator. |
| previmed convocatória | NAV | — | MB | BAIXA | P3 | landing portal (FAQ) | Suporte. |

---

## Cluster 15 — Pillars informacionais legais

**Target:** `/recursos/guias/{slug}/`

| Pillar | Queries-âncora | Prio |
|---|---|---|
| Lei 102/2009 explicada | lei 102/2009, lei medicina trabalho, obrigações empregador medicina trabalho, código trabalho saúde | P1 |
| HACCP para restauração | HACCP restauração, o que é HACCP, princípios HACCP, ASAE inspeção restaurante | P1 |
| Formação 35h obrigatória | formação 35 horas obrigatória, isenção formação 35h, formação contínua trabalhadores | P1 |
| Como escolher MT | como escolher empresa medicina do trabalho, melhor empresa medicina trabalho, fornecedor HSST critérios | P1 |
| Acidente de trabalho: procedimento | participação acidente trabalho, prazo participação, junta médica, perícia médico-legal | P2 |
| ISO 45001 vs OHSAS 18001 | ISO 45001 implementação, ISO 45001 vs OHSAS, certificação ISO 45001 portugal | P2 |

Cada pillar dá origem a **3–8 sub-queries snippet-friendly** que vivem como secções H2/H3 da página, com `FAQPage` schema quando aplicável.

---

## Cluster 16 — Comparativos / "Como escolher"

**Target:** pillar dedicado `/recursos/guias/escolher-medicina-do-trabalho/` + outros

| Query | Intenção | Funil | Vol. est. | Difi. | Prio | Notas |
|---|---|---|---|---|---|---|
| melhor empresa medicina do trabalho | COMM | MID | M | BAIXA | P1 | Ninguém ranqueia bem. **Oportunidade**. |
| medicina trabalho vs seguro acidentes | INFO | TOP | B | BAIXA | P2 | Confusão comum em PMEs. |
| fornecedor HSST critérios | COMM | MID | B | BAIXA | P2 | B2B compras. |
| empresa medicina trabalho recomendada | COMM | MID | B | BAIXA | P3 | Reputação. |

---

## Canibalização — watch list

Queries onde duas páginas potenciais competem. Resolver com title/H1 distintos e internal links direcionais.

| Risco | Páginas em conflito | Resolução |
|---|---|---|
| "medicina do trabalho" | `/servicos/medicina-trabalho/` vs pillar `/recursos/guias/lei-102-2009-medicina-trabalho/` | Serviço é comercial; pillar é "Lei 102/2009 explicada" — title começa por "Lei 102/2009". |
| "formação 35 horas" | `/formacao/catalogo/` vs pillar `/recursos/guias/formacao-35-horas-obrigatoria/` | Pillar é "obrigatória explicada"; catálogo é "inscrição/compra". Title e H1 explicitam. |
| "HACCP" | `/servicos/higiene-seguranca-alimentar/` vs `/formacao/curso-haccp/` vs pillar `/recursos/guias/haccp-restauracao/` | Serviço = consultoria. Curso = formação. Pillar = guia. Title de cada explicita. |
| "previmed formação" | `/formacao/` vs `elearning.previmed.pt` | `/formacao/` é descoberta + inscrição. Subdomínio é plataforma autenticada (noindex áreas internas). |
| "CAP segurança" | múltiplas (CAP TST vs CAP TSST) | Páginas separadas por curso. Hub `/formacao/cap/` agrega. |

---

## Concorrência qualitativa (a validar Fase 2)

**Concorrentes orgânicos prováveis** (a investigar formalmente no Lote 1.4):

| Tipo | Exemplos a verificar | Onde dominam |
|---|---|---|
| Concorrentes B2B HSST nacionais | Medjobs, CMD, Medisport, Medicar, Iberogestão | Queries comerciais ("empresa medicina trabalho") |
| Institucionais | ACT, DGS, DGERT, AEP, APSEI | Queries informacionais legais |
| Escolas profissionais / IEFP | CITEFORMA, INETESE, ISLA | Queries CAP/TST formação |
| Marketplaces de formação | Cursos Online, EuroSafety, Be Safe | Queries "curso HACCP online" |
| Generalistas certificação | SGS, Bureau Veritas, APCER, TÜV | Queries ISO 9001/45001 |

**Tese estratégica**: institucionais dominam informacional mas com má UX/conversão. Previmed pode ganhar long-tail informacional com **clareza prática + CTA contextual** → drena tráfego para conversão. Análise detalhada no Lote 1.4.

---

## Mapeamento keyword → página (síntese)

| Página | Keywords-âncora (Top 3) | Keywords-suporte |
|---|---|---|
| `/` | previmed, empresa HSST, segurança e saúde no trabalho | (brand + institucional) |
| `/servicos/` | serviços HSST, soluções segurança trabalho, fornecedor HSST | hub navegacional |
| `/servicos/medicina-trabalho/` | medicina do trabalho, empresa medicina do trabalho, contratar medicina trabalho | preço, online, rede |
| `/servicos/seguranca-trabalho/` | segurança no trabalho, consultoria segurança trabalho, técnico segurança | avaliação riscos |
| `/servicos/higiene-seguranca-alimentar/` | HACCP, consultoria HACCP, segurança alimentar restaurante | manual, implementação |
| `/servicos/ambiente/` | gestão ambiental, consultoria ambiental | licenciamento, ISO 14001 |
| `/servicos/pericias-medico-legais/` | perícia médico-legal, perícia acidente trabalho | junta médica |
| `/servicos/exames-serologicos/` | exames serológicos, análises serológicas | empresa |
| `/servicos/exames-seguradoras/` | exame médico seguradora | seguro vida |
| `/servicos/certificacao/` | certificação ISO 9001, consultoria ISO | ISO 45001, ISO 14001 |
| `/formacao/` | formação HSST, formação certificada, DGERT | catálogo |
| `/formacao/dgert/` | formação DGERT, entidade formadora DGERT | online |
| `/formacao/cap/` | CAP segurança trabalho, CAP TST, CAP TSST | preço, online |
| `/formacao/curso-haccp/` | curso HACCP, formação HACCP, manipulador alimentos | online, DGERT |
| `/formacao/35-horas/` | formação 35 horas (inscrição/compra) | online, preço |
| `/cobertura/` | rede clínicas medicina trabalho, cobertura nacional HSST | locator, distritos |
| `/sobre/` | quem somos, certificações Previmed | ACT, DGS, ISO 9001 |
| `/recursos/guias/lei-102-2009-medicina-trabalho/` | lei 102/2009, obrigações empregador medicina trabalho | pillar |
| `/recursos/guias/haccp-restauracao/` | HACCP restauração, princípios HACCP | pillar |
| `/recursos/guias/formacao-35-horas-obrigatoria/` | formação 35 horas obrigatória | pillar |
| `/recursos/guias/escolher-medicina-do-trabalho/` | como escolher empresa medicina trabalho, melhor empresa medicina trabalho | pillar |
| `/recursos/guias/acidente-trabalho-procedimento/` | participação acidente trabalho, prazo acidente trabalho | pillar |
| `/recursos/guias/iso-45001-seguranca/` | ISO 45001, ISO 45001 vs OHSAS | pillar |

---

## Queries a monitorizar quando GSC estiver activo (Fase 2)

Lista mínima de queries a verificar nos primeiros 30 dias pós-GSC:

1. previmed *(brand)*
2. medicina do trabalho *(head)*
3. segurança no trabalho *(head)*
4. HACCP *(head)*
5. formação 35 horas *(head)*
6. lei 102/2009 *(informacional crítica)*
7. CAP segurança trabalho *(head formação)*
8. empresa medicina do trabalho *(comercial primária)*
9. preço medicina do trabalho *(comercial directa)*
10. como escolher empresa medicina trabalho *(oportunidade pillar)*
11. previmed portal trabalhador *(brand suporte)*
12. previmed e-learning *(brand sub-negócio)*

Métricas a registar por query: impressões, CTR, posição média, página alvo real (verificar se é a que esperamos). Comparação mensal.

---

## Próximo lote

**Lote 1.4 — Análise de concorrência orgânica** vai:
- identificar 5–10 concorrentes reais via SERP em queries-âncora (carece de ferramenta browser/search ou pesquisa manual);
- mapear padrões SERP por query-tipo;
- identificar lacunas concretas onde Previmed pode ganhar;
- validar/ajustar as estimativas de dificuldade deste documento.

**Limitação importante para 1.4**: sem MCP browser ou ferramenta SERP, vou precisar que faças tu as pesquisas e me passes screenshots/listas dos top 10 — ou autorizas instalar um MCP de search (DataForSEO read-only seria a opção mais segura) na transição para Fase 2.
