""" 
Ejercicio 3.1.10
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor 
y el mayor de los precios.
"""



def ordenarPrecios(precio):
    precio.sort()
    return precio
    
def main():
    precio = [50, 75, 46, 22, 80, 65, 8]
    print(ordenarPrecios(precio))


if __name__ == "__main__":
    main()