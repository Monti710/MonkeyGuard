import pygame, sys
from objetos import objeto,bici,bases
import button
import variables
from Jugador import jugador
from enemigos import enemigo
tamano = 30
azul = (152, 217, 234)
verde = (0, 170, 0)
blanco = (255,255,255)
negro = (0, 0, 0)
hueso = (230, 214, 144)
VERDE = 0, 255, 0
H_FA2F2F = (250, 47, 47)
cafe = (128,64,0)
amarillo = (255,255,0)
naranja = (255,64,0)
verdee = (45,87,44)
transparente=(240,248,255)
paused = pygame.image.load("data/imagenes/Pause.png").convert_alpha()
pa_button = button.Button(10, 10, paused, 0.8)
class Mapa:
    cuenta=1
    espacio = 0
    enemigos = []
    
    def init(self, pantalla ,Nivel1, Objet, Map):
        mapa = open(Map, "r")
        if Nivel1 == True:
            for (idx, fila) in enumerate(mapa):
                for(idx2, col) in enumerate(fila):
                    posx = idx2 * tamano - self.espacio
                    posy = idx * tamano
                    if col == "r" or col == "e":
                        nuevo_enemigo = enemigo()
                        nuevo_enemigo.init(pantalla, posx, posy)
                        self.enemigos.append(nuevo_enemigo)
                    if col == "i" or col == "u":
                        nuevo_enemigo = bases()
                        nuevo_enemigo.init(pantalla, posx, posy)
                        self.enemigos.append(nuevo_enemigo)
        if Objet == True:
    
            for (idx, fila) in enumerate(mapa):
                for(idx2, col) in enumerate(fila):
                    posx = idx2 * tamano - self.espacio
                    posy = idx * tamano
                    if col == "r" or col == "e":
                        nuevo_enemigo = objeto()
                        nuevo_enemigo.init(pantalla, posx, posy)
                        self.enemigos.append(nuevo_enemigo)
                    if col == "o" or col == "x":
                        nuevo_enemigo = bici()
                        nuevo_enemigo.init(pantalla, posx, posy)
                        self.enemigos.append(nuevo_enemigo)
            
                        
        mapa.close()   
    def Actualizar (self, monti):

        for enem in self.enemigos:
            enem.actualizar(monti, self.espacio)
    def dibujar (self, pantalla, monti, fondo, p1, p2, fonNivel, Map, incVidas, imagen):
        self.piso = pygame.image.load(p1)
        self.piso2 = pygame.image.load(p2)
        #Probando
        self.pared = pygame.image.load("data/imagenes/muerto.png").convert_alpha()
        self.pared.set_colorkey((0, 0, 0))
        self.pared = self.pared.convert()
        self.objetivos = pygame.image.load("data/imagenes/cartel-grande.png").convert_alpha()
        self.objetivos.set_colorkey((255, 255, 255))
        self.objetivos = self.objetivos.convert()
        self.cajado = pygame.image.load("data/imagenes/caja.png").convert_alpha()
        self.cajado.set_colorkey((255, 255, 255))
        self.cajado = self.cajado.convert()
        self.cartellago = pygame.image.load("data/imagenes/cartl.png").convert_alpha()
        self.cartellago.set_colorkey((255, 255, 255))
        self.cartellago = self.cartellago.convert()
        self.muro = pygame.image.load("data/imagenes/muro_final.png").convert_alpha()
        self.muro.set_colorkey((0, 0, 0))
        self.muro = self.muro.convert()
        self.muro2 = pygame.image.load("data/imagenes/muro2.png").convert_alpha()
        self.muro2.set_colorkey((0, 0, 0))
        self.muro2 = self.muro2.convert()
        self.puerta = pygame.image.load("data/imagenes/puerta1.png").convert_alpha()
        self.puerta.set_colorkey((0, 0, 0))
        self.puerta = self.puerta.convert()
        self.basura = pygame.image.load("data/imagenes/basura.png").convert_alpha()
        self.basura.set_colorkey((255, 255, 255))
        self.basura = self.basura.convert()
        self.cartel = pygame.image.load("data/imagenes/cartel.png").convert_alpha()
        self.cartel.set_colorkey((255, 255, 255))
        self.cartel = self.cartel.convert()
        self.cartel2 = pygame.image.load("data/imagenes/cartel2.png").convert_alpha()
        self.cartel2.set_colorkey((255, 255, 255))
        self.cartel2 = self.cartel2.convert()
        self.tierra = pygame.image.load("data/imagenes/tierra.png").convert_alpha()
        self.tierra.set_colorkey((0, 0, 0))
        self.tierra = self.tierra.convert()
        self.lago = pygame.image.load("data/imagenes/lago.png").convert_alpha()
        self.lago.set_colorkey((255, 255, 255))
        self.lago = self.lago.convert()
        self.nota = pygame.image.load("data/imagenes/notas.png").convert_alpha()
        self.nota.set_colorkey((255,255,255))
        self.nota = self.nota.convert()
        self.cuadradito = pygame.image.load("data/imagenes/Negro.png").convert_alpha()
        self.cuadradito.set_colorkey((255,255,255))
        self.cuadradito = self.cuadradito.convert()
        self.murido = pygame.mixer.Sound("data/audio/MONO CHILLANDO.wav")
        
        if not pa_button.draw(pantalla):
            pass
        else:
            pausa(pantalla)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pausa(pantalla)
        #Fin probando
        self.fondo = pygame.image.load(fondo).convert_alpha()
        fondoNivel = pygame.image.load(fonNivel).convert()
        x=0
        W = 1000
        x_relativa = x % fondoNivel.get_rect().width
        pantalla.blit(fondoNivel, (x_relativa - x % fondoNivel.get_rect().width, 72))
        if x_relativa < W:
            pantalla.blit(fondoNivel, (x_relativa, 72))
        x-=1
        y = 750
        if y < W:
            self.bicicleta = pygame.image.load(imagen).convert_alpha()
            self.bicicleta.set_colorkey((255, 255, 255))
            self.bicicleta = self.bicicleta.convert()
            pantalla.blit(pygame.transform.scale(self.bicicleta, (50, 50)), (215, 10))
            self.tiempo = pygame.image.load("data/imagenes/reloj.png").convert_alpha()
            self.tiempo.set_colorkey((0, 0, 0))
            self.tiempo = self.tiempo.convert()
            pantalla.blit(pygame.transform.scale(self.tiempo, (40, 40)), (80, 15))
            pantalla.blit(pygame.transform.scale(self.fondo,(260,70)), (y, 0))
            largo = 200
            ancho = 25
            ancho_corto = 19
            calcular_progreso = int((objeto.cantidad * largo / 8))
            borde_barra = pygame.Rect(290, 25, 206, ancho)
            rectangulo_barra = pygame.Rect(293, 28, calcular_progreso, ancho_corto)
            pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
            pygame.draw.rect(pantalla, H_FA2F2F, rectangulo_barra)
            if objeto.cantidad > 2 and objeto.cantidad < 5:
                pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
                pygame.draw.rect(pantalla, naranja, rectangulo_barra)
            if objeto.cantidad > 4 and objeto.cantidad < 7:
                pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
                pygame.draw.rect(pantalla, amarillo, rectangulo_barra)
            if objeto.cantidad == 7 and objeto.cantidad < 8:
                pygame.draw.rect(pantalla, VERDE, borde_barra, 3)
                pygame.draw.rect(pantalla, verdee, rectangulo_barra)
           
        if monti.x > 650:
            monti.x = 650
            self.espacio += monti.velocidad
        if monti.x < 300 and self.espacio > 0:
            monti.x = 300
            self.espacio -= monti.velocidad
        if self.espacio < 0:
            self.espacio = 0
        self.warnig = pygame.image.load(("data/imagenes/vidas.png")).convert_alpha()
        self.warnig.set_colorkey((255,255,255))
        self.warnig = self.warnig.convert_alpha()
        if incVidas==True:
            if monti.vidas == 3:
                pantalla.blit(pygame.transform.scale(self.warnig, (35, 35)), (550, 15))
                pantalla.blit(pygame.transform.scale(self.warnig, (35, 35)), (595, 15))
                pantalla.blit(pygame.transform.scale(self.warnig, (35, 35)), (640, 15))
            if monti.vidas == 2:
                pantalla.blit(pygame.transform.scale(self.warnig, (35, 35)), (550, 15))
                pantalla.blit(pygame.transform.scale(self.warnig, (35, 35)), (595, 15))
            if monti.vidas == 1:
                pantalla.blit(pygame.transform.scale(self.warnig, (35, 35)), (550, 15))
            if monti.vidas == 0:
                objeto.cantidad -= objeto.cantidad
                pygame.mixer.music.set_volume(1.0)
                exec(open('GameOver.py', encoding="utf-8").read())
        rect = monti.parado.get_rect(x=monti.x, y=monti.y)
        f = open(Map, "r")
        for (idx, fila) in enumerate(f):
            for(idx2, col) in enumerate(fila):
                posx = idx2 * 30 - self.espacio
                posy = idx * 30
                if col == "t":
                    bloque = pygame.draw.rect(pantalla, 0, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.pared, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1
                #Probando
                if col == "l":
                    rect = monti.parado.get_rect(x=monti.x, y=monti.y)
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.tierra, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.velocidady = monti.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1
                if col == "c":
                        pantalla.blit(pygame.transform.scale(self.cajado, (tamano * 1, tamano)), (posx, posy))
                if col == "z":
                    bloque = pygame.draw.rect(pantalla, 0, (posx+15, posy+15, tamano * 1, tamano * 0.8))
                    pantalla.blit(pygame.transform.scale(self.cartellago, (tamano * 2, tamano*2)), (posx, posy))
                    if bloque.colliderect(rect):
                        if variables.ingles==True:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (75, 25)), (posx-10, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_ingles[5],1,(255,255,255)), (posx-5, posy-20))
                        else:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (100, 25)), (posx-15, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_español[5],1,(255,255,255)), (posx-10, posy-20))
                        if keys[pygame.K_e]:
                            pantalla.blit(pygame.transform.scale(self.objetivos, (550, 50)), (posx-220, posy-35))
                            if variables.ingles==True:
                                pantalla.blit(variables.fuente1.render(variables.Notas_ingles[6],1,(255,255,255)), (posx-200, posy-20))
                            else:
                                pantalla.blit(variables.fuente1.render(variables.Notas_español[6],1,(255,255,255)), (posx-200, posy-20))
                if col == "g":
                    pantalla.blit(pygame.transform.scale(self.muro, (tamano * 1, tamano)), (posx, posy))
                if col == "a":
                    pantalla.blit(pygame.transform.scale(self.muro2, (tamano * 1, tamano)), (posx, posy))
                if col == "h":
                    pantalla.blit(pygame.transform.scale(self.puerta, (tamano * 1, tamano)), (posx, posy))
                if col == "s":
                    pantalla.blit(pygame.transform.scale(self.cartel, (tamano * 2, tamano * 2)), (posx, posy))
                if col == "y":
                    pantalla.blit(pygame.transform.scale(self.cartel2, (tamano * 2, tamano * 2)), (posx, posy))
                if col == "v":
                    bloque = pygame.draw.rect(pantalla, negro, (posx, posy+10, tamano * 12, tamano))
                    pantalla.blit(pygame.transform.scale(self.lago,(tamano * 12, tamano)), (posx, posy+3))
                    if bloque.colliderect(rect):
                        if monti.vidas == 3:
                            monti.vidas=monti.vidas-3
                        if monti.vidas == 2:
                            monti.vidas-=2
                        if monti.vidas == 1:
                            monti.vidas -=1
                if col == "b":
                    bloque = pygame.draw.rect(pantalla, transparente, (posx+20, posy+10, tamano*.8, tamano*1.5))
                    pantalla.blit(pygame.transform.scale(self.basura,(tamano * 2, tamano * 2)), (posx, posy))
                    if bloque.colliderect(rect):
                        monti.vidas -= 1 
                        monti.x -= 100
                        monti.y -= 20
                        monti.velocidadx =0
                        if monti.vidas==2:
                            self.murido.play()
                        if monti.vidas==1:
                            self.murido.play()
                if col == "p":
                    bloque = pygame.draw.rect(pantalla, 0, (posx+15, posy+15, tamano * 1, tamano * 0.8))
                    pantalla.blit(pygame.transform.scale(self.nota,(tamano * 2, tamano * 2)), (posx, posy))
                    if bloque.colliderect(rect):
                        if variables.ingles==True:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (75, 25)), (posx-10, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_ingles[5],1,(255,255,255)), (posx-5, posy-20))
                        else:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (100, 25)), (posx-15, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_español[5],1,(255,255,255)), (posx-10, posy-20))
                        if keys[pygame.K_e]:
                            pantalla.blit(pygame.transform.scale(self.objetivos, (470, 50)), (posx-140, posy-35))
                            if variables.ingles==True:
                                pantalla.blit(variables.fuente1.render(variables.Notas_ingles[0],1,(255,255,255)), (posx-120, posy-20))
                            else:
                                pantalla.blit(variables.fuente1.render(variables.Notas_español[0],1,(255,255,255)), (posx-120, posy-20))
                if col == "k":
                    bloque = pygame.draw.rect(pantalla, 0, (posx+15, posy+15, tamano * 1, tamano * 0.8))
                    pantalla.blit(pygame.transform.scale(self.nota,(tamano * 2, tamano * 2)), (posx, posy))
                    if bloque.colliderect(rect):
                        if variables.ingles==True:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (75, 25)), (posx-10, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_ingles[5],1,(255,255,255)), (posx-5, posy-20))
                        else:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (100, 25)), (posx-15, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_español[5],1,(255,255,255)), (posx-10, posy-20))
                        if keys[pygame.K_e]:
                            pantalla.blit(pygame.transform.scale(self.objetivos, (400, 50)), (posx-170, posy-35))
                            if variables.ingles==True:
                                pantalla.blit(variables.fuente1.render(variables.Notas_ingles[1],1,(255,255,255)), (posx-120, posy-20))
                            else:
                                pantalla.blit(variables.fuente1.render(variables.Notas_español[1],1,(255,255,255)), (posx-120, posy-20))
                if col == "j":
                    bloque = pygame.draw.rect(pantalla, 0, (posx+15, posy+15, tamano * 1, tamano * 0.8))
                    pantalla.blit(pygame.transform.scale(self.nota,(tamano * 2, tamano * 2)), (posx, posy))
                    if bloque.colliderect(rect):
                        if variables.ingles==True:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (75, 25)), (posx-10, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_ingles[5],1,(255,255,255)), (posx-5, posy-20))
                        else:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (100, 25)), (posx-15, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_español[5],1,(255,255,255)), (posx-10, posy-20))
                        if keys[pygame.K_e]:
                            pantalla.blit(pygame.transform.scale(self.objetivos, (250, 50)), (posx-140, posy-35))
                            if variables.ingles==True:
                                pantalla.blit(variables.fuente1.render(variables.Notas_ingles[2],1,(255,255,255)), (posx-120, posy-20))
                            else:
                                pantalla.blit(variables.fuente1.render(variables.Notas_español[2],1,(255,255,255)), (posx-120, posy-20))
                if col == "q":
                    bloque = pygame.draw.rect(pantalla, 0, (posx+15, posy+15, tamano * 1, tamano * 0.8))
                    pantalla.blit(pygame.transform.scale(self.nota,(tamano * 2, tamano * 2)), (posx, posy))
                    if bloque.colliderect(rect):
                        if variables.ingles==True:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (75, 25)), (posx-10, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_ingles[5],1,(255,255,255)), (posx-5, posy-20))
                        else:
                            pantalla.blit(pygame.transform.scale(self.cuadradito, (100, 25)), (posx-15, posy-25))
                            pantalla.blit(variables.fuente1.render(variables.Notas_español[5],1,(255,255,255)), (posx-10, posy-20))
                        if keys[pygame.K_e]:
                            pantalla.blit(pygame.transform.scale(self.objetivos, (350, 50)), (posx-150, posy-35))
                            if variables.ingles==True:
                                pantalla.blit(variables.fuente1.render(variables.Notas_ingles[3],1,(255,255,255)), (posx-120, posy-20))
                            else:
                                pantalla.blit(variables.fuente1.render(variables.Notas_español[3],1,(255,255,255)), (posx-120, posy-20))
                       #Fin prueba
                if col == "w" or col == "r"  or col == "x" or col == "u":
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.piso, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.velocidady = monti.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1
                if col == "d"  or col == "e" or col == "o" or col == "i":
                    bloque = pygame.draw.rect(pantalla, verde, (posx, posy, tamano * 1, tamano))
                    pantalla.blit(pygame.transform.scale(self.piso2, (tamano * 1, tamano)), (posx, posy))
                    if bloque.colliderect(rect):
                        if rect.y + rect.height < posy + 10 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.tierra = True
                        elif rect.y > posy + tamano -20 and rect.x + rect.width > posx and rect.x < posx + (tamano * 1):
                            monti.velocidady = monti.gravedad
                        elif rect.x + rect.width > posx and rect.x < posx + tamano * 1:
                            if monti.direccion_actual == 1:
                                monti.x = posx - rect.width
                            else:
                                monti.x = posx + tamano * 1
                
        for enem in self.enemigos:
            enem.dibujar(pantalla, self.espacio)
        

        f.close()
def pausa(pantalla):
    # load button images
    fondo= pygame.image.load('data/imagenes/pausa.png').convert_alpha()
    mute_img = pygame.image.load('data/imagenes/Mute.png').convert_alpha()
    exit_img = pygame.image.load('data/imagenes/Volumenon.png').convert_alpha()
    retornar = pygame.image.load(variables.botonMorado).convert_alpha()
    continuar = pygame.image.load(variables.botonMorado).convert_alpha()
    salir = pygame.image.load(variables.botonRojo).convert_alpha()
    # create button instances
    mute_button = button.Button(750, 70, mute_img, 0.8)
    son_button = button.Button(750, 175, exit_img, 0.8)
    con_button = button.Button(250, 435, continuar, 0.8)
    volver = button.Button(500, 435, retornar, 0.8)
    salir = button.Button(50, 450, salir, 0.6)

    pausado = True
    while pausado:
        pantalla.blit(fondo, [0,0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if not volver.draw(pantalla):
            pass
        else:
            if variables.juego1==True:
                objeto.cantidad -= objeto.cantidad
                variables.aparecer=False
                exec(open('./Juego1.py', encoding="utf-8").read())
            if variables.juego2==True:
                objeto.cantidad -= objeto.cantidad
                variables.aparecer=False
                exec(open('./Juego2.py', encoding="utf-8").read())
            if variables.juego3==True:
                objeto.cantidad -= objeto.cantidad
                variables.aparecer=False
                exec(open('./Juego3.py', encoding="utf-8").read())
        if not salir.draw(pantalla):
            pass
        else:
            objeto.cantidad -= objeto.cantidad
            variables.aparecer=False
            pygame.mixer.music.load('data/audio/Menu.wav')
            pygame.mixer.music.play(-1)
            exec(open('./Niveles.py', encoding="utf-8").read())
            sys.exit()
        if not con_button.draw(pantalla):
            pass
        else:
            pausado = False
        if not mute_button.draw(pantalla):
            pass
        else:
            pygame.mixer.music.set_volume(0.0)
        if son_button.draw(pantalla):
            pygame.mixer.music.set_volume(1.0)

        if objeto.cantidad==0:
            pantalla.blit(variables.fuente.render(variables.numeros[0],1,(255,255,255)), (400, 360))
        if objeto.cantidad==1:
            pantalla.blit(variables.fuente.render(variables.numeros[1],1,(255,255,255)), (400, 360))
        if objeto.cantidad==2:
            pantalla.blit(variables.fuente.render(variables.numeros[2],1,(255,255,255)), (400, 360))
        if objeto.cantidad==3:
            pantalla.blit(variables.fuente.render(variables.numeros[3],1,(255,255,255)), (400, 360))
        if objeto.cantidad==4:
            pantalla.blit(variables.fuente.render(variables.numeros[4],1,(255,255,255)), (400, 360))
        if objeto.cantidad==5:
            pantalla.blit(variables.fuente.render(variables.numeros[5],1,(255,255,255)), (400, 360))
        if objeto.cantidad==6:
            pantalla.blit(variables.fuente.render(variables.numeros[6],1,(255,255,255)), (400, 360))
        if objeto.cantidad==7:
            pantalla.blit(variables.fuente.render(variables.numeros[7],1,(255,255,255)), (400, 360))
        
        if variables.ingles==True:
            pantalla.blit(variables.fuente.render(variables.Ingles[16],1,(0,0,0)), (275, 465))
            pantalla.blit(variables.fuente.render(variables.Ingles[1],1,(0,0,0)), (95, 465))
            pantalla.blit(variables.fuente.render(variables.Ingles[17],1,(0,0,0)), (560, 465))
            pantalla.blit(variables.fuente.render(variables.Ingles[15],1,(255,255,255)), (350, 150))
            pantalla.blit(variables.fuente.render(variables.Objetivos_ingles[3],1,(255,255,255)), (350, 270))
            if variables.juego1==True:
                pantalla.blit(variables.fuente.render(variables.Objetivos_ingles[0],1,(255,255,255)), (100, 320))
            if variables.juego2==True:
                pantalla.blit(variables.fuente.render(variables.Objetivos_ingles[1],1,(255,255,255)), (100, 320))
            if variables.juego3==True:
                pantalla.blit(variables.fuente.render(variables.Objetivos_ingles[2],1,(255,255,255)), (100, 320))
        else:
            pantalla.blit(variables.fuente.render(variables.Español[16],1,(0,0,0)), (265, 465))
            pantalla.blit(variables.fuente.render(variables.Español[1],1,(0,0,0)), (82, 465))
            pantalla.blit(variables.fuente.render(variables.Español[17],1,(0,0,0)), (530, 465))
            pantalla.blit(variables.fuente.render(variables.Español[15],1,(255,255,255)), (300, 150))
            pantalla.blit(variables.fuente.render(variables.Objetivos_español[3],1,(255,255,255)), (350, 270))
            if variables.juego1==True:
                pantalla.blit(variables.fuente.render(variables.Objetivos_español[0],1,(255,255,255)), (100, 320))
            if variables.juego2==True:
                pantalla.blit(variables.fuente.render(variables.Objetivos_español[1],1,(255,255,255)), (100, 320))
            if variables.juego3==True:
                pantalla.blit(variables.fuente.render(variables.Objetivos_español[2],1,(255,255,255)), (100, 320))
        pygame.display.update()
        reloj.tick(5)



reloj = pygame.time.Clock()
Termino = False
