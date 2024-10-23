import random



def tauler():
    
    c = [] 
    for i in range(0, 24):
        c.append("")
    
    
    for jugador in jugadores_ordenados:
        inicial = jugador['Inicial']
        posicion = jugador['Posició']
        c[posicion] += inicial

    info_jugadores = []
    for jugador in jugadores_ordenados:
        inicial = jugador['nom']
        diners = jugador['diners']
        propietats = ",".join(jugador['carrers']) if jugador['Propietats'] else "(res)"
        especial = jugador['cartes'] if jugador['cartes'] else "(res)"
        info_jugadores.append(f"Jugador {inicial} | Diners: {diners} | Carrers: {propietats} | Especial: {especial}")


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
        log_movimientos[jugadores_ordenados.index(jugador)] = f"> Juga \"{jugador['Inicial']}\", ha sortit {dado1} i {dado2}"
        jugador['Posició'] = (jugador['Posició'] + dado1 + dado2) % 24

    tauler(jugadores_ordenados, log_movimientos)  # Actualizar el tablero

# Función para jugar el turno de cada jugador
def jugar(jugadores_ordenados):
    log_movimientos = [""] * len(jugadores_ordenados)  # Iniciar el log de movimientos para cada jugador
    while True:
        for jugador in jugadores_ordenados:
            mover_jugadores(jugador, jugadores_ordenados, log_movimientos)  # Ahora se pasa log_movimientos correctamente
            input("Presiona Enter para el siguiente jugador...")  # Pausa entre turnos para cada jugador
            log_movimientos.pop(0)
            log_movimientos.append("")



# EJECUTAR EL JUEGO
jugadores_ordenados = main()
if jugadores_ordenados:
    jugar(jugadores_ordenados)
