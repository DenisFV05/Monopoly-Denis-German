def comprar_propiedad(jugador):
    for x in gd.tablero:
        if gd.tablero[x]["propietario"] == "banca":
            if gd.players[jugador]["posicion"] == gd.tablero[x]["posicion"]:
                precio = gd.tablero[x]["precio"]
                if gd.players[jugador]["dinero"] >= precio:
                    gd.players[jugador]["dinero"] -= precio
                    gd.tablero[x]["propietario"] = jugador
                    gd.players[jugador]["propiedades"].append(x)
                    add_historial(f"{jugador} ha comprado {x} por {precio}€.")
                else:
                    add_historial(f"No tienes suficiente dinero para comprar {x}.")
                return  # Salimos de la función después de intentar comprar

    add_historial("Esta propiedad ya pertenece a alguien o no se ha encontrado.")


def comprar_casa(jugador):
    propiedad_actual = None
    for nombre_propiedad, detalles in gd.tablero.items():
        if detalles["propietario"] == jugador and gd.players[jugador]["posicion"] == detalles["posicion"]:
            propiedad_actual = nombre_propiedad
            break

    if propiedad_actual:
        if gd.tablero[propiedad_actual]["casas"] < 4:
            precio_casa = gd.tablero[propiedad_actual]["Ll. Casa"]
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


def comprar_hotel(jugador):
    propiedad_actual = None
    for nombre_propiedad, detalles in gd.tablero.items():
        if detalles["propietario"] == jugador and gd.players[jugador]["posicion"] == detalles["posicion"]:
            propiedad_actual = nombre_propiedad
            break

    if propiedad_actual:
        if gd.tablero[propiedad_actual]["casas"] >= 2 and gd.tablero[propiedad_actual]["hotels"] < 2:
            precio_hotel = gd.tablero[propiedad_actual]["Ll. Hotel"]
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


def precio_banco(jugador):
    total_a_recibir = 0
    for propiedad in gd.players[jugador]["propiedades"]:
        total_a_recibir += gd.tablero[propiedad]["precio"] * 0.5  # 50% del precio de compra

    add_historial(f"{jugador} podría recibir {total_a_recibir}€ si vende todas sus propiedades al banco.")


def precio_jugador(jugador):
    total_a_recibir = 0
    for propiedad in gd.players[jugador]["propiedades"]:
        total_a_recibir += gd.tablero[propiedad]["precio"] * 0.9  # 90% del precio de compra

    add_historial(f"{jugador} podría recibir {total_a_recibir}€ si vende todas sus propiedades a otro jugador.")


def vendre_al_banc(jugador):
    for propiedad in gd.players[jugador]["propiedades"]:
        precio_venta = gd.tablero[propiedad]["precio"] * 0.5  # 50% del precio de compra
        gd.players[jugador]["dinero"] += precio_venta
        gd.tablero[propiedad]["propietario"] = "banca"
