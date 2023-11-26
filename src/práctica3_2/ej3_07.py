""" 
Ejercicio 3.2.7¶
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""

def contestar_pregunta():
    respuestas = {'s', 'n'}
        
    respuesta= input('¿Desea añadir más artículos? (s/n): ')
        
    while respuesta not in respuestas:
        print('**Respuesta inválida - introduzca s o n.')
        respuesta= input('¿Desea añadir más artículos? (s/n): ')

    return respuesta

def pedir_articulos():
    
    lista_compra = {} 
    cont = 1
    
    while True:
        
        articulo = input(f'Articulo {cont}: ')
        precio = float(input('Precio (€): '))
        respuesta = contestar_pregunta()
        
        
        if respuesta == 's':
            cont += 1            
            lista_compra.setdefault(articulo, precio)             
        elif respuesta == 'n':
            lista_compra.setdefault(articulo, precio)  
                       
            print('\nLISTA DE LA COMPRA')
            print('-' * 18)
            
            for articulos , precios in lista_compra.items():
                print(articulos,'    ', precios,'€')
            break


def main():
    
    pedir_articulos()
    

if __name__ == '__main__':
    main()
