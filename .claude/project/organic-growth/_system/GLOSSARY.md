# SEO Glossário — explicado como se nunca tivesses ouvido falar disto

> Ficheiro **vivo**. Sempre que um relatório SEO usa um termo técnico, adicionar aqui.
> Linguagem direta. Sem jargão a explicar jargão.

## A

### AIO (AI Overview / "Modo IA")

A **resposta gerada por inteligência artificial** que o Google mostra no topo da página de pesquisa, antes dos resultados normais. Em português aparece como "Modo IA".

**Como funciona na prática:** quando alguém pesquisa "medicina do trabalho" no Google.pt, o Google já não devolve só os 10 links azuis — devolve **primeiro** um resumo escrito por IA que combina conteúdo de várias fontes. Por baixo desse resumo, mostra a lista das fontes que usou (8 a 20 sites). Os links azuis tradicionais ficam ainda mais abaixo.

**Porquê interessa:** se o site Previmed estiver entre as fontes citadas, ganha visibilidade e tráfego mesmo que o utilizador nunca clique nos links azuis. Se não estiver, perde para concorrentes que estão.

**Sinónimos:** "AI Overview" (Google em inglês), "Modo IA" (Google em português), "SGE" (Search Generative Experience — nome antigo).

Ver capturas reais em `../clusters/q<N>-*/aio-capture.yml`.

---

### Author / Autor (no schema)

Indicação **explícita de quem escreveu** o artigo, codificada em formato que o Google entende (JSON-LD). Pode ser uma pessoa real (`Person`) ou uma organização (`Organization`).

**Porquê interessa:** o Google usa autor como um dos sinais de [E-E-A-T](#e-e-a-t-experience-expertise-authoritativeness-trustworthiness). Artigo assinado por médico do trabalho real tem mais "peso" que artigo anónimo.

---

## B

### Backlink

Link de **outro site** para o teu site. Ex.: ACT linka para Previmed → isso é um backlink que Previmed recebe da ACT.

**Porquê interessa:** o Google usa backlinks como sinal de autoridade. Mais backlinks de sites credíveis = mais "voto de confiança".

---

### Brand voice

A forma característica como uma marca **escreve** e refere os seus serviços. Ex.: Previmed usa hoje "Medicina No Trabalho" (com N maiúsculo, sem preposição "do") — isto é brand voice. Decisão de a manter ou alterar tem consequências SEO **e** de identidade da marca.

---

## C

### Canonical (URL canonical / tag rel=canonical)

Tag HTML que indica ao Google **qual é a URL "oficial"** de um conteúdo, quando existem várias URLs com conteúdo igual ou parecido.

**Exemplo:** se `previmed.pt/saude-no-trabalho/` e `previmed.pt/saude-no-trabalho/?utm=facebook` mostram o mesmo conteúdo, a canonical de ambas deve apontar para `previmed.pt/saude-no-trabalho/`. Senão o Google considera-as duplicadas e perde-se SEO.

---

### Cluster (keyword cluster / cluster temático)

**Grupo de queries relacionadas** que tratam do mesmo tema e cuja intenção justifica conteúdo agrupado.

**Exemplo:** o cluster "Medicina do Trabalho" inclui:
- "o que é medicina do trabalho"
- "medicina do trabalho obrigatória"
- "exames medicina do trabalho"
- "ficha de aptidão medicina do trabalho"
- "coima medicina do trabalho ACT"

Todas tratam de medicina do trabalho — agrupam-se num **cluster**. O cluster geralmente é coberto por **um pillar** + alguns **spin-offs** (ver abaixo).

Os clusters da Previmed estão definidos em `strategy/KEYWORDS.md` (16 clusters, ~120 queries).

---

### Copy

O **texto final** que vai ser publicado na página. Diferente de **brief** (que é a especificação que diz "o que escrever" antes de escrever). Brief → copy → revisão → publicação.

---

### CPT (Custom Post Type — WordPress)

Tipo de página personalizado no WordPress. Ex.: além de "Post" e "Página" (default WP), pode criar-se um CPT "Guia" para o hub `/recursos/guias/`. Cada CPT pode ter o seu próprio template, schema e campos.

---

### CTA (Call To Action)

**Botão ou link que pede uma ação ao leitor**. Ex.: "Pedir proposta", "Ver mais", "Contactar". Os pillars Previmed terão soft CTAs no meio (contextuais) e hard CTAs no fim ("Próximo passo").

---

### CTR (Click-Through Rate)

**Percentagem de pessoas que viram um link e clicaram.**

Fórmula: `clicks / impressões × 100`.

Ex.: se o título Previmed aparece 1000 vezes no Google e 50 pessoas clicam → CTR = 5%. CTR baixo num bom ranking indica problema no título/meta description.

---

## D

### `dateModified` / `datePublished` (no schema)

Datas registadas no schema indicando quando o artigo **foi publicado** (`datePublished`) e quando foi **atualizado pela última vez** (`dateModified`). O Google premeia conteúdo "fresco" — atualizar e bumpar a data é sinal positivo.

---

## E

### E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

**Quatro dimensões** que o Google usa para avaliar quão de confiança é um conteúdo:

1. **Experience (Experiência)** — Quem escreveu tem **experiência prática** no tema? Ex.: artigo sobre "exames de medicina do trabalho" tem mais E-E-A-T se for assinado por médico do trabalho real (vs por copywriter genérico).
2. **Expertise (Especialização)** — Quem escreveu tem **conhecimento técnico** comprovado? Ex.: credenciais, formação, anos no setor.
3. **Authoritativeness (Autoridade)** — A marca é **referência reconhecida** no tema? Ex.: Previmed = entidade autorizada DGS/ACT.
4. **Trustworthiness (Confiança)** — O site é **fiável**? Ex.: links externos para fontes oficiais (ACT, ASAE, Lei 102/2009), HTTPS, contactos visíveis, política de privacidade clara.

**Porquê interessa:** o Google premeia conteúdo com alto E-E-A-T no ranking e em AIO. Conteúdo sobre **saúde** (que é o caso da Previmed) é categorizado como **YMYL** ("Your Money or Your Life") — Google aplica filtro E-E-A-T mais rigoroso.

**Como Previmed melhora E-E-A-T:**
- Autor real e identificável (médico/técnico do quadro com nome + cargo + LinkedIn).
- Citar fontes institucionais (ACT, ASAE, DGS, leis).
- Mostrar credenciais e certificações (`/credenciacoes/`).
- HTTPS, contactos claros, políticas legais visíveis.

---

### Engagement

Quanto o utilizador **interage** com a página: tempo na página, scroll depth, cliques internos, partilhas. Métricas pós-clique medidas no GA4.

---

## F

### FAQPage (schema)

Tipo de schema markup que diz ao Google **"esta página tem perguntas e respostas estruturadas"**. Quando bem implementado, o Google pode mostrar as FAQ diretamente na SERP (rich result), aumentando visibilidade.

---

### Funil (TOP / MID / BOT)

**Fase em que o utilizador está** na decisão de compra:

- **TOP-of-funnel (TOFU)** — Ainda só está a **informar-se**. Ex.: "o que é medicina do trabalho?". Não está a comprar nada.
- **MID-of-funnel (MOFU)** — Já entende o problema e está a **comparar opções**. Ex.: "como escolher empresa medicina trabalho", "Centralmed vs Forprev".
- **BOT-of-funnel (BOFU)** — Pronto a **comprar**. Ex.: "preço medicina trabalho por trabalhador", "pedido proposta medicina trabalho".

Conteúdo TOP atrai tráfego mas converte pouco. Conteúdo BOT converte muito mas tem volume baixo. Estratégia equilibrada cobre os 3.

---

## G

### GA4 (Google Analytics 4)

Ferramenta gratuita do Google para medir o **comportamento dos visitantes** depois de chegarem ao site: páginas vistas, tempo, eventos, conversões, origem do tráfego (orgânico, redes sociais, direto). Substituiu o "Universal Analytics" antigo.

---

### GSC (Google Search Console)

Ferramenta gratuita do Google que mostra **o que se passa antes do clique**: que queries trazem impressões e cliques ao site, em que posição média ranqueia, quais páginas têm problemas de indexação, sitemap, etc. **É a fonte de verdade** para SEO porque os dados vêm diretamente do Google.

---

## H

### H1, H2, H3, H4

**Títulos hierárquicos** numa página HTML.

- `H1` = título principal da página (um só por página).
- `H2` = secções principais.
- `H3` = sub-secções dentro de H2.
- `H4` = sub-sub-secções dentro de H3.

**Estrutura correta:** H1 → H2 → H3 → H4 (descendente, sem saltos).

**Problema atual Previmed:** páginas saltam de H1 para H3 sem H2 — quebra a hierarquia. Documentado em `reports/2026-05-20__previmed-pages-audit.md`.

---

### HACCP

**Hazard Analysis and Critical Control Points** — "Análise de Perigos e Controlo de Pontos Críticos". Sistema obrigatório por lei (Reg CE 852/2004) para todas as empresas que manipulam alimentos. Fiscalizado em PT pela ASAE.

---

### Hard CTA / Soft CTA

- **Soft CTA**: convite suave no meio do artigo (ex.: "Ver mapa de centros médicos"). Não pressiona.
- **Hard CTA**: convite forte no fim ou em pontos de decisão (ex.: botão grande "Pedir proposta agora"). Conversão direta.

---

### Hierarquia editorial

**Ordem lógica** dos títulos numa página. Ver [H1/H2/H3](#h1-h2-h3-h4).

---

### HowTo (schema)

Schema markup que codifica **instruções passo-a-passo**. Ex.: "Como escolher empresa de medicina do trabalho — 6 passos". Quando bem implementado, o Google pode mostrar os passos diretamente na SERP.

---

### HSST (Higiene, Segurança e Saúde no Trabalho)

Acrónimo usado em PT para a área que engloba **Medicina do Trabalho + Segurança no Trabalho + Higiene/Segurança Alimentar + Formação**. É o segmento B2B core da Previmed.

---

## I

### Impressões (GSC)

Número de vezes que um link do site **apareceu** numa página de resultados Google. Não conta cliques, conta apenas exposição.

---

### Indexação

Estado em que o Google **já registou** uma página nos seus índices e a pode mostrar em resultados. Página não indexada = invisível no Google.

---

### Intenção de pesquisa (search intent)

**O que a pessoa quer mesmo** quando faz uma query.

4 tipos clássicos:
- **Informacional** — quer saber algo. Ex.: "o que é medicina do trabalho".
- **Navegacional** — quer ir a um sítio específico. Ex.: "previmed login".
- **Comercial / Investigation** — está a avaliar opções. Ex.: "melhor empresa medicina trabalho".
- **Transacional** — quer comprar/contratar. Ex.: "pedido proposta medicina trabalho".

Conteúdo SEO bem feito **responde à intenção** — não à query literal.

---

### Internal link / External link

- **Internal link** — link dentro do próprio site (ex.: pillar Q1 → página `/saude-no-trabalho/`). Distribuem autoridade interna.
- **External link** — link para outro site (ex.: pillar HACCP → ASAE). Citar fontes institucionais reforça [E-E-A-T](#e-e-a-t-experience-expertise-authoritativeness-trustworthiness).

---

## J

### JSON-LD

Formato técnico para escrever [schema markup](#schema-markup). Pequeno bloco de código JSON colocado no `<head>` da página. O Google lê-o para perceber que tipo de conteúdo é (Article, FAQPage, Service, etc.).

---

## K

### Keyword

Sinónimo de [query](#query). Mais comum em contextos de planeamento ("escolher keywords-alvo"); query é mais comum em contextos de análise ("a query mais ranqueada foi…").

---

### Keyword Planner

Ferramenta gratuita do Google Ads que mostra **volume estimado** de pesquisas mensais por keyword em Portugal. Volumes vêm em **buckets** (ex.: "100–1k pesquisas/mês") em vez de números exatos, exceto se a conta Ads tiver spend ativo.

---

### KPI (Key Performance Indicator)

**Indicador-chave de desempenho.** Métricas que se acompanham para avaliar se a estratégia SEO está a funcionar. Ex.: impressões GSC, cliques orgânicos, conversões via formulário, posição média.

---

## L

### Lei 102/2009

**Lei portuguesa que define o regime jurídico** da Segurança e Saúde no Trabalho. Define obrigações de medicina do trabalho, segurança, exames médicos, ficha de aptidão, fiscalização ACT. Citada em quase todo o conteúdo HSST PT.

---

### Lei 93/2019

**Lei que alterou** o Art.º 131.º do Código do Trabalho — passou o mínimo de formação contínua de **35 para 40 horas anuais** por trabalhador. Achado crítico documentado em `reports/2026-05-20__aio-expansion.md`.

---

## M

### Meta description

Resumo de **155 caracteres** que aparece debaixo do título nos resultados Google. Influencia [CTR](#ctr-click-through-rate). Não é um sinal direto de ranking mas é determinante para o utilizador clicar ou não.

---

## P

### Pillar (pillar page)

**Página principal** que cobre um cluster temático em profundidade. Ex.: pillar "Medicina do Trabalho" = página dedicada a explicar tudo sobre o tema, com 1500–2000 palavras, estrutura H1→H2→H3, FAQ, schema completo, e links para sub-tópicos (spin-offs).

A estratégia "pillar + spin-offs" foi observada na SEPRI (`reports/2026-05-20__competitor-deep-dive.md`) — 3 URLs SEPRI em AIO Q1.

---

### Persona

**Representação de um decisor típico** do público-alvo. Não é uma pessoa real, é um arquétipo.

Personas Previmed (em `strategy/AUDIENCES.md`):
1. RH/Office Manager de PME.
2. Diretor Industrial / responsável produção.
3. Formando (trabalhador a candidatar-se a curso CAP).

Conteúdo SEO deve **escrever para uma persona específica** — não para "todos".

---

### PSI (PageSpeed Insights)

Ferramenta gratuita do Google que mede a **velocidade e qualidade técnica** de uma página (mobile + desktop). Output principal: Core Web Vitals (LCP, INP, CLS). Quanto mais rápida a página, melhor o ranking.

---

## Q

### Query

**O que alguém escreve no Google** para fazer uma pesquisa.

Ex.: alguém abre o Google.pt e escreve `medicina do trabalho` — essa frase é uma query. As 5 queries P1 analisadas em AIO (medicina do trabalho, segurança no trabalho, HACCP, formação 35 horas obrigatória, como escolher empresa medicina do trabalho) são as 5 queries-alvo principais para Previmed.

**Diferença entre query e keyword:** funcionalmente são o mesmo. "Keyword" é o termo mais usado em planeamento; "query" é mais usado em análise.

---

## R

### Rank tracking

**Acompanhar a posição** em que o site aparece para um conjunto de queries-alvo, ao longo do tempo. Ex.: monitorizar se Previmed ranqueia top 10 para "medicina do trabalho" semana a semana.

Sem tool pago, fazemos rank checks manuais via Playwright (ad-hoc). Documentado em `setup/KEYWORD_DATA_DECISION.md`.

---

### Redirect 301

**Redirecionamento permanente** de uma URL antiga para uma nova. Crítico quando se muda slug — sem 301, perde-se ranking + backlinks da URL antiga. Ex.: se `/saude-no-trabalho/` mudasse para `/medicina-do-trabalho/`, sem 301 perdia-se o foothold AIO atual.

---

### Redirect 302

Redirecionamento **temporário**. Quase nunca usado em SEO — quase sempre se quer 301.

---

## S

### Schema markup

Vocabulário standard ([schema.org](https://schema.org)) que descreve o conteúdo de uma página de forma estruturada **para máquinas**.

Ex.: o utilizador vê "Dr. João Silva, médico do trabalho". O Google só vê isto como texto. Com schema, podemos dizer ao Google "estes dois pedaços de texto são um `Person` com `jobTitle: Médico do Trabalho`". Aí o Google consegue usar a informação melhor em AIO, rich snippets, knowledge graph.

Tipos importantes:
- `Article` — artigo editorial.
- `FAQPage` — secção de perguntas frequentes.
- `HowTo` — passo-a-passo.
- `Service` — serviço comercial.
- `Organization` — empresa.
- `Person` — pessoa (autor, médico).
- `Legislation` — lei citada.

Implementado tipicamente em JSON-LD.

---

### SERP (Search Engine Results Page)

**Página de resultados** do Google. Inclui hoje: AIO (Modo IA) no topo, ads, links azuis, mapas locais, vídeos, imagens, "People also ask", featured snippets, etc.

---

### Slug

**Parte final da URL** após o domínio. Ex.: na URL `https://previmed.pt/saude-no-trabalho/`, o slug é `saude-no-trabalho`. Influencia [CTR](#ctr-click-through-rate) e percepção de tema. Mudar slug requer [301 redirect](#redirect-301).

---

### Snippet (featured snippet)

Caixa especial que o Google mostra **acima dos links azuis** com uma resposta direta retirada de uma página. Aparece em queries informacionais. Mais antigo que AIO mas ainda relevante. Capturar featured snippets requer formatação específica (resposta direta no início, estrutura limpa).

---

### Spin-off

**Página derivada de um pillar**, com foco mais específico. Ex.: pillar "Medicina do Trabalho" + spin-offs: "Ficha de Aptidão", "Periodicidade dos Exames", "Medicina do Trabalho no Porto" (geo).

Estratégia "pillar + spin-offs" replica o padrão SEPRI observado em `reports/2026-05-20__competitor-deep-dive.md` — SEPRI tem 3 URLs em AIO Q1 graças a esta árvore.

---

## T

### Title tag

O texto que aparece como **título no separador do browser** e como link principal nos resultados Google. Limite: 60 caracteres. Diferente do `<h1>` (que aparece no corpo da página).

**Problema atual Previmed:** title duplicado `"<página> - Previmed - PrevimedPrevimed"`. Documentado em `reports/2026-05-20__previmed-pages-audit.md`.

---

## Y

### YMYL (Your Money or Your Life)

Categoria do Google para conteúdo que **impacta significativamente** a saúde, segurança, finanças ou bem-estar do leitor. Saúde ocupacional (Medicina do Trabalho, HACCP) cai aqui. Google aplica filtro [E-E-A-T](#e-e-a-t-experience-expertise-authoritativeness-trustworthiness) mais rigoroso. Implicação prática para Previmed: **autoria identificada + citações institucionais são obrigatórias**, não opcionais.

---

## Acrónimos de entidades portuguesas

| Sigla | Significado | Papel |
|---|---|---|
| **ACT** | Autoridade para as Condições do Trabalho | Fiscaliza SST + Medicina do Trabalho. Aplica coimas. |
| **DGS** | Direção-Geral da Saúde | Autoriza prestadores de medicina do trabalho. |
| **DGAV** | Direção-Geral de Alimentação e Veterinária | Regulação alimentar (cluster HACCP). |
| **DGERT** | Direção-Geral do Emprego e das Relações de Trabalho | Certifica entidades formadoras. |
| **ASAE** | Autoridade de Segurança Alimentar e Económica | Fiscaliza HACCP nas empresas. |
| **OCC** | Ordem dos Contabilistas Certificados | Publica guias práticos de RH/Formação. |
| **SPMT** | Sociedade Portuguesa de Medicina do Trabalho | Sociedade científica de referência. |
| **OA** | Ordem dos Advogados | Publica artigos jurídicos relacionados. |
| **DGEEC** | Direção-Geral de Estatísticas da Educação e Ciência | Publica documentação SST formativa. |
| **AHRESP** | Associação Hotelaria, Restauração, Similares Portugal | Setor restauração (cluster HACCP). |
| **APSEI** | Associação Portuguesa de Segurança Eletrónica | Guias de organização SST. |

---

## Documentos legais referenciados

| Documento | Cluster |
|---|---|
| **Lei n.º 102/2009** | Medicina do Trabalho + Segurança no Trabalho |
| **Lei n.º 93/2019** | Formação obrigatória (mudou 35h → 40h) |
| **Art.º 131.º Código do Trabalho** | Formação obrigatória |
| **Reg CE 852/2004** | HACCP / segurança alimentar |
| **Reg CE 853/2004** | HACCP géneros alimentícios origem animal |
| **Codex Alimentarius (FAO/WHO)** | HACCP (princípios internacionais) |
| **ISO 45001** | SST — sistema de gestão internacional |
| **Nota Técnica 9 ACT** | Contabilização horas formação contínua |

---

## Como usar este glossário

- Quando estiveres a ler um relatório em `reports/` e encontrares um termo que não entendes, vem cá.
- Se um termo importante não estiver aqui, adiciona — ou diz-me para adicionar.
- Os termos têm `anchor` para `#nome-do-termo` — podes linkar diretamente de outros docs.

## Last Updated

2026-05-20 por Claude (SEO Lead). Vai crescer ao longo do projeto — fica vivo.
