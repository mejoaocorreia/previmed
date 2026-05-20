# Current Task

## Objetivo

Construir equipa SEO/Organic Growth para Previmed (HSST B2B nacional) e produzir estratégia greenfield SEO-first antes de instalar WordPress.

## Lote atual

**Lote 1.5 concluído. Fase 1 fechada.**

## Estado

idle — aguarda direção do utilizador para Fase 2 ou Fase 3

## Ficheiros alterados (desta sessão)

- `.mcp.json` — removida flag inválida `--browser chromium` (Playwright MCP só aceita chrome|firefox|webkit|msedge; defaultpara chrome-for-testing após `install-browser`).
- `.gitignore` — adicionado `.playwright-mcp/`.
- `.claude/project/organic-growth/STRATEGY_COMPETITORS.md` — novo (Lote 1.4).

## Feito

- Lote 0.1 (preparação): git init, arquivar duplicados, preencher PROJECT_CONTEXT/FILE_MAP/DECISION_LOG.
- Lote 1.1: `STRATEGY_AUDIENCES.md` — 3 personas + funis.
- Lote 1.2: `STRATEGY_INFORMATION_ARCHITECTURE.md` — mapa de site, URLs, menu, schema.
- Lote 1.3: `STRATEGY_KEYWORDS.md` — 16 clusters, ~120 queries.
- MCPs Tier A: Playwright (chrome-for-testing instalado) + Chrome DevTools.
- Lote 1.4: `STRATEGY_COMPETITORS.md` — 12 SERPs capturadas via Playwright, 5 categorias de concorrentes, 9 lacunas priorizadas, posicionamento Previmed baseline.
- Lote 1.5: `STRATEGY.md` — documento mestre da Fase 1, consolida audiences + IA + keywords + competitors + roadmap + KPIs + decisões em aberto.

## Próximo (a confirmar com utilizador)

Fase 1 está completa (5/5 lotes). Próximas opções:

- **Fase 2:** infraestrutura de dados (GSC, GA4, decisão Ahrefs/DataForSEO, auditoria AIO expandida, crawl técnico previmed.pt actual).
- **Fase 3:** briefs de conteúdo P1 (6 pillars + 3 quick wins L1/L2/L3).
- **Fase 4:** decisões técnicas WordPress (plugin SEO, LMS, page builder, form proposta).
- Alternativa: auditoria AI Overview standalone como ponte (capturar Modo IA expandido em 5 queries).

## Retoma (se a sessão cair)

1. Ler este ficheiro.
2. `git status` (deve estar limpo após commit).
3. Confirmar Playwright funciona: `mcp__playwright__browser_navigate` para qualquer URL.
4. Pedir ao utilizador direção: Lote 1.5 A / B / C / outro.

## Notas técnicas

- Playwright MCP: chrome-for-testing instalado em `%LOCALAPPDATA%\ms-playwright\chromium-1224\`. Sem necessidade de flag `--browser`.
- Extrator JS para SERPs do Google.pt: ver chat history. Captura organic + ads + features. Snippets ocasionalmente sob consent dialog — não é evidência de ausência.
- AI Overview detectado em 12/12 queries mas só como "link Modo IA". Expandir é trabalho futuro.
