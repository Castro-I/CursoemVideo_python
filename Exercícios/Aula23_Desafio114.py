from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    driver = webdriver.Chrome()
    driver.get('http://www.pudim.com.br/')
    imagem_pudim = driver.find_element(By.CLASS_NAME, 'image').is_displayed()
    if imagem_pudim is True:
        print('\033[0;32mO site pudim está conectado.\033[m')
except Exception:
    print('\033[0;31mNão foi possível acessaro o site.\033[m')
finally:
    quit()
