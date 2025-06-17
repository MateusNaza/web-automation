from bs4 import BeautifulSoup

def parser(html):
    soup = BeautifulSoup(html, 'html.parser')
    resultados = []

    for jogo in soup.find_all('li', class_='lista-jogos__jogo'):
        # Nome da partida
        nome_partida = jogo.find('meta', itemprop='name')
        nome_partida = nome_partida['content'] if nome_partida else 'Desconhecido'

        # Captura dos times mandante e visitante
        mandante = jogo.find('div', class_='placar__equipes--mandante')
        visitante = jogo.find('div', class_='placar__equipes--visitante')

        # Siglas dos times
        sigla_mandante = mandante.find('span', class_='equipes__sigla').text if mandante else 'N/A'
        sigla_visitante = visitante.find('span', class_='equipes__sigla').text if visitante else 'N/A'

        # Placar dos times
        placar_mandante = jogo.find('span', class_='placar-box__valor--mandante')
        placar_visitante = jogo.find('span', class_='placar-box__valor--visitante')

        placar_mandante = placar_mandante.text if placar_mandante else '-1'
        placar_visitante = placar_visitante.text if placar_visitante else '-1'

        # Data e Hora dos jogos
        data = jogo.find('meta', itemprop='startDate')
        data_hora = data['content'] if data else 'Data não definida'

        # Adiciona os resultados à lista
        resultados.append({
            'partida': nome_partida,
            'mandante': sigla_mandante,
            'placar_mandante': placar_mandante,
            'visitante': sigla_visitante,
            'placar_visitante': placar_visitante,
            'data_hora': data_hora
        })

    return resultados  # Retorna os resultados como uma lista de dicionários
