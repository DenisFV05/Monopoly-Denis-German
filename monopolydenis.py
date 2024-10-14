import os
import platform
import random

def clearScreen():

    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

tauler = """
+--------+--------+--------+--------+--------+--------+--------+
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
|        |        |        |        |        |        |        |
+--------+--------+--------+--------+--------+--------+--------+
|Aragó   |                                            | Angel  |
|        |                                            |        |
+--------+                                            +--------+
|S.Joan  |                                            |Augusta |
|        |                                            |        |
+--------+                                            +--------+
|Caixa   |                                            |Caixa   |
|        |                                            |        |
+--------+                                            +--------+
|Aribau  |                                            |Balmes  |
|        |                                            |        |
+--------+                                            +--------+
|Muntan  |                                            |Gracia  |
|        |                                            |        |
+--------+--------+--------+--------+--------+--------+--------+
|        |        |        |        |        |        |        |
|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
+--------+--------+--------+--------+--------+--------+--------+
"""


def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2, dado1 == dado2  # Total y dobles

# Ejemplo de uso
# movimiento, dobles = tirar_dados()

historial = []

def add_evento(evento):
    historial.append(evento)
    if len(historial) > 5:  
        historial.pop(0)


def player_data():
    for jugador, datos in players.items():
        print(f"{datos['nom']} - Diners: {datos['diners']} €")
        print("  Propietats:", ", ".join(datos['carrers']) if datos['carrers'] else "Cap")
        print("  Cartes especials:", ", ".join(datos['cartes']) if datos['cartes'] else "Cap")
        print("-" * 20)


posiciones = {
    "J-Vermell": 0,
    "J-Groc": 0,
    "J-Taronja": 0,
    "J-Blau": 0
}

















# No se si esta bien
# No se si esta bien
# No se si esta bien

propiedades = {}  

def comprar_propiedad(jugador, casilla):
    if casilla in propiedades:
        print("La propietat ja està comprada.")
    elif players[jugador]["diners"] >= preus[casilla]["Cmp. Casa"]:
        players[jugador]["diners"] -= preus[casilla]["Cmp. Casa"]
        players[jugador]["carrers"].append(casilla)
        propiedades[casilla] = jugador
        add_evento(f"{jugador} ha comprat {casilla} per {preus[casilla]['Cmp. Casa']} €.")
    else:
        print("No tens suficients diners per comprar aquesta propietat.")

def pagar_alquiler(jugador, casilla):
    propietario = propiedades[casilla]
    alquiler = preus[casilla]["Cmp. Trrny"]
    if players[jugador]["diners"] >= alquiler:
        players[jugador]["diners"] -= alquiler
        players[propietario]["diners"] += alquiler
        add_evento(f"{jugador} paga {alquiler} € de lloguer a {propietario}.")
    else:
        print("No tens diners suficients per pagar el lloguer.")

def construir_edificio(jugador, casilla, tipo):
    if casilla not in players[jugador]["carrers"]:
        print("No pots construir en aquesta propietat perquè no la posseeixes.")
        return

    costo = preus[casilla][f"Ll. {tipo}"]
    if players[jugador]["diners"] >= costo:
        players[jugador]["diners"] -= costo
        add_evento(f"{jugador} ha construït un {tipo} a {casilla} per {costo} €.")
        # Aumenta el alquiler en función del tipo de edificio
        preus[casilla]["Cmp. Trrny"] += 10 if tipo == "Casa" else 25
    else:
        print("No tens diners suficients per construir.")

def verificar_salida(jugador, posicion_anterior, posicion_actual):
    # Si el jugador cruza la casilla de salida
    if posicion_actual < posicion_anterior:
        players[jugador]["diners"] += 200
        agregar_evento(f"{jugador} ha passat per la sortida i guanya 200 €.")

cartas = {}

def robar_carta(jugador, tipo):
    carta = random.choice(cartas_suerte if tipo == "Suerte" else cartas_caixa)
    print(carta["mensaje"])
    carta["accion"](jugador)  # Ejecuta la acción de la carta
    agregar_evento(f"{jugador} roba una carta de {tipo}: {carta['mensaje']}")

def verificar_bancarrota(jugador):
    if players[jugador]["diners"] < 0:
        agregar_evento(f"{jugador} ha fet bancarrota i queda fora del joc.")
        # Liberar propiedades
        for propiedad in players[jugador]["carrers"]:
            propiedades.pop(propiedad)
        players.pop(jugador)  # Elimina al jugador del juego

def turno(jugador):
    clearScreen()
    print(tauler)
    mostrar_datos_jugadores()

    # Tirada de dados y movimiento
    movimiento, dobles = tirar_dados()
    posicion_anterior = posiciones[jugador]
    casilla_actual = mover_jugador(jugador, movimiento)
    
    verificar_salida(jugador, posicion_anterior, posiciones[jugador])
    print(f"{jugador} ha caigut a {casilla_actual}.")
    
    # Acciones según la casilla
    if casilla_actual in propiedades and propiedades[casilla_actual] != jugador:
        pagar_alquiler(jugador, casilla_actual)
    elif casilla_actual in preus and casilla_actual not in propiedades:
        comprar_propiedad(jugador, casilla_actual)
    elif casilla_actual == "Suerte" or casilla_actual == "Caixa":
        robar_carta(jugador, casilla_actual)
    
    # Mostrar opciones al jugador
    if dobles:
        print("Has tret dobles, pots tirar de nou!")
        turno(jugador)  # Llama al turno del mismo jugador otra vez si saca dobles

# Ejemplo del flujo de juego
def jugar():
    jugadores = list(players.keys())
    while len(jugadores) > 1:
        for jugador in jugadores:
            turno(jugador)
            verificar_bancarrota(jugador)
            if jugador not in players:
                jugadores.remove(jugador)
    print(f"{jugadores[0]} és el guanyador!")

# No se si esta bien
# No se si esta bien
# No se si esta bien
















banca = 1000000

def banca_check():
    global banca
    if banca <= 500000:
        banca = banca + 1000000
    return

players = {
    "J-Vermell":{
        "nom":"V",
        "carrers":[],
        "diners":0,
        "cartes":[]
    },
    "J-Groc":{
        "nom":"G",
        "carrers":[],
        "diners":0,
        "cartes":[]
    },
    "J-Taronja":{
        "nom":"T",
        "carrers":[],
        "diners":0,
        "cartes":[]
    },
    "J-Blau":{
        "nom":"B",
        "carrers":[],
        "diners":0,
        "cartes":[]
    },
}

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