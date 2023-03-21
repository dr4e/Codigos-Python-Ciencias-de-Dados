#R² é oq diz o quao preciso é o nosso modelo/Inteligencia

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
#r2_score esta dentro do metrics

#Importar Base de Dados
tabela = pd.read_csv("IntesivãoPython/Aula 4/advertising.csv")
print(tabela)
print(tabela.info())
print(tabela.corr()) #Correlação da Tabela

#Mapa de Calor
sns.heatmap(tabela.corr(), cmap="Blues", annot=True)
plt.show()

#Inteligencias
x = tabela.drop(["Vendas"], axis=1) #x = tabela[["TV", "Radio", "Jornal"]] Oq Tem
y = tabela["Vendas"] #Oq Prever

#--Dados de treino(NESTA ORDEM)
x_treino, x_test, y_treino, y_test = train_test_split(x,y, test_size=0.3) #random_state = 1

#Criar
ia_regressao = LinearRegression()
ia_arvoredecisao = RandomForestRegressor()

#Treinar
ia_regressao.fit(x_treino, y_treino)
ia_arvoredecisao.fit(x_treino, y_treino)

#Testar e Comparar Previsoes
visao_da_regressao = ia_regressao.predict(x_test)
visao_da_arvore = ia_arvoredecisao.predict(x_test)

#Comparar R²
print(metrics.r2_score(y_test, visao_da_regressao))
print(metrics.r2_score(y_test, visao_da_arvore))

#Visualizar previsoes em uma tabela
tabela_das_visoes = pd.DataFrame()
tabela_das_visoes["Y_test"] = y_test
tabela_das_visoes["Visao da Regressao"] = visao_da_regressao
tabela_das_visoes["Visao da Arvore"] = visao_da_arvore

#Visualização Grafica de Previsoes
plt.figure(figsize=(15,6)) #Tamanho Mais Maior
sns.lineplot(data = tabela_das_visoes)
plt.show()

#Novas Previsoes
nova_tabela = pd.read_csv("IntesivãoPython/Aula 4/novos.csv")
print(nova_tabela)

pega_visao = ia_arvoredecisao.predict(nova_tabela)
print(pega_visao)