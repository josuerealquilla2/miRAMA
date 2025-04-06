import random
import requests

def personajeAleatorio():
    api_url = "https://rickandmortyapi.com/api/character"
    response = requests.get(api_url)
    personajes = response.json()['results']
    personaje_random = random.choice(personajes)
    return personaje_random['name']

def adivinaPersonaje():
    nombre_personaje = personajeAleatorio()
    letras_adivinadas = set()
    intentos = 3
    print("ADIVINA EL PERSONAJE DE RICK AND MORTY")
    print("_" * len(nombre_personaje))

    while intentos > 0:
        letra = input("ADIVINA UNA LETRA: ").lower()
        if letra not in letras_adivinadas:
            letras_adivinadas.add(letra)
            if letra not in nombre_personaje:
                intentos -= 1

        palabra_actual = ""
        for letra in nombre_personaje:
            if letra in letras_adivinadas:
                palabra_actual += letra
            else:
                palabra_actual += "_"
        print("Nombre: ", "".join(palabra_actual))
        print(f"Número de intentos restantes: {intentos}")

        if "_" not in palabra_actual:
            print(f"¡GANASTE! El personaje era {nombre_personaje}")
            break

    if intentos == 0:
        print(f"LO SIENTO, PERDISTE. El personaje era {nombre_personaje}")

adivinaPersonaje()
