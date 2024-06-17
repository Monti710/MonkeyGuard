import pygame, sys
import variables
import button

# create display window

pantalla=variables.pantalla
pygame.display.set_caption('data/imagenes/icono.PNG')
icon = pygame.image.load('data/imagenes/icono.PNG').convert_alpha()
pygame.display.set_icon (icon)

pygame.display.set_caption('Monkey Guard')

boton =pygame.image.load(variables.botonRojo).convert_alpha()
d1 = pygame.image.load("data/imagenes/difuminado1.png")
d2 = pygame.image.load("data/imagenes/difuminado2.png")
d3 = pygame.image.load("data/imagenes/difuminado3.png")
# create button instances
volver= button.Button(400,500,boton,0.6)

if variables.dificil==True:
    pygame.mixer.music.load('data/audio/Nivel2.wav')
    pygame.mixer.music.play(-1) 
else:
    pygame.mixer.music.load('data/audio/Mi-video.wav')
    pygame.mixer.music.play(-1) 
objetivos = pygame.image.load("data/imagenes/cartel-grande.png").convert_alpha()
mono = pygame.image.load("data/imagenes/quieto.png").convert_alpha()
Bike = pygame.image.load("data/imagenes/cajaBike.png").convert_alpha()
Bike.set_colorkey((255,255,255))
Bike = Bike.convert()
base = pygame.image.load("data/imagenes/based.png").convert_alpha()
base.set_colorkey((255,255,255))
base = base.convert()
paneles = pygame.image.load("data/imagenes/panel.png").convert_alpha()
paneles.set_colorkey((255,255,255))
paneles = paneles.convert()
# game loop
run = True
while run:
    if variables.difuminado1==True:
        pantalla.blit(d1, [0,0])
        pantalla.blit(pygame.transform.scale(objetivos, (850, 200)), (80, 20))
        pantalla.blit(pygame.transform.scale(objetivos, (850, 135)), (80, 270))
        pantalla.blit(pygame.transform.scale(mono, (200, 200)), (100, 400))
        pantalla.blit(pygame.transform.scale(Bike, (200, 200)), (700, 400))
        if variables.ingles==True:
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[0],1,(255,255,255)), (100, 60))
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[1],1,(255,255,255)), (100, 90))
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[2],1,(255,255,255)), (100, 120))
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[3],1,(255,255,255)), (100, 165))
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[4],1,(255,255,255)), (100, 300))
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[5],1,(255,255,255)), (100, 330))
            pantalla.blit(variables.fuente2.render(variables.Historia1_ingles[6],1,(255,255,255)), (100, 360))
        else:
            pantalla.blit(variables.fuente2.render(variables.Historia1[0],1,(255,255,255)), (100, 60))
            pantalla.blit(variables.fuente2.render(variables.Historia1[1],1,(255,255,255)), (100, 90))
            pantalla.blit(variables.fuente2.render(variables.Historia1[2],1,(255,255,255)), (100, 120))
            pantalla.blit(variables.fuente2.render(variables.Historia1[3],1,(255,255,255)), (100, 165))
            pantalla.blit(variables.fuente2.render(variables.Historia1[4],1,(255,255,255)), (100, 300))
            pantalla.blit(variables.fuente2.render(variables.Historia1[5],1,(255,255,255)), (100, 330))
            pantalla.blit(variables.fuente2.render(variables.Historia1[6],1,(255,255,255)), (100, 360))
        if not volver.draw(pantalla):
            pass
        else:
            exec(open('./Juego1.py', encoding="utf-8").read())
            sys.exit()
    if variables.difuminado2==True:
        pantalla.blit(d2, [0,0])
        pantalla.blit(pygame.transform.scale(objetivos, (850, 200)), (80, 20))
        pantalla.blit(pygame.transform.scale(objetivos, (850, 135)), (80, 270))
        pantalla.blit(pygame.transform.scale(mono, (200, 200)), (100, 400))
        pantalla.blit(pygame.transform.scale(base, (200, 200)), (700, 400))
        if variables.ingles==True:
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[0],1,(255,255,255)), (100, 70))
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[1],1,(255,255,255)), (100, 100))
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[2],1,(255,255,255)), (100, 130))
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[3],1,(255,255,255)), (100, 160))
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[4],1,(255,255,255)), (100, 300))
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[5],1,(255,255,255)), (100, 330))
            pantalla.blit(variables.fuente2.render(variables.Historia2_ingles[6],1,(255,255,255)), (100, 360))
        else:
            pantalla.blit(variables.fuente2.render(variables.Historia2[0],1,(255,255,255)), (100, 70))
            pantalla.blit(variables.fuente2.render(variables.Historia2[1],1,(255,255,255)), (100, 100))
            pantalla.blit(variables.fuente2.render(variables.Historia2[2],1,(255,255,255)), (100, 130))
            pantalla.blit(variables.fuente2.render(variables.Historia2[3],1,(255,255,255)), (100, 160))
            pantalla.blit(variables.fuente2.render(variables.Historia2[4],1,(255,255,255)), (100, 300))
            pantalla.blit(variables.fuente2.render(variables.Historia2[5],1,(255,255,255)), (100, 330))
            pantalla.blit(variables.fuente2.render(variables.Historia2[6],1,(255,255,255)), (100, 360))
        if not volver.draw(pantalla):
            pass
        else:
            exec(open('./Juego2.py', encoding="utf-8").read())
            sys.exit()
    if variables.difuminado3==True:
        pantalla.blit(d3, [0,0])
        pantalla.blit(pygame.transform.scale(objetivos, (850, 200)), (80, 20))
        pantalla.blit(pygame.transform.scale(objetivos, (850, 135)), (80, 270))
        pantalla.blit(pygame.transform.scale(mono, (200, 200)), (100, 400))
        pantalla.blit(pygame.transform.scale(paneles, (200, 200)), (700, 400))
        if variables.ingles==True:
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[0],1,(255,255,255)), (100, 70))
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[1],1,(255,255,255)), (100, 100))
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[2],1,(255,255,255)), (100, 130))
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[3],1,(255,255,255)), (100, 160))
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[4],1,(255,255,255)), (100, 300))
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[5],1,(255,255,255)), (100, 330))
            pantalla.blit(variables.fuente2.render(variables.Historia3_ingles[6],1,(255,255,255)), (100, 360))
        else:
            pantalla.blit(variables.fuente2.render(variables.Historia3[0],1,(255,255,255)), (100, 70))
            pantalla.blit(variables.fuente2.render(variables.Historia3[1],1,(255,255,255)), (100, 100))
            pantalla.blit(variables.fuente2.render(variables.Historia3[2],1,(255,255,255)), (100, 130))
            pantalla.blit(variables.fuente2.render(variables.Historia3[3],1,(255,255,255)), (100, 160))
            pantalla.blit(variables.fuente2.render(variables.Historia3[4],1,(255,255,255)), (100, 300))
            pantalla.blit(variables.fuente2.render(variables.Historia3[5],1,(255,255,255)), (100, 330))
            pantalla.blit(variables.fuente2.render(variables.Historia3[6],1,(255,255,255)), (100, 360))
        if not volver.draw(pantalla):
            pass
        else:
            exec(open('./Juego3.py', encoding="utf-8").read())
            sys.exit()
            
    if variables.ingles == True:
        pantalla.blit(variables.fuente.render(variables.Ingles[18],1,(0,0,0)), (440, 520))  
    else:
        pantalla.blit(variables.fuente2.render(variables.Español[18],1,(0,0,0)), (410, 520))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    pygame.display.update()

pygame.quit()
