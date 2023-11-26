""" 
Ejercicio 3.1.3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> 
donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""



def pedirNota(asignatura):
    for i in asignatura:
        nota = input()
        mensaje = f"En {i} ha sacado un {nota}"
        print(mensaje) 
    
    
def pedirNumAsignaturas():
    return int(input("Número de asignaturas:"))


def pedirAsignaturas():
    numAsignatura = pedirNumAsignaturas()
    return list(input("Introduzca la asignatura: ") for i in range(numAsignatura))


def main():
    
    asignatura = pedirAsignaturas()
    print(pedirNota(asignatura))


if __name__ == "__main__":
    main()