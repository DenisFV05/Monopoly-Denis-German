import os
import platform
import random
import game_data as gd

def clearScreen():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')


banca = 1000000



def banca_check():
    global banca
    if banca <= 500000:
        banca += 1000000
    return

historial = []

def add_historial(evento):
    global historial
    historial.append(evento)
    if len(historial) > 14:
        historial.pop(0)
        return 







def ordre_tirada(players):
    jugadores_lista = list(players.keys())  
    random.shuffle(jugadores_lista)  
    return jugadores_lista 

jugadores_ordenados = ordre_tirada(gd.players) 


def tirar_dados():
    return random.randint(1, 6), random.randint(1, 6)




def jugar_turno():
    r, dobles = tirar_dados()




def comprar_propiedad(jugador):
    for x in gd.tablero:
        if gd.tablero[x]["propietario"] == "banca":
            if gd.players[jugador]["posicion"] == gd.tablero[x]["posicion"]:
                precio = gd.tablero[x]["precio"]
                if gd.players[jugador]["diners"] >= precio:
                    gd.players[jugador]["diners"] -= precio
                    gd.tablero[x]["propietario"] = jugador
                    gd.players[jugador]["propiedades"].append(x)
                    add_historial(f"{jugador} ha comprado {x} por {precio}€.")
                else:
                    add_historial(f"No tienes suficiente diners para comprar {x}.")
        else:
            add_historial("Esta propiedad ya pertenece a alguien.")

def vender_propiedad(jugador, propiedad):
    if propiedad in gd.players[jugador]["propiedades"]:
        precio = gd.tablero[propiedad]["precio"] // 2  # Vender por la mitad del precio
        gd.players[jugador]["diners"] += precio
        gd.tablero[propiedad]["propietario"] = "banca"  # Regresa a la banca
        gd.players[jugador]["propiedades"].remove(propiedad)
        add_historial(f"{jugador} ha vendido {propiedad} por {precio}€.")
    else:
        add_historial(f"{jugador} no es dueño de {propiedad}.")


def pagar_alquiler(jugador, propietario, propiedad):
    casas = gd.tablero[propiedad]["casas"]
    hoteles = gd.tablero[propiedad]["hotels"]
    if casas == 0 and hoteles == 0:
        add_historial(f"{jugador} no tiene que pagar alquiler porque {propietario} no tiene casas ni hoteles en {propiedad}.")
        return
    alquiler_total = 0
    if casas > 0:
        alquiler_total += gd.tablero[propiedad]["Ll. Casa"] * casas
    if hoteles > 0:
        alquiler_total += gd.tablero[propiedad]["Ll. Hotel"] * hoteles
    if gd.players[jugador]["diners"] >= alquiler_total:
        gd.players[jugador]["diners"] -= alquiler_total
        gd.players[propietario]["diners"] += alquiler_total
        add_historial(f"{jugador} ha pagado {alquiler_total}€ de alquiler a {propietario} por {propiedad} (incluyendo {casas} casa(s) y {hoteles} hotel(s)).")
    else:
        add_historial(f"{jugador} no tiene suficiente diners para pagar el alquiler de {alquiler_total}€ por {propiedad}.")

def construir(jugador, propiedad, tipo):
    if propiedad in gd.players[jugador]["carrers"]:
        if tipo == "casa" and gd.tablero[propiedad]["casas"] < 4:
            costo = gd.tablero[propiedad]["Cmp. Casa"]
            if gd.players[jugador]["diners"] >= costo:
                gd.players[jugador]["diners"] -= costo
                gd.tablero[propiedad]["casas"] += 1
                add_historial(f"{jugador} ha construido una casa en {propiedad} por {costo}€.")
            else:
                add_historial(f"{jugador} no tiene suficiente diners para construir una casa.")
        elif tipo == "hotel" and gd.tablero[propiedad]["casas"] == 4:
            costo = gd.tablero[propiedad]["Cmp. Hotel"]
            if gd.players[jugador]["diners"] >= costo:
                gd.players[jugador]["diners"] -= costo
                gd.tablero[propiedad]["hoteles"] += 1
                gd.tablero[propiedad]["casas"] = 0  # Se quitan las casas al construir el hotel
                add_historial(f"{jugador} ha construido un hotel en {propiedad} por {costo}€.")
            else:
                add_historial(f"{jugador} no tiene suficiente diners para construir un hotel.")
        else:
            add_historial(f"{jugador} no puede construir más en {propiedad}.")
    else:
        add_historial(f"{jugador} no es dueño de {propiedad}.")


cartas_suerte = [
    "Recibes 100€ por vender una propiedad.",
    "Paga 50€ por impuestos.",
    "Ganas 200€ en la lotería.",
    "Vas a la cárcel.",
    "Retrocede 3 posiciones."
]

def carta_suerte(jugador):
    carta = random.choice(cartas_suerte)
    add_historial(f"{jugador} saca una carta de Suerte: {carta}")
    
    if "Recibes 100€" in carta:
        gd.players[jugador]["diners"] += 100
    elif "Paga 50€" in carta:
        gd.players[jugador]["diners"] -= 50
    elif "Ganas 200€" in carta:
        gd.players[jugador]["diners"] += 200
    elif "Vas a la cárcel" in carta:
        gd.players[jugador]["carcel"] = True
        gd.players[jugador]["posicion"] = 6  # Posición de la cárcel
    elif "Retrocede 3 posiciones" in carta:
        gd.players[jugador]["posicion"] = (gd.players[jugador]["posicion"] - 3) % 24
        add_historial(f"{jugador} retrocede 3 posiciones a {gd.players[jugador]['posicion']}.")
    
    tauler()

def gestionar_turno():
    for jugador in jugadores_ordenados:
        print(f"Turno de {jugador}")
        
        # Mover jugador
        mover_jugadores(jugador)
        
        # Verificar si cae en propiedad propia o de otro jugador
        propiedad_actual = [propiedad for propiedad, info in gd.tablero.items() if info["posicion"] == gd.players[jugador]["posicion"]]
        
        if propiedad_actual:
            propiedad_actual = propiedad_actual[0]
            propietario = gd.tablero[propiedad_actual]["propietario"]
            if propietario == "banca":
                comprar_propiedad(jugador)
            elif propietario != jugador:
                pagar_alquiler(jugador, propietario, propiedad_actual)
        
        # Fin del turno
        input("Presiona Enter para pasar al siguiente turno...")
        clearScreen()
    tauler()










def mostrar_preus(propiedad):
    precio_casa = gd.tablero[propiedad]["Cmp. Casa"]
    precio_hotel = gd.tablero[propiedad]["Cmp. Hotel"]
    print(f"Preus per {propiedad}: Casa - {precio_casa}€, Hotel - {precio_hotel}€.")

def preu_banc(jugador):
    total = sum(gd.tablero[prop]["precio"] * 0.5 for prop in gd.players[jugador]["propiedades"])
    print(f"{jugador} guanyaria {total}€ si ven totes les propietats al banc.")

def preu_jugador(jugador):
    total = sum(gd.tablero[prop]["precio"] * 0.9 for prop in gd.players[jugador]["propiedades"])
    print(f"{jugador} guanyaria {total}€ si ven totes les propietats a un altre jugador.")

def vendre_al_banc(jugador):
    for propiedad in gd.players[jugador]["propiedades"]:
        precio = gd.tablero[propiedad]["precio"] * 0.5
        gd.players[jugador]["diners"] += precio
        gd.tablero[propiedad]["propietario"] = "banca"
    gd.players[jugador]["propiedades"].clear()
    print(f"{jugador} ha venut totes les propietats al banc.")

def vendre_a_jugador(jugador, jugador_a_vendre):
    if jugador_a_vendre in gd.players:
        # Asume que el jugador a vender puede comprar
        for propiedad in gd.players[jugador]["propiedades"]:
            precio = gd.tablero[propiedad]["precio"] * 0.9
            gd.players[jugador_a_vendre]["diners"] -= precio
            gd.players[jugador]["diners"] += precio
            gd.tablero[propiedad]["propietario"] = jugador_a_vendre
        gd.players[jugador]["propiedades"].clear()
        print(f"{jugador} ha venut totes les propietats a {jugador_a_vendre}.")
    else:
        print("Jugador no vàlid per vendre.")

def interaccion_jugador(jugador):
    opciones = []
    posicion_actual = gd.players[jugador]["posicion"]
    propiedad_actual = None

    # Determinamos si el jugador ha caído en una propiedad
    for propiedad, info in gd.tablero.items():
        if info["posicion"] == posicion_actual:
            propiedad_actual = propiedad
            propietario = info["propietario"]
            break

    # Opciones según la situación del jugador
    if propietario is None:
        opciones.append("comprar terreny")
    elif propietario == jugador:
        # El jugador es propietario
        if gd.tablero[propiedad_actual]["casas"] < 4:
            opciones.append("comprar casa")
        if gd.tablero[propiedad_actual]["casas"] == 2 and gd.tablero[propiedad_actual]["hotels"] < 2:
            opciones.append("comprar hotel")

    # Mostrar opciones disponibles
    print(f"\nJuga '{jugador}', opcions: {', '.join(opciones) if opciones else 'passar'}")
    
    if not opciones:
        print(f"{jugador} no pot fer res en aquesta ronda.")
        return
    
    # Recoger la entrada del jugador
    op = input("Selecciona una opció: ").strip().lower()
    
    if op == "passar":
        return
    elif op == "comprar terreny" and propietario is None:
        comprar_propiedad(jugador)
    elif op == "comprar casa" and propietario == jugador:
        construir(jugador, propiedad_actual, "casa")
    elif op == "comprar hotel" and propietario == jugador:
        construir(jugador, propiedad_actual, "hotel")
    elif op == "preus":
        mostrar_preus(propiedad_actual)
    elif op == "preu banc":
        preu_banc(jugador)
    elif op == "preu jugador":
        preu_jugador(jugador)
    elif op == "vendre al banc":
        vendre_al_banc(jugador)
    elif op.startswith("vendre a "):
        vendre_a_jugador(jugador, op.split()[2])  # Obtén el nombre del jugador

    # Actualizar el tablero después de la interacción
    tauler()


    


def tauler():

    c = [""] * 24 
    casa = [""] * 24  
    hoteles = [""] * 24 

    for jugador_key in jugadores_ordenados:
        jugador = gd.players[jugador_key]  
        inicial = jugador['nom']  
        posicion = jugador['posicion'] 
        c[posicion] += inicial  

    info_jugadores = []
    for jugador_key in jugadores_ordenados:
        jugador = gd.players[jugador_key]  
        inicial = jugador['nom']
        diners = jugador['diners']
        propietats = ",".join(jugador['carrers']) if jugador['carrers'] else "(res)"
        especial = ",".join(jugador['cartes']) if jugador['cartes'] else "(res)"
        info_jugadores.append(f"Jugador: {inicial} | Diners: {diners} | Propietats: {propietats} | Especial: {especial}")

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
    historial_ampliado = historial[:14]  # Se mostrarán las primeras 14 entradas del historial (máximo)

    # Rellenar con espacios vacíos si hay menos de 14 entradas en el historial
    while len(historial_ampliado) < 14:
        historial_ampliado.append('')

    # Imprimir el tablero
    print(f''' 
+--------+----{casa[13]}+----{casa[14]}+--------+----{casa[15]}+----{casa[16]}+--------+----  Banca                           
|{c[12]}  |{c[13]}  |{c[14]}  |{c[15]}  |{c[16]}  |{c[17]}  |{c[18]}  |  Diners: {banca}
|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |
+--------+--------+--------+--------+--------+--------+--------+  {info_jugadores[0]}
|{c[11]}  {casa[11]}                                            |{c[19]}  {casa[19]} 
|Aragó   {hoteles[11]}{historial_ampliado[0].ljust(44)}|Angel   {hoteles[19]}
+--------+                                            +--------+  {info_jugadores[1]}
|{c[10]}  {casa[10]}                                            |{c[20]}  {casa[20]}
|S.Joan  {hoteles[10]}{historial_ampliado[1].ljust(42)}  |Augusta {hoteles[20]} 
+--------+                                            +--------+  {info_jugadores[2]}
|{c[9]}  |                                            |{c[21]}  |
|Caixa   |{historial_ampliado[2].ljust(44)}|Caixa   |
+--------+                                            +--------+  {info_jugadores[3]}
|{c[8]}  {casa[8]}                                            |{c[22]}  {casa[22]}
|Aribau  {hoteles[8]}{historial_ampliado[3].ljust(44)}|Balmes  {hoteles[22]}
+--------+                                            +--------+
|{c[7]}  {casa[7]}                                            |{c[23]}  {casa[23]}
|Muntan  {hoteles[7]}{historial_ampliado[4].ljust(44)}|Gracia  {hoteles[23]}
+--------+----{casa[5]}+----{casa[4]}+--------+----{casa[2]}+----{casa[1]}+--------+----
|{c[6]}  |{c[5]}  |{c[4]}  |{c[3]}  |{c[2]}  |{c[1]}  |{c[0]}  |
|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |
+--------+--------+--------+--------+--------+--------+--------+
''')
    
tauler()
    



def mover_jugadores(jugador_key):
    jugador = gd.players[jugador_key]  
    if jugador['carcel']:
        dado1, dado2 = tirar_dados()
        if dado1 == dado2:
            jugador['carcel'] = False
            jugador['turnos_prision'] = 0
            # Guardamos la posición anterior antes de mover al jugador
            posicion_anterior = jugador['posicion']
            jugador['posicion'] = (jugador['posicion'] + dado1 + dado2) % 24
            
            add_historial(f"{jugador_key} ha tret dobles i ha sortir de la presó.")
            add_historial(f"{jugador_key} es mou a la posició {jugador['posicion']}.")

            # Comprobamos si ha pasado por la casilla de salida
            if jugador['posicion'] < posicion_anterior:
                jugador['diners'] += 200
                add_historial(f"{jugador_key} ha pasado por la casilla de Sortida y recibe 200€.")
        else:
            jugador['turnos_prision'] -= 1
            if jugador['turnos_prision'] <= 0:
                jugador['carcel'] = False
                jugador['turnos_prision'] = 0
                add_historial(f"{jugador_key} ha cumplido su tiempo en prisión y sale.")
            else:
                add_historial(f"A {jugador_key} li quedan {jugador['turnos_prision']} turns en la presó.")
    else:
        dado1, dado2 = tirar_dados()
        avance = dado1 + dado2
        posicion_anterior = jugador['posicion']
        jugador['posicion'] = (jugador['posicion'] + avance) % 24

        add_historial(f"{jugador_key} ha avanzado a la posición {jugador['posicion']}.")

        # Comprobamos si el jugador ha pasado por la casilla de salida
        if jugador['posicion'] < posicion_anterior:
            jugador['diners'] += 200
            add_historial(f"{jugador_key} ha pasado por la casilla de Sortida y recibe 200€.")
    
    # Actualizamos el tablero
    tauler()



