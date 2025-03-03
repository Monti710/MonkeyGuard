import sys
import pygame
import button
import variables
from variables import (W,H, Ingles,Español,fuente)

# create display window


pantalla = pygame.display.set_mode((W, H))
pygame.display.set_caption('Monkey Guard')
icon = pygame.image.load('data/imagenes/icono.png').convert_alpha()
pygame.display.set_icon (icon)

# load button images
level1_img = pygame.image.load('data/imagenes/nivel1.png').convert_alpha()
level2_img = pygame.image.load('data/imagenes/nivel2.png').convert_alpha()
level3_img = pygame.image.load('data/imagenes/nivel3.png').convert_alpha()
boton = pygame.image.load(variables.botonMorado).convert_alpha()
# create button instances
level3_button= button.Button(750,260, level3_img,0.8)
level2_button = button.Button(425, 250, level2_img, 0.9)
level1_button = button.Button(125, 260, level1_img, 0.8)
configuracion = button.Button(750,50,boton,0.7)
nivelFacil = button.Button(450, 450, boton, 0.6)
nivelDificil = button.Button(700, 450, boton, 0.6)
dificil = False
fondo = pygame.image.load("data/imagenes/fondoNiveles.png").convert_alpha()
fondoDificl = pygame.image.load("data/imagenes/fondomenu.png").convert_alpha()
hardcore = pygame.image.load("data/imagenes/hardcore.png").convert_alpha()
easy = pygame.image.load("data/imagenes/easy.png").convert_alpha()
botonR = button.Button(200, 450, pygame.image.load("data/imagenes/botonRojo.png").convert_alpha(), 0.6)
# game loop
run = True
variables.difuminado1=False
variables.difuminado2=False
variables.difuminado3=False

while run:
    pantalla.blit(fondoDificl,[0,0])
    if variables.fD==True:
        pantalla.blit(fondo, [0, 0])   
    if not nivelFacil.draw(pantalla):
        pass
    else: 
        variables.fD=False
        variables.dificil=False
    if not nivelDificil.draw(pantalla):
        pass
    else: 
        variables.fD=True
        variables.dificil=True
    if not configuracion.draw(pantalla):
        pass
    else: 
        exec(open('./configuraciones.py', encoding="utf-8").read())
        sys.exit()
    if not level1_button.draw(pantalla):
        pass
    else:
        variables.difuminado1=True
        exec(open('./introducciones.py', encoding="utf-8").read())
        sys.exit()
    if not level2_button.draw(pantalla):
        pass
    else:
        variables.difuminado2=True
        exec(open('./introducciones.py', encoding="utf-8").read())
        sys.exit()
    if not level3_button.draw(pantalla):
        pass
    else:
        variables.difuminado3=True
        exec(open('./introducciones.py', encoding="utf-8").read())
        sys.exit()
    if botonR.draw(pantalla):
        exec(open('./button_main.py', encoding="utf-8").read())
        sys.exit()
    if variables.ingles ==True:
        pantalla.blit(fuente.render(Ingles[7],1,(0,0,0)), (160, 280))
        pantalla.blit(fuente.render(Ingles[8],1,(0,0,0)), (460, 280))
        pantalla.blit(fuente.render(Ingles[9],1,(0,0,0)), (780, 280))
        pantalla.blit(fuente.render(Ingles[1],1,(0,0,0)), (245, 465))
        pantalla.blit(fuente.render(Ingles[10],1,(0,0,0)), (767, 72))
        pantalla.blit(fuente.render(Ingles[13],1,(0,0,0)), (740, 470))
        pantalla.blit(fuente.render(Ingles[12],1,(0,0,0)), (495, 470))
    else:
        pantalla.blit(fuente.render(Español[7],1,(0,0,0)), (160, 280))
        pantalla.blit(fuente.render(Español[8],1,(0,0,0)), (460, 280))
        pantalla.blit(fuente.render(Español[9],1,(0,0,0)), (780, 280))
        pantalla.blit(fuente.render(Español[1],1,(0,0,0)), (232, 465))
        pantalla.blit(fuente.render(Español[10],1,(0,0,0)), (770, 72))
        pantalla.blit(fuente.render(Español[13],1,(0,0,0)), (735, 470))
        pantalla.blit(fuente.render(Español[12],1,(0,0,0)), (495, 470))
    if variables.dificil==True:
        pantalla.blit(pygame.transform.scale(hardcore, (180, 180)), (400, 10))
        if variables.ingles == True:
            pantalla.blit(fuente.render(Ingles[13],1,(255,255,255)), (430, 200))
        else:
            pantalla.blit(fuente.render(Español[13],1,(255,255,255)), (430, 200))
    else:
        pantalla.blit(pygame.transform.scale(easy, (200, 200)), (370, 10))
        if variables.ingles == True:
            pantalla.blit(fuente.render(Ingles[12],1,(255,255,255)), (430, 200))
        else:
            pantalla.blit(fuente.render(Español[12],1,(255,255,255)), (430, 200))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
