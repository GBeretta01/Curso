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

        #Determinamos el valor absoluto de la diferente entre el número escogido por el usuario y el número elegido por el programa
        diferencia = abs(user_num - bot_num)

        rangos = {
            range(0,6) : "Caliente",
            range(6,16): "Tibio",
            range(16,31): "Frío"
        }

        #Usamos condicional if para determinar si el número es el mismo
        if user_num == bot_num:
            print("Adivinaste el número!")
            print(f"Lo adivinaste en {contador} intentos")
            break
        
        #De caso contrario creamos el else, para ver qué tan distante está el número
        else:

            #Creamos la variable mensaje para saber el estado (Lo creamos en None es decir, vacío)
            mensaje = None

            #Se crea el for con el fin de iterar sobre el rango y el mensaje
            for rango, msg in rangos.items():

                #El if determina si la diferencia está dentro de los rangos del diccionarios y de ser así guarda el mensaje dentro de la variable para su uso
                if diferencia in rango:
                    mensaje = msg
                    break
            
            #Terminamos el bucle, si hay mensaje, se imprime el mensaje
            if mensaje: 
                print(mensaje)

            #Caso contrario que terminado el for, y no se haya conseguido el valor de la diferencia entre el diccionario, se coloca "Demasiado frío"
            else:
                print("Demasiado frío")

            #Se imprime otro intento y se agrega +1 al contador
            print("Otro intento\n ")
            contador += 1

#Inicio del juego usando __name__

if __name__ == "__main__":
    juego()

#Version 1.1 del juego