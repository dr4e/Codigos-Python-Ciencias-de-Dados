# Chrome -> chromedriver
# Firefox -> geckodriver

# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True 
# navegador = webdriver.Chrome(options=chrome_options)

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


#Abri Navegador e entrar no google

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

#Passo 1: Cotação Dolar
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotaçao dolar")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Passo 2: Cotação Euro
navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotaçao euro")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Passo 3: Cotação Ouro
navegador = webdriver.Chrome()
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

print(cotacao_dolar)
print(cotacao_euro)
print(cotacao_ouro)

navegador.quit()

#Passo 4: Importar base de dados
tabela = pd.read_excel("IntesivãoPython/Aula 3/Produtos.xlsx")
print(tabela)

#Passo 5 recalcular Preços
#-- Atualizar Cotação
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

#-- Recalcular o preço base(preço original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

#-- Recalcular o preço final(preço original * margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

#Passo 6: Exportar nova base de dados
#tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format) Formatar tabela
tabela.to_excel("IntesivãoPython/Aula 3/ProdutosNovo.xlsx", index=False) #Index para tirar o índice