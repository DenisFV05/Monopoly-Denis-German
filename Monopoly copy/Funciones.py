import os
import platform
import random
def clearScreen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

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









def ordre_tirada(players):
    random.shuffle(players)

    #añadir al log
    return players  


def tirar_dados():
    a = random.randint(1,6)
    b = random.randint(1,6)
    return a + b, a == b




def jugar_turno():
    r, dobles = tirar_dados()