import sys
import pygame
import button
import variables
from variables import (pantalla, botonMorado)
# create display window


pygame.display.set_caption('data/imagenes/icono.PNG')
icon = pygame.image.load('data/imagenes/icono.PNG').convert_alpha()
pygame.display.set_icon (icon)

pygame.display.set_caption('Monkey Guard')
fondo = pygame.image.load('data/imagenes/PantallaWin.png').convert_alpha()
# load button images
retornar = pygame.image.load(variables.botonDorado).convert_alpha()

pygame.mixer.init()
# create button instances
ret_button = button.Button(342, 400, retornar, 1.1)
pygame.mixer.music.load("data/audio/Winner.wav")
pygame.mixer.music.play(1) 
# game loop
run = True
contador=1
while run:
    pantalla.blit(fondo, [0, 0])
    contador+=1
    if contador >3000:
        if not ret_button.draw(pantalla):
            pass
        else:
            variables.aparecer=False
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.load('data/audio/MENU.wav')
            pygame.mixer.music.play(-1)
            exec(open('./Niveles.py', encoding="utf-8").read())
            sys.exit()
    if variables.ingles==True:
        if contador>3000:
            pantalla.blit(variables.fuente.render(variables.Ingles[2],1,(0,0,0)), (352, 445))
        pantalla.blit(variables.fuente.render(variables.Ingles[11],1,(255,255,255)), (417, 110))
    else:
        if contador>3000:
            pantalla.blit(variables.fuente.render(variables.Español[2],1,(0,0,0)), (352, 445))
        pantalla.blit(variables.fuente.render(variables.Español[11],1,(255,255,255)), (404, 110))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
