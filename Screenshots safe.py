from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# 'obra' vai receber a lista de pastas contidas em 'diretorio'; 'bi1' e 'bi2' são a primeira e terceira parte da url a ser aberta

i = 0
diretorio = 'Caminho\para\pasta'
obra = os.listdir(diretorio)
bi1 = 'Prefixo da URL'
bi2 = 'Sufixo da URL'

# Abrir o Chrome, maximizar e navegar para o endereço do BI

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('URL do site')

# Procura os campos de usuário e senha e preenche

username = browser.find_element_by_xpath('//*[@name="username"]')
username.clear()
username.send_keys("USER EMAIL")  # Trocar email
username.send_keys(Keys.RETURN)
password = browser.find_element_by_xpath('//*[@name="password"]')
password.clear()
password.send_keys("PASSWORD")  # Trocar senha
password.send_keys(Keys.RETURN)
time.sleep(3)

# Enquanto não esgotar a lista de obras, abrir uma aba para cada BI e tirar 2 screenshots nas pastas da lista

while i < len(obra):
	site = bi1 + obra[i] + bi2
	browser.execute_script("window.open('');")
	browser.switch_to.window(browser.window_handles[1]) # Troca a aba do navegador
	browser.get(site)

	cursor = browser.find_element_by_xpath('//*[@id="toggle-fullscreen-ToolbarButton"]') # Botão do Tableu que maximiza a tela
	cursor.click()
	time.sleep(3)
	print1 = diretorio + '\\' + obra[i] + '\\' + 'Tela1.png'
	browser.save_screenshot(print1)

	cursor = browser.find_element_by_xpath('//*[@widgetid="tableauTabbedNavigation_tab_1"]') # Troca a aba interna do Tableau
	cursor.click()
	time.sleep(3)
	print2 = diretorio + '\\' + obra[i] + '\\' + 'Tela2.png'
	browser.save_screenshot(print2)

	browser.close()
	browser.switch_to.window(browser.window_handles[0]) # Retorna pra primeira aba do navegador para recomeçar
	time.sleep(3)
	
	i = i + 1

browser.close()