import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ...

# Criando o bot para abrir o site da Shopee
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)  # Certifique-se de ter o ChromeDriver instalado e adicionado ao PATH
driver.get('https://shopee.com.br/celular_mais_barato')

# Mantendo a janela do navegador aberta
while True:
    time.sleep(10)  # Aguarda 10 segundos antes de verificar novamente

# Fechando a janela do navegador
driver.quit()
