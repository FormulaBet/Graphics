import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# Leitura do arquivo CSV
dados_novos = pd.read_csv(r'Drivers Championship_updated.csv')

# Lista de pilotos seguindo a ordem do pódio
pilotos = []
for p in range(0, 27):
    pilotos.append(dados_novos.loc[p, 'Participant']) # Adiciona os pilotos da coluna "Participant" à lista seguindo a ordem do pódio
# print(pilotos)

# Lista de equipes respectivas de cada piloto
equipes = []
for t in range(0, 27):
    equipes.append(dados_novos.loc[t, 'TEAM']) # Adiciona as equipes da coluna "TEAM" à lista seguindo a ordem do pódio
# print(equipes)


# Gera um gráfico para cada corredor seguindo a ordem do pódio 
for k in range(0, 27):
    pontos = [] # Armazena os pontos de cada corrida
    i = 9 # Coluna em que se encontra a primeira corrida
    while i <= 169:    
        pontos.append(dados_novos.loc[k, dados_novos.columns[i]] + dados_novos.loc[k, dados_novos.columns[i + 5]]) # Soma os pontos da corrida com os pontos extras e joga na lista
        i += 13 # Intervalo da coluna de uma corrida até a outra

    fig, ax = plt.subplots() # Cria a figura e os sublots(axes)

    ax.plot(range(len(pontos)), pontos, marker='o') # Gera as linhas do gráfico e marca os pontos exatos

    ax.set_title(f'N°{k + 1} {pilotos[k]}({equipes[k]})') # Título do gráfico que exibe posição no pódio, nome e equipe do piloto
    ax.set_xlabel('Corrida') # Label do eixo x
    ax.set_ylabel('Pontos') # Label do eixo y 

    ax.set_xlim(0, 12) # Valores do eixo x
    ax.set_ylim(0, 27) # Valores do eixo y

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) # Faz com que o intervalo do eixo x seja de um em um
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1)) # Faz com que o intervalo do eixo y seja de um em um

    plt.show() # Exibe o gráfico criado