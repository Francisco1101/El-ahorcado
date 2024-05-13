import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)
    while "_" in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():
    print("==================")
    print("    El Ahocado    ")
    print("==================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te queda {vidas} vidas y has usado estas letras: {" ".join(letras_adivinadas)}")       
        palabra_lista = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {" ".join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)


            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra")

        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra escoge otra")

        else:
            print("\nEsta letra no es valida")

    if vidas == 0:
        print(vidas_diccionario_visual [vidas])
        print(f"perdiste, la palabra era {palabra}")
    else:
        print(f"ganaste la palabra era {palabra}")


ahorcado()      
