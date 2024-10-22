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

    print(f'''text  
+--------+--------+--------+--------+--------+--------+--------+  Banca                           
|{c [12]}  |{c [13]}  |{c [14]}  |{c [15]}  |{c [16]}  |{c [17]}  |{c [18]}  |  Diners: {banca}
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+  {info_jugadores[0] if len(info_jugadores) > 0 else ""}
|{c [11]}  |                                            |{c [19]}  | 
|Aragó   |{log_movimientos[0].ljust(44)}|Angel   |
+--------+                                            +--------+  {info_jugadores[1] if len(info_jugadores) > 1 else ""}
|{c [10]}  |                                            |{c [20]}  |
|S.Joan  |  {log_movimientos[1].ljust(44)}|Augusta |
+--------+                                            +--------+  {info_jugadores[2] if len(info_jugadores) > 2 else ""}
|{c [9]}  |                                            |{c [21]}  |
|Caixa   |  {log_movimientos[1].ljust(44)}|Caixa   |
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

#TERCERA PARTE: MOVIMIENTO DE JUGADORES USANDO EL ORDEN DEFINIDO

# Función para tirar los dados
def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Función para mover los jugadores
def mover_jugadores(jugador, jugadores_ordenados, log_movimientos):
    if jugador['Especial'] == 'Presó':
        dado1, dado2 = tirar_dados()
        log_movimientos[jugadores_ordenados.index(jugador)] = f"Juga \"{jugador['Inicial']}\", ha sortit {dado1} i {dado2}"
        
        # Si saca dobles, sale de la prisión
        if dado1 == dado2:
            log_movimientos[jugadores_ordenados.index(jugador)] += f" \"{jugador['Inicial']}\" surt de la presó"
            jugador['Especial'] = None
            jugador['Posició'] = (jugador['Posició'] + dado1 + dado2) % 24
        else:
            log_movimientos[jugadores_ordenados.index(jugador)] += f" \"{jugador['Inicial']}\" segueix a la presó."
    else:
        dado1, dado2 = tirar_dados()
        log_movimientos[jugadores_ordenados.index(jugador)] = f"Juga \"{jugador['Inicial']}\", ha sortit {dado1} i {dado2}"
        jugador['Posició'] = (jugador['Posició'] + dado1 + dado2) % 24

    tauler(jugadores_ordenados, log_movimientos)  # Actualizar el tablero

# Función para jugar el turno de cada jugador
def jugar(jugadores_ordenados):
    log_movimientos = [""] * len(jugadores_ordenados)  # Iniciar el log de movimientos para cada jugador
    while True:
        for jugador in jugadores_ordenados:
            mover_jugadores(jugador, jugadores_ordenados, log_movimientos)  # Ahora se pasa log_movimientos correctamente
            input("Presiona Enter para el siguiente jugador...")  # Pausa entre turnos para cada jugador

# EJECUTAR EL JUEGO
jugadores_ordenados = main()
if jugadores_ordenados:
    jugar(jugadores_ordenados)
