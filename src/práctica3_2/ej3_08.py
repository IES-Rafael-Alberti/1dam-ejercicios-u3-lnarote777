""" 
Ejercicio 3.2.8
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

def crear_dicionario():
    
    diccionario = {}

    palabras = input('Introduzca las palabra en español y su traducción al inglés con el formato <palabra>:<traducción> y separadas por comas: ')
    palabras= palabras.split(', ')
    
    for traduccion in palabras:
        espanol, ingles = traduccion.split(':')
        diccionario.setdefault(espanol, ingles)
            
    return diccionario
    
    
def introducir_frase():
    
    return input('\nIntroduzca la frase que desee traducir: ')


def traductor(esp_ing: dict, frase: str) -> str:
    
    for palabra in frase.split(' '):
        if palabra in esp_ing:
            print(esp_ing[palabra], end=' ')
        else:
            print(palabra, end = ' ')



def main():
     
    esp_ing = crear_dicionario()
    frase = introducir_frase()
    
    traductor(esp_ing, frase)  


if __name__ == '__main__':
    main()
