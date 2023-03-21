import pandas as pd
import plotly.express as px # para edições nos gráficos: https://plotly.com/python/histograms/

#Passo 1: Importando Base de Dados
tabela = pd.read_csv("IntesivãoPython/Aula 2/telecom_users.csv")

# - Entender quais as informações tão disponíveis
# - Descobrir os erros da base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)

#Passo 2: Tratamento de Dados
# - Valores reconhecidos de forma incorreta
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores Vazios
#Deletando Colunas Vazias #dropna exclui valores vazios
tabela = tabela.dropna(how="all", axis=1)

# axis = 0 > linha ou axis = 1 > coluna

#Deletando Linhas Vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

#Passo 3: Análise Completa
#Verificar quantos % estão cancelando
print(tabela["Churn"].value_counts(normalize=True))

#comparar cada coluna da minha tabela com a coluna de cancelamento

#Criar Gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()