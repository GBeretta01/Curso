import random

#Creamos la función de elegir el número al azar entre 1 al 3
def numero():
    bot_ia = random.randrange(1, 4)
    return bot_ia

#Hacemos un bucle para el juego
while True:
    #Creamos la entrada de datos para el jugador
    elc = input("Piedra, papel o tijera: ").capitalize().strip()

    #Creamos el diccionario para convertir la elección del jugador a entero
    opc_p = {'Piedra':1,'Papel':2,'Tijera':3}

    #Creamos el diccionario para convertir la elección del bot a entero
    opc_ia = {1:'Piedra',2:'Papel',3:'Tijera'}

    #Creamos la condición if para verificar si la respuesta ingresada en 'elc' es de acuerdo usando el diccionario
    if elc not in opc_p:
        print("Opción no válida")
        continue
    
    #Creamos y determinamos la variable en entero del jugador
    jugador = opc_p[elc]

    #Creamos y determinamos la variable en entero del bot
    ia = numero()

    #Creamos y determinamos la elección del jugador en palabras
    jugador_c = elc

    #Creamos y determinamos la elección del bot en palabras
    ia_c = opc_ia[ia]

    #Determinamos si la elección del jugador y el bot es igual = empate
    if jugador_c == ia_c:
        print(f"Jugador: {elc} \nvs\nBOT: {opc_ia[ia]}")
        print("Empate!")
    
    #Determinamos si la elección del jugador menos el del bot dividido entre 3 da un residuo de 1, de ser así gana el jugador
    elif (jugador - ia) % 3 == 1:
        print(f"Jugador: {elc} \nvs\nBOT: {opc_ia[ia]}")
        print("Ganaste!")

    #Habiendo evaluado todas las anteriores condiciones y no encaja con ninguna, se determina que el jugador perdió por descarte
    else:
        print(f"Jugador: {elc} \nvs\nBOT: {opc_ia[ia]}")
        print("Perdiste!")