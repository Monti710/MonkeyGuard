import pygame,sys
from Jugador import jugador
import variables
from objetos import objeto
from variables import (pantalla,negro,fps,reloj,Termino)
from Mapa import Mapa
import button

variables.juego1=True
variables.juego2=False
variables.juego3=False
pygame.display.set_caption('Monkey Guard')
icon = pygame.image.load('data/imagenes/icono.PNG')
pygame.display.set_icon (icon)
p1 = "data/imagenes/pizo.png"
p2 = "data/imagenes/rt.png"
fondo = "data/imagenes/nivel1.png"
img = "data/imagenes/cajaBike.png"
if variables.dificil==True:
    counter, text = 100, '100'.rjust(7)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    fonNivel = "data/imagenes/fondoNivel1.png"
    Map = "nivel1_Di.txt"
    Nivel=False
    Vidas=True
    Objeto = True
else:
    counter, text = 300, '300'.rjust(7)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    fonNivel = "data/imagenes/fondoNivel1-1.png"
    Map = "nivel1.txt"
    Nivel=False
    Vidas=True
    Objeto = True
#Inicializar
mapa=Mapa()
monti = jugador()
mapa.init(pantalla=pantalla, Nivel1=Nivel, Map=Map, Objet=Objeto)
monti.init(pantalla)
if variables.dificil == True:
    monti.vidas= monti.vidas-2
#Prueba
#fin prueba
while not Termino:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termino = True
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(7) 
            if counter < 0 : 
                Termino=True
                objeto.cantidad -= objeto.cantidad
                exec(open('GameOver.py', encoding="utf-8").read())
        #Eventos
        monti.eventos(event)
        
    # Actualizacion de los sprite
    monti.actualizar()
    mapa.Actualizar(monti)
    pantalla.fill(negro)
    pantalla.blit(font.render(text, True, (255, 255, 255)), (70, 20))
    #Dibujar
    mapa.dibujar(pantalla, monti, fondo=fondo, p1=p1, p2=p2, fonNivel=fonNivel, Map=Map,incVidas=Vidas, imagen=img)
    monti.dibujar(pantalla)
    if variables.ingles==True:
        pantalla.blit(variables.fuente.render(variables.Ingles[7],1,(0,0,0)), (815, 20))
    else:
        pantalla.blit(variables.fuente.render(variables.Español[7],1,(0,0,0)), (815, 20))
    pygame.display.flip()
    reloj.tick(fps)

# Salida del juego
pygame.quit()