from bs4 import BeautifulSoup
import pandas as pd

# Lendo o HTML do arquivo
with open('html.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Encontrando todos os times
teams = [team.text.strip() for team in soup.find_all('div', class_='match-team')]

# Agrupando os times de dois em dois
match_pairs = list(zip(teams[0::2], teams[1::2]))  # Pega pares consecutivos

# Parser Odds
odd_values = [odd.text.strip() for odd in soup.find_all('span', class_='odd__value')]
triple_odds = list(zip(odd_values[0::3], odd_values[1::3], odd_values[2::3]))

# Criando o DataFrame
df = pd.DataFrame(match_pairs, columns=['team1', 'team2'])

df[['1', 'x', '2']] = pd.DataFrame(triple_odds)
df[['1', 'x', '2']] = df[['1', 'x', '2']].astype(float)


def aposta_ganha(row, meta=100):
    custo = sum([meta / (row['1']), meta / row['x'], meta / row['2']])
    return round(meta - custo, 2)
    
# Aplicar a função a cada linha do DataFrame
df["lucro"] = df.apply(aposta_ganha, axis=1)

df = df.sort_values(by='lucro', ascending=False)

print(df.head(10))

