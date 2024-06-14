import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

dados_novos = pd.read_csv(r'Drivers Championship_updated.csv')

pilotos = []
for p in range(0, 27):
    pilotos.append(dados_novos.loc[p, 'Participant'])
print(pilotos)

equipes = []
for t in range(0, 27):
    equipes.append(dados_novos.loc[t, 'TEAM'])
print(equipes)