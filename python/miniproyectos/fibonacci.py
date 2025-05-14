#Vamos a hacer la serie de fibonacci, pero primero vamos a entender qué es una serie fibonacci
#Es la secuencia de 2 números que empiezan en 0 y 1, donde cada número que le sigue es igual a la suma de los 2 anteriores
#Entendiendo esto tenemos:

#Determinamos las 2 variables principales
a, b = 0, 1

#Ahora hacemos la serie con un while, en donde terminamos hasta donde queremos llegar, es este caso hasta 10 por ejemplo
# while a < 10:
#     #Imprimimos la suma primeramente
#     print(a)
#     #Realizamos la suma de las 2 variables, siguiendo la teoría:
#     #[a] es el resultado de [a]+[b] y [b] sería la suma de las 2 variables
#     a, b = b, a+b

#Siguiendo con esto, podemos hacer un contador de n cantidad para que termine el while cuando llegue a ese punto, sería:
#Agregamos una nueva variable que determine el contador, incializandolo en 0
contador = 0

#Creamos el while para que cuando el contador llegue a 15 pare la serie
while contador <= 25:
#Implementamos el mismo código para el while
    print(a)
    a, b = b, a+b
    #Aumentamos el contador en 1 por cada while
    contador += 1