# Security Rules

## Ações críticas

Exigem confirmação explícita:

- ativar tema;
- alterar tema ativo;
- instalar/remover plugins;
- ativar/desativar plugins;
- alterar wp-config.php;
- mexer na base de dados;
- mexer em uploads;
- apagar ficheiros;
- alterar slugs/URLs;
- alterar redirects;
- alterar formulários;
- alterar menus críticos;
- alterar links externos importantes;
- fazer deploy;
- limpar cache de produção se puder afetar visitantes;
- alterar credenciais;
- alterar permissões;
- correr comandos destrutivos.

## Produção

Não mexer em produção sem confirmação.

Preferir:
- ambiente local;
- branch;
- staging;
- preview/theme switcher;
- tema novo.

## Plugins

Não instalar plugins sem autorização.

Antes de sugerir plugin:
- justificar necessidade;
- verificar alternativa sem plugin;
- avaliar manutenção;
- avaliar performance;
- avaliar segurança;
- avaliar lock-in.

## Dados e credenciais

Não expor:
- passwords;
- tokens;
- cookies;
- API keys;
- app passwords;
- sessões;
- dados privados.

## Links externos/áreas de acesso

Tratar como sensíveis:
- CTAs para plataformas externas;
- área de cliente/acesso;
- links de login;
- formulários;
- integrações.

Validar antes de alterar.

## MCPs

MCPs devem seguir princípio de menor privilégio.

Não usar MCP com acesso destrutivo sem necessidade.
Não expor produção a MCPs experimentais sem análise de risco.
