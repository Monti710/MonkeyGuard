import pygame,sys
from pygame import mixer
import button

pygame.init()
pantalla = pygame.display.set_mode((1000,600))
W,H = 1000,600
negro = (0, 0, 0)
fps=600
reloj = pygame.time.Clock()
Termino = False

Español= [
    "JUGAR",
    "SALIR",
    "VOLVER AL MENU",
    "VOLVER",
    "ESPAÑOL",
    "INGLES",
    "CONTROLES",
    "NIVEL 1",
    " NIVEL    2",
    "NIVEL 3",
    "AJUSTES",
    "¡GANASTE!",
    "FACIL",
    "DIFICIL",
    "MODO :",
    "JUEGO EN PAUSA",
    "CONTINUAR",
    "REINICIAR",
    "SIGUIENTE"
]
Ingles= [
    "PLAY",
    "QUIT",
    "RETURN TO MENU",
    "BACK",
    "SPANISH",
    "ENGLISH",
    "CONTROLS",
    "LEVEL 1",
    "LEVEL    2",
    "LEVEL 3",
    "SETTINGS",
    "¡WINNER!",
    "EASY",
    "HARD",
    "MODE:",
    "GAME PAUSED",
    "CONTINUE",
    "RESET",
    "NEXT"
]
Objetivos_español=[
    "Recoge todas las partes de la bicicleta: ",
    "Destruye todos los paneles de control: ",
    "Recoge todos los paneles solares: ",
    "OBJETIVOS:"
]
Objetivos_ingles=[
    "Collect all the parts of the bicycle: ",
    "Destroy all control panels: ",
    "Collect all solar panels: ",
    "OBJECTIVES:"
]
Notas_español=[
    "Recuerda usar siempre una bicicleta y no un carro",
    "Ten cuidado con los slimes malignos",
    "Cuida el medio ambiente",
    "No gastes luz de manera innecesaria ",
    "Recuerda que al completar todo el juego, hay una parte de la historia extra",
    "Presiona E",
    "Los lagos radioactivos son capaces de quitarte todas las vidas"
]
Notas_ingles=[
    "Remember to always use a bicycle and not a car.",
    "Beware of the evil slimes.",
    "Take care of the environment",
    "Don't waste light unnecessarily.",
    "Remember that when you complete the whole game, there is an extra part of the story",
    "Press E",
    "Radioactive lakes are capable of taking all your lives"
]
Historia1=[
    "MONKEY MONTI HA DECIDIDO ESCAPAR DEL ZOOLOGICO",
    "  PARA BUSCAR AL CULPABLE DE QUE LA CIUDAD ESTE",                                       #  !
    "                                           ENFERMA                                       ",
    "                 AYUDA A MONTI A SALVAR LA CIUDAD",
    "        RECOGE TODAS LAS PARTES DE LA BICICLETA",
    "           PARA PODER BUSCAR AL CULPABLE DE LA ",
    "                     CONTAMINACION DE LA CIUDAD"
]
Historia1_ingles=[
    "MONKEY MONTI HAS DECIDED TO ESCAPE FROM THE ZOO",
    "       TO LOOK FOR THE CULPRIT THAT THE CITY IS",
    "                                          SICK ",
    "                HELP MONKEY MONTI SAVE THE CITY",
    "           COLLECT ALL THE PARTS OF THE BICYCLE",
    "                TO LOOK FOR THE CULPRIT OF THE ",
    "                          POLLUTION OF THE CITY", 
]
Historia2=[
    "DESPUES DE ENCONTRAR AL CULPABLE, MONKEY MONTI",
    "           HA DECIDIDO DETENER A LOS CULPABLES",
    "       PARA ASI PODER SALVAR A LA CIUDAD DE LA",
    "                                 CONTAMINACION",
    "           AYUDA A MONKEY MONTI A DESTRUIR LOS",
    "                            PANELES DE CONTROL",
    "             ¡CUIDADO CON LOS SLIMES MALIGNOS!"
]
Historia2_ingles=[
    "       AFTER FINDING THE CULPRIT, MONKEY MONTI",
    "         HE HAS DECIDED TO ARREST THE CULPRITS",
    "            IN ORDER TO SAVE THE CITY FROM THE",
    "                                     POLLUTION",
    "                 HELP MONKEY MONTI DESTROY THE",
    "                                CONTROL PANELS",
    "                    BEWARE OF THE EVIL SLIMES!"
]
Historia3=[
    "     DESPUES DE LOGRAR DETENER A LOS CULPABLES",
    "   ¡A MONKEY MONTI, SE LE HA OCURRIDO UNA IDEA",
    "  BRILLANTE!, PARA SOLUCIONAR LA CONTAMINACION",
    "    RECOGER PANELES SOLARES PARA HACER ENERGIA",
    "              AYUDA A MONKEY MONTI CON SU IDEA",
    "              RECOGE TODOS LOS PANELES SOLARES",
    "               ANTES DE QUE SE ACABE EL TIEMPO"
]
Historia3_ingles=[
    "                  AFTER CAPTURING THE CULPRITS",
    "    MONKEY MONTI HAS COME UP WITH A BRILLIANT.",
    "                     IDEA! TO SOLVE POLLUTION.",
    "           COLLECT SOLAR PANELS TO MAKE ENERGY",
    "               HELP MONKEY MONTI WITH HIS IDEA",
    "                  COLLECT ALL THE SOLAR PANELS",
    "                      BEFORE THE TIME RUNS OUT"
]
numeros=["0/8","1/8","2/8","3/8","4/8","5/8","6/8","7/8"]
fuente = pygame.font.Font(None, 50)
fuente1 = pygame.font.Font(None, 25)
fuente2 = pygame.font.Font(None,40)
ingles=False
dificil=False
fD=False
aparecer=True
mapa=True
botonMorado = "./data/imagenes/botonMorado.png"
botonRojo = "./data/imagenes/botonRojo.png"
botonDorado = "./data/imagenes/botonRosado.png"
juego1=False
juego2=False
juego3=False
class musica: 
    pygame.init()
    pygame.mixer.init(22050, -16, 2, 512)
    # Musica agregada
    pygame.mixer.music.load('./data/audio/Menu.wav')
    pygame.mixer.music.play(-1) 

difuminado1=False
difuminado2=False
difuminado3=False
