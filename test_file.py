from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # Para visualizar o processo precisa desativar o headless


    page = browser.new_page()

    # User Agent (evita block)
    # page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})

    page.goto("https://www.youtube.com")

    time.sleep(5)

    # Captura uma imagem da página
    page.screenshot(path="output/screenshot.png") 

    browser.close()
