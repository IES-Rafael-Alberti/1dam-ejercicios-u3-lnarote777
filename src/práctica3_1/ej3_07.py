""" 
Ejercicio 3.1.7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""

def posicion_multiplo3(abecedario: list):
    for i in range(len(abecedario), 1, -1):
        if i % 3 == 0:
            abecedario.pop(i-1)
    print(abecedario)



def main():
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    posicion_multiplo3(abecedario)

if __name__ == '__main__':
    main()