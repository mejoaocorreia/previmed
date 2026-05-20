# Dependencies and Installs Policy

## Regra principal

Não instalar dependências, plugins, pacotes, MCPs, connectors ou ferramentas
sem autorização explícita.

## Antes de sugerir instalação

Explicar:

- para que serve;
- porque é necessário;
- alternativa sem instalar;
- impacto em segurança;
- impacto em performance;
- impacto em manutenção;
- impacto em produção;
- permissões necessárias;
- como remover/reverter.

## Alto risco

- plugins WordPress;
- MCP servers;
- scripts npm/pip desconhecidos;
- ferramentas com acesso filesystem;
- ferramentas com acesso Git/GitHub;
- ferramentas com acesso email;
- ferramentas com acesso browser/autenticação;
- dependências sem manutenção;
- pacotes com postinstall scripts.

## Regra

Instalar é criar dependência.
Dependência é risco.
