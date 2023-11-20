""" 
Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""


def pedirnumero(numeros):
    cont = 0
    while cont != 6:
        num_loteria = int(input('Introduzca un numero del 1 al 49: '))
        cont += 1
        numeros.append(num_loteria)
        if num_loteria <= 0 or num_loteria >= 50 :
            print('el numero debe ser del 1 al 49.')
    return numeros    


def main():
    numeros = []
    pedirnumero(numeros)


if __name__ == '__main__':
    main()