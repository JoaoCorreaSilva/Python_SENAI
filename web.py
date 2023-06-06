from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from sqlip import conn, cursor


class Web:
    def __init__(self):
        self.link = 'https://shopee.com.br/celular_mais_barato'
        self.map = {
            "modelo": "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[%cural%]/a/div/div/div[2]/div[1]/div[1]/div",
            "preco": "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[%pamonha%]/a/div/div/div[2]/div[2]/div/span[2]"
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.abrir_site()

    def abrir_site(self):
        self.driver.get(self.link)
        sleep(5)
        k = 0
        for j in range(1, 5):
            print(self.driver.find_element(By.XPATH, self.map["modelo"].replace('%cural%', f'{j}')).text, end='\t')
            modelo = self.driver.find_element(By.XPATH, self.map["modelo"].replace('%cural%', f'{j}')).text
            k += 1
            print(self.driver.find_element(By.XPATH, self.map["preco"].replace('%pamonha%', f'{k}')).text)
            preco = self.driver.find_element(By.XPATH, self.map["preco"].replace('%pamonha%', f'{k}'))

            inserir = f"""INSERT INTO celulares(marca, valor)
                values
                ('{modelo}', '{preco}');"""
            cursor.execute(inserir)
            conn.commit()
