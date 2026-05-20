# Strategy — Arquitetura de Informação

> Lote 1.2 da Fase 1.
> Última atualização: 2026-05-19.
> Autor: SEO Lead + Site Structure agent.
> Base: `strategy/AUDIENCES.md` + `PROJECT_CONTEXT.md`.

## Princípios da arquitetura

1. **Audiência principal manda na navegação** — menu serve a *Cliente Empresa* (65% do esforço).
2. **Sub-hub para Formando** — `/formacao/` tem vida própria mas mantém-se no mesmo domínio para concentrar autoridade.
3. **Portal Trabalhador em subdomínio** — separação técnica e SEO clara.
4. **Profundidade ≤ 3 níveis** a partir da raiz para qualquer página de conversão.
5. **Páginas regionais só quando há substância real** — nada de doorway pages.
6. **Hub → Pillar → Cluster** como padrão de conteúdo.

---

## Decisão 1 — Subdomínio vs sub-pasta

| Área | Local | Motivo |
|---|---|---|
| Site institucional + serviços + conteúdo | `www.previmed.pt/` (raiz) | Concentra autoridade. |
| Formação | `www.previmed.pt/formacao/` | Sub-hub no mesmo domínio: cruza autoridade com serviços e aproveita pontes internal linking. |
| Portal Trabalhador | `portal.previmed.pt` | Auth separada, stack diferente, sem objetivo SEO. Subdomínio é correcto. |
| E-learning | `elearning.previmed.pt` **ou** `www.previmed.pt/formacao/elearning/` | **A decidir na Fase 4** consoante for LMS WP (LearnDash/LifterLMS → sub-pasta) ou plataforma externa (Moodle/Talent LMS → subdomínio). |

**Recomendação inicial**: e-learning em subdomínio se for plataforma existente que já gere; sub-pasta se for novo e WP-native.

---

## Decisão 2 — Páginas regionais

**Decisão**: NÃO criar páginas regionais (`/medicina-trabalho/lisboa/`, etc.) **na fase inicial**.

Razões:
- Sem morada física própria, qualquer página "Medicina do Trabalho em Lisboa" seria thin content / doorway.
- Concorrência regional é capturada por queries muito específicas; baixa intenção comercial sem clínica própria.

**Em vez disso**, criar **uma única página `/cobertura/`** com:
- mapa interativo de clínicas parceiras;
- pesquisa por código postal/distrito (uma feature, não 20 páginas);
- schema `Organization` com `areaServed: Portugal`.

**Revisitar na Fase 5**: se GSC mostrar volume real em queries regionais não capturadas, considerar páginas por distrito **com conteúdo único** (não template multiplicado).

---

## Decisão 3 — Separação de jornadas no menu

| Elemento | Localização | Audiência |
|---|---|---|
| Menu principal | Topo central | Cliente Empresa + Formando |
| Utility nav | Topo direita, mais discreto | Trabalhador + Formando login |
| CTA proposta | Topo direita, destacado (botão) | Cliente Empresa |

Não usar audience switcher ("Sou empresa / sou trabalhador") na home — é fricção. Usar **clareza visual e copy** em cada CTA.

---

## Mapa de site top-level

```
/                                            Homepage (institucional + 3 jornadas)
│
├── /servicos/                                Hub Serviços (Empresa)
│   ├── /servicos/medicina-trabalho/
│   ├── /servicos/seguranca-trabalho/
│   ├── /servicos/higiene-seguranca-alimentar/
│   ├── /servicos/ambiente/
│   ├── /servicos/pericias-medico-legais/
│   ├── /servicos/exames-serologicos/
│   ├── /servicos/exames-seguradoras/
│   └── /servicos/certificacao/
│
├── /formacao/                                Hub Formação (Formando + Empresa)
│   ├── /formacao/catalogo/                   Listagem com filtros
│   ├── /formacao/{curso-slug}/               Página por curso
│   ├── /formacao/modalidades/online/
│   ├── /formacao/modalidades/presencial/
│   ├── /formacao/dgert/                      Página autoridade DGERT
│   └── /formacao/para-empresas/              Ponte para Cliente Empresa
│
├── /cobertura/                               Cobertura nacional + locator
│
├── /recursos/                                Hub conteúdo SEO
│   ├── /recursos/guias/
│   │   ├── /recursos/guias/{guia-slug}/      Pillar pages
│   ├── /recursos/faq/
│   └── /recursos/noticias/
│
├── /sobre/                                   Hub institucional
│   ├── /sobre/certificacoes/                 ACT, DGS, DGERT, ISO 9001
│   ├── /sobre/equipa/
│   └── /sobre/historia/
│
├── /recrutamento/                            Mantém da estrutura atual
├── /contactos/
├── /proposta/                                Form pedido de proposta
│
└── [legal]
    ├── /politica-privacidade/
    ├── /politica-cookies/
    └── /termos/

[subdomínios]
portal.previmed.pt                            Portal Trabalhador
elearning.previmed.pt | /formacao/elearning/  E-learning (decisão Fase 4)
```

Profundidade máxima de uma página de conversão: **2 cliques da home** (Home → /servicos/ → /servicos/medicina-trabalho/).

---

## Pillar pages prioritárias (a criar na Fase 5)

Cada pillar serve dois propósitos: capturar query informacional + fornecer internal links de alta relevância para páginas de serviço.

| Pillar | URL | Cluster (sub-páginas) |
|---|---|---|
| Lei 102/2009 explicada | `/recursos/guias/lei-102-2009-medicina-trabalho/` | exames de admissão, periodicidade, ficha de aptidão, obrigações empregador |
| HACCP para restauração | `/recursos/guias/haccp-restauracao/` | manual HACCP, formação HACCP, manipulação alimentos |
| Formação 35h: o que é obrigatório | `/recursos/guias/formacao-35-horas-obrigatoria/` | quem precisa, quando, isenções |
| Como escolher empresa de medicina do trabalho | `/recursos/guias/escolher-medicina-do-trabalho/` | critérios, perguntas, red flags |
| Acidente de trabalho: o que fazer | `/recursos/guias/acidente-trabalho-procedimento/` | participação, prazos, perícia |
| ISO 45001 vs OHSAS | `/recursos/guias/iso-45001-seguranca/` | implementação, auditoria |

Cada pillar tem ~2500–4000 palavras, FAQs, schema `Article` + `FAQPage`, e CTA contextual ("precisa de fornecedor HSST? Peça proposta").

---

## Regras de URL/slug

| Regra | Exemplo correcto | Exemplo errado |
|---|---|---|
| Lowercase | `/medicina-trabalho/` | `/Medicina-Trabalho/` |
| Hifens, não underscores | `/lei-102-2009/` | `/lei_102_2009/` |
| Sem acentos | `/pericias-medico-legais/` | `/perícias-médico-legais/` |
| Slug PT, não EN | `/cobertura/` | `/coverage/` |
| Singular em serviços | `/medicina-trabalho/` | `/medicinas-trabalho/` |
| Plural em hubs | `/servicos/` | `/servico/` |
| Sem datas | `/recursos/guias/iso-45001/` | `/2026/05/iso-45001/` |
| Sem prefixos de CMS | `/recursos/guias/iso-45001/` | `/category/guias/iso-45001/` |
| Max ~60 caracteres | `/recursos/guias/lei-102-2009-medicina-trabalho/` | `/recursos/guias/a-lei-102-2009-de-10-de-setembro-medicina-trabalho-portugal/` |
| Números só quando naturais | `/formacao-35-horas/` | `/curso-numero-3/` |

**Não usar** `/category/`, `/tag/`, `/post/`, `/page/` nem outras estruturas geradas por defeito pelo WordPress. Configurar permalinks na Fase 4.

**Redirects da Fase 6** — quando substituirmos o site existente, mapeamento URL antigo → novo é obrigatório. Tarefa documentada para Fase 6 com `wordpress-seo-implementation`.

---

## Estrutura de menu (proposta de UI)

**Header desktop:**

```
[Logo Previmed]    Serviços ▾   Formação ▾   Cobertura   Recursos ▾   Sobre ▾   Contactos    [Portal] [E-learning]   [Pedir Proposta →]
```

**Mega-menu Serviços** (3 colunas):
- Col 1 — Saúde: Medicina Trabalho, Exames Serológicos, Exames Seguradoras
- Col 2 — Segurança: Segurança Trabalho, Perícias Médico-Legais
- Col 3 — Compliance: HACCP, Ambiente, Certificação
- Rodapé do mega-menu: link "Ver todos os serviços" → `/servicos/`

**Mega-menu Formação** (2 colunas):
- Col 1 — Catálogo por área (Segurança, Alimentar, Ambiente, CAP)
- Col 2 — Modalidades, Para Empresas, Certificações DGERT

**Header mobile:**
- Hamburger menu acumula menu principal
- Utility nav (Portal/E-learning) num bloco superior antes do menu principal
- CTA Proposta fixo no topo

**Footer:**
- Sitemap completo (4–5 colunas)
- Badges certificações (ACT, DGS, DGERT, ISO 9001)
- NIPC, morada legal, contacto
- Redes sociais
- Links legais

---

## Schema architecture (alto nível, detalhe no Lote 1.4+)

| Página | Schema principal | Schema complementar |
|---|---|---|
| Home `/` | `Organization` + `WebSite` (com `SearchAction`) | `BreadcrumbList` |
| Hub `/servicos/` | `WebPage` + `BreadcrumbList` | — |
| Serviço `/servicos/{x}/` | `Service` + `BreadcrumbList` | `FAQPage` se houver FAQ visível |
| Hub `/formacao/` | `EducationalOrganization` + `BreadcrumbList` | — |
| Curso `/formacao/{x}/` | `Course` + `CourseInstance` + `BreadcrumbList` | `EducationalOccupationalCredential` quando DGERT |
| Pillar `/recursos/guias/{x}/` | `Article` + `BreadcrumbList` | `FAQPage` |
| Sobre `/sobre/` | `Organization` com `hasCredential` (ACT, DGS, DGERT, ISO 9001) | — |
| Contactos | `Organization` + `ContactPoint` | — |
| Cobertura | `Organization` com `areaServed: Country: PT` | — |

`LocalBusiness` **não usar** — Previmed não tem morada comercial física única. Usar `Organization` (mais genérico) com `areaServed`.

---

## Indexabilidade por área

| Área | `robots` | Motivo |
|---|---|---|
| Páginas serviço, formação, recursos, sobre | `index, follow` | Aquisição. |
| Form `/proposta/` | `noindex, follow` | Sem valor SEO, evita thin content. |
| Páginas legais (privacidade, cookies, termos) | `index, follow` (sinal de confiança) | Mas baixa prioridade. |
| Resultados de pesquisa interna | `noindex` | Default. |
| Tag/category WordPress nativos | `noindex` | Plugin SEO desliga. |
| Author archives | `noindex` | Default. |
| `portal.previmed.pt` (subdomínio) | `noindex` (excepto landing principal) | Não competir com www. |
| `elearning.previmed.pt` | `noindex` em áreas autenticadas; landing `index` | Aquisição via landing. |

---

## Relação com previmed.pt existente

O site `https://previmed.pt` em produção **não é tocado** nesta fase. Quando entrarmos na Fase 6 (go-live), o mapeamento será:

| URL atual (a confirmar via crawl no início da Fase 6) | URL novo |
|---|---|
| (TBD) | (TBD) |

**Action item Fase 6**: crawl completo do site actual + tabela de redirects 301 antes do switch.

---

## Próximo lote

**Lote 1.3 — Universo de keywords** vai:
- popular cada hub/sub-hub/pillar com queries reais por cluster;
- atribuir intenção (informacional/comercial/transacional/brand);
- marcar prioridade por impacto (volume × intenção × dificuldade estimada);
- detectar canibalizações entre `/servicos/` e `/formacao/`;
- detectar oportunidades não previstas neste mapa (e.g. pillars adicionais).

A arquitetura definida aqui é a **espinha dorsal** — pode receber ajustes pequenos quando Lote 1.3 trouxer dados; alterações maiores ficam registadas no `DECISION_LOG.md`.
