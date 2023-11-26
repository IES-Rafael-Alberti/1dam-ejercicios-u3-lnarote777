""" 
Ejercicio 3.3.5
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""


def crear_conjuntosPares(numeros: set) -> set:
    pares = set()
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.add(numero)
    return pares
    

def multiplos_de_tres(numeros: set) -> set:
    multiplos3 = set()
    
    for numero in numeros:
        if numero % 3 == 0:
            multiplos3.add(numero)
    return multiplos3


def interseccion_pares_multiplos(pares: set, multiplos: set) -> set:
    inter = pares&multiplos
    return inter

def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = crear_conjuntosPares(numeros)
    multiplos = multiplos_de_tres(numeros)
    interseccion = interseccion_pares_multiplos(pares, multiplos)
    
    print(f'Lista números: {numeros}')
    print(f'Numeros pares de la lista: {pares}')
    print(f'Multiplos de 3 en la lista: {multiplos}')
    print(f'Intersección entre los números pares y los múltiplos de 3: {interseccion}')

if __name__ == '__main__':
    main()
