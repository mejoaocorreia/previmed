# Routing Model

Como o supervisor/agentes encaminham o trabalho na Previmed.

## Objetivo
Definir a lógica de routing para reduzir ambiguidade e garantir que cada pedido é tratado no contexto certo — incluindo a camada de **modules**.

## Identificação de contexto (por ordem)
Antes de agir, o supervisor identifica:
1. **workspace** — em que espaço de trabalho concreto isto vive? (ex.: previmed_pt, careview)
2. **department** — que departamento é responsável? (commercial, operations, communications, web, compliance, health_safety, training)
3. **manuals** — existe procedimento documentado em `manuals/`?
4. **shared** — que contexto comum de `shared/` é preciso ler?
5. **tools** — que ferramentas reutilizáveis de `tools/` são relevantes?
6. **modules** — existe um module reutilizável que cobre esta capacidade? (ex.: `seo-growth-system`)
7. **agente/capacidade** — que agente ou skill específico executa?

## Modules
Os modules vivem em [`.claude/modules/`](../../modules/README.md) e são **unidades reutilizáveis** (agents + commands + project + skills). O supervisor não executa a capacidade do module diretamente — **encaminha para o líder do module**.

Regras de modules e records:
- **Workspaces usam modules; não absorvem modules.** Um workspace referencia um module, mas **não** copia agentes/skills/regras para dentro dele. O workspace guarda contexto específico; o module guarda capacidade reutilizável.
- **Records reais** vivem em `.claude/records/`.
- **Templates de records** vivem em `.claude/records/templates/` (SEO em `.claude/records/templates/seo/`). Os modules **referenciam** estes templates; **não** guardam templates próprios.
- **Decisões arquiteturais** vivem em `.claude/records/architecture/` (distinto de `.claude/records/decisions/`, que são logs operacionais).
- O module SEO usa os templates SEO a partir de `.claude/records/templates/seo/` e **já não depende** de migração nem de qualquer archive.

### Regra SEO (module `seo-growth-system`)
Quando o pedido tocar **SEO, pesquisa orgânica, web content, Google, SERP, schema, performance SEO, AI Search ou WordPress SEO**, usar o module:
[`.claude/modules/seo-growth-system/`](../../modules/seo-growth-system/README.md).

- O **supervisor geral não faz SEO diretamente** — encaminha para o **SEO Lead** do module ([`agents/seo-lead.md`](../../modules/seo-growth-system/agents/seo-lead.md)), ou via comando `/seo`.
- O SEO Lead decide os subagentes, coordena e passa por SEO QA antes de entregar.
- O SEO Growth System é **reutilizável e exportável**: não pertence exclusivamente à Previmed; pode ser usado por outros projetos. A Previmed usa-o quando necessário.

## Regras de encaminhamento
- **SEO** só quando o pedido tocar web/search/content/WordPress SEO — não contaminar outros contextos.
- **compliance / system-safety** entra **transversalmente** sempre que houver dados sensíveis, RGPD, permissões, risco ou produção.
- **Careview** é workspace próprio (`workspaces/careview/`).
- **Previmed.pt** é workspace próprio (`workspaces/previmed_pt/`).
- **Tools reutilizáveis** ficam em `tools/`, não dentro dos workspaces.
- **Modules** são chamados pelo supervisor/comandos; não se auto-ativam e não substituem a governação do supervisor.

## Compatibilidade Claude Code
O Claude Code não descobre conteúdo dentro de `.claude/modules/`. Por isso existem **pontes**: comando global `.claude/commands/seo.md` e pontes de agentes em `.claude/agents/seo-growth-system/`. A fonte da verdade é sempre o module.

## O que este modelo não faz
- Não define comandos reais por área de negócio (`/previmed`, `/careview`, `/website` **não** existem ainda).
- O único comando real ligado a um module é `/seo` (ponte para o `seo-growth-system`).

## Estado atual
Routing com camada de modules documentado. Um module ativo: `seo-growth-system`.

## Próximos passos
- [ ] validar a ordem de identificação de contexto na prática
- [ ] avaliar futuros modules (careview, compliance, wordpress, visual, communications, operations) — só quando justificado
