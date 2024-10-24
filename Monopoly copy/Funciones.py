import os
import platform
import random
import game_data as gd

def clearScreen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

banca = 1000000

def banca_check():
    global banca
    if banca <= 500000:
        banca += 1000000
    return

historial = []

def add_historial(evento):
    global historial
    historial.append(evento)
    if len(historial) > 14:
        historial.pop(0)
        return 







def ordre_tirada(players):
    jugadores_lista = list(players.keys())  
    random.shuffle(jugadores_lista)  
    return jugadores_lista 




def tirar_dados():
    return random.randint(1, 6), random.randint(1, 6)




def jugar_turno():
    r, dobles = tirar_dados()




def comprar_propiedad(jugador):
    for x in gd.tablero:
        if gd.tablero[x]["propietario"] == "banca":
            if gd.players[jugador]["posicion"] == gd.tablero[x]["posicion"]:
                precio = gd.tablero[x]["precio"]
                if gd.players[jugador]["dinero"] >= precio:
                    gd.players[jugador]["dinero"] -= precio
                    gd.tablero[x]["propietario"] = jugador
                    gd.players[jugador]["propiedades"].append(x)
                    add_historial(f"{jugador} ha comprado {x} por {precio}€.")
                else:
                    add_historial(f"No tienes suficiente dinero para comprar {x}.")
        else:
            add_historial("Esta propiedad ya pertenece a alguien.")


def pagar_alquiler(jugador, propietario, propiedad):
    casas = gd.tablero[propiedad]["casas"]
    hoteles = gd.tablero[propiedad]["hotels"]
    if casas == 0 and hoteles == 0:
        add_historial(f"{jugador} no tiene que pagar alquiler porque {propietario} no tiene casas ni hoteles en {propiedad}.")
        return
    alquiler_total = 0
    if casas > 0:
        alquiler_total += gd.tablero[propiedad]["Ll. Casa"] * casas
    if hoteles > 0:
        alquiler_total += gd.tablero[propiedad]["Ll. Hotel"] * hoteles
    if gd.players[jugador]["diners"] >= alquiler_total:
        gd.players[jugador]["diners"] -= alquiler_total
        gd.players[propietario]["diners"] += alquiler_total
        add_historial(f"{jugador} ha pagado {alquiler_total}€ de alquiler a {propietario} por {propiedad} (incluyendo {casas} casa(s) y {hoteles} hotel(s)).")
    else:
        add_historial(f"{jugador} no tiene suficiente dinero para pagar el alquiler de {alquiler_total}€ por {propiedad}.")












    

jugadores_ordenados = ordre_tirada(gd.players) 

def tauler():

     

    c = [""] * 24 

    for jugador_key in jugadores_ordenados:
        jugador = gd.players[jugador_key]  
        inicial = jugador['nom']  
        posicion = jugador['posicion'] 
        c[posicion] += inicial  

    info_jugadores = []
    for jugador_key in jugadores_ordenados:
        jugador = gd.players[jugador_key]  
        inicial = jugador['nom']
        diners = jugador['diners']
        propietats = ",".join(jugador['carrers']) if jugador['carrers'] else "(res)"
        especial = ",".join(jugador['cartes']) if jugador['cartes'] else "(res)"
        info_jugadores.append(f"Jugador: {inicial} | Diners: {diners} | Propietats: {propietats} | Especial: {especial}")

    for i in range(len(c)):
        c[i] = c[i].ljust(6)

    print(f''' 
+--------+--------+--------+--------+--------+--------+--------+  Banca                           
|{c [12]}  |{c [13]}  |{c [14]}  |{c [15]}  |{c [16]}  |{c [17]}  |{c [18]}  |  Diners: {banca}
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+  {info_jugadores[0]}
|{c [11]}  |                                            |{c [19]}  | 
|Aragó   |{historial[0].ljust(44)}|Angel   |
+--------+                                            +--------+  {info_jugadores[1]}
|{c [10]}  |                                            |{c [20]}  |
|S.Joan  |{historial[1].ljust(44)}|Augusta |
+--------+                                            +--------+  {info_jugadores[2]}
|{c [9]}  |                                            |{c [21]}  |
|Caixa   |{historial[2].ljust(44)}|Caixa   |
+--------+                                            +--------+  {info_jugadores[3]}
|{c [8]}  |                                            |{c [22]}  |
|Aribau  |                                            |Balmes  |
+--------+                                            +--------+
|{c [7]}  |                                            |{c [23]}  |
|Muntan  |                                            |Gracia  |
+--------+--------+--------+--------+--------+--------+--------+
|{c [6]}  |{c [5]}  |{c[ 4]}  |{c [3]}  |{c [2]}  |{c [1]}  |{c [0]}  |
|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
+--------+--------+--------+--------+--------+--------+--------+
''')
    



def mover_jugadores(jugador_key):
    jugador = gd.players[jugador_key]  
    if jugador['carcel']:
        dado1, dado2 = tirar_dados()
        if dado1 == dado2:
            jugador['carcel'] = False
            jugador['turnos_prision'] = 0
            # Guardamos la posición anterior antes de mover al jugador
            posicion_anterior = jugador['posicion']
            jugador['posicion'] = (jugador['posicion'] + dado1 + dado2) % 24
            
            add_historial(f"{jugador_key} ha tret dobles i ha sortir de la presó.")
            add_historial(f"{jugador_key} es mou a la posició {jugador['posicion']}.")

            # Comprobamos si ha pasado por la casilla de salida
            if jugador['posicion'] < posicion_anterior:
                jugador['diners'] += 200
                add_historial(f"{jugador_key} ha pasado por la casilla de Sortida y recibe 200€.")
        else:
            jugador['turnos_prision'] -= 1
            if jugador['turnos_prision'] <= 0:
                jugador['carcel'] = False
                jugador['turnos_prision'] = 0
                add_historial(f"{jugador_key} ha cumplido su tiempo en prisión y sale.")
            else:
                add_historial(f"A {jugador_key} li quedan {jugador['turnos_prision']} turns en la presó.")
    else:
        dado1, dado2 = tirar_dados()
        avance = dado1 + dado2
        posicion_anterior = jugador['posicion']
        jugador['posicion'] = (jugador['posicion'] + avance) % 24

        add_historial(f"{jugador_key} ha avanzado a la posición {jugador['posicion']}.")

        # Comprobamos si el jugador ha pasado por la casilla de salida
        if jugador['posicion'] < posicion_anterior:
            jugador['diners'] += 200
            add_historial(f"{jugador_key} ha pasado por la casilla de Sortida y recibe 200€.")
    
    # Actualizamos el tablero
    tauler()



