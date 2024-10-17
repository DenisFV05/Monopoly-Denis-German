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
    c = [] #c = casillas
    
    print(f'''text
+--------+--------+--------+--------+--------+--------+--------+
|{c [12]}|{c [13]}|{c [14]}|{c [15]}|{c [16]}|{c [17]}|{c [18]}|
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pr  |
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
|{c [6]} |{c[5]}  |{c[4]}  |{c[3]}  |{c[2]}  |{c [1]} |{c [0]} |
|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
+--------+--------+--------+--------+--------+--------+--------+
''')
tauler()