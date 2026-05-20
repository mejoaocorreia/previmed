# Production Safety

## Regra principal

Produção é sempre área crítica.

Se o ambiente for desconhecido, tratar como produção.

## Nunca executar sem autorização explícita

- ativar tema;
- alterar tema ativo;
- instalar/remover plugin;
- ativar/desativar plugin;
- alterar `wp-config.php`;
- mexer em base de dados;
- apagar uploads;
- alterar slugs/URLs;
- alterar redirects;
- alterar robots/sitemap/canonical;
- limpar cache de produção;
- deploy/go-live;
- alterar credenciais;
- alterar permissões;
- executar comando destrutivo.

## Antes de produção

Confirmar:

- objetivo;
- impacto;
- ambiente;
- backup;
- rollback;
- janela de execução;
- validação;
- responsável humano;
- comunicação pós-alteração.

## Regra

Produção não é local de experiências.
