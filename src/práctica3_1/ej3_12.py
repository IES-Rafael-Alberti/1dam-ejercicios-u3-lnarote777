""" 
Ejercicio 3.1.12
Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

def producto_matrices(matriz_a, matriz_b):
    resultado = []
    for i in range(len(matriz_a)):
        fila_resultado = []
        for j in range(len(matriz_b[0])):
            suma = 0 
            for k in range(len(matriz_b)):
                suma += matriz_a[i][k] * matriz_b[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado
    


def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


def main():
    matriz_a = [[1, 2], [3, 4], [5, 6]]
    matriz_b = [[-1, 0, 0] ,[1, 1, 1]]
    
    print("Matriz A:")
    mostrar_matriz(matriz_a)
    print("\nMatriz B:")
    mostrar_matriz(matriz_b)
    
    print("\nProducto de las matrices A y B:")
    producto = producto_matrices(matriz_a, matriz_b)
    mostrar_matriz(producto)



if __name__ == "__main__" :
    main()