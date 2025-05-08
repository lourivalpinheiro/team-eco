# 🔎 Manual do usuário
# 🎯 Objetivo
Planilhas Nfse" foi desenvolvido como um projeto piloto, tendo o intuito de ajudar o processo de lançamento de notas fiscais de serviço no setor Contábil, com margem para ter suas funcionalidades expandidas.

## Como o processo funcionava antes?
1. Criar uma planilha no excel;
2. Criar o cabeçalho com colunas portadoras dos seguintes campos: 
    - DÉBITO;
    - CRÉDITO;
    - DATA;
    - VALOR;
    - HISTÓRICO;
    - NF;
    - MATRIZ;
    - FILIAL.
3. Preencher as linhas de acordo com cada variável (coluna);
4. Concatenar as colunas "HISTÓRICO" e "NF" a fim de formar uma única célula;
5. Salvar em formato .CSV;
6. Importar no sistema.


## O processo agora

1. Por meio do formulário, conseguimos inserir os dados de uma forma mais rápida, além de não precisarmos perder tempo para primeiro criar a estrutura aceita pelo sistema, nem aplicar fórmula de concatenação;
2. Após a inserção dos dados, podemos clicar no botão de **"download"**, que aparece ao passarmos o "mouse" em cima da tabela, e baixá-la em formato **.CSV**, formato de importação aceito pelo sistema;
3. Ao abrirmos o arquivo, nós deparamos com todos os dados agrupados em uma única coluna, tendo como solução a opção nativa do excel de "Texto para colunas". Para ter acesso à essa funcionalidade, **basta navegar até a aba dados, e selecionar a opção "Texto para colunas"**.
4. Selecionamos "DELIMITADO" como a nossa opção de **"TIPOS DE DADOS ORIGINAIS"** e clicamos em **AVANÇAR**;
5. Selecionamos a opção **"OUTROS"** como delimitador e clicamos em avançar e, depois, em **"CONCLUIR"**;

OBD.: ***Faz-se necessário removermos a primeira coluna e cabeçalho, assim como alterarmos o formato da data.***
