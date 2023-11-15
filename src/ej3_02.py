""" 
Ejercicio 3.1.2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""
from borrarTerminal import borrarTerminal


def listaAsignaturas(asignaturas): 
    for i in asignaturas:
        print("Yo estudio" , i)
        
def pedirAsignatura(asignatura):
    numAsign = int(input("Introduzca el numero de asignaturas: "))
    for i in range(numAsign):
        lista = input("Introduce las asignatuas: ")
        asignatura.append(lista)
    return asignatura

def main():
    asignatura = []
    pedirAsignatura(asignatura)
    listaAsignaturas(asignatura)
    



if __name__ == "__main__":
    main()