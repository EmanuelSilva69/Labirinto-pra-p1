import json
import GerarMaze
import Breadth_First_Search
import pygame
import time
import random
# carrega o arquivo
with open('walls_data.json', 'r') as file:
    maze = json.load(file)

# organizar as celulas
cells = {(cell['x'], cell['y']): cell['walls'] for cell in maze}
TILE_SIZE = GerarMaze.TILE
RES = WIDTH, HEIGHT = 1200, 900  #parametros da janela
PATH_COLOR = pygame.Color('#68B684')
GRID_COLOR = pygame.Color('#3eb489')
AGENT_COLOR=pygame.Color('#F35B04')
FPS=10
"""Tudo foi retirado do arquivo GerarMaze. Não quis fazer um config pq ai teria q mudar tudo ai seria paia."""
BACKGROUND_COLOR = pygame.Color('#3eb489')
screen = GerarMaze.sc
path = Breadth_First_Search.BFS(Breadth_First_Search.start, Breadth_First_Search.goal)

def desenhar_agente_grid(screen,maze,path,current_index):
    screen.fill(BACKGROUND_COLOR) #limpa a tela
    for cell in maze:
        x,y = cell['x'], cell['y']
        walls = cell['walls']
        rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, GRID_COLOR, rect)  # Desenha a grid

        # Draw walls
        if walls['cima']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), (x * TILE_SIZE, y * TILE_SIZE), ((x + 1) * TILE_SIZE, y * TILE_SIZE),
                             2)
        if walls['baixo']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), (x * TILE_SIZE, (y + 1) * TILE_SIZE),
                             ((x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE), 2)
        if walls['esquerda']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), (x * TILE_SIZE, y * TILE_SIZE), (x * TILE_SIZE, (y + 1) * TILE_SIZE),
                             2)
        if walls['direita']:
            pygame.draw.line(screen, pygame.Color('#1e4f5b'), ((x + 1) * TILE_SIZE, y * TILE_SIZE),
                             ((x + 1) * TILE_SIZE, (y + 1) * TILE_SIZE), 2)
    # Mostra o caminho percorrido
    for idx in range(current_index):  # apenas pinta o que já foi visitado
        x, y = path[idx]
        rect = pygame.Rect(x * TILE_SIZE + 10 , y * TILE_SIZE + 10 , TILE_SIZE - 20, TILE_SIZE - 20) #diminui as bolas que ficam no caminho
        pygame.draw.rect(screen, pygame.Color('#3D348B'), rect,border_radius=20,) #deixei com borda ai, e não no gerarmaze pq lá é bonito sem borda, aqui é FEIO, n pode fechar todo o negócio n

    if current_index < len(path):
        x, y = path[current_index]
        agent_pos = (x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2) #posição do agente dentro do tileset
        pygame.draw.circle(screen, AGENT_COLOR, agent_pos, TILE_SIZE // 4) #desenha o agente no local atual


        # Desenha o Objetivo
    gx, gy = Breadth_First_Search.goal
    goal_rect = pygame.Rect(gx * TILE_SIZE +5, gy * TILE_SIZE +5, TILE_SIZE - 10, TILE_SIZE - 10)
    pygame.draw.rect(screen, pygame.Color('#F9627D'), goal_rect,border_radius=10)  #Pinta o tile do objetivo

    pygame.display.flip()  # Atualiza o display
def animar_agente(maze,path):
    #animar o agente andando (animar é uma palavra forte)
    sc = pygame.display.set_mode(GerarMaze.RES)
    clock = pygame.time.Clock()

    for current_index in range(len(path)):
        desenhar_agente_grid(sc, maze, path, current_index)

        # Fechar a janela que nem o outro no Gerar Maze
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        clock.tick(FPS)  # Velocidade do negócio

    # Quando chegar no path, fecha.
    time.sleep(2)
    pygame.quit()

if __name__ == "__main__":


    # Perform BFS to get the path
    path = Breadth_First_Search.BFS(Breadth_First_Search.start, Breadth_First_Search.goal)
    if path:
        print(f"Caminho de {Breadth_First_Search.start} para {Breadth_First_Search.goal}: {path}")
        animar_agente(maze, path)
    else:
        print(f"O objetivo {Breadth_First_Search.goal} não existe.")