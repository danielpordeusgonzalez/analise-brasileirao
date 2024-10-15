import pandas as pd

df_planilha_brasileirao = pd.read_excel('./planilhas/planilha_brasileirao_2024.xlsx')
# df_planilha_corinthians = pd.read_excel('./planilhas/planilha_Corinthians_2024.xlsx')

# print(df_planilha_brasileirao)

#Seleciona colunas

# partida = df_planilha_brasileirao[['nome_times', 'Posição']]
# print(partida)

#Seleciona uma linha ou um range de linhas
# print(df_planilha_brasileirao.loc[50:55])

#pegar linhas que correspodem a uma condição
# print(df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time'] == 'Juventude'])


# pegar várias linhas e colunas usando o loc
# time_juventude = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time'] == 'Juventude', ['nome_time', 'gols', 'assist']]
# print(time_juventude)

#pegar 1 valor específico 
# print(df_planilha_brasileirao.loc[26, 'gols'])

# adicionar uma nova coluna
# adicionar uma coluna que já existe
# df_planilha_brasileirao['participacao_gol'] = df_planilha_brasileirao['gols'] + df_planilha_brasileirao['assist']
# print(df_planilha_brasileirao.head(30))

#criar uma coluna com valor padrão
# df_planilha_brasileirao.loc[:, 'participacao_gol'] = 0
# print(df_planilha_brasileirao)

# adicionar 1 linha
#df_santos = pd.read_excel('planilha_santos')
#df_planilha_brasileirao = df_planilha_brasileirao.append(df_santos)

#excluir linhas e colunas
#df_planilha_brasileirao = df_planilha_brasileirao.drop('assist', axis=0 ou 1) 1 eixo da coluna e 0 eixo da linha

#Deletar linhas e colunas completamentes vazias
# df_planilha_brasileirao = df_planilha_brasileirao.dropna(how='all', axis = 1) exclui todas as linhas que tiver valores vazios

# Deletar linhas que possuem pelo menos 1 valor vazio
# df_planilha_brasileirao = df_planilha_brasileirao.dropna()

#preencher valores vazios
#preencher com a media da coluna
# df_planilha_brasileirao['gols'] = df_planilha_brasileirao['gols'].fillna(1) preenche
# df_planilha_brasileirao['gols'] = df_planilha_brasileirao['gols'].fillna(df_planilha_brasileirao['gols'].mean()) - media
# print(df_planilha_brasileirao)55

#preencher com ultimo valor:
#df_planilha_brasileirao = df_planilha_brasileirao.ffill()

 