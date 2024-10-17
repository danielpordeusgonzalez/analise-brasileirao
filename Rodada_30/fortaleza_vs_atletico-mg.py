import pandas as pd #importei o pandas

#Data Frame principal
df_planilha_brasileirao = pd.read_excel('./planilhas/planilha_brasileirao_2024.xlsx')

#Data Frame com todos os jogadores do fortaleza
df_time_fortaleza = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time'] == 'Fortaleza'].reset_index(drop=True)
# print(df_time_fortaleza)

#Data Frame com todos os jogadores do Atlético-mg
df_time_atletico = df_planilha_brasileirao[df_planilha_brasileirao['nome_time'] == 'Atlético Mineiro'].reset_index(drop=True)
# print(df_time_atletico)

#Mostra por posição quantos gols e assistincias o Fortaleza tem
gols_assist_time_fortaleza = df_time_fortaleza[['Posição', 'gols','assist']].groupby('Posição').sum()
#estou criando uma nova coluna com a participação de gols que os jogadores do fortaleza tem por posição
gols_assist_time_fortaleza['participação gol'] = gols_assist_time_fortaleza['gols'] + gols_assist_time_fortaleza['assist']
# print(gols_assist_time_fortaleza)

#Mostra por posição quantos gols e assistincias o atletico-mg tem
gols_assist_time_atletico_mg = df_time_atletico[['Posição', 'gols', 'assist']].groupby('Posição').sum()
#estou criando uma nova coluna com a participação de gols que os jogadores do atletico-mg tem por posição
gols_assist_time_atletico_mg['participação gol'] = gols_assist_time_atletico_mg['gols'] + gols_assist_time_atletico_mg['assist']
# print(gols_assist_time_atletico_mg)

# Quem tem 2 ou mais de 2 gols por jogo no fortaleza
mais_2_gols_fortaleza = df_time_fortaleza[df_time_fortaleza.gols >= 2]
print(mais_2_gols_fortaleza)

# Quem tem mais de 2 gols por jogo no atlético-mg

mais_2_gols_atletico = df_time_atletico[df_time_atletico.gols >= 2]
# print(mais_2_gols_atletico)

# Quem Tem mais de 2 gols são paulo ordenado por nome jogador, posição gols, assist, participação gol
mais_2_gols_fortaleza = df_time_fortaleza[df_time_fortaleza.gols >= 2]
mais_2_gols_fortaleza['participação gol'] = mais_2_gols_fortaleza['gols'] + mais_2_gols_fortaleza['assist']
# print(mais_2_gols_fortaleza[['nome_jogadores','Posição', 'gols', 'assist','participação gol']])

# Quem Tem mais de 2 gols vasco ordenado por nome jogador, posição gols, assist, participação gol
mais_2_gols_atletico = df_time_atletico[df_time_atletico.gols >= 2]
mais_2_gols_atletico['participação gol'] = mais_2_gols_atletico['gols'] + mais_2_gols_atletico['assist']
# print(mais_2_gols_atletico[['nome_jogadores','Posição', 'gols', 'assist','participação gol']])
