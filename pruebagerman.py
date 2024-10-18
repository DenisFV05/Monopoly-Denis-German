# MENÚ MONOPOLY + JUGADORES

colores_jugadores = ['Groc', 'Taronja', 'Vermell', 'Blau']
jugadores_seleccionados = {}

# FUNCIÓN MENÚ

class Player:
    def __init__(self, color):
        self.color = color
        self.name = self.get_name_from_color(color)
    
    def get_name_from_color(self, color):
        color_names = {
            'blau': 'B',
            'taronja': 'T',
            'vermell': 'V',
            'groc': 'G'
        }
        return color_names.get(color.lower(), 'Unknown')


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

def main():
    players = []
    mostrar_menu()

    num_players = int(input("Ingrese número de jugadores (2-4): "))

    if num_players < 2 or num_players > 4:
        print("Lo siento, el número de jugadores debe estar entre 2 y 4.")
        return

    for i in range(num_players):
        while True:
            choice = input(f"Jugador {i + 1}, elija su color (1-4) o salga (5): ")
            if choice == '1':
                color = 'blau'
                break
            elif choice == '2':
                color = 'taronja'
                break
            elif choice == '3':
                color = 'vermell'
                break
            elif choice == '4':
                color = 'groc'
                break
            elif choice == '5':
                print("Saliendo de Monopoly...")
                return
            else:
                print("Inténtelo de nuevo")

        players.append(Player(color))
        print(f"Jugador {i + 1} ha elegido el color {color} y su nombre es {players[-1].name}.")

    print("\nJugadores en la partida:")
    for jugador in players:
        print(f"Color: {jugador.color}, Nombre: {jugador.name}")

if __name__ == "__main__":
    main()