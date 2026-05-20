# MCP Stack

## Estado actual (2026-05-19)

Configuração em `.mcp.json` (project scope):

| MCP | Estado | Comando | Versão | Credenciais |
|---|---|---|---|---|
| `playwright` | ✅ Activo | `npx -y @playwright/mcp@latest` | latest | nenhuma |
| `chrome-devtools` | ✅ Activo | `npx -y chrome-devtools-mcp@latest` | latest | nenhuma |

**Decisões registadas** (ver `DECISION_LOG.md`):
- Tier B (GSC/GA4) adiado até existir site novo em staging.
- Tier C (DataForSEO/SerpAPI pagos) recusado por agora — SERP via Playwright manual.
- Tier D (WordPress, GBP, Figma) adiado para fase apropriada.

**Como adicionar MCPs futuros** (project scope):
```bash
claude mcp add --scope project <nome> -- <comando> [args]
```

Verificar saúde:
```bash
claude mcp list
```

Remover:
```bash
claude mcp remove <nome>
```

---

## Princípio

MCP é uma forma padronizada de ligar agentes a ferramentas e fontes de contexto.

Usar MCPs apenas quando trazem valor claro.

Evitar instalar MCPs só porque existem.

## MCPs essenciais/recomendados

### Filesystem / projeto

Uso:
- ler ficheiros;
- pesquisar;
- editar escopo permitido.

Risco:
- pode alterar ficheiros sensíveis.

Regra:
- restringir à pasta do projeto;
- não permitir escrita fora do escopo.

### Git / GitHub

Uso:
- status;
- diff;
- branches;
- commits;
- PRs;
- issues.

Risco:
- comandos perigosos podem reverter/apagar trabalho.

Regra:
- usar para status/diff/checkpoint;
- comandos destrutivos só com confirmação.

### Playwright MCP

Uso:
- preview;
- navegar site;
- testar UI;
- screenshots;
- mobile/desktop;
- fluxos de menu/formulário.

Nota:
- Playwright MCP usa snapshots de acessibilidade e pode manter perfil persistente por projeto.
- Bom para exploração visual/interativa.
- Para testes repetíveis, scripts Playwright/CLI podem ser mais eficientes.

Regra:
- não executar ações reais em produção;
- usar staging/preview;
- não submeter formulários reais sem autorização.

### Chrome DevTools MCP

Uso:
- debug no browser;
- console;
- network;
- performance;
- identificar problemas reais de frontend.

Regra:
- usar para diagnóstico e performance;
- não alterar produção.

### Lighthouse / PageSpeed

Uso:
- performance;
- Core Web Vitals;
- acessibilidade;
- SEO técnico;
- boas práticas.

Regra:
- medir antes/depois de alterações importantes.

### SEO MCP / Search Console / GA4

Uso:
- Search Console;
- GA4;
- inspeção de URLs;
- sitemaps;
- indexação;
- PageSpeed;
- schema/robots.

Regra:
- acesso read-only por defeito;
- ações de indexação/submit só com aprovação.

### WordPress MCP / WP-CLI / REST

Uso:
- posts/pages;
- estrutura;
- blocos;
- conteúdo;
- eventualmente plugins/settings.

Risco:
- pode alterar conteúdo/produção.

Regra:
- preferir read-only inicialmente;
- escrita só em staging/preview;
- publicação/alteração em produção só com confirmação.

## MCPs opcionais

- Figma MCP: ler designs/tokens/componentes.
- Browser/search MCP: pesquisa competitiva e referência visual.
- Image/asset tools: moodboards/assets.
- Database read-only: apenas se necessário e seguro.
- Sentry/logs: erros reais.
- Analytics: comportamento, top pages, fontes.

## MCPs para SEO

Prioridade:
1. Google Search Console;
2. PageSpeed/Lighthouse;
3. GA4;
4. crawler/sitemap;
5. schema validator;
6. SERP/keyword tool, se disponível.

## Segurança MCP

MCPs podem ampliar risco.

Antes de usar MCP novo:
- identificar permissões;
- saber se é read-only ou write;
- avaliar manutenção;
- verificar fonte;
- limitar escopo;
- evitar credenciais em texto;
- confirmar ações destrutivas.

## Recomendação inicial

Começar com:
- Git/GitHub;
- Filesystem;
- Playwright;
- Chrome DevTools;
- Lighthouse/PageSpeed;
- Search Console/SEO MCP quando houver acesso;
- WordPress MCP apenas em staging ou read-only.
