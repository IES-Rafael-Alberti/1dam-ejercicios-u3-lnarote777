""" 
Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""


def pedirNumero(numeros: list):
    cont = 1
    while cont != 6:
        
        num_loteria = int(input(f'({cont}) => '))

        if 0 < num_loteria and num_loteria> 50 :
            num_loteria = int(input(f'**número repetido ingrese un numero válido porfavor.\n({cont}) => '))
            while num_loteria in numeros:
                num_loteria = int(input(f'**número repetido ingrese un numero válido porfavor.\n({cont}) => '))
            numeros.append(num_loteria)
            
            cont += 1
        else:
            while 0 >= num_loteria or 50 <=  num_loteria:
                num_loteria = int(input(f'** numero inválido. introduzca un número del 1 al 49 porfsvor. \n({cont}) => '))
            if 0 < num_loteria and num_loteria < 50 :
                while num_loteria in numeros:
                    num_loteria = int(input(f'**número repetido ingrese un numero válido porfavor.\n({cont}) => '))
                numeros.append(num_loteria)
            numeros.append(num_loteria)
            
            cont += 1
        
    pedirReintegro(numeros)    


def pedirReintegro(numeros: list):
    numeros.sort()
    reintegro = int(input('Ingrese el reintegro: '))
    while  0 > reintegro  or 9 <reintegro :
        reintegro = int(input('Reintegro no vaálido ingrese un número del 1 al 9. => '))
    numeros.append(reintegro)
    
    print(f'Sus números de la primitiva son: {numeros}')
        

def main():
    numeros = []
    print('Ingrese los numeros de la lotería:')
    pedirNumero(numeros)


if __name__ == '__main__':
    main()