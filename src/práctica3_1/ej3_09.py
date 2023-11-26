""" 
Ejercicio 3.1.9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
"""

 
def pedirPalabra() -> tuple:
    palabra = tuple(input("Introduzca  una palabra: "))
    return palabra

def contarVocales(palabra: tuple) -> tuple:
    vocales = (["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0])
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales


def main():
    palabra = pedirPalabra()
    vocales = contarVocales(palabra)
    print(vocales)
    
    
if __name__ == "__main__":
    main()