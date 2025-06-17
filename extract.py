from playwright.sync_api import sync_playwright
import time
from parser import parser


def extract_html(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Para visualizar o processo precisa desativar o headless


        page = browser.new_page()

        # User Agent (evita block)
        # page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})

        page.goto(url)

        html_dict = {}

        while True:
            # Capturar o valor do elemento que precisa ser 1
            valor_elemento = page.locator('//*[@id="classificacao__wrapper"]/section/nav/span[2]').inner_text()
            print(valor_elemento)
            

            # Capturar o HTML desejado
            html_content = page.wait_for_selector('//*[@id="classificacao__wrapper"]/section/ul').inner_html()
            html_dict[valor_elemento] = html_content

            # Verificar se atingiu a condição de parada
            if valor_elemento == "1ª RODADA":
                break

            # Clicar no botão
            page.click('//*[@id="classificacao__wrapper"]/section/nav/span[1]')

            time.sleep(2)

        browser.close()

    return html_dict