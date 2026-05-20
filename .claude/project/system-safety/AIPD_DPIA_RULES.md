# AIPD / DPIA Rules

AIPD significa Avaliação de Impacto sobre a Proteção de Dados.
DPIA é o termo inglês equivalente.

## Quando considerar AIPD

Considerar AIPD quando a tarefa envolver:

- dados de saúde;
- categorias especiais de dados;
- dados de trabalhadores em escala relevante;
- profiling;
- decisões automatizadas com impacto;
- monitorização sistemática;
- videovigilância em larga escala;
- uso novo de tecnologia;
- cruzamento de bases de dados;
- AI/LLM com dados pessoais reais;
- tratamento que possa gerar risco elevado.

## O que o agente deve fazer

O agente não decide juridicamente se a AIPD é obrigatória.

Deve:

1. identificar sinais de risco elevado;
2. parar antes de tratar dados;
3. explicar porque pode exigir AIPD;
4. sugerir revisão por DPO/jurista/direção;
5. não executar processamento até decisão humana se o risco for alto/crítico.

## Mini-checklist

- Que tratamento é proposto?
- Que dados são usados?
- Quem são os titulares?
- Qual a finalidade?
- Há categorias especiais?
- Há grande escala?
- Há decisão automatizada?
- Há nova tecnologia?
- Há alternativa menos intrusiva?
- Quais os riscos?
- Que medidas mitigam?

## Regra

Se envolver dados de saúde/trabalhadores + automação/IA + escala relevante,
tratar como possível AIPD até avaliação humana.


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
