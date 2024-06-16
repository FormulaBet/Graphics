import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

# Leitura do arquivo CSV
dados_novos = pd.read_csv(r'Drivers Championship_updated.csv')

posicao_piloto = int(input('Insira a posição do corredor desejado(1 à 27): ')) - 1

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


def exibir_grafico(piloto):
    # Cria um gráfico para o corredor escolhido
    pontos = [dados_novos.iloc[piloto, i] + dados_novos.iloc[piloto, i + 5] for i in range(9, 170, 13)] # Soma os pontos da corrida com os pontos extras e joga na lista

    fig, ax = plt.subplots() # Cria a figura e os sublots(axes)

    ax.plot(range(len(pontos)), pontos, marker='o') # Gera as linhas do gráfico e marca os pontos exatos

    ax.set_title(f'N°{piloto + 1} {pilotos[piloto]}({equipes[piloto]})') # Título do gráfico que exibe posição no pódio, nome e equipe do piloto
    ax.set_xlabel('Corrida') # Label do eixo x
    ax.set_ylabel('Pontos') # Label do eixo y 

    ax.set_xlim(0, 12) # Valores do eixo x
    ax.set_ylim(0, 27) # Valores do eixo y

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1)) # Faz com que o intervalo do eixo x seja de um em um
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1)) # Faz com que o intervalo do eixo y seja de um em um

    plt.show() # Exibe o gráfico criado

exibir_grafico(posicao_piloto)