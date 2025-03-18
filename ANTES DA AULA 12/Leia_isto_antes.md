
# CONSULTE A DOCUMENTAÇÃO DO PANDAS
https://pandas.pydata.org/docs/user_guide/index.html#user-guide

# Instale o Pandas com o pip

# USE ISTO NO TERMINAL
    pip install pandas

# IMPORTE O MESMO NO SEU ARQUIVO
    import pandas as pd


# Ajudinha básica
    Criação e visualização
        pd.DataFrame(#Recebe a variavel com os dados) → Cria o DataFrame a partir do dicionário
# df(Data Frame) seria -> df = pd.DataFrame(Dados)
        df.head() → Mostra as primeiras linhas
        df.info() → Mostra informações gerais (tipos, nulos, etc.)
        df.describe() → Estatísticas básicas dos dados numéricos

    Manipulação de colunas
        df['NovaColuna'] = ... → Criar nova coluna (ex: calcular total da venda)
        df[['Coluna1', 'Coluna2']] → Selecionar colunas específicas

    Filtros
        df[df['Valor'] > 100] → Filtrar linhas com base em uma condição
        df[(df['Valor'] > 50) & (df['Quantidade'] > 2)] → Filtros com múltiplas condições

    Agrupamento e estatísticas
        df.groupby('Vendedor') → Agrupar os dados
        .sum(), .mean(), .count() → Aplicar operações nos grupos
        df.groupby('Produto')['Quantidade'].sum() → Soma total por produto

     Ordenação
        df.sort_values(by='Total', ascending=False) → Ordenar DataFrame

    Extras úteis
        df.drop(columns=['Coluna']) → Remover coluna
        df.reset_index() → Resetar o índice após agrupamentos ou filtros
        df.to_csv('arquivo.csv', index=False) → Exportar para CSV