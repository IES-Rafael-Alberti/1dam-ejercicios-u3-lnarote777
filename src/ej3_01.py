""" 
Ejercicio 3.1.1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla.
"""


def listaAsignaturas(asignaturas):  
    for asignatura in asignaturas:
        print(asignatura)


def main():
    asignaturas =["Matemáticas","Física", "Química", "Historia", "Lengua"]
    listaAsignaturas(asignaturas)


if __name__ == "__main__":
    main()