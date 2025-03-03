import sys
import pygame
import button
from variables import (pantalla,fuente,Español, Ingles)
from variables import musica
import variables
pygame.init()
pygame.display.set_caption('data/imagenes/icono.png')
icon = pygame.image.load('data/imagenes/icono.png').convert_alpha()
pygame.display.set_icon (icon)
pygame.display.set_caption('Monkey Guard')

pygame.display.set_caption('Monkey Guard')
fondo = pygame.image.load('data/imagenes/Background.jpeg').convert_alpha()
botonM = button.Button(200, 350, pygame.image.load("data/imagenes/botonMorado.png").convert_alpha(), 0.6)
botonR = button.Button(200, 450, pygame.image.load("data/imagenes/botonRojo.png").convert_alpha(), 0.6)
musica=musica()
# game loop
run = True
while run:

    pantalla.blit(fondo, [0, 0])
    if not botonM.draw(pantalla):
        pass
    else:
        exec(open('./Niveles.py', encoding="utf-8").read())
        sys.exit()
    if botonR.draw(pantalla):
        sys.exit()
    if variables.ingles ==True:
        pantalla.blit(fuente.render(Ingles[0],1,(0,0,0)), (242, 365))
        pantalla.blit(fuente.render(Ingles[1],1,(0,0,0)), (245, 465))
    else:
        pantalla.blit(fuente.render(Español[0],1,(0,0,0)), (220, 365))
        pantalla.blit(fuente.render(Español[1],1,(0,0,0)), (232, 465))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
