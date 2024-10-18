import pandas as pd

df_planilha_brasileirao = pd.read_excel('./planilhas/planilha_brasileirao_2024.xlsx')
df_flamengo = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time']  == 'Flamengo'].reset_index(drop=True)

mais_2_gols_assist_flamengo = df_flamengo[df_flamengo.gols >= 2]
mais_2_gols_assist_flamengo['Participação_gol'] = df_flamengo['gols'] + df_flamengo['assist']

print(mais_2_gols_assist_flamengo[['Posição', 'nome_jogadores','gols','assist','Participação_gol']])

df_fluminense = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time']  == 'Fluminense'].reset_index(drop=True)

mais_2_gols_assist_fluminense = df_fluminense[df_fluminense.gols >= 2]
mais_2_gols_assist_fluminense['Participação_gol'] = df_fluminense['gols'] + df_fluminense['assist']

print(mais_2_gols_assist_fluminense[['Posição', 'nome_jogadores','gols','assist','Participação_gol']])