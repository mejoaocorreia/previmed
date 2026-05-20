# GDPR / RGPD Access Gate

Este gate é obrigatório antes de qualquer acesso a dados amarelos, laranja ou vermelhos.

## Quando usar

Usar antes de:

- ler;
- abrir;
- resumir;
- extrair;
- copiar;
- exportar;
- enviar;
- comparar;
- automatizar;
- fazer OCR;
- usar IA/LLM;
- guardar em relatório;
- usar connector/MCP;
- anexar;
- publicar.

---

## Gate obrigatório

```md
## Possível acesso a dados pessoais / sensíveis

Detetei que esta ação pode envolver dados pessoais, dados internos,
dados de trabalhadores, dados de saúde ou informação confidencial.

### O que pode estar envolvido
[explicar tipo de dados sem expor dados reais]

### Porque isto é sensível
[explicar risco simples]

### Finalidade
[para que é necessário tratar estes dados]

### Necessidade
[porque não basta usar dados fictícios, metadados ou versão anonimizada]

### Ação pretendida
[ler / resumir / extrair / copiar / exportar / enviar / comparar / OCR / automatizar]

### Ferramenta/connector/MCP
[indicar ferramenta]

### Escopo autorizado pretendido
[ficheiros/pastas/campos/tempo]

### Risco
[baixo / médio / alto / crítico]

### Opções
1. Autorizar leitura limitada.
2. Autorizar apenas análise anonimizada.
3. Autorizar apenas metadados.
4. Fornecer dados fictícios/sanitizados.
5. Cancelar esta ação.
6. Pedir revisão humana/DPO/jurista.

### Registo
Se autorizares, a decisão será registada sem conteúdo sensível.
```

---

## O que não fazer

- Não mostrar dados reais no gate.
- Não colar anexos sensíveis no chat.
- Não guardar dados pessoais no log.
- Não pedir autorização vaga como “posso ver tudo?”.
- Não continuar por inferência.
- Não assumir autorização de uma tarefa antiga.

---

## Autorização válida

Uma autorização deve indicar:

- ação;
- finalidade;
- ficheiros/pastas;
- dados permitidos;
- dados proibidos;
- ferramenta;
- duração;
- se pode copiar/exportar;
- se precisa de log.

Autorização vaga = insuficiente.


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
