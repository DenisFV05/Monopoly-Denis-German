
import random
import game_data as gd
# PRIMERA PARTE MENÚ + ORDEN DE TIRADA
def mostrar_menu():
    print ("======================================")
    print ("---            MONOPOLY            ---")
    print ("--------------------------------------")
    print ("-------Hecho por: Denis y Germán------")
    print ("======================================")
    print ("======================================")
    print ("----- Menú de Selección de Color -----")
    print ("Seleccione su color:")
    print ("1. Blau")
    print ("2. Taronja")
    print ("3. Vermell")
    print ("4. Groc")   
    print ("5. Salir")
    print ("---------------------------------------")

# Función para obtener la inicial del color
def get_inicial_color(color):
    color_names = {
        'blau': 'B',
        'taronja': 'T',
        'vermell': 'V',
        'groc': 'G'
    }
    return color_names.get(color.lower(), 'Unknown')

# Función para determinar el orden de tirada aleatorio
def ordre_tirada(players):
    random.shuffle(players)
    orden = "".join([player['Inicial'] for player in players])
    print(f"\nOrdre de tirada aleatori: {orden}")
    return players  # Se devuelve la lista de jugadores ordenada
    
# Función principal
def main():
    players = []  # Lista para almacenar a los jugadores
    mostrar_menu()

    num_players = int(input("Ingrese número de jugadores (2-4): "))

    if num_players < 2 or num_players > 4:
        print("Lo siento, el número de jugadores debe estar entre 2 y 4.")
        return

    selected_colors = []  # Lista para almacenar los colores ya elegidos

    for i in range(num_players):
        while True:
            choice = input(f"Jugador {i + 1}, elija su color (1-4) o salga (5): ")
            if choice == '1' and 'blau' not in selected_colors:
                color = 'blau'
                selected_colors.append(color)
                break
            elif choice == '2' and 'taronja' not in selected_colors:
                color = 'taronja'
                selected_colors.append(color)
                break
            elif choice == '3' and 'vermell' not in selected_colors:
                color = 'vermell'
                selected_colors.append(color)
                break
            elif choice == '4' and 'groc' not in selected_colors:
                color = 'groc'
                selected_colors.append(color)
                break
            elif choice == '5':
                print("Saliendo de Monopoly...")
                return
            else:
                print("Color no disponible o inválido. Inténtelo de nuevo.")

        # Añadimos el jugador a la lista con su color, inicial y datos iniciales
        players.append({
            'Color': color,
            'Inicial': get_inicial_color(color),
            'Diners': 2000,
            'Propietats': [],
            'Especial': None,
            'Posició': 0
        })
        print(f"Jugador {i + 1} ha elegido el color {color} y su nombre es {players[-1]['Inicial']}.")

    print("\nJugadores en la partida:")
    for jugador in players:
        print(f"Color: {jugador['Color']}, Nombre: {jugador['Inicial']}")

    # Determinar y mostrar el orden de tirada
    players = ordre_tirada(players)
    return players  # Devuelve la lista de jugadores en orden

#SEGUNDA PARTE: ACTUALIZAR TABLERO Y JUEGO CON EL ORDEN CORRECTO

def tauler(jugadores_ordenados, log_movimientos):
    # Definir el texto que sale en cada casilla del juego
    c = []  # c = casilla
    casa = []
    hoteles = []
    for i in range(0, 24):
        c.append("")
        casa.append("")
        hoteles.append("")
    
    # Llenar las posiciones del tablero con los jugadores según el orden
    for jugador in jugadores_ordenados:
        inicial = jugador['Inicial']
        posicion = jugador['Posició']
        c[posicion] += inicial

    info_jugadores = []
    for jugador in jugadores_ordenados:
        inicial = jugador['Inicial']
        diners = jugador['Diners']
        propietats = ",".join(jugador['Propietats']) if jugador['Propietats'] else "(ninguna)"
        especial = jugador['Especial'] if jugador['Especial'] else "(res)"
        info_jugadores.append(f"Jugador {inicial} | Diners: {diners} | Carrers: {propietats} | Especial: {especial}")


    for i in range(len(c)):
        c[i] = c[i].ljust(6)

    for calle in gd.tablero:
        casas = gd.tablero[calle]["casas"]
        hotel = gd.tablero[calle]["hoteles"]
        pos = gd.tablero [calle]["posicion"]
        if casas == 0 and hotel > 0:
            casa [pos] = str(hotel) + "H" + '--'
        elif casas > 0 and hotel == 0:
            casa [pos] = str(casas) + "C" + '--'
        elif casas > 0 and hotel > 0:
            casa[pos] = str(casas) + "C" + str(hotel) + "H"
        else:
            casa[pos] = '----'

        if pos in [7, 8, 10, 11, 19, 20, 22, 23]:
            if casas > 0:
                casa [pos] = str(casas) + "C" + '|'
            else:
                casa[pos] = '|'
            if hotel > 0:
                hoteles[pos] = str(hotel) + 'H' + '|'
            else:
                hoteles[pos] = '|'
            


    print(f''' 
+--------+----{casa[13]}+----{casa[14]}+--------+----{casa[15]}+----{casa[16]}+--------+----  Banca                           
|{c [12]}  |{c [13]}  |{c [14]}  |{c [15]}  |{c [16]}  |{c [17]}  |{c [18]}  |  Diners: {banca}
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+  {info_jugadores[0] if len(info_jugadores) > 0 else ""}
|{c [11]}  {casa[11]}                                            |{c [19]}  {casa[19]} 
|Aragó   {hoteles[11]}{log_movimientos[0].ljust(44)}|Angel   {hoteles[19]}
+--------+                                            +--------+  {info_jugadores[1] if len(info_jugadores) > 1 else ""}
|{c [10]}  {casa[10]}                                            |{c [20]}  {casa[20]}
|S.Joan  {hoteles[10]}{log_movimientos[1].ljust(42)}  |Augusta {hoteles[20]} 
+--------+                                            +--------+  {info_jugadores[2] if len(info_jugadores) > 2 else ""}
|{c [9]}  |                                            |{c [21]}  |
|Caixa   |{log_movimientos[1].ljust(44)}|Caixa   |
+--------+                                            +--------+  {info_jugadores[3] if len(info_jugadores) > 3 else ""}
|{c [8]}  {casa[8]}                                            |{c [22]}  {casa[22]}
|Aribau  {hoteles [8]}                                            |Balmes  {hoteles[22]}
+--------+                                            +--------+
|{c [7]}  {casa [7]}                                            |{c [23]}  {casa[23]}
|Muntan  {hoteles[7]}                                            |Gracia  {hoteles[23]}
+--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+----
|{c [6]}  |{c [5]}  |{c[ 4]}  |{c [3]}  |{c [2]}  |{c [1]}  |{c [0]}  |
|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
+--------+--------+--------+--------+--------+--------+--------+
''')

def add_historial(mensaje):
    # Aquí puedes agregar la lógica para añadir mensajes al historial
    pass

# Función para comprar una propiedad
def comprar_propiedad(jugador):
    for x in gd.tablero:
        if gd.tablero[x]["propietario"] == "banca":
            if gd.players[jugador]["posicion"] == gd.tablero[x]["posicion"]:
                precio = gd.tablero[x]["Cmp. Trrny"]  # Precio de compra del terreno
                if gd.players[jugador]["dinero"] >= precio:
                    gd.players[jugador]["dinero"] -= precio
                    gd.tablero[x]["propietario"] = jugador
                    gd.players[jugador]["propiedades"].append(x)
                    add_historial(f"{jugador} ha comprado {x} por {precio}€.")
                else:
                    add_historial(f"No tienes suficiente dinero para comprar {x}.")
                return  # Salimos de la función después de intentar comprar

    add_historial("Esta propiedad ya pertenece a alguien o no se ha encontrado.")

propiedades = {"Lauria": {
        "posicion": 1,
        "precio": 50,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Casa": 200,
        "Cmp. Hotel": 250,
        "propietario": "banca"
    },
    "Rossell": {
        "posicion": 0,
        "precio": 50,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 10,
        "Ll. Hotel": 15,
        "Cmp. Casa": 225,
        "Cmp. Hotel": 255,
        "propietario": "banca"
    },


    "Marina": {
        "posicion": 4,
        "precio": 50,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 15,
        "Ll. Hotel": 15,
        "Cmp. Casa": 250,
        "Cmp. Hotel": 260,
        "propietario": "banca"
    },
    "Consell": {
        "posicion": 5,
        "precio": 50,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 15,
        "Ll. Hotel": 20,
        "Cmp. Casa": 275,
        "Cmp. Hotel": 265,
        "propietario": "banca"
    },


    "Muntan": {
        "posicion": 7,
        "precio": 60,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Casa": 300,
        "Cmp. Hotel": 270,
        "propietario": "banca"
    },
    "Aribau": {
        "posicion": 8,
        "precio": 60,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 20,
        "Ll. Hotel": 20,
        "Cmp. Casa": 325,
        "Cmp. Hotel": 275,
        "propietario": "banca"
    },


    "S.Joan": {
        "posicion": 10,
        "precio": 60,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Casa": 350,
        "Cmp. Hotel": 280,
        "propietario": "banca"
    },
    "Aragó": {
        "posicion": 11,
        "precio": 60,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 25,
        "Ll. Hotel": 25,
        "Cmp. Casa": 375,
        "Cmp. Hotel": 285,
        "propietario": "banca"
    },


    "Urquina": {
        "posicion": 13,
        "precio": 70,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 30,
        "Ll. Hotel": 25,
        "Cmp. Casa": 400,
        "Cmp. Hotel": 290,
        "propietario": "banca"
    },
    "Fontan": {
        "posicion": 14,
        "precio": 70,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 30,
        "Ll. Hotel": 30,
        "Cmp. Casa": 425,
        "Cmp. Hotel": 300,
        "propietario": "banca"
    },


    "Rambles": {
        "posicion": 16,
        "precio": 70,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Casa": 450,
        "Cmp. Hotel": 310,
        "propietario": "banca"
    },
    "Pl.Cat": {
        "posicion": 17,
        "precio": 70,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 35,
        "Ll. Hotel": 30,
        "Cmp. Casa": 475,
        "Cmp. Hotel": 320,
        "propietario": "banca"
    },


    "P.Àngel": {
        "posicion": 19,
        "precio": 80,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Casa": 500,
        "Cmp. Hotel": 330,
        "propietario": "banca"
    },
    "Augusta": {
        "posicion": 20,
        "precio": 80,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 40,
        "Ll. Hotel": 35,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 340,
        "propietario": "banca"
    },


    "Balmes": {
        "posicion": 22,
        "precio": 80,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 50,
        "Ll. Hotel": 40,
        "Cmp. Casa": 550,
        "Cmp. Hotel": 350,
        "propietario": "banca"
    },
    "Gràcia": {
        "posicion": 23,
        "precio": 80,
        "casas": 0,
        "hoteles": 0,
        "Ll. Casa": 50,
        "Ll. Hotel": 50,
        "Cmp. Casa": 525,
        "Cmp. Hotel": 360,
        "propietario": "banca"
    }
}


# Función para comprar una casa
def comprar_casa(jugador):
    propiedad_actual = None
    for nombre_propiedad, detalles in gd.tablero.items():
        if detalles["propietario"] == jugador and gd.players[jugador]["posicion"] == detalles["posicion"]:
            propiedad_actual = nombre_propiedad
            break

    if propiedad_actual:
        if gd.tablero[propiedad_actual]["casas"] < 4:
            precio_casa = gd.tablero[propiedad_actual]["Ll. Casa"]  # Precio de la casa
            if gd.players[jugador]["dinero"] >= precio_casa:
                gd.players[jugador]["dinero"] -= precio_casa
                gd.tablero[propiedad_actual]["casas"] += 1
                add_historial(f"{jugador} ha comprado una casa en {propiedad_actual} por {precio_casa}€.")
            else:
                add_historial(f"No tienes suficiente dinero para comprar una casa en {propiedad_actual}.")
        else:
            add_historial(f"No puedes comprar más casas en {propiedad_actual}. Ya tienes 4 casas.")
    else:
        add_historial("No tienes propiedades para construir casas.")

# Función para comprar un hotel
def comprar_hotel(jugador):
    propiedad_actual = None
    for nombre_propiedad, detalles in gd.tablero.items():
        if detalles["propietario"] == jugador and gd.players[jugador]["posicion"] == detalles["posicion"]:
            propiedad_actual = nombre_propiedad
            break

    if propiedad_actual:
        if gd.tablero[propiedad_actual]["casas"] >= 2 and gd.tablero[propiedad_actual]["hotels"] < 2:
            precio_hotel = gd.tablero[propiedad_actual]["Ll. Hotel"]  # Precio del hotel
            if gd.players[jugador]["dinero"] >= precio_hotel:
                gd.players[jugador]["dinero"] -= precio_hotel
                gd.tablero[propiedad_actual]["hotels"] += 1
                gd.tablero[propiedad_actual]["casas"] -= 2  # Resta 2 casas al construir un hotel
                add_historial(f"{jugador} ha comprado un hotel en {propiedad_actual} por {precio_hotel}€.")
            else:
                add_historial(f"No tienes suficiente dinero para comprar un hotel en {propiedad_actual}.")
        elif gd.tablero[propiedad_actual]["hotels"] >= 2:
            add_historial(f"No puedes comprar más hoteles en {propiedad_actual}. Ya tienes 2 hoteles.")
        else:
            add_historial(f"No tienes suficientes casas en {propiedad_actual} para construir un hotel.")
    else:
        add_historial("No tienes propiedades para construir hoteles.")

# Función para mostrar precios de casas y hoteles
def mostrar_precios(jugador):
    propiedad_actual = None
    for nombre_propiedad, detalles in gd.tablero.items():
        if gd.players[jugador]["posicion"] == detalles["posicion"]:
            propiedad_actual = nombre_propiedad
            break

    if propiedad_actual:
        precio_casa = gd.tablero[propiedad_actual]["Ll. Casa"]
        precio_hotel = gd.tablero[propiedad_actual]["Ll. Hotel"]
        add_historial(f"Preus per {propiedad_actual}: Casa - {precio_casa}€, Hotel - {precio_hotel}€.")
    else:
        add_historial("No te encuentras en una propiedad para consultar precios.")

# Función para calcular el precio de venta al banco
def precio_banco(jugador):
    total_a_recibir = 0
    for propiedad in gd.players[jugador]["propiedades"]:
        total_a_recibir += gd.tablero[propiedad]["Cmp. Trrny"] * 0.5  # 50% del precio de compra

    add_historial(f"{jugador} podría recibir {total_a_recibir}€ si vende todas sus propiedades al banco.")

# Función para calcular el precio de venta a otro jugador
def precio_jugador(jugador):
    total_a_recibir = 0
    for propiedad in gd.players[jugador]["propiedades"]:
        total_a_recibir += gd.tablero[propiedad]["Cmp. Trrny"] * 0.9  # 90% del precio de compra

    add_historial(f"{jugador} podría recibir {total_a_recibir}€ si vende todas sus propiedades a otro jugador.")

# Función para vender propiedades al banco
def vendre_al_banc(jugador):
    for propiedad in gd.players[jugador]["propiedades"]:
        precio_venta = gd.tablero[propiedad]["Cmp. Trrny"] * 0.5  # 50% del precio de compra
        gd.players[jugador]["dinero"] += precio_venta
        gd.tablero[propiedad]["propietario"] = "banca"
        gd.tablero[propiedad]["casas"] = 0  # Vende todas las casas
        gd.tablero[propiedad]["hotels"] = 0  # Vende todos los hoteles

    gd.players[jugador]["propiedades"] = []  # El jugador pierde todas las propiedades
    add_historial(f"{jugador} ha vendido todas sus propiedades al banco y ahora tiene {gd.players[jugador]['dinero']}€.")

# Función para vender propiedades a otro jugador
def vendre_a(jugador, comprador):
    if comprador in gd.players:
        for propiedad in gd.players[jugador]["propiedades"]:
            precio_venta = gd.tablero[propiedad]["Cmp. Trrny"] * 0.9  # 90% del precio de compra
            gd.players[comprador]["dinero"] += precio_venta
            gd.players[jugador]["dinero"] -= precio_venta
            gd.tablero[propiedad]["propietario"] = comprador

        gd.players[jugador]["propiedades"] = []  # El jugador pierde todas las propiedades
        add_historial(f"{jugador} ha vendido todas sus propiedades a {comprador}.")


import random

# Variables globales
import random

# Variables globales
banca = 1000000

def banca_check():
    global banca
    if banca <= 500000:
        banca += 1000000
    return

# Función para tirar los dados
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función para mover los jugadores
def mover_jugadores(jugador, jugadores_ordenados, log_movimientos):
    # Almacenar la posición original antes de mover
    posicion_original = jugador['Posició']
    
    if jugador['Especial'] == 'Presó':
        # Si está en prisión, aumentar el contador de turnos en prisión
        jugador['Turnos_presion'] += 1
        dado1, dado2 = tirar_dados()
        log_movimientos[jugadores_ordenados.index(jugador)] = f"Juga \"{jugador['Inicial']}\", ha sortit {dado1} i {dado2}"
        
        # Si saca dobles, sale de la prisión
        if dado1 == dado2:
            log_movimientos[jugadores_ordenados.index(jugador)] += f" \"{jugador['Inicial']}\" surt de la presó"
            jugador['Especial'] = None
            jugador['Turnos_presion'] = 0  # Reiniciar contador
            jugador['Posició'] = (jugador['Posició'] + dado1 + dado2) % 24
        # Si pasa 3 turnos en prisión, sale automáticamente
        elif jugador['Turnos_presion'] >= 3:
            log_movimientos[jugadores_ordenados.index(jugador)] += f" \"{jugador['Inicial']}\" surt després de 3 torns"
            jugador['Especial'] = None
            jugador['Turnos_presion'] = 0
            jugador['Posició'] = (jugador['Posició'] + dado1 + dado2) % 24
        else:
            log_movimientos[jugadores_ordenados.index(jugador)] += f" \"{jugador['Inicial']}\" es queda a la presó"
            return
    else:
        dado1, dado2 = tirar_dados()
        log_movimientos[jugadores_ordenados.index(jugador)] = f"Juga \"{jugador['Inicial']}\", ha sortit {dado1} i {dado2}"
        jugador['Posició'] = (jugador['Posició'] + dado1 + dado2) % 24

    # Comprobar si ha pasado por "Sortida"
    if jugador['Posició'] < posicion_original:
        jugador['Diners'] += 200
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i passa per Sortida, guanya 200€"

    # Comprobar la casilla donde cayó
    casilla = jugador['Posició']
    if casilla == 6:  # Presó
        jugador['Especial'] = 'Presó'
        jugador['Turnos_presion'] = 0  # Reiniciar el contador de turnos en prisión
        log_movimientos[jugadores_ordenados.index(jugador)] += " i va a la Presó."
    elif casilla == 18:  # Anr pró
        jugador['Posició'] = 6  # Va a la casilla de la prisión
        jugador['Especial'] = 'Presó'
        jugador['Turnos_presion'] = 0
        log_movimientos[jugadores_ordenados.index(jugador)] += " i va a la casella Anr pró, directe a la Presó."
    elif casilla == 9 or casilla == 21:  # Caixa
        evento_caixa(jugador, jugadores_ordenados, log_movimientos)
    elif casilla == 3 or casilla == 14:  # Sort
        evento_sort(jugador, jugadores_ordenados, log_movimientos)

# Funciones para eventos de Caixa y Sort
def evento_sort(jugador, jugadores_ordenados, log_movimientos):
    opciones_sort = [
        "Sortir de la presó",
        "Anar a la presó",
        "Anar a la sortida",
        "Anar tres espais endarrera",
        "Fer reparacions a les propietats",
        "Ets escollit alcalde"
    ]
    evento = random.choice(opciones_sort)

    # Mostrar mensaje al jugador sobre el evento
    log_movimientos[jugadores_ordenados.index(jugador)] += f" i ha aterrat a la casella Sort i li ha tocat: {evento}."
    
    if evento == "Sortir de la presó":
        jugador['Especial'] = "Sortir de la presó"
    elif evento == "Anar a la presó":
        jugador['Especial'] = "Presó"
        jugador['Posició'] = 6
        jugador['Turnos_presion'] = 0
    elif evento == "Anar a la sortida":
        jugador['Posició'] = 0
        jugador['Diners'] += 200
    elif evento == "Anar tres espais endarrera":
        jugador['Posició'] = (jugador['Posició'] - 3) % 24
    elif evento == "Fer reparacions a les propietats":
        propiedades = len(jugador['Propietats'])
        hoteles = sum(1 for prop in jugador['Propietats'] if 'hotel' in prop.lower())
        costo_total = propiedades * 25 + hoteles * 100
        jugador['Diners'] -= costo_total
        global banca
        banca += costo_total
    elif evento == "Ets escollit alcalde":
        for otro_jugador in jugadores_ordenados:
            if otro_jugador != jugador:
                otro_jugador['Diners'] -= 50
                jugador['Diners'] += 50

def evento_caixa(jugador, jugadores_ordenados, log_movimientos):
    opciones_caixa = [
        "Sortir de la presó",
        "Anar a la presó",
        "Error de la banca al teu favor",
        "Despeses mèdiques",
        "Despeses escolars",
        "Reparacions al carrer",
        "Concurs de bellesa"
    ]
    evento = random.choice(opciones_caixa)

    log_movimientos[jugadores_ordenados.index(jugador)] += f" i ha passat per Caixa i li ha tocat: {evento}."

    if evento == "Sortir de la presó":
        jugador['Especial'] = "Sortir de la presó"
    elif evento == "Anar a la presó":
        jugador['Especial'] = "Presó"
        jugador['Posició'] = 6
        jugador['Turnos_presion'] = 0
    elif evento == "Error de la banca al teu favor":
        jugador['Diners'] += 150
        global banca
        banca -= 150
    elif evento == "Despeses mèdiques":
        jugador['Diners'] -= 50
        banca += 50
    elif evento == "Despeses escolars":
        jugador['Diners'] -= 50
        banca += 50
    elif evento == "Reparacions al carrer":
        jugador['Diners'] -= 40
        banca += 40
    elif evento == "Concurs de bellesa":
        jugador['Diners'] += 10

# Función principal del juego
def jugar(jugadores_ordenados):
    log_movimientos = [""] * len(jugadores_ordenados)  # Inicializamos el log de movimientos

    while True:
        for jugador in jugadores_ordenados:
            # Comprobar si algún jugador se queda sin dinero
            if jugador['Diners'] <= 0:
                print(f"El jugador {jugador['Inicial']} s'ha quedat sense diners! Ha estat eliminat.")
                jugadores_ordenados.remove(jugador)  # Eliminar al jugador sin dinero
                if len(jugadores_ordenados) == 1:
                    print(f"El jugador {jugadores_ordenados[0]['Inicial']} ha guanyat la partida!")
                    return  # Salir del juego cuando solo quede un jugador

            banca_check()
            mover_jugadores(jugador, jugadores_ordenados, log_movimientos)
            tauler(jugadores_ordenados, log_movimientos)

        # Opción para finalizar el juego manualmente
        respuesta = input("¿Desea continuar jugando? (s/n): ").lower()
        if respuesta == 'n':
            print("Fin del juego.")
            return  # Salir del bucle y terminar el juego

# EJECUTAR EL JUEGO
jugadores_ordenados = main()
if jugadores_ordenados: 
    jugar(jugadores_ordenados)
