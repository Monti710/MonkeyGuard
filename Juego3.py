import pygame,sys
from Jugador import jugador
from Mapa import Mapa
import variables
from objetos import objeto
from variables import (negro,fps,reloj,Termino)
import button

variables.juego1=False
variables.juego2=False
variables.juego3=True

pantalla = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Monkey Guard')
icon = pygame.image.load('data/imagenes/icono.png')
pygame.display.set_icon (icon)
p1 = "data/imagenes/piso_pasto.png"
p2 = "data/imagenes/pizo2.png"
fondo = "data/imagenes/nivel3.png"
img = "data/imagenes/panel.png"

if variables.dificil==True:
    counter, text = 100, '100'.rjust(7)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    fonNivel = "data/imagenes/fondoNivel3.png"
    Map = "nivel3_Di.txt"
    Nivel=False
    Vidas=False
    Objeto = True
else:
    counter, text = 300, '300'.rjust(7)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    fonNivel = "data/imagenes/fondoNivel3.png"
    Map = "nivel3.txt"
    Nivel=False
    Vidas=False
    Objeto = True
#Inicializar
mapa=Mapa()
monti = jugador()
mapa.init(pantalla=pantalla, Nivel1=Nivel, Objet=Objeto, Map=Map)
monti.init(pantalla)



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
                #enemigo.
                exec(open('GameOver.py', encoding="utf-8").read())
                
        #Eventos
        monti.eventos(event)
    
    # Actualizacion de los sprite
    monti.actualizar()
    mapa.Actualizar(monti)
    pantalla.fill(negro)
    pantalla.blit(font.render(text, True, (255, 255, 255)), (70, 20))
    #Dibujar
    mapa.dibujar(pantalla, monti, fondo=fondo, p1=p1, p2=p2, fonNivel=fonNivel, Map=Map, incVidas=Vidas, imagen=img)
    monti.dibujar(pantalla)
    if variables.ingles==True:
        pantalla.blit(variables.fuente.render(variables.Ingles[9],1,(0,0,0)), (815, 20))
    else:
        pantalla.blit(variables.fuente.render(variables.Español[9],1,(0,0,0)), (815, 20))
    pygame.display.flip()
    reloj.tick(fps)

# Salida del juego
pygame.quit()