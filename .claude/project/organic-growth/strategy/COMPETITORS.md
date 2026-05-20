# Strategy — Concorrência Orgânica

> Lote 1.4 da Fase 1.
> Última atualização: 2026-05-20.
> Base: 12 SERPs capturadas via Playwright MCP em Google.pt (pws=0, hl=pt-PT, gl=PT, localização detectada: Porto Salvo/Oeiras).
> Snapshots: `.playwright-mcp/page-2026-05-20T*.yml`

---

## Metodologia

- **Fonte:** 12 queries-âncora de `strategy/KEYWORDS.md` § "Queries a monitorizar quando GSC estiver activo".
- **Extração:** `mcp__playwright__browser_evaluate` em cada SERP — top ~10 orgânicos + SERP features (FS, PAA, KP, local pack, AIO, ads).
- **Limitações:**
  - Captura única (snapshot 2026-05-20), sem mediana temporal.
  - Personalização: `pws=0` minimiza mas não elimina. Geo=Porto Salvo afeta local pack.
  - Consent dialog do Google overlaia mas não bloqueia SERP renderizada por baixo. PAA/Related searches por vezes não detectados (sob dialog) — não é evidência de ausência.
  - AI Overview presente em **12/12 queries** mas só "link Modo IA" detectado, não expandido. Provável que AIO genuíno surja em queries head.

---

## Universo competitivo identificado

5 categorias por padrão de presença SERP. Lista não exaustiva — só players que apareceram top 10 em ≥1 query.

### 1. Empresas SST diretas (concorrentes nucleares)

| Empresa | URL | Presença SERP observada | Posicionamento | Sinais |
|---|---|---|---|---|
| **Centralmed** | centralmed.pt | medicina trabalho #7, empresa medicina #1, HACCP #10, como escolher #1, local pack #1, ads topo+fundo | Líder de mercado em SEO+SEM+GMB. Cobre desde info-content até serviço. | Blog robusto, ads constantes, GMB nacional, sub-brand "Sucursal Oeiras", páginas dedicadas por área. |
| **Preveris** | preveris.pt | empresa medicina #4, blog Sepri-style | Claim "maior rede nacional de clínicas autorizadas DGS". | Escala nacional declarada. |
| **Preslaboral** | preslaboral.pt | medicina trabalho #6, empresa medicina #3, preço #10 | Regional forte (Lisboa, Margem Sul, Évora, Beja) + unidade móvel. | Especialização regional + diferenciação serviço móvel. |
| **Medicisforma** | medicisforma.pt | empresa medicina #2, ads em "medicina trabalho" | Certificada DGERT — combina SST + formação + segurança alimentar + pragas. | Multi-serviço integrado. |
| **SEPRI** | sepri.pt, empresassaudaveis.sepri.pt | medicina trabalho #3, ads topo em head queries, blog "como escolher" #3 | "Empresa certificada DGS e ACT com + 30 anos." | Blog SEO ativo, ads, subdomínio dedicado. |
| **Ecosaude** | ecosaude.pt | medicina trabalho #6 | Empresa SST padrão. | Página de serviço otimizada para FAQ. |
| **Mesetrab** | mesetrab.pt | empresa medicina #5, local pack #1 | Regional Queluz. | Forte GMB local. |
| **STA / Medipreve** | sta.pt | empresa medicina #8 | Grupo multi-marca (STA+Medipreve), 4 áreas. | Diversificação. |
| **Seepmed** | seepmed.pt | ads em "medicina trabalho", blog "como escolher" #7 | Sintra/Linhó. Investe em ads + content. | Combina ads + blog. |
| **Clínica Polima** | clinicapolima.pt | empresa medicina #6 | Clínica especializada. | — |
| **Clínica Forjaz** | clinicaforjaz.com | empresa medicina #10 | Clínica. | — |
| **PTMedical** | ptmedical.pt | preço medicina #6 | Posiciona-se em "Preço Competitivo". | Diferenciação por preço (sem expor número). |
| **Ceniude** | ceniude.pt | preço medicina #5 | Tem "plataforma on-line" para preços. | Tooling público. |
| **GPmedicos** | gpmedicos.com | preço medicina #1 | **Expõe preços públicos** (45€ consulta). | Única empresa B2C com transparência total. |
| **UACS** (Câmara Sintra Comércio) | uacs.pt | preço medicina #2 | Associação — preços diferenciados associado/não associado. | Modelo associativo. |

### 2. Centros hospitalares (concorrentes por força de marca)

| Empresa | Presença SERP | Notas |
|---|---|---|
| **Hospital da Luz** | medicina trabalho FS, preço #3 | **Featured snippet** em head term. Marca dominante. |
| **Lusíadas** | preço #4 | Listagem genérica de especialidades. Não otimizada SST. |

### 3. Empresas de formação (concorrentes do sub-negócio)

Cluster "CAP segurança trabalho" tem 7+ academias em top 10:

| Empresa | URL | Posição CAP |
|---|---|---|
| Traininghouse | traininghouse.pt | #2 |
| ForSeguro | forseguro.pt | #5 |
| Instituto CRIAP | institutocriap.com | #6 |
| Triformis Técnica | triformistecnica.pt | #7 |
| Academia Zona Verde | academiazonaverde.pt | #8 |
| ConsultUA | consultua.pt | #9 |
| ProInstitute | proinstitute.pt | #10 |
| RFA Academy | shop.rfaacademy.com | #4 |

### 4. Info-content sites (atraem awareness, não convertem em SST)

| Site | Tipo | Onde aparecem |
|---|---|---|
| Santander Salto | Blog corporativo | segurança trabalho #3, como escolher #5 |
| Doutor Finanças | Blog finanças | formação 35h #6, como escolher #9 |
| Factorial HR | SaaS HR + blog | preço #9, como escolher #4 |
| Twind | Blog jurídico/SST | lei 102/2009 #7 — única versão "explicada" da lei |
| Generali Tranquilidade | Blog seguradora | formação 35h #5 |
| SGS, APCER | Certificação | HACCP #3, #7 |
| AHRESP | Sectorial restauração | HACCP #5 |
| Kaizen, Infraspeak | Consultoria/SaaS | HACCP #6, #9 |

### 5. Institucionais (não-competidores comerciais; relevantes para autoridade)

- **ACT** (portal.act.gov.pt), **DGAV**, **ASAE**, **gov.pt**, **DGERT**, **DGEEC**, **DRE/Diário da República**, **PGD Lisboa**
- **Ordem dos Médicos**, **SPMT** (Sociedade Portuguesa de Medicina do Trabalho)
- **ULisboa**, **IPVC** (universidades)
- **ILO**, **OSHA-EU**
- **CGTP, FIEQUIMETAL, Stop-Sindicato** (sindicatos)

Estes não competem por leads B2B mas dominam queries informacionais/legais — sinal de que para entrar nessas SERPs Previmed precisa de **autoridade citacional** (linkar para eles + ser linkado por eles).

---

## Padrões SERP por cluster

| Cluster | Ads | FS | PAA | KP | Local pack | AIO | Dominância orgânica |
|---|---|---|---|---|---|---|---|
| Head SST genérica ("medicina do trabalho", "segurança no trabalho") | Sim (3) / Não | Sim (head 1) / Não | Sim / — | Sim / — | Sim (2 packs) / Não | ✓ | Fragmentada: hospitais + institucionais + 4-5 SST |
| Legal ("lei 102/2009", "formação 35h") | Não | Não | Detectado fragmentado | Não | Não | ✓ | DRE/PGD/gov dominam; sindicatos + blogs jurídicos completam |
| Norma técnica ("HACCP") | Não | Não | — | Não | Não | ✓ | Reguladores (ASAE/DGAV) + certificadoras (SGS/APCER) |
| Formação (CAP, "formação 35 horas") | Não | Não | — | Não | Não | ✓ | 7+ academias em CAP; legal/sindical em "35 horas" |
| Comercial primária ("empresa medicina trabalho") | Não | Não | — | Não | 2 packs | ✓ | 100% empresas SST. **Previmed #9.** |
| Comercial preço ("preço medicina trabalho") | Não | Não | — | Não | Não | ✓ | Mix hospitalar + SST + blog HR; só 2 com preço público |
| Pillar oportunidade ("como escolher empresa MT") | Não | Não | — | Não | Não | ✓ | Centralmed/Sepri/Seepmed lideram via blog. **Previmed #10** com página de serviço. |
| Brand ("previmed", "previmed e-learning", "previmed portal trabalhador") | Não | Não | — | Sim (sitelinks) | Não | ✓ | Previmed domina 7-9 de 10. |

**Observações transversais:**

- **AI Overview ativo em 12/12 queries.** Sinal massivo de Google PT 2026. Conteúdo precisa de ser citável (factos, listas, definições, schema).
- **Local pack só dispara em queries com intenção comercial geográfica explícita ou implícita.** Centralmed domina o pack na zona Lisboa. Mesetrab no Queluz.
- **Ads escassos.** Só 3 das 12 queries têm anúncios. Mercado SST em PT não é mass-PPC.
- **Featured snippet só em head term mais geral.** Hospital da Luz tem essa posição privilegiada.
- **PAA aparenta estar sub-detectado** (consent dialog overlaia). Em "medicina do trabalho" capturamos 4 perguntas: "Em que consiste…", "Quem é obrigado…", "Quanto custa…", "O que se faz…".

---

## Posicionamento atual da Previmed (baseline)

| Query | Posição Previmed observada | URL alvo | Comentário |
|---|---|---|---|
| previmed | #1 (homepage) | previmed.pt/ | Brand defendida com sitelinks. |
| previmed e-learning | #1 | previmed.pt/e-learning/ | OK. LMS real em `previmed-academia.careview.pt` (white-label, sem SEO). |
| previmed portal trabalhador | — | nenhuma URL dedicada | **GAP UX/SEO:** trabalhadores caem na homepage; produto existe mas sem landing pública. |
| empresa medicina do trabalho | **#9** | previmed.pt/saude-no-trabalho/ | Comercial primária crítica; já no top 10 mas com página genérica. |
| como escolher empresa medicina trabalho | **#10** | previmed.pt/saude-no-trabalho/ | Página de serviço a aparecer em query de blog. Quick win se criar artigo dedicado. |
| medicina do trabalho | fora do top 10 | — | Head term: Hospital da Luz + ULisboa + Sepri + Ordem + SPMT dominam. |
| segurança no trabalho | fora do top 10 | — | Domínio governamental/institucional puro. |
| HACCP | fora do top 10 | — | Centralmed entrou via blog; Previmed sem conteúdo. |
| formação 35 horas | fora do top 10 | — | Domínio sindical/legal. |
| lei 102/2009 | fora do top 10 | — | Texto oficial domina; Twind é a única "explicada". |
| CAP segurança trabalho | fora do top 10 | — | 7+ academias dominam. |
| preço medicina do trabalho | fora do top 10 | — | Hospitais + 2 com preços públicos dominam. |

**Resumo:** Previmed defende a brand bem; entra no top 10 em **2 de 9 queries não-brand** (empresa MT, como escolher) — ambas com a mesma URL `/saude-no-trabalho/`. Tem **zero presença** em queries informacionais, legais, de formação, de HACCP e de preço.

---

## Lacunas concretas (oportunidades priorizadas)

Critério: tamanho da intent × facilidade de ataque × distância à oferta Previmed.

### Prioridade 1 — Quick wins (entrar no top 5 em <90 dias)

**L1. Blog "Como escolher uma empresa de medicina do trabalho"**
- *Estado SERP:* Centralmed #1, LinkedIn #2, Sepri #3, Seepmed #7. Previmed #10 com página de serviço.
- *Ataque:* Artigo pillar 1500-2000 palavras com critérios reais (certificações ACT/DGS, cobertura, transparência de preço, plataforma trabalhador). Distinguir Previmed por critério: **"transparência de preço"** se publicar tabela.
- *Risco:* baixo.

**L2. Página dedicada "Portal do Trabalhador"**
- *Estado SERP:* `previmed portal trabalhador` mostra homepage Previmed; **não existe landing**. Trabalhadores procuram e não encontram URL clara.
- *Ataque:* Criar `previmed.pt/portal-trabalhador/` com explicação, screenshots, FAQ, link claro para login. Resolve query brand + capta `portal trabalhador medicina` long-tails.
- *Risco:* nenhum.

**L3. Tabela/simulador de preço B2B**
- *Estado SERP:* só GPmedicos (B2C clínica) e UACS (associação) expõem preço. Centralmed, Preslaboral, Ecosaude pedem proposta.
- *Ataque:* página `previmed.pt/precos-medicina-do-trabalho/` com tabela em função de nº trabalhadores + tipo serviço. Mesmo intervalos (ex: "20-50€ por trabalhador/ano") já é diferenciador massivo.
- *Risco:* comercial — abrir preço pode reduzir margem em negociação. Decisão de negócio.

### Prioridade 2 — Hubs estruturais (3-6 meses)

**L4. Pillar "Guia Lei 102/2009 explicada"**
- *Estado SERP:* DRE/PGD em texto bruto, Twind como única "explicada" (#7), CGTP/sindicatos completam. Nenhuma empresa SST com pillar.
- *Ataque:* hub `previmed.pt/recursos/lei-102-2009/` com:
  - Resumo executivo da lei.
  - Tabela obrigações por dimensão de empresa.
  - Calculadora de periodicidade de exames (ex: input: idade trabalhador + tipo de risco → output: periodicidade).
  - Multas e prazos.
  - FAQ por persona (empregador / trabalhador).
- *Risco:* moderado — precisa validação jurídica antes de publicar.

**L5. Hub "Formação obrigatória 35h (ou 40h?)"**
- *Estado SERP:* só blogs (Infeira, Doutor Finanças, Generali, Alento) e ACT pdf. Confusão 35 vs 40h pós Lei 93/2019 é a "dor" central.
- *Ataque:* página clarificadora + lista de cursos Previmed elegíveis para essas horas. Conecta-se ao sub-negócio Previforma.
- *Risco:* baixo.

**L6. Hub HACCP por setor**
- *Estado SERP:* reguladores (ASAE) + certificadoras (SGS, APCER) + Kaizen/Infraspeak. Centralmed entrou via blog em #10.
- *Ataque:* `previmed.pt/recursos/haccp-restauracao/`, `/haccp-hoteis/`, `/haccp-distribuicao/`. Verticalização por setor é o diferenciador.
- *Risco:* baixo.

### Prioridade 3 — Defensivo / médio prazo

**L7. Reforço GMB nacional.** Centralmed tem múltiplos GMB; Previmed apenas Lisboa visível. Para queries "medicina trabalho [cidade]" Previmed perde por GMB.

**L8. Identidade SEO para "Previforma".** Sub-brand existe (vídeos FB, perfis sociais) mas sem presença orgânica autónoma — possível diluição de autoridade.

**L9. Linkar com SPMT, Ordem dos Médicos, ACT no conteúdo.** Citation building para passar de "empresa SST mais" a "autoridade citável".

---

## Ângulos de diferenciação possíveis (vs concorrentes diretos)

1. **Transparência de preço** — ninguém em B2B SST PT expõe preço público. Risco comercial, ganho massivo de qualified leads.
2. **Profundidade legal/regulatória** — Sepri faz blog mas thin. Centralmed faz markeitng-light. Espaço para Previmed ser a "fonte" — tipo Twind mas com autoridade de SST a sério.
3. **Verticalização por setor** — Centralmed/Preveris/Sepri são generalistas. Previmed pode posicionar-se em 2-3 setores (ex: restauração/hotelaria, indústria, escritórios) com hub vertical.
4. **Geo nacional via Preveris-style claim** — sem inflar, mostrar mapa de clínicas + cobertura real (vs Preveris que reclama "maior rede").
5. **Integração Previforma (formação + MT)** — única forma de juntar formação 35h + medicina do trabalho num pacote vendável B2B. Centralmed tem ads mas não combina.

---

## Limitações & próximos passos

**Limitações desta análise:**
- Captura única, não temporal. SERPs mudam (especialmente local pack).
- Sem dados de tráfego real por concorrente (precisa Ahrefs/Semrush).
- AI Overview detectado mas não expandido — não sabemos que fontes Google cita lá.
- 11 das 12 queries são de `strategy/KEYWORDS.md`; não cobre long-tail.

**Próximos lotes:**
- **Lote 1.5 (sugestão):** definição de Quick Wins concretos (L1+L2+L3 acima) com briefs de conteúdo + arquitectura URL final.
- **Fase 2 (pós-GSC):** re-validar volumes, recalibrar dificuldade, expandir captura para top 20-30 concorrentes via Ahrefs.
- **Crítico para AIO:** auditar como Google cita Previmed (ou não) no Modo IA — clicar e capturar fontes citadas em 3-5 queries de teste.

---

## Anexo — Concorrentes a monitorizar trimestralmente

Top 5 a vigiar (frequência + agressividade SEO/SEM):

1. **Centralmed** — líder a bater. Watch: novos posts blog, novos GMB, palavras-chave nos ads.
2. **Sepri** — blog ativo, ambition multi-cluster.
3. **Preveris** — claim nacional, scaling.
4. **Hospital da Luz** — força bruta de marca em head queries.
5. **Seepmed** — pequeno mas investe em ads + content.
