# Risk Model

## Baixo risco

- texto;
- labels;
- pequenas cores;
- pequenos ajustes CSS locais;
- alinhamentos simples;
- imagens decorativas;
- correção visual isolada.

Pode ser direto.

## Médio risco

- novas secções;
- cards/listas;
- template-parts;
- CSS de página;
- JS local;
- pequenos filtros UI;
- alterações responsive;
- ajustes de conteúdo em páginas principais;
- alteração de CTA local.

Requer:
- plano curto;
- critérios de aceitação;
- teste visual.

## Alto risco

- functions.php;
- header.php;
- footer.php;
- JS global;
- CSS global;
- menus;
- formulários;
- SEO estrutural;
- slugs/URLs;
- redirects;
- schema;
- performance;
- motion pesado;
- alteração que afeta várias páginas;
- alterações em templates globais.

Requer:
- análise;
- lote;
- checkpoint;
- testes;
- revisão.

## Crítico

- ativar tema em produção;
- alterar tema ativo;
- instalar/remover/ativar/desativar plugins;
- wp-config.php;
- base de dados;
- uploads;
- WordPress core;
- deploy/go-live;
- apagar ficheiros;
- credenciais;
- permissões;
- comandos destrutivos;
- alterações irreversíveis.

Requer:
- confirmação explícita;
- backup/checkpoint;
- rollback;
- validação manual.

## Regra

Se houver dúvida, subir o nível de risco.
