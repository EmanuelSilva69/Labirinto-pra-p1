import pygame #Gerar o labirinto
import random #randomizar o negócio
import time 

#Aqui vou definir o tamanho da janela do pygame (tamanho da maze tbm né)
RES = WIDTH, HEIGHT = 1200, 900 #parametros da janela
TILE = 50
cols, rows = WIDTH // TILE, HEIGHT // TILE #isso daqui é a divisão inteira. N pode ter meio Bloco de altura
pygame.init()

sc = pygame.display.set_mode(RES) #faz a janela abrir usando os parametros lá de cima
#84BCDA hash de Carolina Blue (botei uma cor aleatória)