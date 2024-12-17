# Labirinto pra p1
Labirinto criado para a realização de parte da nota da P1 na Cadeira de Inteligência Artificial 
------------------------------------------
Requisitos :
Instalar o Pygame





-----------------------------------------------------------------------------------------------------
Um adendo aqui, eu fiz que a pintura do mapa na criação do mundo tenha 3 jeitos. O labirinto colorido:
![image](https://github.com/user-attachments/assets/29a67180-4898-421f-852c-46e6a53990b7)

que é só botar "col" no :         if self.visitado:
            col = (cwrap(self.x * 14), #coloque col na cor pra o fundo ficar doidão.
                   cwrap(self.y * -20),
                   cwrap(self.y * 30)) #caso queira usar o fundo cinza, pygame.Color('#1e1e1e')
            pygame.draw.rect(sc, **AQUI** , (x, y, TILE, TILE))
ou o padrão que tá normalmente que é uma cor sólida. Só bota o código da cor ali no local marcado.
Há tambem a opção de tirar o rastro colorido, que é só comentar a parte do código :
[pygame.draw.rect(sc, colors[i],
                          (cell.x * TILE + 2, cell.y * TILE + 2,
                           TILE , TILE )) for i,
         cell in enumerate(stack)]
        # Descomente caso for usar Cinza! (cinza ai é a cor base que eu coloquei no **Aqui**. 
        #eu tinha feito usando o cwrap mas ficou colorido demais, ai n sei se devo fazer daquele jeito

