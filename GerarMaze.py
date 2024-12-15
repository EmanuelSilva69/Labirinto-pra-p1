import pygame  #Gerar o labirinto
import random  #randomizar o negócio
import json
from PIL import Image
import time
#Aqui vou definir o tamanho da janela do pygame (tamanho da maze tbm né)
RES = WIDTH, HEIGHT = 1200, 900  #parametros da janela
TILE = 30
cols, rows = WIDTH // TILE, HEIGHT // TILE  #isso daqui é a divisão inteira. N pode ter meio Bloco de altura
pygame.init()

sc = pygame.display.set_mode(RES)  #faz a janela abrir usando os parametros lá de cima
#84BCDA hash de Carolina Blue (botei uma cor aleatória)
clock = pygame.time.Clock()
pygame.display.set_caption('Gerador do Labirinto')


#eu vi isso daqui pra botar as cores no reddit. Fiquei interessado ent vou implementar aqui
def cwrap(x):
    q, r = divmod(x, 255)
    if q % 2:
        return 255 - r
    else:
        return r
#bonito papo reto.
#classe de célula

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.walls = {'cima': True, 'esquerda': True, 'direita': True, 'baixo': True}
        self.visitado = False

    def draw_current_cell(self):
        x, y = self.x * TILE, self.y * TILE
        pygame.draw.rect(sc, pygame.Color('#067BC2'), (x + 2, y + 2, TILE - 2, TILE - 2))

    def draw(self):
        x, y = self.x * TILE, self.y * TILE
        if self.visitado:
            col = (cwrap(self.x * 14), #coloque col na cor pra o fundo ficar doidão.
                   cwrap(self.y * -20),
                   cwrap(self.y * 30)) #caso queira usar o fundo cinza, pygame.Color('#1e1e1e')
            pygame.draw.rect(sc, pygame.Color('#3eb489'), (x, y, TILE, TILE))
        if self.walls['cima']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x, y), (x + TILE, y), 3)
        if self.walls['esquerda']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x, y + TILE), (x, y), 3)
        if self.walls['direita']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x + TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['baixo']:
            pygame.draw.line(sc, pygame.Color('#1e4f5b'), (x + TILE, y + TILE), (x, y + TILE), 3)

    def check_cell(self, x, y):
        find_index = lambda x, y: x + y * cols
        if x < 0 or x > cols - 1 or y < 0 or y > rows - 1:  #comando geral pra checar as células
            return False
        return grid_cells[find_index(x, y)]

    def check_neighbors(self):
        neighbors = []
        cima = self.check_cell(self.x, self.y - 1)
        esquerda = self.check_cell(self.x - 1, self.y)
        direita = self.check_cell(self.x + 1, self.y)
        baixo = self.check_cell(self.x, self.y + 1)
        if cima and not cima.visitado:
            neighbors.append(cima)  #visita o de cima
        if esquerda and not esquerda.visitado:
            neighbors.append(esquerda)  #visita o da esquerda
        if direita and not direita.visitado:
            neighbors.append(direita)  #visita o da direita
        if baixo and not baixo.visitado:
            neighbors.append(baixo)  #visita o de cima
        return random.choice(neighbors) if neighbors else False


def remove_wall(current, next):  #remover a parede (ava)
    dx = current.x - next.x
    dy = current.y - next.y
    if dx == 1:
        current.walls['esquerda'] = False
        next.walls['direita'] = False
    elif dx == -1:
        current.walls['direita'] = False
        next.walls['esquerda'] = False
    if dy == 1:
        current.walls['cima'] = False
        next.walls['baixo'] = False
    if dy == -1:
        current.walls['baixo'] = False
        next.walls['cima'] = False

def reset_game_state(): #resetar o negócio
    global grid_cells, current_cell, stack, colors, color, maze_array #assume as variáveis normais
    grid_cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
    current_cell = grid_cells[0]
    stack = []
    colors, color = [], 80


grid_cells = [Cell(col, row)
              for row in range(rows)
              for col in range(cols)]
current_cell = grid_cells[0]
colors, color = [], 80
stack = []

while True:
    sc.fill(pygame.Color('#D56062'))  #bota a Carolina Blue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #fecha se eu apertar o x
            exit()
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE: #resetar a criação do mapa
            reset_game_state()
    [cell.draw() for cell in grid_cells]
    current_cell.visitado = True
    current_cell.draw_current_cell()
    [pygame.draw.rect(sc, colors[i],
                      (cell.x * TILE + 2, cell.y * TILE + 2,
                       TILE , TILE )) for i,
     cell in enumerate(stack)]
    # Descomente caso for usar Cinza!
    #eu tinha feito usando o cwrap mas ficou colorido demais, ai n sei se devo fazer daquele jeito
    next_cell = current_cell.check_neighbors()
    if next_cell:
        next_cell.visited = True
        stack.append(current_cell)
        colors.append((cwrap(current_cell.x * 32), cwrap(current_cell.y * -12), cwrap(current_cell.y * 42))) #isso dai serve pra pintar coloridinho os quadrados que passam na criação
        #comente acima caso for usar o gradiente do fundo
        remove_wall(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()
    else:
        # Quando o labirinto for concluído, saia do loop
        time.sleep(2)
        print("Labirinto concluído!")
        pygame.image.save(sc, "labirinto.png")
        pygame.quit()
        exit()
    pygame.display.flip()
    clock.tick(20)


    # exportar a imagem
    Maze_array = [{'x': cell.x, 'y': cell.y, 'walls': cell.walls} for cell in grid_cells]
    print(Maze_array)
    file_path = 'walls_data.json'
    # Salvar a Imagem
    with open(file_path, 'w') as json_file:
        json.dump(Maze_array, json_file)