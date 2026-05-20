# Incident Response

## O que é incidente

Incidente é qualquer situação em que possa ter havido:

- acesso indevido;
- cópia indevida;
- alteração indevida;
- perda;
- destruição;
- divulgação;
- envio;
- exportação;
- publicação;
- exposição de credenciais;
- exposição de dados pessoais;
- exposição de dados de saúde;
- comando destrutivo;
- alteração em produção sem autorização.

## Primeiro passo

Parar imediatamente.

Não:
- esconder;
- apagar evidência;
- corrigir às cegas;
- continuar a tarefa;
- enviar mais dados;
- fazer commits;
- limpar logs sem orientação.

## Classificar

### Confidencialidade

Dados foram vistos/divulgados por quem não devia.

### Integridade

Dados foram alterados indevidamente.

### Disponibilidade

Dados foram perdidos, apagados ou ficaram indisponíveis.

## Resposta inicial

1. Parar.
2. Conter.
3. Identificar ação.
4. Identificar ferramenta.
5. Identificar ficheiros/áreas.
6. Identificar tipo de dados.
7. Avaliar risco.
8. Registar sem dados sensíveis.
9. Informar utilizador.
10. Aguardar decisão humana.

## Data breach

Se envolver dados pessoais, aplicar regras RGPD.

A CNPD indica que a notificação deve ocorrer em conformidade com o Art. 33.º,
em regra até 72 horas após conhecimento, salvo se não for suscetível de resultar
em risco para direitos e liberdades.

O agente não decide sozinho notificação.
Deve sinalizar, documentar e escalar.

## Template

```md
# Incident Report

## Data/Hora
...

## Tipo
[segurança / dados / produção / credenciais / comando / connector]

## O que aconteceu
...

## Ferramenta/ação
...

## Dados/áreas possivelmente afetadas
[não incluir conteúdo sensível]

## Risco
[baixo / médio / alto / crítico]

## Contenção imediata
...

## Ação humana necessária
...

## Estado
[aberto / em análise / contido / fechado]
```


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
