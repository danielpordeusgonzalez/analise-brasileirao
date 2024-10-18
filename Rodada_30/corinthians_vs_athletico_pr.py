import pandas as pd

df_planilha_brasileirao = pd.read_excel('./planilhas/planilha_brasileirao_2024.xlsx')
df_corinthians = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time']  == 'Corinthians'].reset_index(drop=True)

mais_2_gols_assist_corinthians = df_corinthians[df_corinthians.gols >= 2]
mais_2_gols_assist_corinthians['Participação_gol'] = df_corinthians['gols'] + df_corinthians['assist']

print(mais_2_gols_assist_corinthians[['Posição', 'nome_jogadores','gols','assist','Participação_gol']])

df_athletico = df_planilha_brasileirao.loc[df_planilha_brasileirao['nome_time']  == 'Athletico Paranaense'].reset_index(drop=True)

mais_2_gols_assist_athletico = df_athletico[df_athletico.gols >= 2]
mais_2_gols_assist_athletico['Participação_gol'] = df_athletico['gols'] + df_athletico['assist']

print(mais_2_gols_assist_athletico[['Posição', 'nome_jogadores','gols','assist','Participação_gol']])