# SEO Growth Operating System

Fonte principal de detalhe operacional do **SEO Growth System**.

Este ficheiro define como o module trabalha — como é activado, como flui o trabalho, que áreas cobre, como priorizar, como fazer handoff e como garantir persistência. É a referência de funcionamento para qualquer agente que entre numa tarefa SEO.

Este ficheiro não é um agente.  
Este ficheiro não executa análises.  
Este ficheiro não substitui o `seo-lead`, o `seo-qa`, a skill `seo-quality-gate`, o `QUALITY_GATE.md` nem o Supervisor/System Safety.

---

## Objetivo

Garantir que qualquer trabalho SEO conduzido por este module resulta num activo orgânico que:

- é tecnicamente rastreável e indexável;
- responde melhor às intenções de pesquisa reais;
- representa serviços com clareza e especificidade;
- transmite confiança e autoridade;
- tem conteúdo útil e diferenciado;
- é rápido e bom em mobile;
- está preparado para Search clássico e AI Search;
- converte visitantes em clientes ou leads;
- pode ser medido e melhorado.

---

## Âmbito

Este operating system cobre:

- como o module é activado e como o fluxo começa;
- áreas de trabalho cobertas;
- workflow padrão para trabalho médio/grande;
- priorização (impacto × esforço × risco);
- handoff entre áreas;
- persistência de análises;
- regras de governança.

---

## Fora de âmbito

- detalhe técnico de SEO — ver `TECHNICAL_RULES.md`;
- detalhe de conteúdo — ver `CONTENT_RULES.md`;
- estratégia e intenção — ver `STRATEGY_RULES.md`;
- quality gate e critérios de aprovação — ver `QUALITY_GATE.md`;
- ferramentas — ver `TOOLING_MODEL.md`;
- KPIs e métricas — ver `KPI_MODEL.md`;
- persistência de records — ver `REPORTING_MODEL.md`.

---

## Como o module é activado

O SEO Growth System é activado quando o Supervisor detecta um pedido que toca SEO, pesquisa orgânica, web content, Google/SERP, schema, performance SEO, AI Search ou WordPress SEO.

Fluxo de activação:

1. **Supervisor** identifica pedido SEO e encaminha para o módulo via comando `/seo` ou directamente para `seo-growth-system:seo-lead`.
2. **Comando `/seo`** ou **`seo-lead`** recebem o pedido ao nível do agente principal/topo.
3. O comando ou `seo-lead` identificam o modo correcto e escolhem subagentes necessários.
4. **Fan-out paralelo** acontece ao nível do comando/topo — não dentro de subagentes folha.
5. Subagentes executam as suas partes e devolvem outputs.
6. `seo-lead` consolida.
7. `seo-qa` valida antes de entrega relevante.
8. Resultado final é entregue ao Supervisor/utilizador.

---

## Regras principais de funcionamento

1. **Não há SEO sem intenção clara.** Antes de criar qualquer página, confirmar intenção de pesquisa.
2. **Não há página nova sem papel na arquitectura.** Cada página tem um cluster, um tipo e uma relação com as outras.
3. **Não há alteração de slug sem plano de redirect.** URL changes são sempre sensíveis.
4. **Não há schema sem conteúdo visível correspondente.** Schema representa realidade, não intenção.
5. **Não há conteúdo SEO genérico.** Conteúdo específico da empresa, não de qualquer empresa.
6. **Não há design que esconda conteúdo crítico.** Conteúdo crítico deve estar visível e indexável.
7. **Não há dependência pesada sem performance review.** Scripts, fontes e assets têm impacto em CWV.
8. **Não há análise grande sem record persistente.** Análise que não é persistida não existe no futuro.
9. **SEO não passa por cima de segurança, produção, rollback, performance, acessibilidade, marca ou dados pessoais.** Em conflito, Supervisor/System Safety decidem.

---

## Áreas de trabalho

O module cobre estas áreas quando relevantes para o projecto:

| Área | Agentes principais | Docs principais |
|---|---|---|
| Estratégia e intenção | `seo-lead`, `keyword-intent` | `STRATEGY_RULES` |
| Pesquisa e clusters | `keyword-intent` | `STRATEGY_RULES`, `keyword-cluster-map` |
| Concorrência/SERP | `serp-competitor-analyst` | `COMPETITOR_RESEARCH_PLAYBOOK` |
| Arquitectura de informação | `seo-lead`, `keyword-intent` | `STRATEGY_RULES` |
| SEO técnico | `technical-seo` | `TECHNICAL_RULES` |
| Conteúdo | `content-growth`, `content-brief` | `CONTENT_RULES` |
| On-page | `onpage-seo` | `CONTENT_RULES`, `onpage-optimization-pass` |
| Internal linking | `internal-linking` | `STRATEGY_RULES` |
| Schema/entidades | `schema-entity` | `SCHEMA_ENTITY_MODEL` |
| Local SEO | `local-seo` | `LOCAL_SEO_PLAYBOOK` |
| Performance/CWV | `cwv-performance-seo` | `TECHNICAL_RULES` |
| WordPress implementation | `wordpress-seo-implementation` | `TECHNICAL_RULES` |
| Medição e reporting | `seo-data-analyst` | `KPI_MODEL`, `REPORTING_MODEL` |
| AI Search/GEO | `ai-search-visibility` | `STRATEGY_RULES`, `CONTENT_RULES` |
| Validação e go-live | `seo-qa` | `QUALITY_GATE`, `seo-quality-gate` |

---

## Workflow padrão

Para trabalho médio ou grande, seguir esta sequência:

1. **Definir objectivo de negócio** — o que queremos alcançar?
2. **Identificar público e serviço** — para quem? que oferta?
3. **Mapear intenção de pesquisa** — que queries? que tipo de conteúdo?
4. **Analisar concorrência/SERP** — quem rankeia? que padrões? que gaps?
5. **Definir arquitectura/página** — que página serve esta intenção?
6. **Criar brief de conteúdo** — especificar o que escrever e com que prova.
7. **Validar SEO técnico** — está tudo tecnicamente correcto?
8. **Validar visual/mobile/performance** — está rápido, legível e acessível?
9. **Validar schema quando aplicável** — schema representa conteúdo real?
10. **Implementar com WordPress Engineering** (se necessário) — com autorização, staging e rollback.
11. **Testar indexabilidade e experiência** — antes de go-live.
12. **Medir com GSC/GA4** (quando disponível) — o que está a acontecer?
13. **Actualizar backlog e decisões** — registar o que ficou e o que foi decidido.
14. **Refresh quando necessário** — SEO é manutenção contínua.

Para microtarefas simples (ex.: rever um title, verificar um canonical), usar directamente a regra ou agente relevante sem o workflow completo.

---

## Priorização

Ao priorizar trabalho SEO, usar este framework:

**Impacto:**
- tráfego potencial e intenção comercial;
- conversão e impacto em negócio;
- número de páginas afectadas;
- autoridade e reputação;
- risco técnico (bloqueio de indexação, etc.);
- prioridade de negócio.

**Esforço:**
- conteúdo (briefing, redacção, revisão);
- WordPress/design (implementação, aprovação);
- aprovação humana necessária;
- ferramentas e dependências.

**Risco:**
- produção e deploy;
- URLs e redirects;
- indexação e canonical;
- performance e mobile;
- marca e compliance;
- RGPD e dados;
- acessibilidade.

**Output recomendado:**

| Tipo | Critério |
|---|---|
| Quick wins | Alto impacto + baixo esforço + baixo risco |
| High-impact projects | Alto impacto + esforço razoável |
| Technical blockers | Bloqueia outras melhorias — resolver primeiro |
| Content opportunities | Intenção comercial forte + gap real |
| Long-term authority | Construção lenta, impacto duradouro |

---

## Handoff entre áreas

| Quem recomenda | Quem implementa/decide |
|---|---|
| `technical-seo` recomenda | `wordpress-seo-implementation` implementa (com autorização) |
| `seo-*` agentes recomendam | WordPress Engineering implementa técnica complexa |
| `seo-*` agentes recomendam | Visual Experience / Accessibility valida experiência |
| `seo-*` agentes identificam risco | System Safety valida risco e RGPD |
| `seo-lead` consolida | Supervisor aprova mudanças sensíveis |

**Regra:** SEO recomenda. Não implementa sem autorização. Não passa por cima de segurança, produção, RGPD ou rollback.

---

## Persistência

**Regra central:** análise longa sem record persistente = desperdício de contexto.

Antes de continuar uma análise grande, confirmar:

> "Isto está a ser persistido?"

Se não, criar o record a partir do template e só depois continuar.

Ver [`REPORTING_MODEL.md`](REPORTING_MODEL.md) para processo completo.

---

## Gates de governança

O SEO Growth System respeita estes limites não negociáveis:

- Segurança e RGPD/dados pessoais vencem sempre.
- Produção, rollback e credenciais pertencem ao Supervisor/System Safety.
- WordPress sensível (produção, tema activo, plugins) requer autorização explícita.
- GBP e ferramentas externas requerem autorização.
- Ferramentas pagas requerem autorização.
- Dados pessoais, dados de trabalhadores e dados de saúde nunca entram no module.
- Records nunca guardam credenciais, dados sensíveis ou informação confidencial desnecessária.

---

## Relação com outros componentes

- [`seo-lead`](../agents/seo-lead.md) — coordena tudo.
- [`seo-qa`](../agents/seo-qa.md) — valida antes de entregar.
- [`seo-quality-gate`](../skills/seo-quality-gate/SKILL.md) — procedimento de validação.
- [`QUALITY_GATE.md`](QUALITY_GATE.md) — standard de qualidade.
- [`commands/seo.md`](../commands/seo.md) — entrada por modos.
- Todos os agentes e skills do module.

---

## Regra final

SEO excelente não é apenas tráfego.

É utilidade para o utilizador, clareza para motores, confiança para o negócio, performance para todos e sustentabilidade para o projecto.

Se uma recomendação melhora ranking mas prejudica confiança, UX, performance, acessibilidade, marca ou dados — não está pronta.
