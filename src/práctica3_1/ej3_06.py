""" 
Ejercicio 3.1.6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""


def preguntar_nota(asignaturas: list, aprobadas:list):
    for asignatura in asignaturas:
        nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
        if nota >= 5:
            aprobadas.append(asignatura)
    for asignatura in aprobadas:
        asignaturas.remove(asignatura)
    print(f"Tienes que repetir{asignaturas}")


def main():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    aprobadas = []
    preguntar_nota(asignaturas, aprobadas)
    
    
if __name__ == '__main__':
    main()