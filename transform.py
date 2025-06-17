import pandas as pd

# Carrega o JSON em um dataframe
df = pd.read_json('resultados.json')

# Transforma colunas do Dataframe em Linhas
df_melted = df.melt(var_name="Rodada", value_name="Dados")

# Expande o dicionário da coluna dados, transformando as chaves em colunas
df_expandido = df_melted["Dados"].apply(pd.Series)

# Adicionar a coluna de Rodada de volta
df_expandido["Rodada"] = df_melted["Rodada"]

df_expandido.to_csv('tabela.csv')