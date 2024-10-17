# PRUEBA 
import os
import platform
import random

#JUGADORES MONOPOLY
idxPosicio = 0
idxEspera = 1
idxColor = 2
idxNom = 3

jugadors = []  
ranking = []   
prompt = []     

def clearScreen():

    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Busca un jugador a partir del color de la fitxa (torna -1 si no juga)
def buscaJugador(color):
    idxJugador = -1
    for cnt in range(0, len(jugadors)):
        if jugadors[cnt][idxColor] == color:
            idxJugador = cnt
            break
    return idxJugador

# Assigna un nom a una fitxa
def assignarColor(color):
    global jugadors
    
    nom = ""
    while True:
        nom = input(f"Escull un jugador per la fitxa '{color}': ")
        nomValid = True
        for cnt in range(0, len(nom)):
            lletra = nom[cnt]
            if not lletra.isalpha() and not lletra == " ":
                nomValid = False
                break # Sortir del for de lletres del nom
        if not nomValid:
            print("El nom escollit no és vàlid.")
        else:
            break # Sortir del while de nom vàlid

    # Busquem aquest color de fitxa a la llista de jugadors
    idxJugador = buscaJugador(color)

    # Assignar el nom al jugador que toca (o afegir-lo si no està a la llista)
    if idxJugador == -1:
        jugadors.append([0, 0, color, nom])
    else:
        jugadors[idxJugador][idxNom] = nom

# Funció per mostrar el menú principal
def menuPrincipalDibuix():
    global jugadors

    # Defineix els textos dels noms i partida
    textos = [ "no assignat", "no assignat", "no assignat", "no assignat"]
    nom = ""

    # Assignar els noms als textos (i justificar-los)
    for cnt in range(0, len(textos)):
        if cnt == 0:
            idxJugador = buscaJugador("Vermella")
            if idxJugador != -1:
                textos[0] = jugadors[idxJugador][idxNom]
        elif cnt == 1:
            idxJugador = buscaJugador("Blava")
            if idxJugador != -1:
                textos[1] = jugadors[idxJugador][idxNom]
        elif cnt == 2:
            idxJugador = buscaJugador("Verda")
            if idxJugador != -1:
                textos[2] = jugadors[idxJugador][idxNom]
        elif cnt == 3:
            idxJugador = buscaJugador("Groga")
            if idxJugador != -1:
                textos[3] = jugadors[idxJugador][idxNom]

    # Afegir els parentesis i alinear a la dreta
    for cnt in range(0, len(textos)):
        textos[cnt] = f"({textos[cnt]})"
        textos[cnt] = textos[cnt].rjust(16)

    # Text de començar la partida
    if len(jugadors) >= 2:
        textComencar = ""
    else:
        textComencar = "(no disponible)"
        
    textComencar = textComencar.rjust(16)

    # Neteja la pantalla
    clearScreen()

    # Dibuixa el menu
    print(f"""
La Oca
----------
1) Assignar jugador Vermell {textos[0]}
2) Assignar jugador Blau    {textos[1]}
3) Assignar jugador Verd    {textos[2]}
4) Assignar jugador Groc    {textos[3]}
5) Començar partida         {textComencar}
0) Sortir
    """)

# Funció per executar el menú principal
def menuPrincipal():
    global jugadors

    menuError = ""
    while True:
        menuPrincipalDibuix()
        
        # Si hi ha un error, mostrar-lo
        if menuError != "":
            print(f"La opció '{menuError}' no és vàlida.")

        # Demanar una opció del menú
        menuOpcioText = input("Escull una opció [0 - 5]: ")
        menuError = ""

        # Comprovar si la opció sel·leccionada és vàlida i escollir-la
        if not menuOpcioText.isdigit():
            menuError = menuOpcioText
        else:
            menuOpcioNum = int(menuOpcioText)
            if len(jugadors) < 2 and menuOpcioNum == 5:
                menuError = menuOpcioText
            elif not (menuOpcioNum in [0, 1, 2, 3, 4, 5]):
                menuError = menuOpcioText
            elif menuOpcioNum == 0:
                # Sortir del menú
                break
            elif menuOpcioNum == 1:
                assignarColor("Vermella")
            elif menuOpcioNum == 2:
                assignarColor("Blava")
            elif menuOpcioNum == 3:
                assignarColor("Verda")
            elif menuOpcioNum == 4:
                assignarColor("Groga")
            elif menuOpcioNum == 5:
                jocJugar()

# Dibuixa el taulell de joc
def taulellDibuixar():
    global jugadors

    # Definir el text que surt a cada casella del joc
    t = []
    for cntCasella in range(0, 54):
        txtCasella = " "
        jugadorsCasella = 0

        # Posar la lletra que correspon el jugador que hi ha a la casella (si n'hi ha)
        for cntJugador in range(0, len(jugadors)):
            if jugadors[cntJugador][idxPosicio] == cntCasella:
                jugadorsCasella = jugadorsCasella + 1
                color = jugadors[cntJugador][idxColor]
                if color == "Verda":
                    txtCasella = "D"
                else:
                    txtCasella = color[0]

        # Si hi ha més d'un jugador apareix el número de jugadors
        if jugadorsCasella > 1:
            txtCasella = str(jugadorsCasella)

        t.append(txtCasella)

# TABLERO

def tauler():
    c = [''] * 24 #c = casillas
    
    print(f'''text  
+--------+--------+--------+--------+--------+--------+--------+
|{c [12]}|{c [13]}|{c [14]}|{c [15]}|{c [16]}|{c [17]}|{c [18]}|
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+
|{c [11]}|                                            |{c [19]}|
|Aragó   |                                            |Angel   |
+--------+                                            +--------+
|{c [10]}|                                            |{c [20]}|
|S.Joan  |                                            |Augusta |
+--------+                                            +--------+
|{c [9]} |                                            |{c [21]}|
|Caixa   |                                            |Caixa   |
+--------+                                            +--------+
|{c [8]} |                                            |{c [22]}|
|Aribau  |                                            |Balmes  |
+--------+                                            +--------+
|{c [7]} |                                            |{c [23]}|
|Muntan  |                                            |Gracia  |
+--------+--------+--------+--------+--------+--------+--------+
|{c [6]} |{c [5]} |{c[ 4]} |{c [3]} |{c [2]} |{c [1]} |{c [0]} |
|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
+--------+--------+--------+--------+--------+--------+--------+
''')
tauler()

# NO SÉ SI ESTÁ BIEN
# JUGADORES:
# JUGADORES:
# JUGADORES:
# JUGADORES:

import random

casillas = [
    "Parking", "Urqinoa", "Fontan", "Sort", "Rambles", "Pl.Cat", "Anr pró",
    "Aragó", "Angel", "S.Joan", "Augusta", "Caixa", "Caixa", 
    "Aribau", "Balmes", "Muntan", "Gracia", 
    "Presó", "Consell", "Marina", "Sort", "Rosell", "Lauria", "Sortida"
]

jugadores = {
    'Groc': {'Posició': 0, 'Diners': 2000, 'Propietats': [], 'Especial': None},
    'Taronja': {'Posició': 0, 'Diners': 2000, 'Propietats': [], 'Especial': None},
    'Vermell': {'Posició': 0, 'Diners': 2000, 'Propietats': [], 'Especial': None},
    'Blau': {'Posició': 0, 'Diners': 2000, 'Propietats': [], 'Especial': None}
}

def mostra_tauler(jugadores,orden_tirada):
    tauler = {i: [""] for i in range(len(casillas))} #CREAR UNA LISTA CON CASILLAS VACIAS

    # Colocar los jugadores en sus respectivas posiciones
    for jugador, data in jugadores.items():
        posicion = data['posicion']
        if posicion < len(casillas):  # Asegurarse que la posición sea válida
            tauler[posicion][0] += jugador[0]

    print("+--------+--------+--------+--------+--------+--------+--------+")   #IMPRIMIR EN EL TABLERO LAS FICHAS DE LOS JUGADORES
    for i in range (0,7):
        print (f"|{casillas[i].ljust(8)}|{''.join(tauler[i]).ljust(8)}|")
        print("+--------+--------+")
    print()

#MOSTRAR LOS JUGADORES:
def enseñar_info_jugadores(jugadores, orden_tirada):
    print ("Banca: Diners: 10000000\n")
    for jugador in orden_tirada:
        data = jugadores[jugador]
        print (f"Jugador: {jugador}:")
        print(f"  Carrers: {', '.join(data['propiedades']) if data['propiedades'] else '(cap)'}")
        print(f"  Diners: {data['dinero']}")
        print(f"  Especial: {data['especial'] if data['especial'] else '(res)'}")
        print()

# Escoger un orden aleatorio para los jugadores
ordre_tirada = list(jugadores.keys())
random.shuffle(ordre_tirada)  # Orden aleatorio de los jugadores

# Asignar posiciones iniciales en el tablero
for i, jugador in enumerate(ordre_tirada):
    jugadores[jugador]['posicion'] = i  # Asignar a cada jugador su posición inicial

# Mostrar el tablero y la información de los jugadores
mostra_tauler(jugadores)
enseñar_info_jugadores(jugadores)


# BANCA

banca = 1000000
def preu_banca():
    global banca
    if banca <= 500000:
        banca = banca + 500000
    return

# PRECIOS
preus = {
    "Lauria": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250
    },
    "Rosselló": {
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 225,
        "Cmp. Hotel": 255
    },
    "Marina": {
        "Ll. Casa": 15,
        "Ll. Hotel": 15,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 250,
        "Cmp. Hotel": 260
    },
    "C. de cent": {
        "Ll. Casa": 15,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 50,
        "Cmp. Casa": 275,
        "Cmp. Hotel": 265
    },
    "Muntaner": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270
    },
    "Aribau": {
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 325,
        "Cmp. Hotel": 275
    },
    "Sant Joan": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 350,
        "Cmp. Hotel": 280
    },
    "Aragó": {
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 60,
        "Cmp. Casa": 375,
        "Cmp. Hotel": 285
    },
    "Urquinaona": {
        "Ll. Casa": 30,
        "Ll. Hotel": 25,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 400,
        "Cmp. Hotel": 290
    },
    "Fontana": {
        "Ll. Casa": 30,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 425,
        "Cmp. Hotel": 300
    },
    "Les Rambles": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 450,
        "Cmp. Hotel": 310
    },
    "Pl. Catalunya": {
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Trrny": 70,
        "Cmp. Casa": 475,
        "Cmp. Hotel": 320
    },
    "P. Àngel": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 500,
        "Cmp. Hotel": 330
    },
    "Via Augusta": {
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 340
    },
    "Balmes": {
        "Ll. Casa": 50,
        "Ll. Hotel": 40,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 550,
        "Cmp. Hotel": 350
    },
    "Pg. de Gràcia": {
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Trrny": 80,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360
    }
}



#CODIGO MEJORADO CON CHATGPT
#CODIGO MEJORADO CON CHATGPT
#CODIGO MEJORADO CON CHATGPT
#CODIGO MEJORADO CON CHATGPT
import random

# Nombres de las casillas
casillas = [
    "Parking", "Urqinoa", "Fontan", "Sort", "Rambles", "Pl.Cat", "Anr pró",
    "Aragó", "Angel", "S.Joan", "Augusta", "Caixa", "Caixa", 
    "Aribau", "Balmes", "Muntan", "Gracia", 
    "Presó", "Consell", "Marina", "Sort", "Rosell", "Lauria", "Sortida"
]

# Inicializar las posiciones de los jugadores y sus propiedades
jugadores = {
    'Groc': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None},
    'Taronja': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None},
    'Vermell': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None},
    'Blau': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None}
}

# Función para mostrar el tablero
def mostrar_tauler(jugadores):
    # Crear una lista con las casillas vacías
    tauler = {i: [""] for i in range(len(casillas))}
    
    # Colocar los jugadores en sus respectivas posiciones
    for jugador, data in jugadores.items():
        posicion = data['posicion']
        if posicion < len(casillas):  # Asegurarse que la posición sea válida
            tauler[posicion][0] += jugador[0]  # Añadir la letra inicial del color (G, T, V, B)

    # Impresión del tablero
    print("+--------+--------+--------+--------+--------+--------+--------+")
    # Imprimir la fila superior del tablero
    print(f"|{tauler[0][0].ljust(8)}|{tauler[1][0].ljust(8)}|{tauler[2][0].ljust(8)}|{tauler[3][0].ljust(8)}|{tauler[4][0].ljust(8)}|{tauler[5][0].ljust(8)}|{tauler[6][0].ljust(8)}|")
    print(f"|        |        |        |        |        |        |        |")
    print("+--------+--------+--------+--------+--------+--------+--------+")

    # Imprimir la parte media del tablero
    for i in range(7, 14):
        if i == 9:  # Casilla del "Angel"
            print(f"|{casillas[i].ljust(8)}|                                            |{tauler[i][0].ljust(8)}|")
        else:
            print(f"|{casillas[i].ljust(8)}|                                            |{casillas[i + 1].ljust(8)}|")
        print(f"|        |                                            |        |")
        print("+--------+                                            +--------+")

    # Imprimir la fila inferior del tablero
    print(f"|{tauler[15][0].ljust(8)}|{tauler[16][0].ljust(8)}|{tauler[17][0].ljust(8)}|{tauler[18][0].ljust(8)}|{tauler[19][0].ljust(8)}|{tauler[20][0].ljust(8)}|{tauler[21][0].ljust(8)}|")
    print("+--------+--------+--------+--------+--------+--------+--------+")

# Función para mostrar la información de los jugadores
def mostrar_info_jugadores(jugadores):
    print("Banca: Diners: 10000000\n")
    for jugador in jugadores:
        data = jugadores[jugador]
        print(f"Jugador {jugador}:")
        print(f"  Carrers: {', '.join(data['propiedades']) if data['propiedades'] else '(cap)'}")
        print(f"  Diners: {data['dinero']}")
        print(f"  Especial: {data['especial'] if data['especial'] else '(res)'}")
        print()

# Escoger un orden aleatorio para los jugadores
ordre_tirada = list(jugadores.keys())
random.shuffle(ordre_tirada)  # Orden aleatorio de los jugadores

# Asignar posiciones iniciales en el tablero
for i, jugador in enumerate(ordre_tirada):
    jugadores[jugador]['posicion'] = i  # Asignar a cada jugador su posición inicial

# Mostrar el tablero y la información de los jugadores
mostrar_tauler(jugadores)
mostrar_info_jugadores(jugadores)
