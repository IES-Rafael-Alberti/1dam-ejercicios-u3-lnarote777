""" 
Ejercicio 3.3.4
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""

def crear_conjunto(frutas1, frutas2):
    set_frutas1= set(frutas1)
    set_frutas2 = set(frutas2)

    frutas_comunes = set_frutas1 & set_frutas2
    print (f'frutas que hay en común en las dos listas: {frutas_comunes}\n')
    
    solo_frutas1(set_frutas1, set_frutas2)
    solo_frutas2(set_frutas1, set_frutas2)

    
def solo_frutas1(set_frutas1, set_frutas2):
    frutas_solo_en_frutas1 = set_frutas1 - set_frutas2
    
    print(f'Frutas que están en frutas1 pero no en frutas2{frutas_solo_en_frutas1}\n')
    
    
def solo_frutas2(set_frutas1, set_frutas2):
    frutas_solo_en_frutas2 = set_frutas2 - set_frutas1
    
    print(f'Frutas que están en frutas2 pero no en frutas1{frutas_solo_en_frutas2}')


def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    print(f'Lista frutas1: {frutas1}')
    print(f'Lista frutas2: {frutas2}\n')
    
    crear_conjunto(frutas1, frutas2)
    

if __name__ == '__main__':
    main()
