import random

import requests


def pokemonAleatorio():
    pokerand=random.randint(1,900)
    pokeapi="https://pokeapi.co/api/v2/pokemon/"
    pokeresultado=requests.get(f"{pokeapi}/{pokerand}")
    return pokeresultado.json()['name']
def pokeahorcados():
    pokenombre=pokemonAleatorio()
    letraAdivina=set()
    intentos=3
    print("ADIVINA EL POKEMON ")
    print("_" * len(pokenombre))

    while intentos > 0:
        letra=input("ADIVINA UNA LETRA ").lower()
        if letra not in letraAdivina:
            letraAdivina.add(letra)
            if letra not  in pokenombre:
                intentos -=1
        palabras=""
        for letra in pokenombre:
            if letra in letraAdivina:
                palabras += letra
            else:
                palabras +="_"
        print("nombre ", "".join(palabras))
        print(f"numero de intentos{intentos}")

        if "_" not in palabras:
            print(f"GANASTE EL POKEMON ERA {pokenombre}")
            break
    if intentos ==0:
        print(f"LO SIENTO PERDISTE ESTE ERA EL POKEMON {pokenombre}")

pokeahorcados()

