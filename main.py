import json
from extract.extract import extract_html
from extract.parser import parser
from transform.transform import load_to_csv

url = 'https://ge.globo.com/futebol/brasileirao-serie-b/'

# Extrai dados do Site solicitado
html_dict = extract_html(url) 

# Cria o json
json_data = {rodada: parser(html) for rodada, html in html_dict.items()}

# Salva o json
json_file_name = 'output/resultados.json'
with open(json_file_name, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)

print(f'\nArquivo JSON disponível em {json_file_name}!')

print(load_to_csv(json_file_name))
