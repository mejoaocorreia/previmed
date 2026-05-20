# SEO Decision Log

> Ficheiro **vivo**. Decisões SEO **importantes e duradouras**.
> Não regista todas as decisões — só as que afetam estratégia, arquitetura, ferramentas ou políticas a médio/longo prazo.
> Análise que justifica cada decisão vive em `reports/` ou em ficheiros de decisão dedicados.

## O que entra aqui

- Decisões arquiteturais (estrutura de URLs, hubs editoriais, taxonomias).
- Escolha de ferramentas SEO core (keyword data, crawler, monitorização).
- Políticas de SEO (regras de schema, política de canonicals, política de redirect).
- Trade-offs estratégicos (priorizar HSST B2B vs formação B2C, etc.).
- Mudanças de stack/plugins SEO no WordPress.

## O que **não** entra

- Tarefas operacionais (vão para `./BACKLOG.md`).
- Hipóteses não validadas (vão para `./OPPORTUNITIES.md`).
- Análise detalhada (vai para `reports/`).
- Estado atual (vai para `_living/CURRENT_STATUS.md`).

## Formato

```
## YYYY-MM-DD — [Título curto da decisão]

- **Contexto**: 1–3 linhas sobre porquê foi precisa.
- **Decisão**: o que ficou decidido.
- **Alternativas consideradas**: o que foi rejeitado e porquê.
- **Origem**: link para relatório / discussão / ficheiro de decisão.
- **Revisão**: quando reavaliar (data ou condição).
- **Decisor**: utilizador / SEO Lead / Supervisor.
```

## Decisões

### 2026-05-20 — Brand voice: "Medicina do Trabalho" (forma canónica)

- **Contexto**: as páginas Previmed atuais usam "Medicina **No** Trabalho" (N maiúsculo, sem preposição "do"). A query que as pessoas escrevem no Google é "medicina **do** trabalho" (forma idiomática PT). Divergência detectada em `.../reports/2026-05-20__competitor-deep-dive.md` §C2.
- **Decisão**: usar **"Medicina do Trabalho"** (forma canónica) em todo o conteúdo novo (5 pillars + spin-offs + futuras peças). Implica corrigir as páginas existentes (`/saude-no-trabalho/`, `/seguranca-no-trabalho/`, etc.) quando o template for refeito.
- **Porquê**: alinhar com a [query](./_system/GLOSSARY.md#query) que aparece nas pesquisas Google e na [AIO](./_system/GLOSSARY.md#aio-ai-overview-modo-ia). A AIO Q1 do Google.pt fala em "medicina do trabalho" — divergência da Previmed reduz match semântico e probabilidade de citação AIO.
- **Alternativas consideradas**: (a) manter "Medicina No Trabalho" como brand voice — rejeitado, perde alinhamento Google. (b) Híbrido (title/H1 canónico, body com brand) — rejeitado, incoerência editorial.
- **Origem**: discussão com utilizador 2026-05-20 sobre brand voice (ver `.../reports/2026-05-20__competitor-deep-dive.md` §Decisions Needed #1).
- **Revisão**: reavaliar se a marca tiver branding work que decida o contrário; nesse caso, ponderar criar 2 layers (marca interna vs SEO público).
- **Decisor**: utilizador.

### 2026-05-20 — Autoria dos pillars: pessoa real do quadro

- **Contexto**: os pillars P1 vão ser publicados com schema [Article](./_system/GLOSSARY.md#schema-markup). O campo `author` pode ser pessoa real, organização ou ausente. Saúde ocupacional cai em [YMYL](./_system/GLOSSARY.md#ymyl-your-money-or-your-life) — Google aplica filtro [E-E-A-T](./_system/GLOSSARY.md#e-e-a-t-experience-expertise-authoritativeness-trustworthiness) mais rigoroso.
- **Decisão**: autor identificado é **pessoa real do quadro Previmed**, com nome + cargo + foto + LinkedIn. SEPRI (concorrente que domina AIO Q1) usa este padrão.
- **Sub-decisão (2026-05-20)**: 4 **placeholders fictícios** com cargos diretivos para arrancar o copy, **a substituir por pessoas reais antes de publicar**:
  - Q1 (Medicina do Trabalho) + Q5 (Como escolher MT) → **Dr. Miguel Henriques** (Diretor Clínico, Medicina do Trabalho).
  - Q2 (Segurança no Trabalho) → **Eng.ª Sara Vilela** (Diretora de Segurança e Saúde no Trabalho).
  - Q3 (HACCP) → **Eng.ª Carla Tavares** (Diretora de Segurança Alimentar).
  - Q4 (Formação 40h) → **Dra. Inês Carvalho** (Diretora Pedagógica, DGERT).
- ⚠️ **Aviso E-E-A-T**: nomes fictícios apenas para fluxo editorial. **Publicar com autores falsos viola E-E-A-T do Google e tem risco de penalização para YMYL** (saúde ocupacional cai aqui — ver [`_system/GLOSSARY.md#ymyl-your-money-or-your-life`](./_system/GLOSSARY.md#ymyl-your-money-or-your-life)). Antes de cada publicação, substituir por: nome real + cargo + foto + perfil LinkedIn.
- **Porquê**: [E-E-A-T](./_system/GLOSSARY.md#e-e-a-t-experience-expertise-authoritativeness-trustworthiness) é forte para YMYL. Autor real e identificável é o sinal mais barato e mais potente para Previmed entrar em AIO. Schema `Person` permite ao Google ligar o autor a credenciais (LinkedIn `sameAs`).
- **Alternativas consideradas**: (a) "Equipa Editorial Previmed" como Organization — rejeitado, perde sinal individual. (b) Sem autor declarado — rejeitado, fraco em YMYL.
- **Origem**: discussão com utilizador 2026-05-20 + análise em `.../reports/2026-05-20__competitor-deep-dive.md` §M2.
- **Revisão**: se Previmed contratar editor externo (freelancer), reavaliar se faz sentido manter autor interno ou rotacionar.
- **Decisor**: utilizador (decisão conceptual fechada; nomes por confirmar).

### 2026-05-20 — Tool keyword data: orçamento zero (Cenário Z)

- **Contexto**: 6 cenários avaliados em [`../setup/KEYWORD_DATA_DECISION.md`](./setup/KEYWORD_DATA_DECISION.md) (A=DataForSEO ~$300/ano, B=SerpAPI ~$300, C=Ahrefs Lite ~$1 548, D=Semrush ~$1 668, E=SE Ranking ~$660, F=Híbrido ~$650). Recomendação interna era Cenário A.
- **Decisão**: nenhum tool pago. Stack só com ferramentas gratuitas: **Google Search Console + GA4 + Google Keyword Planner + Playwright MCP + PageSpeed Insights API**.
- **Alternativas consideradas**: todas as 6 opções pagas A–F. Rejeitadas todas — preferência declarada por orçamento zero ("*se não houver nada gratuito, não quero nada*").
- **Trade-offs aceites**: sem volumes finos (buckets de Keyword Planner), sem competitor ranked keywords automatizadas, sem rank tracking automatizado, sem backlinks data, sem dashboard SaaS. Compensações: GSC = fonte de verdade quando ligado; Playwright = SERPs ad-hoc; relatórios markdown em `reports/`.
- **Origem**: discussão 2026-05-20 + [`../setup/KEYWORD_DATA_DECISION.md`](./setup/KEYWORD_DATA_DECISION.md).
- **Revisão**: reavaliar se (a) volume de queries cresce significativamente, (b) briefs precisam de competitor ranked KWs em massa, (c) auditoria de backlinks se torna crítica, (d) aparecer free tier viável.
- **Decisor**: utilizador.

### 2026-05-20 — Cluster "Formação 35h" passa a refletir 35→40h

- **Contexto**: AIO Q4 (`formação 35 horas obrigatória`) confirma que Lei 93/2019 alterou Art.º 131.º do Código do Trabalho: o mínimo de formação contínua passou de **35 para 40 horas anuais** por trabalhador. `../strategy/KEYWORDS.md` (linhas 213–216) ainda usa "35h" — refletia a query do utilizador, não o referencial legal atual.
- **Decisão**: manter "35 horas" no slug/título visível (pelo volume de pesquisa esperado) **mas** abrir todas as páginas pillar do cluster Formação com a correção 35→40h explícita, citando Lei 93/2019 e Nota Técnica 9 da ACT. Adicionar variantes "40 horas obrigatórias", "Lei 93/2019 formação", "40h formação contínua" no `../strategy/KEYWORDS.md` quando keyword data tool estiver ligado.
- **Alternativas consideradas**: (a) ignorar a correção e manter conteúdo "35h" — rejeitado, conteúdo desatualizado perde credibilidade e arrisca queda AIO; (b) migrar todo conteúdo para "40h" e perder volume da query "35h" — rejeitado, query mantém volume residual e ignorá-la deixa terreno aos competidores.
- **Origem**: [`.../reports/2026-05-20__aio-expansion.md`](../reports/2026-05-20__aio-expansion.md) §Q4 + §C1.
- **Revisão**: reavaliar a cada 12 meses ou quando uma nova alteração legal for publicada.
- **Decisor**: SEO Lead (sujeito a validação do utilizador na próxima revisão de keywords).

### 2026-05-20 — Persistência de análises SEO em `reports/`

- **Contexto**: análises grandes ficavam só no chat, desperdiçando contexto.
- **Decisão**: toda análise SEO grande (auditoria, keyword research, competitor, content gap, CWV, schema, local, AI/GEO, plano de ação) é persistida em `.claude/project/organic-growt../reports/YYYY-MM-DD__report-type.md`.
- **Alternativas consideradas**: deixar no chat (rejeitado, desperdiça contexto); usar `.txt` (rejeitado, renderiza pior no GitHub).
- **Origem**: instrução do utilizador 2026-05-20 (Change Management Supervisor).
- **Revisão**: rever se estrutura `reports/` cresce a ponto de exigir subpastas por ano ou por tipo.
- **Decisor**: utilizador.

<!--
Próxima decisão será adicionada acima desta linha. Manter ordem cronológica inversa (mais recente em cima).
-->

## Decisões soltas em ficheiros próprios

Algumas decisões grandes têm ficheiro dedicado e são apenas **indexadas** aqui:

- `../setup/KEYWORD_DATA_DECISION.md` — escolha do tool de keyword data (status: **pendente decisão do utilizador**, cenários A–F).
