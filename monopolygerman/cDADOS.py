import random


jugadores = {
    'Groc': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'G', 'Posició': 0},
    'Taronja': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'T', 'Posició': 0},
    'Vermell': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'V', 'Posició': 0},
    'Blau': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'B', 'Posició': 0}
}

def tauler():



    # Definir el text que surt a cada casella del joc
    c = [] #c = casilla
    for i in range(0,24):
            c.append("")
    for jugador in jugadores:
            inicial = jugadores[jugador]['Inicial']
            posicion = jugadores[jugador]['Posició']
            c[posicion] += inicial

    for i in range(len(c)):
        c[i] = c[i].ljust(6)

    print(f'''text  
+--------+--------+--------+--------+--------+--------+--------+
|{c [12]}  |{c [13]}  |{c [14]}  |{c [15]}  |{c [16]}  |{c [17]}  |{c [18]}  |
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+
|{c [11]}  |                                            |{c [19]}  |
|Aragó   |                                            |Angel   |
+--------+                                            +--------+
|{c [10]}  |                                            |{c [20]}  |
|S.Joan  |                                            |Augusta |
+--------+                                            +--------+
|{c [9]}  |                                            |{c [21]}  |
|Caixa   |                                            |Caixa   |
+--------+                                            +--------+
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




# Definir el diccionario de jugadores
jugadores = {
    'Groc': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'G', 'Posició': 0},
    'Taronja': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'T', 'Posició': 0},
    'Vermell': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'V', 'Posició': 0},
    'Blau': {'Diners': 2000, 'Propietats': [], 'Especial': None, 'Inicial' : 'B', 'Posició': 0}
}

# Función para tirar los dados
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función para mover los jugadores
def mover_jugadores(jugador):
    if jugadores[jugador]['Especial'] == 'Presó':
        dado1, dado2 = tirar_dados()
        print(f"{jugador} está en prisión. Tirada: {dado1} y {dado2}")

        # Si saca dobles, sale de la prisión
        if dado1 == dado2:
            print(f"El jugador {jugador} ha salido de prisión con {dado1} y {dado2}.")
            jugadores[jugador]['Especial'] = None
            jugadores[jugador]['Posició'] = (jugadores[jugador]['Posició'] + dado1 + dado2) % 24
        else:
            print(f"El jugador {jugador} sigue en la cárcel.")
    else:
        dado1, dado2 = tirar_dados()
        print(f"{jugador} tira los dados: {dado1}, {dado2}")
        jugadores[jugador]['Posició'] = (jugadores[jugador]['Posició'] + dado1 + dado2) % 24

    tauler()  # Actualizar el tablero

#bucle
def jugar():
    while True:
        for jugador in jugadores:
            print(f"\nTurno del jugador {jugador}:")
            mover_jugadores(jugador)
            continuar = input("Presiona Enter para el siguiente turno o escribe 'salir' para terminar: ")
            if continuar.lower() == 'salir':
                print("Juego terminado.")
                return  # Salir del bucle infinito y finalizar el juego

# Llamada a la función jugar para comenzar
jugar()




