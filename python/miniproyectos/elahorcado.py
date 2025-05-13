import random

def elegir_palabra(palabras):
    palabra_elegida = random.choice(palabras)
    return palabra_elegida

lista_palabras = ['comida', 'casa', 'auto', 'manzana', 'panda', 'programar']

elec_palabra = elegir_palabra(lista_palabras)

letrasporadivinar = set(elec_palabra)

letras_correctas = []
letras_incorrectas = []
intentos_max = 6

while len(letras_incorrectas) < intentos_max and letrasporadivinar:
    palabra_oculta = [letra if letra in letras_correctas else '_ ' for letra in elec_palabra]
    print(f"\nPalabra {' '.join(palabra_oculta)}")
    print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
    print(f"Intentos restantes: {intentos_max - len(letras_incorrectas)}")

    while True:
        letra = input("Adivina una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Error: debe ingresar una letra únicamente")
        elif letra in letras_correctas or letra in letras_incorrectas:
            print("Ya has probado esta letra anteriormente")
        else:
            break
    
    if letra in letrasporadivinar:
        letras_correctas.append(letra)
        letrasporadivinar.discard(letra)
        print(f"Correcto! La letra: '{letra}' está dentro de la palabra")
    else:
        letras_incorrectas.append(letra)
        print(f"Incorrecto! La letra: {letra} no está dentro de la palabra")

if not letrasporadivinar:
    print(f"Felicidades! Ganaste, la palabra era: {elec_palabra}")
else:
    print(f"Se acabaron los intentos! Perdiste, la palabra era: {elec_palabra}")