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

#calcular indicadores

#value counts
# posicao_jogadores = df_planilha_brasileirao['Posição'].value_counts()
# print(posicao_jogadores)

#groupby
# gols_atacantes = df_planilha_brasileirao[['Posição', 'gols','assist']].groupby('Posição').sum()
# print(gols_atacantes)

#Mesclar 2 dataframes (procurar a informação de um dataframe em outro)
#ex: gerentes_df = pd.read_excel('gerentes.xlsx')

#ex: vendas_df = vendas_df.merge(gerentes_df) -- esse gerentes_df possui um id igual a tabela vendas_df e o pandas consegue assimilar que 
# são a mesma tabela
#fazendo com que não se replique a coluna id.

# print(df_planilha_brasileirao['assist'].mean()) faz a média das assistencias

# df_planilha_brasileirao = df_planilha_brasileirao.where(df_planilha_brasileirao['gols'] > df_planilha_brasileirao['gols'].mean(), 0)
# print(df_planilha_brasileirao)
#o where server para passa uma condição

# print(df_planilha_brasileirao.where(df_planilha_brasileirao['gols'] > df_planilha_brasileirao['gols'].mean()) & (df_planilha_brasileirao['Posição'].isin(['atacante'])))
# no código acima da pra comparar a média de gols e separar por posição mas está dando um erro pois não suporta float and bool

# df_planilha_brasileirao = df_planilha_brasileirao.where(df_planilha_brasileirao['gols'] > df_planilha_brasileirao['gols'].mean()).dropna().reset_index(drop=True)
#essa condição do where compara os gols com a media de gols, dropna retira as tabela com numero 0 qquqe foi colocado a cima, e resetou o index.






