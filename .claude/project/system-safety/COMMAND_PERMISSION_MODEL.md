# Command Permission Model

## Objetivo

Classificar comandos por risco antes de executar.

## Seguro / leitura

Exemplos:
- listar ficheiros;
- verificar status;
- procurar texto;
- `git status`;
- `git diff`;
- testes sem escrita.

Pode avançar se estiver no escopo.

## Escrita limitada

Exemplos:
- criar ficheiro aprovado;
- editar ficheiro específico;
- gerar relatório;
- formatar ficheiro específico.

Requer:
- escopo;
- ficheiros autorizados;
- validação.

## Perigoso

Exemplos:
- mover pastas;
- apagar ficheiros;
- alterar permissões;
- instalar dependências;
- correr scripts;
- limpar cache;
- reset Git.

Requer:
- explicação;
- autorização;
- rollback;
- log se relevante.

## Proibido sem autorização explícita

- `rm -rf`;
- `git reset --hard`;
- `git clean`;
- force push;
- apagar base de dados;
- alterar `wp-config.php`;
- mexer em produção;
- instalar/remover plugins em produção;
- expor credenciais;
- enviar dados para terceiros;
- scripts desconhecidos.

## Antes de executar

Perguntar:

- Que comando é?
- O que altera?
- Onde corre?
- Há produção?
- Há dados?
- Há rollback?
- Há alternativa read-only?
