# Data Protection Policy

Este ficheiro define a política operacional de proteção de dados para agentes,
skills, commands, connectors e workflows.

Não substitui aconselhamento jurídico, DPO/EPD ou decisão da direção.
Serve para impedir tratamento indevido de dados e obrigar a gates claros.

---

## Princípios RGPD operacionais

Antes de tratar dados pessoais, verificar:

1. **Licitude, lealdade e transparência**
   - há finalidade legítima?
   - o titular poderia perceber este tratamento?

2. **Limitação das finalidades**
   - os dados são usados apenas para a finalidade definida?

3. **Minimização**
   - estamos a usar só o necessário?

4. **Exatidão**
   - os dados podem estar errados/desatualizados?

5. **Limitação da conservação**
   - vamos guardar só pelo tempo necessário?

6. **Integridade e confidencialidade**
   - há segurança adequada?

7. **Responsabilização**
   - conseguimos demonstrar decisão, autorização e limites?

---

## Perguntas obrigatórias

Antes de ler/processar/copiar/exportar/enviar dados pessoais:

- Qual é a finalidade?
- Que dados são necessários?
- Há alternativa anonimizada?
- Há alternativa com metadados?
- Quem autorizou?
- Que ferramenta vai aceder?
- O acesso é read-only?
- Vai haver exportação?
- Vai haver envio externo?
- Vai haver log?
- Vai haver retenção?
- É dado de saúde/categoria especial?
- Precisa de AIPD?
- Precisa de DPO/jurista?

---

## Dados de saúde e trabalhadores

Dados de saúde e dados ocupacionais devem ser tratados como vermelhos.

Exemplos:
- fichas de aptidão;
- exames;
- relatórios médicos;
- apto/não apto;
- restrições;
- acidentes;
- medicina do trabalho.

Regra:
Não analisar conteúdo clínico/sensível sem autorização explícita e finalidade clara.

---

## AI / LLM com dados pessoais

Não usar modelos/IA para tratar dados pessoais reais se a tarefa puder ser feita com:

- dados fictícios;
- dados anonimizados;
- metadados;
- contagens;
- estrutura sem conteúdo;
- amostra sanitizada.

Quando for inevitável:
- aplicar GDPR Access Gate;
- limitar escopo;
- mascarar dados;
- não guardar conteúdo sensível;
- não enviar para terceiros sem validação;
- registar decisão.

---

## Direitos dos titulares

Se uma tarefa envolver pedido de titular, lembrar que podem existir direitos de:

- informação;
- acesso;
- retificação;
- apagamento;
- limitação;
- portabilidade;
- oposição;
- revisão humana em decisões automatizadas.

Não responder juridicamente sem validação humana.

---

## Escalação

Escalar para humano/DPO/jurista/direção quando:

- dados de saúde;
- tratamento em larga escala;
- risco elevado;
- incidente;
- pedido de titular complexo;
- transferência para terceiros;
- decisão automatizada;
- dúvida sobre base legal;
- dúvida sobre conservação;
- conflito entre produtividade e privacidade.

Ficheiros relacionados:
[PERSONAL_DATA_CLASSIFICATION.md](./PERSONAL_DATA_CLASSIFICATION.md) ·
[GDPR_ACCESS_GATE.md](./GDPR_ACCESS_GATE.md) ·
[AIPD_DPIA_RULES.md](./AIPD_DPIA_RULES.md)


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
