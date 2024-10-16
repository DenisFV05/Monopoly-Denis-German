import random

# Definición de las acciones de las casillas
def accion_casilla_salida(jugador):
    jugador['dinero'] += 200
    print(f"{jugador['nombre']} pasa por la Salida y gana 200€.")

def accion_casilla_prision(jugador):
    print(f"{jugador['nombre']} ha caído en la Prisión.")
    if jugador['tiene_carta_salir']:
        jugador['tiene_carta_salir'] = False
        print(f"{jugador['nombre']} usa su carta de 'Salir de la prisión'.")
    else:
        jugador['turnos_prision'] += 1
        print(f"{jugador['nombre']} debe esperar {3 - jugador['turnos_prision']} turnos para salir.")

def accion_casilla_anar_prision(jugador):
    print(f"{jugador['nombre']} cae en Anar a la prisión y va directamente a la prisión.")
    jugador['en_prision'] = True
    jugador['turnos_prision'] = 0

def accion_casilla_parking(jugador):
    print(f"{jugador['nombre']} cae en Parking. No pasa nada.")

def accion_casilla_sort(jugador):
    evento = random.choice([
        "salir_prision",
        "ir_prision",
        "ir_salida",
        "ir_tres_atras",
        "reparaciones",
        "ser_alcalde"
    ])

    if evento == "salir_prision":
        jugador['tiene_carta_salir'] = True
        print(f"{jugador['nombre']} ha recibido una carta para salir de la prisión.")
    elif evento == "ir_prision":
        jugador['en_prision'] = True
        print(f"{jugador['nombre']} va a la prisión.")
    elif evento == "ir_salida":
        jugador['dinero'] += 200
        print(f"{jugador['nombre']} va a la salida y cobra 200€.")
    elif evento == "ir_tres_atras":
        jugador['posicion'] = max(0, jugador['posicion'] - 3)  # Asegura que la posición no sea negativa
        print(f"{jugador['nombre']} avanza 3 espacios hacia atrás.")
    elif evento == "reparaciones":
        jugador['dinero'] -= (jugador['casas'] * 25 + jugador['hoteles'] * 100)
        print(f"{jugador['nombre']} paga reparaciones.")
    elif evento == "ser_alcalde":
        for j in jugadores:
            if j != jugador:
                j['dinero'] -= 50
        print(f"{jugador['nombre']} es elegido alcalde, y cada jugador le paga 50€.")

def accion_casilla_caja(jugador):
    evento = random.choice([
        "salir_prision",
        "ir_prision",
        "error_banco",
        "gastos_medicos",
        "gastos_escolares",
        "reparaciones",
        "concurs_belleza"
    ])

    if evento == "salir_prision":
        jugador['tiene_carta_salir'] = True
        print(f"{jugador['nombre']} ha recibido una carta para salir de la prisión.")
    elif evento == "ir_prision":
        jugador['en_prision'] = True
        print(f"{jugador['nombre']} va a la prisión.")
    elif evento == "error_banco":
        jugador['dinero'] += 150
        print(f"{jugador['nombre']} recibe 150€ por un error del banco.")
    elif evento == "gastos_medicos":
        jugador['dinero'] -= 50
        print(f"{jugador['nombre']} paga 50€ en gastos médicos.")
    elif evento == "gastos_escolares":
        jugador['dinero'] -= 50
        print(f"{jugador['nombre']} paga 50€ en gastos escolares.")
    elif evento == "reparaciones":
        jugador['dinero'] -= 40
        print(f"{jugador['nombre']} paga 40€ en reparaciones.")
    elif evento == "concurs_belleza":
        jugador['dinero'] += 10
        print(f"{jugador['nombre']} gana 10€ en un concurso de belleza.")

# Clase Jugador para manejar las propiedades de cada jugador


# Esto habria q hacerlo distinto - Denis
jugadores = [
    {"nombre": "Jugador 1", "dinero": 1500, "en_prision": False, "tiene_carta_salir": False, "turnos_prision": 0, "posicion": 0, "casas": 0, "hoteles": 0},
    {"nombre": "Jugador 2", "dinero": 1500, "en_prision": False, "tiene_carta_salir": False, "turnos_prision": 0, "posicion": 0, "casas": 0, "hoteles": 0}
]

# Definición de las casillas
casillas = {
    "Salida": accion_casilla_salida,
    "Prisión": accion_casilla_prision,
    "Anar a la prisión": accion_casilla_anar_prision,
    "Parking": accion_casilla_parking,
    "Sort": accion_casilla_sort,
    "Caja": accion_casilla_caja
}

#Yo lo haria de otra forma - Denis
# Simulación de tiradas
for jugador in jugadores:
    for _ in range(5):  # Simular 5 tiradas
        tirada = random.choice(list(casillas.keys()))
        print(f"\n{jugador['nombre']} ha caído en la casilla: {tirada}")
        casillas[tirada](jugador)  # Llama a la función correspondiente
        print(f"Dinero actual de {jugador['nombre']}: {jugador['dinero']}€")