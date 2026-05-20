# MCP / Connector Permission Model

## Objetivo

Definir como connectors/MCPs podem ser usados com segurança.

## Princípio

Read-only por defeito.
Menor privilégio possível.
Escopo explícito.
Log quando houver risco médio/alto.

## Níveis

### Read-only

Pode:
- listar;
- ler ficheiros autorizados;
- consultar estado;
- recolher metadados.

Não pode:
- escrever;
- apagar;
- enviar;
- executar;
- exportar.

### Limited write

Pode:
- alterar ficheiros específicos;
- criar ficheiros aprovados;
- atualizar docs no escopo.

Não pode:
- mexer em produção;
- tocar dados sensíveis;
- alterar credenciais;
- executar comandos destrutivos.

### Controlled execute

Pode executar apenas comandos aprovados.

Requer:
- comando explícito;
- motivo;
- ambiente;
- rollback;
- autorização se risco alto.

### Restricted / forbidden

Usar quando:
- dados de saúde;
- produção;
- credenciais;
- exportações;
- envio externo;
- OCR sensível;
- comando destrutivo.

## Autorização mínima

Toda autorização deve indicar:

- connector;
- ação;
- ficheiros/pastas;
- ambiente;
- duração;
- dados permitidos;
- dados proibidos;
- read/write/execute;
- necessidade de log.

## Riscos MCP

- prompt injection por conteúdo externo;
- tool poisoning;
- excessive agency;
- permissões amplas;
- execução local de comandos;
- exfiltração;
- alteração de ficheiros;
- acesso a credenciais;
- confiança indevida em outputs.

## Regra

Connector não é “confiança”.
Connector é poder.
Poder exige limites.


## Referências externas base

- RGPD — Regulamento (UE) 2016/679: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Comissão Europeia — Data protection explained: https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en
- Comissão Europeia — Direitos dos titulares: https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en
- CNPD — Registo de atividades de tratamento: https://www.cnpd.pt/organizacoes/outras-obrigacoes/registo-de-atividades-de-tratamento/
- CNPD — Violação de dados ou data breach: https://www.cnpd.pt/organizacoes/outras-obrigacoes/violacao-de-dados-ou-data-breach/
- CNPD — Encarregado de Proteção de Dados: https://www.cnpd.pt/organizacoes/obrigacoes/encarregado-de-protecao-de-dados/
- CNPD — Avaliação de Impacto sobre a Proteção de Dados: https://www.cnpd.pt/organizacoes/obrigacoes/avaliacao-de-impacto/
- EDPB — Data Protection by Design and by Default: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-42019-article-25-data-protection-design-and_en
- EDPB — Personal Data Breach Notification Guidelines 9/2022: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-92022-personal-data-breach-notification-under_en
- EDPB — Data Breach Examples Guidelines 01/2021: https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-012021-examples-regarding-personal-data-breach_en
- MCP Security Best Practices: https://modelcontextprotocol.io/specification/2025-06-18/basic/security_best_practices
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
- CNCS — Boas práticas em teletrabalho: https://www.cncs.gov.pt/pt/ciberseguranca-em-teletrabalho/
