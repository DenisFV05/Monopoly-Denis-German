import random

# Nombres de las casillas
casillas = [
    "Sortida", "Lauria", "Rosselló", "Marina", "Consell de cent", 
    "Muntaner", "Aribau", "Sant Joan", "Aragó", "Urquinaona", 
    "Fontana", "Les Rambles", "Plaça Catalunya", "Portal de l'Àngel", 
    "Via Augusta", "Balmes", "Passeig de Gràcia"
]

# Inicializar las posiciones de los jugadores y sus propiedades
jugadores = {
    'Groc': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None},
    'Taronja': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None},
    'Vermell': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None},
    'Blau': {'posicion': 0, 'dinero': 2000, 'propiedades': [], 'especial': None}
}

# Función para mostrar el tablero
def mostrar_tauler(jugadores, ordre_tirada):
    # Crear una lista con las casillas vacías
    tauler = {i: [] for i in range(len(casillas))}
    
    # Colocar los jugadores en sus respectivas posiciones según el orden de tirada
    for jugador, data in jugadores.items():
        posicion = data['posicion']
        if posicion in tauler:  # Verificar que la posición exista en el tablero
            tauler[posicion].append(jugador[0])  # Añadir la letra inicial del color (G, T, V, B)
    
    # Mostrar el orden de tirada en la casilla de salida (casilla 0)
    tauler[0] = [j[0] for j in ordre_tirada]  # Colocar el orden de tirada en Sortida
    
    # Imprimir el tablero con las fichas de los jugadores
    print("+--------+--------+--------+--------+--------+--------+--------+")
    for i in range(0, 7):
        print(f"|{casillas[i].ljust(8)}|{''.join(tauler[i]).ljust(8)}|")
        print("+--------+--------+")
    print()

# Función para mostrar la información de los jugadores
def mostrar_informacio_jugadors(jugadores, ordre_tirada):
    print("Banca: Diners: 10000000\n")
    for jugador in ordre_tirada:
        data = jugadores[jugador]
        print(f"Jugador {jugador}:")
        print(f"  Carrers: {', '.join(data['propiedades']) if data['propiedades'] else '(cap)'}")
        print(f"  Diners: {data['dinero']}")
        print(f"  Especial: {data['especial'] if data['especial'] else '(res)'}")
        print()

# Escoger un orden aleatorio para los jugadores
ordre_tirada = list(jugadores.keys())
random.shuffle(ordre_tirada)  # Orden aleatorio de los jugadores

# Mostrar el tablero y la información de los jugadores con el nuevo orden de tirada
mostrar_tauler(jugadores, ordre_tirada)
mostrar_informacio_jugadors(jugadores, ordre_tirada)
