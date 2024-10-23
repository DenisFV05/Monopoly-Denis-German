import os
import platform
import random
def clearScreen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')



def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2, dado1 == dado2  # Total y dobles

# Ejemplo de uso
# movimiento, dobles = tirar_dados()

historial = []

def add_evento(evento):
    historial.append(evento)
    if len(historial) > 15:  
        historial.pop(0)







"""
Tablero: Players, casas, hoteles + Derecha: Banc & Info players + History en el centro + Input abajo
Diccionario ciudades / casillas
Banca 
Funcion para que la banca no se arruine
Orden de tirada entre los 4 players
Al principio cada player tiene 2k
Las fichas se muestran en el orden de llegada
Cada casilla tiene las propiedades en un sitio distinto

Special Casillas:
Sortida +200
Presó. Carta / Dobles / 3 turnos
Anar a la presó. 
Parking

Sort:
Sortir preso
Anar preso
Anar sortida
Anar 3 atras
Reparacions: 25 cada P y 100 cada H
Alcalde: -50 cada player

Caixa:
Sortir preso
Anar preso
Error banc: +150
Medico -50
Escuela -50
Reps -40
Bello +10

Cobrar pagar o invertir

Opcions disponibles:

- passar
- comprar terreny
- comprar casa, si n'hi ha menys de 4
- comprar hotel, si hi ha 2 cases. Al comprar cada hotel resta 2 cases. No hi pot haber més de 2 hotels.
- preus, mostra els preus de comprar una casa o un hotel a l'espai central d'informació
- preu banc, si el jugador no pot pagar, mostra a l'informació què guanyarà si ven totes les propietats (50% del què ha pagat per comprar les propietats)
- preu jugador, " a un altre jugador (90% del què ha pagat per comprar les propietats)
- vendre al banc
- vendre a B, disponible si el jugador no pot pagar i "B" pot comprar totes les propietats (terrenys, cases i hotels) per un valor del 90% del què ha pagat el jugador

Truc:
- anar a "Nom de la casella o carrer"
- afegir X cases (on X és un número entre 1 i 4)
- afegir X hotels (on X és 1 o bé 2)
- seguent X (on X és el proper jugador a jugar, G, T, V o B)
- diners X YY (on X és el jugador i YY els diners que tindrà disponibles)
- diners X banca (on X són els diners que tindrà la banca)

"""



banca = 1000000

def banca_check():
    global banca
    if banca <= 500000:
        banca = banca + 1000000
    return




def iniciar_joc():
    colors = ['G', 'T', 'V', 'B']  # Groc, Taronja, Vermell, Blau
    random.shuffle(colors)  # Aleatoritza l'ordre dels jugadors
   # jugadors = {} for color in colors}
    banca = 10000000
    return 






# Exemple de tirada
jugador_actual = 'B'  # Blau
dau1, dau2 = tirar_daus()
casella, diners = moure_jugador(jugador_actual, dau1, dau2, jugadors, taulell, banca)
print(f"El jugador {jugador_actual} ha arribat a {casella} i té {diners}€")



def comprar_terreny(jugador, jugadors, taulell, casella):
    if taulell[casella]["propietari"] is None:
        preu = taulell[casella]["preu"]
        if jugadors[jugador]["diners"] >= preu:
            jugadors[jugador]["diners"] -= preu
            taulell[casella]["propietari"] = jugador
            jugadors[jugador]["propietats"].append(taulell[casella]["nom"])
            return True
    return False

# Exemple de compra
casella = jugadors[jugador_actual]["posicio"]
if taulell[casella]["tipus"] == "carrer" and taulell[casella]["propietari"] is None:
    if comprar_terreny(jugador_actual, jugadors, taulell, casella):
        print(f"El jugador {jugador_actual} ha comprat {taulell[casella]['nom']}")
    else:
        print(f"El jugador {jugador_actual} no pot comprar {taulell[casella]['nom']}")


def torn_jugador(jugador, players, posicions, taulell, preus):
    print(f"Torn del jugador {players[jugador]['nom']}")
    
    moviment, dobles = tirar_dados()
    casella = moure_jugador(jugador, moviment, players, posicions, taulell)
    
    # Mostrem les dades del jugador actual després de moure's
    player_data()
    
    # Gestionar les accions segons la casella on ha caigut
    accions_casella(jugador, casella, players, taulell, preus)
    
    # Si no ha tret dobles, acaba el torn
    if not dobles:
        add_evento(f"{players[jugador]['nom']} acaba el seu torn.")
    else:
        add_evento(f"{players[jugador]['nom']} ha tret dobles! Torna a jugar.")
        torn_jugador(jugador, players, posicions, taulell, preus)  # Torna a jugar si treu dobles


def accions_casella(jugador, casella, players, taulell, preus):
    # Si la casella és un carrer
    if casella in preus:
        propietari = taulell[casella].get("propietari")
        if propietari is None:
            # Pot comprar el terreny
            preu = preus[casella]["Cmp. Trrny"]
            if players[jugador]["diners"] >= preu:
                resposta = input(f"Vols comprar {casella} per {preu}€? (sí/no): ").lower()
                if resposta == "sí":
                    players[jugador]["diners"] -= preu
                    players[jugador]["carrers"].append(casella)
                    taulell[casella]["propietari"] = jugador
                    add_evento(f"{players[jugador]['nom']} ha comprat {casella} per {preu}€.")
        else:
            # El terreny ja té propietari, pagar lloguer si no és el mateix jugador
            if propietari != jugador:
                lloguer = preus[casella]["Ll. Casa"]
                players[jugador]["diners"] -= lloguer
                players[propietari]["diners"] += lloguer
                add_evento(f"{players[jugador]['nom']} paga {lloguer}€ de lloguer a {players[propietari]['nom']}.")
    else:
        # Aquí podem gestionar altres tipus de caselles, com la presó, anar a presó, etc.
        if casella == "Presó":
            add_evento(f"{players[jugador]['nom']} ha arribat a la Presó.")

def joc():
    jugadors = list(players.keys())  # Llista dels jugadors en l'ordre actual
    random.shuffle(jugadors)  # Aleatoritzem l'ordre inicial
    while True:
        for jugador in jugadors:
            torn_jugador(jugador, players, posiciones, preus.keys(), preus)
            # Aquí podries afegir condicions per acabar la partida, com si un jugador es queda sense diners.
            if players[jugador]["diners"] <= 0:
                add_evento(f"{players[jugador]['nom']} s'ha arruïnat!")
                jugadors.remove(jugador)
            if len(jugadors) == 1:  # Si només queda un jugador
                print(f"El jugador {players[jugadors[0]]['nom']} ha guanyat!")
                return  # Finalitza el joc
            

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