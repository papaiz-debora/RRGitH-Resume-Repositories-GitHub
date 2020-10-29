#!/usr/bin/env python3

#IMPORTAR PACOTES
import requests #API
import json #JSON FORMAT
import pandas as pd #DATA MANUPULATION
import matplotlib.pyplot as plt #PLOTTING

#DEFINIR VARIAVEL URL (RESULTADO DE BUSCA)
url =  'https://api.github.com/search/repositories?q=language:python&sort=starts'

#BAIXAR CONTEÚDO USANDO REQUESTS
JSONContent = requests.get(url)

#CONVERTER PARA FORMATO JSON/DICTIONARY
content = JSONContent.json()

#SALVAR CONTENT EM CSV
pd.DataFrame(content).to_csv('github_repositorio.csv', index=False)

#VERIFICAR KEYS DO DICTIONARY (DADOS ESTÃO NA KEY = ‘ITEMS’)
content.keys()

#DEFINIR OBJETO PARA RECEBER VALORES
pop =[]

#SELECIONAR VALORES DO DICTIONARY QUE CONTÉM AS INFORMAÇÕES: ID, NAME E STARGAZERS_COUNT
for id in content['items']:
 pop.append((id['id'], id['name'], id['stargazers_count']))

#MONTAR DATAFRAME COM NOME DE COLUNAS E VALORES 
df = pd.DataFrame(pop, columns=['id', 'name', 'stargazers_count'])
print(df)

#SALVAR DATAFRAME EM CSV
df.to_csv('stargazersCount_repositorios.csv')

#ANALISE ESTATISTICA DESCRITIVA
summary = df.describe(include= "all")
print(summary)

#DEFINIR VARIÁVEIS E PLOTAR GRÁFICO DE BARRAS
x = df['name']
y = df['stargazers_count']
plt.bar(x,y)
plt.xlabel('Nome do repositorio')
plt.xticks(rotation=90)
plt.ylabel('Stargazers Count')
plt.title('Repositorios mais populares no GitHub')

#SALVAR GRÁFICOS EM PNG E SVG
plt.savefig('Popularidade_repositorios.png', dpi=300, bbox_inches='tight')
plt.savefig('Popularidade_repositorios.svg', bbox_inches='tight')
plt.clf()

#SELECIONAR 6 REPERTÓRIOS MAIS POPULARES
#ORDENAR O DF DO MAIOR PARA O MENOR BASEANDO-SE NOS COUNTS
df_top6 = df.sort_values(by=['stargazers_count'], ascending=False)

#SELECIONAR AS PRIMEIRAS 6 LINHAS
df_top6 = df_top6.iloc[0:6]
print(df_top6)

#DEFINIR VARIÁVEIS E PLOTAR GRÁFICO
x = df_top6['name']
y = df_top6['stargazers_count']
plt.bar(x,y)
plt.xlabel('Nome do repositorio')
plt.xticks(rotation=90)
plt.ylabel('Stargazers Count')
plt.title('Seis repositorios mais populares no GitHub')

#SALVAR GRÁFICOS EM PNG E SVG
plt.savefig('Top6_repositorios_populares.png', dpi=300, bbox_inches='tight')
plt.savefig('Top6_repositorios_populares.svg', bbox_inches='tight')

plt.clf()
