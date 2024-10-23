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

historial = ["a","b","c"]

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
    a = random.randint(1,6)
    b = random.randint(1,6)
    return a + b, a == b




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



def tauler():

    jugadores_ordenados = ordre_tirada(gd.players)  

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
    

tauler()