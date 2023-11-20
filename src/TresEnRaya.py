import os

#Símbolos que se mostrarán en el tablero
FICHAS = (' ', 'X' , 'O')


def BorrarConsola():
    """ Limpiar consola"""
    os.system("cls")
    
    
def pulse_tecla_para_continuar():
    """ Mostrar el mensaje presione una tecla para continuar y hacer una pausa hasta que se realice la acción."""
    os.system("pause")


def crear_fila(num_columnas = 3) -> list:
    """Crear la fila

    Args:
        num_columnas (int, optional): _description_. Defaults to 3.

    Returns: lista con la fila generada con los valores por defecto (0 = casilla vacía)
    """
    return list(0 for _ in range(num_columnas))
    

def mostrar_fila(fila):
    contenido_fila ="| "
    for celda in fila:
        contenido_fila += FICHAS[celda] + " | "
    print(contenido_fila)    
    
    

    
def mostrar_tablero(tablero: tuple):
    """ Mostrar en la consola el tblero con las fichas.
    :param tablero: matriz de 3x3 con la información del tablero"""
    BorrarConsola()
    print("-" * 13)
    for fila in tablero:
        mostrar_fila(fila)
        print("_" * 13)

def crear_tablero(num_filas = 3) -> tuple :
    """Crear el tablero 3x3
    :param num_filas : numero de filas del tablero.
        (por defecto se establece el valor 3)
    :returns: tupla con la matriz num_filas x num  columnas
    """
    return tuple(crear_fila() for _ in range(num_filas))


def cambiar_turno(turno: int) -> int:
    if turno % 2 == 0 :
        return 1
    return 2


def pedir_posicion(fila_col: str, msj: str = "") -> int :
    pos = None
    if msj != "": print(msj)
    while pos == None:
        try:
            pos = int(input(f"elige la {fila_col} (1,2,3): ")) - 1
            if not 0 <= pos <= 2:
                raise ValueError
        except ValueError:
            pos = None
            print(f"***ERROR*** {fila_col} no válida")
    return pos

  
def comprobar_casilla(tablero: tuple, pos_ficha: dict) -> bool:
    return tablero[pos_ficha['fila']][pos_ficha['columna']] ==  0
    

"""def verificar_ganador(tablero)-> tuple:
    m"""

def colocar_ficha(tablero: tuple , jugador: int):
    """solicitar a un jugador las posiciones de la ficha que va a colocar.
    :param tablero: matriz de 3x3 con la información del tablero
    :param jugador: numero del jugador
    """
    
    pos_ficha = {'fila': None, 'columna': None}
    pos_correcta = False
    
    while not pos_correcta :
        pos_ficha['fila']= pedir_posicion("fila", f"\nJugador {jugador} coloque una ficha... ")
        pos_ficha['columna']= pedir_posicion("columna")
        
        pos_correcta = comprobar_casilla(tablero, pos_ficha)
        
        if pos_correcta:
            tablero[pos_ficha['fila']][pos_ficha['columna']] = jugador
        else:
            pos_ficha['fila'] = pos_ficha['columna'] = None
            print("error movimiento inválido")
            pulse_tecla_para_continuar()
            mostrar_tablero(tablero)
        


def jugar(tablero: tuple):
    
    
    turno = 0
    ronda = 0
    hay_ganador = False
    
    while not hay_ganador:
        turno = cambiar_turno(turno)
        if turno == 1:
            ronda +=1
            
        print(f"\nRONDA {ronda}")
        print(f"-" * len(f"\nRONDA {ronda}") + "\n")
        
        colocar_ficha(tablero, jugador)
        mostrar_tablero(tablero)
         #verificar_ganador(tablero) 

        if ronda <= 3:
           ganador, hay_ganador = 3
        if hay_ganador :
            print(f"\nEl jugador {ganador} ha ganado \n")
            
        if ronda == 9 :
            hay_ganador = True
            print('\nEmpate\n')

def main():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    jugar(tablero)
    
    
if __name__ == "__main__":
    main()