# Previmed Core

Núcleo de regras operacionais da Previmed dentro do `.claude/`.

## Objetivo
Documentar como a equipa de agentes deve entender e navegar o repositório Previmed **agora que é mais do que SEO/WordPress**. Não cria comandos nem código — apenas a lógica operacional.

## Contexto
A Previmed passou de "pacote de Organic Growth" a **sistema operacional modular**: `departments/`, `workspaces/`, `tools/`, `manuals/`, `shared/` e `.claude/`. O SEO/WordPress é uma **capacidade** (departamento `web`), não a identidade do repo.

Dentro do `.claude/` existe agora a camada **`modules/`** — unidades reutilizáveis e exportáveis. O primeiro module estruturado é o **`seo-growth-system`** (equipa SEO completa: SEO Lead + 14 subagentes, comando `/seo`, project docs e skills). Ver [`.claude/modules/README.md`](../../modules/README.md).

Regras estruturais a reter:
- **Workspaces usam modules; não absorvem modules** (referenciam, não copiam).
- **Records reais** em `.claude/records/`; **templates de records** em `.claude/records/templates/` (SEO em `.claude/records/templates/seo/`).
- **Decisões arquiteturais** em `.claude/records/architecture/`.
- O module SEO usa os templates SEO de `.claude/records/templates/seo/` e **não depende** de archive nem de mapa de migração.

## Ficheiros
- [ROUTING_MODEL.md](ROUTING_MODEL.md) — como o supervisor identifica contexto e encaminha o trabalho.
- [STRUCTURE_MAP.md](STRUCTURE_MAP.md) — mapa da estrutura e o que cada parte significa.

## O que NÃO está aqui
- Sem comandos reais por área de negócio (nada de `/previmed`, `/careview`, `/website` ainda).
- Exceção: existe o comando `/seo` como ponte para o module `seo-growth-system`.
- Sem código funcional.
- Apenas documentação da lógica de routing e estrutura.

## Estado atual
Base inicial do núcleo operacional.

## Próximos passos
- [ ] consolidar o routing antes de considerar comandos reais
- [ ] manter o STRUCTURE_MAP alinhado com a estrutura real
