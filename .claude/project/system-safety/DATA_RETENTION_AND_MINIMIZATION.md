# Data Retention and Minimization

## Objetivo

Evitar que agentes, skills, commands e reports guardem mais dados do que necessário.

## Minimização

Antes de usar dados, tentar nesta ordem:

1. Sem dados pessoais.
2. Dados fictícios.
3. Metadados.
4. Contagens.
5. IDs internos.
6. Dados mascarados.
7. Dados pseudonimizados.
8. Dados reais limitados, só se necessário e autorizado.

## Retenção

Não guardar em `.claude/records/`:

- dados de saúde;
- fichas de aptidão;
- exames;
- relatórios médicos;
- anexos;
- emails completos;
- passwords;
- tokens;
- credenciais;
- dados pessoais desnecessários.

Guardar apenas:

- decisão;
- tipo de dado;
- finalidade;
- ferramenta usada;
- risco;
- autorização;
- limites;
- resultado sem conteúdo sensível.

## Mascaramento

Exemplos:

- `joao.silva@empresa.pt` → `j***@empresa.pt`
- `SMTP_PASS=valor` → `SMTP_PASS=********`
- `123456789` → `***6789`
- nome de trabalhador → `Trabalhador A`

## Anonimização vs pseudonimização

- Dados anonimizados não devem permitir reidentificação.
- Dados pseudonimizados continuam a ser dados pessoais se for possível reidentificar.

Regra:
Pseudonimização reduz risco, mas não remove RGPD.


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
