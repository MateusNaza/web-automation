import json
from extract import extract_html
from parser import parser
from transform import load_to_csv

url = 'https://ge.globo.com/futebol/brasileirao-serie-b/'

# Extrai dados do Site solicitado
html_dict = extract_html(url) 

# Cria o json
json_data = {rodada: parser(html) for rodada, html in html_dict.items()}

# Salva o json
json_file_name = 'resultados.json'
with open(json_file_name, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print('Arquivo JSON criado com sucesso!')

# Transforma e carrega o arquivo em CSV
load_to_csv(json_file_name)
