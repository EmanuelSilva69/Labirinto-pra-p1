import json
import random
import os
import time
import sys
import subprocess
start = (0, 0)  # Inicio
goal = (random.randrange(38), random.randrange(28))  # Objetivo aleatório
python_executable = sys.executable

if not os.path.isfile('walls_data.json'):
    print("O arquivo 'walls_data.json' não foi encontrado. Gerando agora...")
    time.sleep(3)
    # Executa o script GerarMaze.py para criar o arquivo
    subprocess.run([python_executable, "GerarMaze.py"])
    print('\035[31m' + "Os arquivos foram gerados. O main irá rodar." + '\035[0m')


# carrega o arquivo
if os.path.isfile('walls_data.json'):
    with open('walls_data.json', 'r') as file:
        maze = json.load(file)

# organizar as celulas
cells = {(cell['x'], cell['y']): cell['walls'] for cell in maze}
def get_neighbors(x, y, walls):

    directions = {
        "cima": (x, y - 1),
        "baixo": (x, y + 1), #basicamnete as direções apresentadas.
        "esquerda": (x - 1, y),
        "direita": (x + 1, y),
    }
    neighbors = []
    for wall, (nx, ny) in directions.items():
        if not walls.get(wall, True):  # Sem uma parede, dá pra passar. É o que é possível andar.
            neighbors.append((nx, ny))
    return neighbors

def BFS (start,goal):
    queue = [start]
    visitado = []
    parente = {start : None}
    while queue:
        current = queue.pop(0)  # Tira da lista o primeiro elemento
        if current == goal:     # Verifica se é o objetivo final
            break
        visitado.append(current) # Marca o atual como visitado
        # Pega os dados do bloco atual
        walls = cells.get(current, {})
        # Acha os vizinhos
        for neighbor in get_neighbors(*current, walls):
            if neighbor not in visitado and neighbor not in queue:
                queue.append(neighbor)  # Adiciona na lista
                parente[neighbor] = current  # Anda o caminho
    #constroi o caminho ideal para ser seguido
    path = []
    while goal is not None:
        path.append(goal)
        goal = parente.get(goal)
    return path[::-1]  # Faz o caminho ser o correto, pois a lista adiciona do objetivo até o inicio
if __name__ == "__main__":
    #verificar se não vai cair fora do labirinto#
    if start not in cells or goal not in cells:
        print("Início ou objetivo fora do labirinto.")
    exit()

    # carrega o arquivo
    with open('walls_data.json', 'r') as file:
        maze = json.load(file)
    if goal in cells:
        path = BFS(start, goal)
        print(f"Caminho de {start} para {goal}: {path}")
    else:
        print(f"O objetivo {goal} não existe.")
