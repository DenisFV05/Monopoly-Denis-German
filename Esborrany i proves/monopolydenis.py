
"""
Tablero: Players, casas, hoteles + Derecha: Banc & Info players + History en el centro + Input abajo
Diccionario ciudades / casillas
Banca 
Funcion para que la banca no se arruine
Orden de tirada entre los 4 players
Al principio cada player tiene 2k
Las fichas se muestran en el orden de llegada
Cada casilla tiene las propiedades en un sitio distinto

Special Casillas:
Sortida +200
Presó. Carta / Dobles / 3 turnos
Anar a la presó. 
Parking

Sort:
Sortir preso
Anar preso
Anar sortida
Anar 3 atras
Reparacions: 25 cada P y 100 cada H
Alcalde: -50 cada player

Caixa:
Sortir preso
Anar preso
Error banc: +150
Medico -50
Escuela -50
Reps -40
Bello +10

Cobrar pagar o invertir

Opcions disponibles:

- passar
- comprar terreny
- comprar casa, si n'hi ha menys de 4
- comprar hotel, si hi ha 2 cases. Al comprar cada hotel resta 2 cases. No hi pot haber més de 2 hotels.
- preus, mostra els preus de comprar una casa o un hotel a l'espai central d'informació
- preu banc, si el jugador no pot pagar, mostra a l'informació què guanyarà si ven totes les propietats (50% del què ha pagat per comprar les propietats)
- preu jugador, " a un altre jugador (90% del què ha pagat per comprar les propietats)
- vendre al banc
- vendre a B, disponible si el jugador no pot pagar i "B" pot comprar totes les propietats (terrenys, cases i hotels) per un valor del 90% del què ha pagat el jugador

Truc:
- anar a "Nom de la casella o carrer"
- afegir X cases (on X és un número entre 1 i 4)
- afegir X hotels (on X és 1 o bé 2)
- seguent X (on X és el proper jugador a jugar, G, T, V o B)
- diners X YY (on X és el jugador i YY els diners que tindrà disponibles)
- diners X banca (on X són els diners que tindrà la banca)

"""



