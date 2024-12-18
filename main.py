import agente
import Breadth_First_Search
import GerarMaze
import random
import json
import os
import subprocess
import time
import os
import pygame  #Gerar o labirinto
import random  #randomizar o negócio

# Define uma função que mostra uma mensagem de espera com pontos animados
def mensagembase(n): #TIREI DIRETO DA p3 DE SO, EU QUE FIZ EU VOU REUSAR
    print('\b' * n + ' ' * n + '\b' * n, end='', flush=True)

def waiting_dots(wait, ndots=4, interval=0.5, message="Gerando o Labirinto", final_message=""):
    start = time.time()  # Obtém o tempo atual
    print(message, end="", flush=True)  # Imprime a mensagem inicial
    while time.time() - start < wait:  # Loop enquanto o tempo decorrido for menor que o tempo de espera
        for _ in range(ndots):  # Loop para cada ponto a ser exibido
            print('.', end='', flush=True)  # Imprime um ponto
            time.sleep(interval)  # Aguarda um intervalo de tempo
        mensagembase(ndots)  # Limpa os pontos
        time.sleep(interval)  # Aguarda um intervalo de tempo
    if final_message is not None:  # Se houver uma mensagem final especificada
        mensagembase(len(message))  # Limpa a mensagem inicial
        print(final_message)  # Imprime a mensagem final


def main1():
    print('\033[31m'+"Iniciando o processo"+'\033[0m')

    subprocess.run(["E:/projetos python/.venv/Scripts/python.exe", "GerarMaze.py"])
def main2():

    subprocess.run(["E:/projetos python/.venv/Scripts/python.exe", "Breadth_First_Search.py"])
    time.sleep(1)
    subprocess.run(["E:/projetos python/.venv/Scripts/python.exe", "agente.py"])

if __name__ == "__main__":
    # carrega o arquivo

    main1()
    time.sleep(3)
    # carrega o arquivo
    with open('walls_data.json', 'r') as file:
        maze = json.load(file)
    main2()

