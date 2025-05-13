import random

#Definimos el número a elegir por el programa para el juego
def elegirnumero():
    num_elegido = random.randrange(1, 101)
    return num_elegido

def juego():

    #Mensaje de bienvenida al juego
    print("Bienvenido al juego adivine el número\n ")

    #Llamamos a la función creada y determinamos el número del juego
    bot_num = elegirnumero()

    #Creamos un contador para saber cuántas rondas van del juego (Lo iniciamos en 1)
    contador = 1

    # Definimos el bucle del juego
    while True:
        
        #Pedimos al usuario que ingrese el número para adivinar
        user_num = int(input("Ingrese un número entero (1-100): "))

        #Usamos condicional if para determinar si el número es el mismo
        if user_num == bot_num:
            print("Adivinaste el número!")
            print(f"Lo adivinaste en {contador} intentos")
            break

        #Usamos elif para determinar si el número elegido es mayor que el número del juego y decimos que es más abajo
        elif user_num > bot_num:
            print("Más abajo")
            print("Otro intento \n ")
            contador += 1

        #Caso contrario, si no es mayor, por ende es más arriba
        else:
            print("Más arriba")
            print("Otro intento \n ")
            contador += 1

#Inicio del juego usando __name__

if __name__ == "__main__":
    juego()

#Version 1.0 del juego