"""
Ejercicio 3.2.2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""
 
def datos():
    """Datos del usuario.

    Raises:
        ValueError: salta cuando la edad es negativa

    Returns:
        str: cadena de caracteres
    """
    nombre = input("Indique su nombre: " )
    nombre = nombre.title()
    edad =int(input("Indique su edad: "))
    direccion = input("Indique su dirección: ")
    telefono = int(input("indique sunúmero de teléfono: "))
    
    usuario = {'nombre': nombre , 'edad': edad, 'dirección': direccion , 'teléfono': telefono}
     
    if edad < 0 :
        raise ValueError
    
    mensaje = f'\n{usuario['nombre']} tiene {usuario['edad']}, vive en {usuario['dirección']} y su número de teléfono es {usuario['teléfono']}. '
    return mensaje


def main():
    try :
        print(datos())
    except ValueError:
        print('ERROR - La edad no puede ser negativa.')
        
    
    
if __name__ == "__main__":
    main()