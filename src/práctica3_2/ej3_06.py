""""
Ejercicio 3.2.6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""
# con cualquier dato que se quiera introducir 
    
def crearDiccionario(info: dict):
    
    while True:
        clave = input('Introduzca el dato que quiera introducir: ')
        valor = input(f'Introduzca su {clave}: ')
        info.setdefault(clave, valor)
        print(info)
        continuar = input('¿Desea continuar? (s/n): ')
        if continuar.lower() == 'n':
            break
            
        

def main():
    info = {}
    crearDiccionario(info)
    
    
    
if __name__ == '__main__' :
    main()