# Decision Log

## Formato

### YYYY-MM-DD — Título

Decisão:
...

Motivo:
...

Impacto:
...

Estado:
ativo / revogado / em revisão

---

## 2026-05-19 — Organic Growth tem precedência sobre agentes/skills da raiz

Decisão:
Para qualquer trabalho SEO/Organic Growth, usar exclusivamente `.claude/agents/organic-growth/`, `.claude/skills/organic-growth/` e `.claude/commands/organic-growth/`. Versões equivalentes da raiz movidas para `.claude/_archive/`.

Motivo:
- Suite organic-growth é mais rica, hierárquica e cobre 14 áreas SEO especializadas.
- Duplicação criava risco de instruções contraditórias.

Impacto:
- 4 agentes, 7 skills e 1 command arquivados (ver `_archive/README.md`).
- Agentes da raiz não-SEO continuam ativos (supervisor, codebase-analyst, frontend-ui, etc.).

Estado:
ativo

---

## 2026-05-19 — Abordagem greenfield, SEO-first

Decisão:
Construir estratégia, arquitetura, content model e schema **antes** de instalar WordPress. WordPress entra apenas na Fase 4 (local), e go-live só na Fase 6.

Motivo:
- Não existe tema, staging nem dados (GSC/GA4 não configurados).
- Site previmed.pt em produção fica fora do scope até existir plano explícito.
- Greenfield permite SEO-first, o que é raro e estrategicamente valioso.

Impacto:
- Fase 1 deixa de ser "auditoria read-only" e passa a ser "estratégia + arquitetura".
- Fases 2-3 fazem keyword/competitor research sem dados próprios.
- Fase 4 instala WP local + cria tema com SEO já desenhado.

Estado:
ativo

---

## 2026-05-19 — MCP stack inicial: Playwright + Chrome DevTools, scope projecto

Decisão:
Instalar **apenas** Playwright MCP e Chrome DevTools MCP no scope projecto (`.mcp.json` versionado). Adiar GSC/GA4 para quando houver site em staging. Recusar ferramentas pagas (DataForSEO, Ahrefs, SerpAPI) por agora.

Motivo:
- Greenfield: sem site em staging, GSC/GA4 não têm dados úteis e adicionar a propriedade existente previmed.pt acarreta risco de tocar em produção.
- Playwright permite SERP research manual + screenshots + a11y snapshots — chega para Lote 1.4 e Fase 4.
- Chrome DevTools cobre performance/network/console quando entrar a Fase 4.
- Sem credenciais → risco de exposure mínimo.

Impacto:
- Lote 1.4 (competitor SERP) pode arrancar imediatamente via Playwright.
- Volumes de keyword permanecem qualitativos até Tier C ser reconsiderado ou GSC entrar.
- `.mcp.json` versionado: qualquer pessoa que clone o repo herda a config (sem credenciais expostas).

Estado:
ativo

---

## 2026-05-19 — Preferência inicial: Rank Math Free (a confirmar na Fase 4)

Decisão:
Trabalhar provisoriamente com a hipótese de usar **Rank Math Free** como plugin SEO. Confirmação final só depois de decidir o tema e ver que schema o tema gera nativamente.

Motivo:
- Rank Math Free oferece mais tipos de schema, redirects manager, 404 monitor e múltiplas focus keywords vs Yoast Free.
- Sub-decisão sensível ao tema: se o tema gerar schema próprio, queremos um plugin mais leve para evitar duplicação.

Impacto:
- Nenhum até à Fase 4. Documentação assume Rank Math como referência.

Estado:
em revisão
