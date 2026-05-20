# Connector Permission Matrix

## Níveis

| Nível | Pode | Não pode |
|---|---|---|
| Read-only | ler/listar/consultar | escrever/apagar/enviar |
| Limited write | editar ficheiros aprovados | produção/dados sensíveis/credenciais |
| Controlled execute | comandos aprovados | destrutivos sem autorização |
| Restricted | nada sem aprovação | qualquer ação autónoma |

## Connectors

| Connector | Default | Elevação possível | Riscos |
|---|---|---|---|
| filesystem | read-only | limited write | leitura indevida, overwrite, exfiltração |
| git | read-only | controlled execute | reset, clean, force push |
| github | read-only | limited write | PR/issue com dados, secrets, workflows |
| playwright | read-only/test | controlled execute | áreas autenticadas, dados reais |
| lighthouse | read-only | n/a | resultados incompletos, falso conforto |
| gmail | restricted | limited action | dados pessoais, anexos, envio externo |
| ocr | restricted | read-only limitado | transformar documento sensível em texto |
| context7/docs | read-only | n/a | documentação desatualizada ou mal aplicada |

## Regra

Qualquer elevação deve indicar:
- tarefa;
- connector;
- ação;
- escopo;
- duração;
- dados permitidos/proibidos;
- autorização;
- log.
