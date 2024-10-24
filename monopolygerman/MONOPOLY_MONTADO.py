import random

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
            'Posició': 0,
            'Turnos_presion': 0  # Contador de turnos en prisión
        })
        print(f"Jugador {i + 1} ha elegido el color {color} y su nombre es {players[-1]['Inicial']}.")

    print("\nJugadores en la partida:")
    for jugador in players:
        print(f"Color: {jugador['Color']}, Nombre: {jugador['Inicial']}")

    # Determinar y mostrar el orden de tirada
    players = ordre_tirada(players)
    return players  # Devuelve la lista de jugadores en orden

# SEGUNDA PARTE: ACTUALIZAR TABLERO Y JUEGO CON EL ORDEN CORRECTO

def tauler(jugadores_ordenados, log_movimientos):
    # Definir el texto que sale en cada casilla del juego
    c = []  # c = casilla
    for i in range(0, 24):
        c.append("")
    
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

    print(f''' 
+--------+--------+--------+--------+--------+--------+--------+  Banca                           
|{c [12]}  |{c [13]}  |{c [14]}  |{c [15]}  |{c [16]}  |{c [17]}  |{c [18]}  |  Diners: {banca}
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+  {info_jugadores[0] if len(info_jugadores) > 0 else ""}
|{c [11]}  |                                            |{c [19]}  | 
|Aragó   |{log_movimientos[0].ljust(44)}|Angel   |
+--------+                                            +--------+  {info_jugadores[1] if len(info_jugadores) > 1 else ""}
|{c [10]}  |                                            |{c [20]}  |
|S.Joan  |{log_movimientos[1].ljust(44)}|Augusta |
+--------+                                            +--------+  {info_jugadores[2] if len(info_jugadores) > 2 else ""}
|{c [9]}  |                                            |{c [21]}  |
|Caixa   |{log_movimientos[1].ljust(44)}|Caixa   |
+--------+                                            +--------+  {info_jugadores[3] if len(info_jugadores) > 3 else ""}
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

    if evento == "Sortir de la presó":
        jugador['Especial'] = "Sortir de la presó"
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i guanya carta Sortir de la presó."
    elif evento == "Anar a la presó":
        jugador['Especial'] = "Presó"
        jugador['Posició'] = 6
        jugador['Turnos_presion'] = 0
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i va a la Presó."
    elif evento == "Anar a la sortida":
        jugador['Posició'] = 0
        jugador['Diners'] += 200
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i va a la Sortida, guanya 200€."
    elif evento == "Anar tres espais endarrera":
        jugador['Posició'] = (jugador['Posició'] - 3) % 24
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i retrocedeix tres espais."
    elif evento == "Fer reparacions a les propietats":
        propiedades = len(jugador['Propietats'])
        hoteles = sum(1 for prop in jugador['Propietats'] if 'hotel' in prop.lower())
        costo_total = propiedades * 25 + hoteles * 100
        jugador['Diners'] -= costo_total
        global banca
        banca += costo_total
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i paga {costo_total}€ en reparacions."
    elif evento == "Ets escollit alcalde":
        for otro_jugador in jugadores_ordenados:
            if otro_jugador != jugador:
                otro_jugador['Diners'] -= 50
                jugador['Diners'] += 50
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i és escollit alcalde, cada jugador li paga 50€."

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

    if evento == "Sortir de la presó":
        jugador['Especial'] = "Sortir de la presó"
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i guanya carta Sortir de la presó."
    elif evento == "Anar a la presó":
        jugador['Especial'] = "Presó"
        jugador['Posició'] = 6
        jugador['Turnos_presion'] = 0
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i va a la Presó."
    elif evento == "Error de la banca al teu favor":
        jugador['Diners'] += 150
        global banca
        banca -= 150
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i guanya 150€ per error de la banca."
    elif evento == "Despeses mèdiques":
        jugador['Diners'] -= 50
        banca += 50
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i paga 50€ en despeses mèdiques."
    elif evento == "Despeses escolars":
        jugador['Diners'] -= 50
        banca += 50
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i paga 50€ en despeses escolars."
    elif evento == "Reparacions al carrer":
        jugador['Diners'] -= 40
        banca += 40
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i paga 40€ en reparacions al carrer."
    elif evento == "Concurs de bellesa":
        jugador['Diners'] += 10
        log_movimientos[jugadores_ordenados.index(jugador)] += f" i guanya 10€ en un concurs de bellesa."

# Función principal del juego
def jugar():
    jugadores_ordenados = main()  # Lista de jugadores ordenados
    if not jugadores_ordenados:
        return  # Si no hay jugadores, salir del juego

    log_movimientos = ["", "", "", ""]  # Inicializamos el log de movimientos

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
        
# Todo el código que has implementado va aquí...

if __name__ == "__main__":
    jugar()  # Llama a la función principal para iniciar el juego

