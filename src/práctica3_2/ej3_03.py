"""
Ejercicio 3.2.3¶
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
    
    Fruta	 Precio
    Plátano	  1.35
    Manzana	  0.80
    Pera	  0.85
    Naranja	  0.70
    
"""
def fruta_y_kilos():
    """Pide la fruta y los kilos al usuario y comprueba que esté en el diccionario.
    """
    frutas_precios = {'Plátano': 1.35 , 'Manzana': 0.80 , 'Pera': 0.85 , 'Naranja': 0.70}
    fruta = input('¿Que fruta quiere? ')
    fruta = fruta.title()
    kilos = float(input('¿Cuántos kilos? '))
    
    if fruta in frutas_precios:
        print(f'{fruta}: {frutas_precios.get(fruta) * kilos} €')
    else: 
        print('La fruta no se encuentra disponible.')


def main():
    fruta_y_kilos()
        
    
    
if __name__ == "__main__":
    main()