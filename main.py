import json
from extract import extract_html
from parser import parser

url = 'https://ge.globo.com/futebol/brasileirao-serie-b/'

# Extrai dados do Site solicitado
html_dict = extract_html(url) 

# Cria o json
json_data = {rodada: parser(html) for rodada, html in html_dict.items()}

# Salva o json
with open("resultados.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print("Arquivo JSON criado com sucesso!")
