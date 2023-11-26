""" 
Ejercicio 3.3.6
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
"""



def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    letras_comunes = vocales|consonantes
    print(f'Vocales: {sorted(vocales)}')
    print(f'Consonantes: {sorted(consonantes)}')
    print(f'Abecedario: {sorted(letras_comunes)}' )


if __name__ == '__main__':
    main()
