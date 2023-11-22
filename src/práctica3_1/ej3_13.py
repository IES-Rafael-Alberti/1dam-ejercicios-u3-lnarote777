""" 
Ejercicio 3.1.13
Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
"""

def convertir_a_entero(num):
    n = len(num)
    for i in range(n):
        num[i] = int(num[i])
    lista = tuple(num)
    return lista


def pedir_numeros():
    num = input("Introduzca una serie de números separados por comas: ")
    num =num.split(",")

    return num


def media_y_deviacion_numeros(enteros):
    suma = 0
    suma_desviacion = 0
    for i in enteros :
        suma += i
        suma_desviacion += i**2
    media = suma/len(enteros)
    desviacion = (suma_desviacion/len(enteros)-media**2)**(1/2)
    return f'La media es {media} y la desviación típica es {desviacion}'

def main():
    numeros = pedir_numeros()
    enteros = convertir_a_entero(numeros)
    print(media_y_deviacion_numeros(enteros))

if __name__ == "__main__":
    main()