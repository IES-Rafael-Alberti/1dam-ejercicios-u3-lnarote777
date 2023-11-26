""" 
Ejercicio 3.2.9¶
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""


import os

def borrarconsola():
    os.system ("cls")


def menu():
    facturas = {}
    
    while True:  
        
        print('MENÚ')
        print('-' * 5)
        print('1. Añadir nueva factura.')
        print('2. Pagar una factura existente.')
        print('3. Terminar.')
        
        opcion = input('Elija una opción: ')
        
        if opcion == '1':
            anadir_factura(facturas)
        elif opcion == '2':
            pagar_factura(facturas)
        elif opcion == '3':
            print('Hasta Pronto!')
            break


def anadir_factura(facturas: dict) -> dict:
    
    nueva = input('\nIntroduzca el número y cantidad de la factura que desee guardar.(Formato: nºfactura: cantidad a cobrar) -> ')
    
    numero_factura, cobro = nueva.split(': ')
    facturas.setdefault(numero_factura, cobro)
    
    print('---Factura añadida correctamente.---\n')
    
    return facturas


def pagar_factura(facturas: dict):
    
    if not facturas:
        print('***No se encontró ninguna Factura. Porfavor añada una factura antes de continuar.***\n')
    else:
        print('\nFacturas por cobrar')
        print('-' * 20)
        print('Nº factura \t Cantidad a cobrar')
        for numFact , cobro in facturas.items():
            print(numFact, '\t\t\t', cobro,'€')
        print('')
        
        pagar = input('Introduzca el número de la factura que desee pagar: ')
        facturas.pop(pagar)    
        print('\nFactura pagada con éxito!\n')


    
def main():
    borrarconsola()
    menu()



if __name__ == '__main__':
    main()
