import sys
import pygame
import button
import variables
from variables import (pantalla, botonMorado)
# create display window

pygame.display.set_caption('data/imagenes/icono.png')
icon = pygame.image.load('data/imagenes/icono.png').convert_alpha()
pygame.display.set_icon (icon)

pygame.display.set_caption('Monkey Guard')
fondo1 = pygame.image.load('data/imagenes/Game_over_español.png').convert_alpha()
fondo2 = pygame.image.load('data/imagenes/Game_over_ingles.png').convert_alpha()
# load button images
retornar = pygame.image.load(botonMorado).convert_alpha()

pygame.mixer.music.load("data/audio/Game-Over.wav")
pygame.mixer.music.play(1) 

# create button instances
ret_button = button.Button(240, 400, retornar, 1.1)
contador=1
# game loop
run = True
while run:
    if variables.ingles==False:
        pantalla.blit(fondo1, [0, 0])
    else:
        pantalla.blit(fondo2, [0,0])
    if contador>1000:
        if not ret_button.draw(pantalla):
            pass
        else:
            variables.aparecer=False
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.load('data/audio/Menu.wav')
            pygame.mixer.music.play(-1)
            exec(open('./Niveles.py', encoding="utf-8").read())
            sys.exit()
    else:
        contador+=1
    if variables.ingles==True:
        pantalla.blit(variables.fuente.render(variables.Ingles[2],1,(0,0,0)), (250, 445))
    else:
        pantalla.blit(variables.fuente.render(variables.Español[2],1,(0,0,0)), (250, 445))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
