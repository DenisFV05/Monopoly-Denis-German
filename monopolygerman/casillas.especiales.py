import random

# PRIMERA PARTE MENÚ + ORDEN DE TIRADA


def main():
    players = []  # Lista para almacenar a los jugadores
    mostrar_menu()


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

