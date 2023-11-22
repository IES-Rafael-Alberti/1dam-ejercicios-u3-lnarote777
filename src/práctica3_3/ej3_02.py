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
    print( '---Cuando desee finalizar introduzca x---\n')


def primariaIncluidosSecundaria(conjunto_primaria, conjunto_secundaria):
    incluidos = conjunto_primaria <= conjunto_secundaria    
    
    print(f'¿Los nombres de primaria estan incluidos en secundaria? {incluidos}')


def alumnosNoRepetidos(conjunto_primaria, conjunto_secundaria):
    norepetidos = conjunto_primaria - conjunto_secundaria
    print(f'\nNombres de primaria que no se repiten en secundaria: {norepetidos}')


def alumnosRepetidos(conjunto_primaria, conjunto_secundaria):
    repetidos = conjunto_primaria & conjunto_secundaria
    print(f'\nNombres que se repiten en los dos cursos: {repetidos}')


def crearConjunto():
    
    primaria = añadirAlumnosPrimaria()
    conjunto_primaria = set(primaria)
    print('Lista alumnado de primaria:\n', conjunto_primaria)
    
    secundaria = añadirAlumnosSecundaria()
    conjunto_secundaria = set(secundaria)
    print('Lista alumnado secundaria:\n', conjunto_secundaria)

    alumnosRepetidos(conjunto_primaria, conjunto_secundaria)
    alumnosNoRepetidos(conjunto_primaria, conjunto_secundaria)
    primariaIncluidosSecundaria(conjunto_primaria, conjunto_secundaria)
    

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

    print('\n---ALUMNADO SECUNDARIA---')
    
    alumnos_secundaria = []
    
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
