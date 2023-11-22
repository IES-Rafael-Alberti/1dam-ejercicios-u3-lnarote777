""" 
Ejercicio 3.3.2
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""

import os

def borrarConsola():
    os.system('cls')


def finalizar():
    print( 'Cuando desee finalizar introduzca x\n')


def crearConjunto():
    
    primaria = añadirAlumnosPrimaria()
    secundaria = añadirAlumnosSecundaria()
    conjunto_primaria = set(primaria)
    conjunto_secundaria = set(secundaria)
    print('Lista alumnado de primaria:\n', conjunto_primaria)
    print('\nLista alumnado secundaria:\n', conjunto_secundaria)


def añadirAlumnosPrimaria() -> list:
    finalizar()
    print('---ALUMNADO PRIMARIA---')
    alumnos_primaria = []
    while True:
        nombre_pila= input('Introduzca el nombre de pila del alumno: ')
        
        if nombre_pila.lower() == 'x':
            break
        else:
            nombre_pila = nombre_pila.title()
            alumnos_primaria.append(nombre_pila)
        
    return alumnos_primaria
        
        
def añadirAlumnosSecundaria() -> list:       

    print('---ALUMNADO SECUNDARIA---')
    alumnos_secundaria =[]
    while True:
        nombre_pila= input('Introduzca el nombre de pila del alumno: ')
        
        if nombre_pila.lower() == 'x':
            break 
        else: 
            nombre_pila = nombre_pila.title()
            alumnos_secundaria.append(nombre_pila)
            
    return alumnos_secundaria


def main():
    borrarConsola()
    
    crearConjunto()

     



if __name__ == '__main__':
    main()
