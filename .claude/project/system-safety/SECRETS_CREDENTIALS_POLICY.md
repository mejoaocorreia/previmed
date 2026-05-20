# Secrets and Credentials Policy

## O que são segredos

- passwords;
- tokens;
- API keys;
- cookies;
- session tokens;
- SMTP passwords;
- credenciais WordPress;
- credenciais de base de dados;
- OAuth tokens;
- chaves privadas;
- `.env`;
- `wp-config.php`;
- ficheiros de configuração com acessos.

## Regra principal

Se encontrares um segredo:

1. parar;
2. não copiar;
3. não mostrar;
4. não guardar em logs;
5. não colocar em commit/issue/PR;
6. avisar o utilizador;
7. continuar apenas com autorização e mascaramento.

## Mascaramento

Exemplos:

- `API_KEY=********`
- `SMTP_PASS=********`
- `DB_PASSWORD=********`
- token: mostrar só últimos 4 caracteres se necessário.

## Se um segredo foi exposto

Tratar como incidente.

Ações possíveis:
- revogar token;
- rodar credencial;
- remover do histórico;
- verificar acessos;
- registar incidente;
- validar com responsável humano.


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
