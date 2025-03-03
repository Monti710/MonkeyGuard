import pygame, sys
import variables
import button

# create display window

pantalla=variables.pantalla
pygame.display.set_caption('data/imagenes/icono.png')
icon = pygame.image.load('data/imagenes/icono.png').convert_alpha()
pygame.display.set_icon (icon)

pygame.display.set_caption('Monkey Guard')
fondo = pygame.image.load('data/imagenes/FondoIdiomas.png').convert_alpha()

boton =pygame.image.load(variables.botonMorado).convert_alpha()
botonR = pygame.image.load(variables.botonRojo).convert_alpha()
mute_img = pygame.image.load('data/imagenes/Mute.png').convert_alpha()
exit_img = pygame.image.load('data/imagenes/Volumenon.png').convert_alpha()
# create button instances
cambioIngles = button.Button(350, 100, boton, 0.8)
cambioEspañol = button.Button(350, 250, boton, 0.8)
controles= button.Button(335,400,boton,0.9)
volver= button.Button(40,40,botonR,0.6)
mute_button = button.Button(750, 70, mute_img, 0.8)
son_button = button.Button(750, 175, exit_img, 0.8)
# game loop
run = True
while run:
    pantalla.blit(fondo, [0, 0])
    
    if not mute_button.draw(pantalla):
         pass
    else:
        pygame.mixer.music.set_volume(0.0)
    if son_button.draw(pantalla):
        pygame.mixer.music.set_volume(1.0)
    if not cambioIngles.draw(pantalla):
        pass
    else:
        variables.ingles=True
        variables.ingles=variables.ingles
    if not cambioEspañol.draw(pantalla):
        pass
    else:
        variables.ingles=False
        variables.ingles=variables.ingles
    if not controles.draw(pantalla):
        pass
    else:
        exec(open('./controles.py', encoding="utf-8").read())
    if not volver.draw(pantalla):
        pass
    else:
        exec(open('./Niveles.py', encoding="utf-8").read())
        sys.exit()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    if variables.ingles==True:
        pantalla.blit(variables.fuente.render(variables.Ingles[4],1,(0,0,0)), (395, 278))
        pantalla.blit(variables.fuente.render(variables.Ingles[5],1,(0,0,0)), (395, 128))
        pantalla.blit(variables.fuente.render(variables.Ingles[6],1,(0,0,0)), (375, 435))
        pantalla.blit(variables.fuente.render(variables.Ingles[3],1,(0,0,0)), (83, 58))
    else:
        pantalla.blit(variables.fuente.render(variables.Español[4],1,(0,0,0)), (390, 275))
        pantalla.blit(variables.fuente.render(variables.Español[5],1,(0,0,0)), (405, 130))
        pantalla.blit(variables.fuente.render(variables.Español[6],1,(0,0,0)), (360, 435))
        pantalla.blit(variables.fuente.render(variables.Español[3],1,(0,0,0)), (58, 58))  
    pygame.display.update()

pygame.quit()
