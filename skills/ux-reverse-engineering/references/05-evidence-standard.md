# 05 | Padrão de evidência, citações e calibração

## Hierarquia operacional
1. Inspeção direta autorizada com data, plataforma, região, variante, conta/plano e passos reprodutíveis (forte para observação, não para causa).
2. Documentação oficial, help, release notes ou estudo metodologicamente descrito (forte para comportamento documentado dentro do escopo declarado).
3. Vídeos e capturas datados de usuários/reviewers ou testes independentes (úteis, com possível desatualização e viés).
4. Opiniões em comunidades, reviews e artigos de UX (bons para gerar hipóteses; não comprovam generalização).
5. Conhecimento prévio e inferência não inspecionada (ilustrativos; rotular como tais).

## Registro obrigatório por afirmação material
`ID | afirmação | app/versão/região | status [observado/documentado/inferido/desconhecido] | fonte URL ou arquivo | data da fonte | data da consulta | confiança [alta/média/baixa] | limitações`

Use `templates/evidence-ledger.csv`. Se ausência de URL, registre evidência direta por arquivo fornecido ou marque sem verificação externa. Não simule data de acesso.

## Separar mecanismo, causalidade e valor
- "A interface oferece X" é descrição do produto.
- "X pode reduzir a carga cognitiva" é hipótese teórica.
- "X causou maior conversão" é afirmação causal, necessita experimento, identificação causal confiável ou pesquisa robusta, com população/métrica/intervalo.
- "X é ético" é julgamento contextual, requer analisar transparência, reversibilidade e autonomia.

## Escala de confiança
- **Alta:** múltiplas fontes consistentes e atuais, observação reprodutível, escopo claro.
- **Média:** uma fonte sólida ou convergência parcial, mudanças entre versões possíveis.
- **Baixa:** material antigo, anedótico, hipótese ou evidências conflitantes.

Não confundir confiança sobre **existência da funcionalidade** com confiança sobre **eficácia da intervenção**. Cite a fonte junto da alegação no relatório. Relate diferenças por versão, dispositivo, país, plano, sessão e teste A/B.

## Padrões de incerteza recomendados
- "No vídeo fornecido, a mecânica é representada como..."
- "É plausível que o gatilho dependa de..., mas não há evidência do algoritmo interno."
- "Não foi possível confirmar se a experiência segue ativa em outubro de 2026."
- "A eficácia deve ser medida no nosso público por experimento e guardrails."
