import random
import requests

def fraseAleatoria():
    api_url = "https://thesimpsonsquoteapi.glitch.me/quotes"
    response = requests.get(api_url)
    frase_data = response.json()[0]
    return frase_data['quote']

def adivinaFrase():
    frase = fraseAleatoria()
    letras_adivinadas = set()
    intentos = 5
    print("ADIVINA LA FRASE DE LOS SIMPSON")
    print("_" * len(frase))

    while intentos > 0:
        letra = input("ADIVINA UNA LETRA: ").lower()
        if letra not in letras_adivinadas:
            letras_adivinadas.add(letra)
            if letra not in frase:
                intentos -= 1

        frase_actual = ""
        for letra in frase:
            if letra in letras_adivinadas or letra == " ":
                frase_actual += letra
            else:
                frase_actual += "_"
        print("Frase: ", "".join(frase_actual))
        print(f"Número de intentos restantes: {intentos}")

        if "_" not in frase_actual:
            print(f"¡GANASTE! La frase era: {frase}")
            break

    if intentos == 0:
        print(f"LO SIENTO, PERDISTE. La frase era: {frase}")

adivinaFrase()
