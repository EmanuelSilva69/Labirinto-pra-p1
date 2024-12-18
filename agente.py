import json
import GerarMaze
import Breadth_First_Search
import pygame
import time
import random
import os
import subprocess
try:
    with open('walls_data.json', 'r') as file:
        maze = json.load(file)  # Define a variável maze
except FileNotFoundError:
    print("Erro: O arquivo 'walls_data.json' não foi encontrado.")

# Carrega o arquivo para o labirinto rodae
if os.path.isfile('walls_data.json'):
    with open('walls_data.json', 'r') as file:
        maze = json.load(file)

# Organização das células
cells = {(cell['x'], cell['y']): cell['walls'] for cell in maze}
TILE_SIZE = GerarMaze.TILE
RES = WIDTH, HEIGHT = 1200, 900  # Parâmetros da janela
PATH_COLOR = pygame.Color('#68B684')
GRID_COLOR = pygame.Color('#3eb489')
AGENT_COLOR = pygame.Color('#F35B04')
FPS = 10

BACKGROUND_COLOR = pygame.Color('#3eb489')
screen = GerarMaze.sc
path = Breadth_First_Search.BFS(Breadth_First_Search.start, Breadth_First_Search.goal)

# desenhaa o labirinto e o agente
def desenhar_agente_grid(screen, maze, agent_pos, goal_pos, path=None, current_index=0):
    screen.fill(BACKGROUND_COLOR)  # Limpa a tela
    for cell in maze:
        x, y = cell['x'], cell['y']
        walls = cell['walls']
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, GRID_COLOR, rect)  # Desenha a grid

        # Desenha as paredes
        if walls['cima']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), (x * TILE_SIZE, y * TILE_SIZE), ((x + 1) * TILE_SIZE, y * TILE_SIZE), 2)
        if walls['baixo']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), (x * TILE_SIZE, (y + 1) * TILE_SIZE), ((x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE), 2)
        if walls['esquerda']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), (x * TILE_SIZE, y * TILE_SIZE), (x * TILE_SIZE, (y + 1) * TILE_SIZE), 2)
        if walls['direita']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), ((x + 1) * TILE_SIZE, y * TILE_SIZE), ((x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE), 2)

    # Mostra o caminho percorrido para o agente automático
    if path:
        for idx in range(current_index):
            x, y = path[idx]
            rect = pygame.Rect(x * TILE_SIZE + 10, y * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)
            pygame.draw.rect(screen, pygame.Color('#3D348B'), rect, border_radius=20)

    # Desenha o agente
    agent_draw_pos = (agent_pos[0] * TILE_SIZE + TILE_SIZE // 2, agent_pos[1] * TILE_SIZE + TILE_SIZE // 2)
    pygame.draw.circle(screen, AGENT_COLOR, agent_draw_pos, TILE_SIZE // 4)

    # Desenha o objetivo
    gx, gy = goal_pos
    goal_rect = pygame.Rect(gx * TILE_SIZE + 5, gy * TILE_SIZE + 5, TILE_SIZE - 10, TILE_SIZE - 10)
    pygame.draw.rect(screen, pygame.Color('#F9627D'), goal_rect, border_radius=10)

    pygame.display.flip()  # Atualiza a tela

# Função para animar o agente automático
def animar_agente(maze, path):
    sc = pygame.display.set_mode(GerarMaze.RES)
    clock = pygame.time.Clock()

    for current_index in range(len(path)):
        desenhar_agente_grid(sc, maze, path[current_index], Breadth_First_Search.goal, path, current_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(FPS)

    time.sleep(2)
    pygame.image.save(sc, "labirintoconcluido.png")
    pygame.quit()

# Função para controlar o agente manualmente
def controlar_agente(maze, start, goal):
    sc = pygame.display.set_mode(GerarMaze.RES)
    clock = pygame.time.Clock()
    agent_pos = start

    while agent_pos != goal:
        desenhar_agente_grid(sc, maze, agent_pos, goal)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        new_pos = list(agent_pos)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if not cells[agent_pos]['cima']:
                new_pos[1] -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if not cells[agent_pos]['baixo']:
                new_pos[1] += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if not cells[agent_pos]['esquerda']:
                new_pos[0] -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if not cells[agent_pos]['direita']:
                new_pos[0] += 1

        agent_pos = tuple(new_pos)
        clock.tick(FPS)

    print("Objetivo alcançado!")
    time.sleep(2)
    pygame.quit()
    # Função Main com escolha de modo
if __name__ == "__main__":
    print("Escolha o modo do agente:")
    print("1 - Modo Automático (BFS)")
    print("2 - Modo Manual (Controle com Teclas)")

    choice = input("Escolha 1 ou 2: ")

    start = Breadth_First_Search.start
    goal = Breadth_First_Search.goal

    if choice == '1':
        path = Breadth_First_Search.BFS(start, goal)
        if path:
            print(f"Caminho de {start} para {goal}: {path}")
            animar_agente(maze, path)
        else:
            print(f"O objetivo {goal} não existe.")
    elif choice == '2':
        controlar_agente(maze, start, goal)
    else:
        print("Escolha inválida.")


