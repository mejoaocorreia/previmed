# Architecture Log

Registo cronológico das decisões de arquitetura do repositório Previmed.

---

## 2026-05-24 — Previmed modular architecture decisions

### 1. `departments/`
Usamos `departments` porque é a linguagem real usada dentro da empresa.

### 2. `workspaces/`
Usamos `workspaces` para espaços concretos de trabalho. Neste repo, `workspaces` **não** significa VS Code workspace.

### 3. Não usamos `projects` nem `initiatives`
Rejeitados porque não representam bem a forma como queremos organizar frentes concretas de trabalho.

### 4. Não usamos `domains`
Rejeitado para evitar confusão com domínios de websites.

### 5. `tools/`
Tools são ferramentas reutilizáveis. Podem nascer por necessidade de um workspace, mas não pertencem ao workspace. Podem futuramente virar repos próprios, ferramentas públicas, open source ou produtos.

### 6. `manuals/`
Manuals centraliza procedimentos. Os procedimentos podem estar relacionados com departments ou workspaces, mas vivem num sítio próprio.

### 7. `shared/`
Shared guarda contexto comum, glossário, marca, referências e templates globais. Não deve guardar dados sensíveis em bruto nem tarefas operacionais.

### 8. `.claude/modules/`
Modules são unidades reutilizáveis/exportáveis de capacidade. Podem conter agentes, comandos, project docs e skills. O primeiro module é `seo-growth-system`.

### 9. Workspaces usam modules; não absorvem modules
Um workspace pode referenciar um module, mas não deve copiar agentes, skills ou regras para dentro dele. O workspace guarda contexto específico; o module guarda capacidade reutilizável.

### 10. Templates de records
Templates vivem em `.claude/records/templates/`. Modules podem referenciar templates, mas não devem guardar templates de records dentro do próprio module. Os templates SEO ficam em `.claude/records/templates/seo/`.

### 11. Migration/archive
O `MIGRATION_MAP.md` e o `.claude/_archive/` foram úteis durante a migração, mas não fazem parte da arquitetura final. A estrutura final vive **sem dependência** do archive. Ambos foram removidos em 2026-05-24.

---

> Adicionar novas entradas no topo (mais recente primeiro), com data e título.
