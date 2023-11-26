""" 
Ejercicio 3.1.1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.
"""


def pedirNumAsignaturas():
    return int(input("Número de asignaturas:"))


def pedirAsignaturas():
    numAsignatura = pedirNumAsignaturas()
    return tuple(input("Introduzca la asignatura: ") for i in range(numAsignatura))
    

def listaAsignaturas(asignaturas):  
    for asignatura in asignaturas:
        print(asignatura)


def main():
    
    asignaturas = pedirAsignaturas()
    listaAsignaturas(asignaturas)


if __name__ == "__main__":
    main()