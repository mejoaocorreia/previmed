# Personal Data Classification

Este ficheiro classifica dados por risco para decidir gates, permissões e logs.

## Verde — baixo risco

Dados públicos ou sem identificação pessoal sensível.

Exemplos:
- páginas públicas;
- textos institucionais;
- assets públicos;
- nome público de empresa;
- NIPC;
- morada pública de empresa;
- código sem dados reais.

Pode ser tratado com cuidado normal.

---

## Amarelo — dados pessoais normais

Dados que identificam ou podem identificar uma pessoa.

Exemplos:
- nome;
- email;
- telefone;
- cargo;
- assinatura de email;
- interlocutor;
- responsável;
- contacto comercial;
- IP/cookie/user ID quando aplicável.

Requer:
- finalidade;
- minimização;
- escopo;
- cuidado com logs.

---

## Laranja — dados internos/confidenciais

Dados empresariais ou operacionais não públicos.

Exemplos:
- listas de clientes;
- listas de trabalhadores;
- contratos;
- contas correntes;
- cobranças;
- valores em dívida;
- histórico de contactos;
- relatórios internos;
- dados extraídos de plataformas;
- anexos de faturação;
- documentos de clientes.

Requer:
- autorização contextual;
- escopo limitado;
- evitar exportação;
- log de decisão quando relevante.

---

## Vermelho — dados especiais/sensíveis/saúde

Dados que exigem paragem obrigatória antes de tratar.

Exemplos:
- fichas de aptidão;
- exames médicos;
- relatórios de saúde;
- medicina do trabalho;
- apto/não apto;
- restrições médicas;
- baixas;
- acidentes de trabalho;
- dados biométricos;
- dados genéticos;
- menores;
- documentos pessoais;
- credenciais;
- passwords/tokens/API keys.

Requer:
- parar;
- explicar risco;
- pedir autorização explícita;
- aplicar GDPR Access Gate;
- registar decisão sem conteúdo sensível;
- escalar se houver risco elevado.

---

## Regra de dúvida

Se não for claro, subir uma categoria.

Se ainda houver dúvida, tratar como vermelho.


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
