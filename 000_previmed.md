# Previmed

Entrada principal do repositório operacional da Previmed.

## O que é a Previmed neste repo
A Previmed, aqui, é o **sistema operacional digital, técnico e de processos** da empresa. Não é um site nem um projeto de SEO: é a base que organiza departamentos, frentes de trabalho, ferramentas, manuais e contexto comum, mais a equipa de agentes que opera tudo isso.

## Relação com o CortexCore
Este repo é um **repositório Git separado**, mantido dentro da árvore local do Cortex-Core (em `professional/previmed/`) por conveniência de trabalho no mesmo workspace VS Code. O Cortex-Core trata a Previmed como **área/projeto guarda-chuva profissional**; a ponte documental vive em `professional/previmed.md` (fora deste repo). Commits da Previmed são feitos **dentro deste repo**, separados dos commits do Cortex-Core.

## As partes do sistema
- **departments/** — a estrutura/departamentos da empresa (comercial, operações, comunicações, web, compliance, SST, formação). Representa *quem/que área* é responsável.
- **workspaces/** — espaços concretos de trabalho (ex.: Previmed.pt, Careview). Representa *onde* o trabalho acontece. Aqui, `workspaces` **não** significa VS Code workspace.
- **tools/** — ferramentas reutilizáveis. Representa *com o quê* se trabalha; ficam fora dos workspaces para poderem ser reutilizadas.
- **manuals/** — manuais e procedimentos. Representa *como se faz*.
- **shared/** — contexto, glossário, marca, referências e templates comuns. Representa *o que toda a gente precisa de saber*.
- **.claude/** — agentes, comandos, skills, connectors, records e regras operacionais. Representa *a equipa* que executa.
- **.claude/modules/** — *unidades reutilizáveis e exportáveis* de capacidade (agents + commands + project + skills). Primeiro module: **`seo-growth-system`** (a equipa SEO). Representa *capacidades que podem servir vários workspaces ou outros projetos*. **Workspaces usam modules; não os absorvem.**
- **.claude/records/** — registos reais. Inclui `templates/` (templates reutilizáveis de records; SEO em `templates/seo/`) e `architecture/` (decisões estruturais e razões). Os modules **usam** os templates centralizados; não guardam templates próprios.

## Não é só website/SEO
SEO e WordPress vieram da origem deste repo, mas passam a ser **capacidades dentro do departamento `web`**, não a identidade do sistema. A Previmed cobre comercial, operações, comunicações, compliance, saúde & segurança e formação — além do digital.

## Como o supervisor/agentes devem agir
Antes de agir, identificar **primeiro o contexto**:
1. **department** — que departamento é responsável?
2. **workspace** — em que espaço de trabalho concreto isto vive?
3. **tools** — que ferramentas reutilizáveis são relevantes?
4. **manuals** — existe procedimento documentado para isto?
5. **shared** — que contexto comum é preciso ler?
6. **modules** — há um module reutilizável que cobre isto? (ex.: SEO → `seo-growth-system`, via SEO Lead / `/seo`)
7. **agente/capacidade** — que agente ou skill executa?

Só depois disto é que se age. A lógica de routing está documentada em `.claude/project/previmed-core/ROUTING_MODEL.md`.

## Estado atual
Base modular inicial. Documentação explicativa, sem funcionalidades reais.

## Próximos passos
- [ ] preencher departamentos e workspaces com contexto real
- [ ] ligar manuais e tools às frentes de trabalho ativas
- [ ] consolidar o modelo de routing antes de criar comandos reais
