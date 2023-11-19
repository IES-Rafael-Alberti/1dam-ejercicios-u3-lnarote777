""" 
Ejercicio 3.2.1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


def preguntar_divisa():
    """Pregunta la divisa que se desea conocer y devuelve el valor de la divisa introducida.
    """
    divisa = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    pregunta = input("¿Que divisa desea conocer? (Euro, Dollar o Yen): ")
    pregunta = pregunta.title()
    if pregunta in divisa :
        print(divisa.get(pregunta))
    else:
        print("La divisa no se encuentra")
    

def main():
    preguntar_divisa()

if __name__ == "__main__":
    main()