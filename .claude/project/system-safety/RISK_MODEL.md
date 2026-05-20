# Risk Model

## Objetivo

Classificar tarefas por risco para decidir se podem avançar diretamente,
se precisam de plano, autorização, rollback ou bloqueio.

## Baixo risco

Exemplos:
- documentação pública;
- ficheiros vazios;
- ajuste local sem impacto;
- texto sem dados pessoais;
- análise sem ferramentas sensíveis.

Pode avançar diretamente.

## Médio risco

Exemplos:
- alterações em `.claude/`;
- criação/edição de agentes/skills;
- CSS/JS local;
- alterações em página;
- uso read-only de repo;
- análise com dados internos não sensíveis.

Requer:
- escopo claro;
- plano curto;
- validação;
- reportar ficheiros alterados.

## Alto risco

Exemplos:
- WordPress sensível;
- functions.php/header/footer;
- SEO estrutural;
- slugs/redirects/schema;
- dados internos;
- contas correntes;
- emails reais;
- connectors com escrita;
- scripts;
- vários ficheiros.

Requer:
- análise;
- lote;
- autorização se necessário;
- rollback;
- validação;
- log se relevante.

## Crítico

Exemplos:
- produção;
- base de dados;
- plugins;
- wp-config.php;
- credenciais;
- tokens;
- dados de saúde;
- fichas de aptidão;
- exames;
- envio externo;
- comandos destrutivos;
- exportação de dados;
- incidente.

Requer:
- parar;
- explicar risco;
- autorização explícita;
- log;
- revisão humana;
- rollback;
- não executar automaticamente.

## Regra de dúvida

Se houver dúvida, subir risco.
Se envolver dados vermelhos, tratar como alto/crítico.
