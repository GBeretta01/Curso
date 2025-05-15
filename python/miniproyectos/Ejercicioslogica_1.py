def suma_lista():
    #- 1Dada una lista de números, calcula la suma de la lista
    print("\nDada una lista de números, calcula la suma de la lista")

    #Primero definiré la lista como x
    x = [5,3,6,4,8,0,1]

    #Ahora hacemos la suma de la lista con un bucle for que itere sobre cada caracter de la lista

    #Determinamos la variable para la suma de la variable, donde debe ser entero, no tipo lista
    sum_x = 0

    #Hacemos el for donde n es el iterador en x, recorrerá cada uno desde el 0,1,2,3,4,5,6 = [5,3,6,4,8,0,1]
    for n in x:
        #Sumamos en la variable sum_x el valor anterior con el próximo n, donde sum_x = 0 -> 0+5, 5+3, 8+6 y así sucesivamente hasta que acabe el for
        sum_x += n
    
    print(f"\n{sum_x}")

def factorial_de_un_numero():
    #Escribe una función factorial(n) que reciba un entero no negativo n y devuelva su factorial n!
    print("\nEscribe una función factorial(n) que reciba un entero no negativo n y devuelva su factorial n!")

    #Definimos la entrada de un número entero no negativo
    while True:
        numero_str = input("Ingrese un número entero no negativo: ")
        try:
            numero = int(numero_str)  
            if numero < 0:
                print("ERROR! Ingrese un número positivo")
            else:
                break
        except ValueError:
            print("ERROR! Debe ingresar un número entero")
    
    #Definimos donde se sumará el factorial, lo definimos en 1 porque no podemos poner 0, si ponemos 0, todo el resultado sería 0
    factorial = 1

    #Determinamos el for con x para iterador en un rango de 1 hasta el número + 1; el factorial es el x * x, en cada recorrido del iterador
    for x in range(1, numero + 1):
        factorial *= x

    print(factorial)

def es_palindromo():
    #Crea una función es_palindromo(s: str) -> bool que determine si la cadena s es un palíndromo, ignorando espacios, puntuación y mayúsculas
    print("Crea una función es_palindromo(s: str) -> bool que determine si la cadena s es un palíndromo")

    #Determinamos la entrada y los carácteres permitidos
    entrada = input("Ingrese una palabra para determinar si es palindroma: ")
    caracteres_permitidos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    #Limpiamos la cadena asignando a la variable un join donde recorra con un for la entrada asegurandose que estén dentro de los permitidos
    palabra = ''.join(n for n in entrada if n in caracteres_permitidos).lower()

    #Determinamos la validación
    validacion = None
    
    #Si la palabra es igual a su inversa [::-1] es True, caso contrario False
    if palabra == palabra[::-1]:
        validacion = True
    else:
        validacion = False
    
    #Imprimimos el resultado
    print(f"¿La palabra es palíndroma?: {validacion}")

def primos():
    import math
    #Escribe primos_hasta(N: int) -> list[int] que devuelva todos los primos desde 2 hasta N.
    print("Escribe primos_hasta(N: int) -> list[int] que devuelva todos los primos desde 2 hasta N.")

    while True:
        numero_str = input("Ingrese un número entero no negativo: ")
        try:
            numero = int(numero_str)  
            if numero < 2:
                print("ERROR! Ingrese un número positivo o mayor a 2")
            else:
                break
        except ValueError:
            print("ERROR! Debe ingresar un número entero")

    primos_v = []
    primos_f = []
    for n in range(2, numero+1):
        es_primo = True
        limit = int(math.sqrt(n)) + 1
        for i in range (2, limit):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            primos_v.append(n)
        else:
            primos_f.append(n)
    
    print(f"Los números primos son: {primos_v}")
    print(f"Los números no primos son: {primos_f}")

def tablas_multiplicar() -> None:
    #Imprime las tablas de multiplicar del 1 al 10.
    print("Imprime las tablas de multiplicar del 1 al 10.")

    for base in range(1, 11):
        for x in range(1, 11):
            print(f"{base} x {x} = {base*x}")
        print()

def bubble_sort() -> int:
    #Implementa la función bubble_sort(lista: list[int]) -> list[int] que reciba una lista de enteros y la ordene de menor a mayor usando el algoritmo de burbujeo.
    print("Implementa la función que reciba una lista de enteros y la ordene de menor a mayor usando el algoritmo de burbujeo.")

    #Creamos la lista de enteros
    enteros = [6,4,3,8,6,17,42,34,2,7,34,87,9]

    #Creamos un bucle principal donde n en un rango de [total de enteros]
    for n in range(len(enteros)):
    #Creamos el bucle aninado donde i recorre dentro del rango de 0 a (el total de enteros - 1 - n que va recorriendo)
        for i in range(0, len(enteros)-1-n):
    #Y por último, definimos el if, donde si el entero que se está viendo es mayor que su siguiente, su valor se invierte y así sucesivamente con cada
            if enteros[i] > enteros [i+1]:
                enteros[i], enteros[i+1] = enteros [i+1], enteros[i]
    
    print(enteros)