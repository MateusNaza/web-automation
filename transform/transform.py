import pandas as pd

def load_to_csv(json):
    # Carrega o JSON em um dataframe
    df = pd.read_json(json)

    # Transforma colunas do Dataframe em Linhas
    df_melted = df.melt(var_name="Rodada", value_name="Dados")

    # Expande o dicionário da coluna dados, transformando as chaves em colunas
    df_expandido = df_melted["Dados"].apply(pd.Series)

    # Adicionar a coluna de Rodada de volta
    df_expandido["Rodada"] = df_melted["Rodada"]

    csv_file_name = 'output/tabela.csv'

    df_expandido.to_csv(csv_file_name, sep='|')

    return f'\nDados históricos disponíveis em {csv_file_name}!\n'