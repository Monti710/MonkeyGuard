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
control_e = pygame.image.load("data/imagenes/controles_español.png")
control_i = pygame.image.load("data/imagenes/controles_ingles.png")
# create button instances
volver= button.Button(400,500,boton,0.6)

# game loop
run = True
while run:
    if variables.ingles==True:
        pantalla.blit(control_i, [0,0])
    else:
        pantalla.blit(control_e, [0,0])
    if not volver.draw(pantalla):
        pass
    else:
        exec(open('./configuraciones.py', encoding="utf-8").read())
        sys.exit()
    if variables.ingles == True:
        pantalla.blit(variables.fuente.render(variables.Ingles[3],1,(0,0,0)), (440, 520))  
    else:
        pantalla.blit(variables.fuente.render(variables.Español[3],1,(0,0,0)), (420, 520))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
     
    pygame.display.update()

pygame.quit()
