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

for k in range(0, 27):
    pontos = []
    i = 9
    while i <= 169:    
        pontos.append(dados_novos.loc[k, dados_novos.columns[i]] + dados_novos.loc[k, dados_novos.columns[i + 5]])
        i += 13

    fig, ax = plt.subplots()

    ax.plot(range(len(pontos)), pontos, marker='o')

    plt.show()