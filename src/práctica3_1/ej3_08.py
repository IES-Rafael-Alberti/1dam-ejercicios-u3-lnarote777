""" 
Ejercicio 3.1.8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

def palindromo(palabra, invertida):

    if palabra == invertida:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


def main():
    palabra = input("Introduce una palabra: ")
    invertida = palabra
    palabra = list(palabra)
    invertida = list(invertida)
    invertida.reverse()
    
    palindromo(palabra, invertida)

if __name__ == '__main__':
    main()




