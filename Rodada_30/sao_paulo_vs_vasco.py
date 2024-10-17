import pandas as pd #importei o pandas

#Data Frame principal
df_planilha_brasileirao = pd.read_excel('./planilhas/planilha_brasileirao_2024.xlsx')

#Data Frame com todos os jogadores do são paulo
df_time_sao_paulo = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time'] == 'São Paulo'].reset_index(drop=True)
# print(df_time_sao_paulo)

#Data Frame com todos os jogadores do vasco
df_time_vasco = df_planilha_brasileirao[df_planilha_brasileirao['nome_time'] == 'Vasco'].reset_index(drop=True)
# print(df_time_vasco)

#Mostra por posição quantos gols e assistincias o São Paulo tem
gols_assist_time_sao_paulo = df_time_sao_paulo[['Posição', 'gols','assist']].groupby('Posição').sum()
#estou criando uma nova coluna com a participação de gols que os jogadores do São paulo tem por posição
gols_assist_time_sao_paulo['participação gol'] = gols_assist_time_sao_paulo['gols'] + gols_assist_time_sao_paulo['assist']
# print(gols_assist_time_sao_paulo)

#Mostra por posição quantos gols e assistincias o vasco tem
gols_assist_time_vasco = df_time_vasco[['Posição', 'gols', 'assist']].groupby('Posição').sum()
#estou criando uma nova coluna com a participação de gols que os jogadores do vasco tem por posição
gols_assist_time_vasco['participação gol'] = gols_assist_time_vasco['gols'] + gols_assist_time_vasco['assist']
# print(gols_assist_time_vasco)

# Quem tem 2 ou mais de 2 gols por jogo no são paulo
mais_2_gols_sao_paulo = df_time_sao_paulo[df_time_sao_paulo.gols >= 2]
print(mais_2_gols_sao_paulo)

# Quem tem mais de 2 gols por jogo no vasco
mais_2_gols_vasco = df_time_vasco[df_time_vasco.gols >= 2]
print(mais_2_gols_vasco)

# Quem Tem mais de 2 gols são paulo ordenado por nome jogador, posição gols, assist, participação gol
mais_2_gols_sao_paulo = df_time_sao_paulo[df_time_sao_paulo.gols >= 2]
mais_2_gols_sao_paulo['participação gol'] = mais_2_gols_sao_paulo['gols'] + mais_2_gols_sao_paulo['assist']
print(mais_2_gols_sao_paulo[['nome_jogadores','Posição', 'gols', 'assist','participação gol']])

# Quem Tem mais de 2 gols vasco ordenado por nome jogador, posição gols, assist, participação gol
mais_2_gols_vasco = df_time_vasco[df_time_vasco.gols >= 2]
mais_2_gols_vasco['participação gol'] = mais_2_gols_vasco['gols'] + mais_2_gols_vasco['assist']
print(mais_2_gols_vasco[['nome_jogadores','Posição', 'gols', 'assist','participação gol']])