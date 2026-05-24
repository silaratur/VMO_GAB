# Opensquad Preferences

- **User Name:** Marcelo Silveira
- **Output Language:** Português (Brasil)
- **IDEs:** claude-code
- **Date Format:** YYYY-MM-DD
- **Document Output Format:** PDF por padrão — toda documentação gerada pelos agentes VMO deve ser entregue em PDF. Gerar DOCX somente se explicitamente solicitado. Nunca gerar os dois formatos automaticamente sem solicitação explícita. O arquivo .md interno é mantido como fonte de verdade, mas o que é compartilhado via SendUserFile é o .pdf (ou .docx quando pedido). Utilitário: `python3 _opensquad/utils/md_to_docs.py <arquivo.md> --format pdf` (ou `--format docx` ou `--format both`). O PDF deve seguir padrão formal de documentos de projeto: cabeçalho institucional com ID e título do projeto, tipografia profissional, tabelas formatadas, numeração de página, rodapé com elaborador e data — não um simples HTML-to-PDF.
