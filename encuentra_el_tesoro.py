import os
from lectura import leer_mapa
from busqueda import buscar_tesoro
from interaccion import pedir_coordenadas, menu_interactivo
from codigo_ascii import mostrar_codigo_ascii_ganador, mostrar_codigo_ascii_bienvenida, mostrar_codigo_ascii_perdedor

"""Juego: encuentra el tesoro
   Objetivo: encontrar el tesoro mediante pistas que te ofrece el juego segun su 
   posicion, con vidas limitadas y tamaño de matriz definido por el nivel."""

# Elaborado por: Jose Guerrero


# SUBPROGRAMA para dar pistas al usuario

def dar_pistas(pos_usuario, pos_tesoro):
    if pos_usuario == pos_tesoro:
        mostrar_codigo_ascii_ganador()
        return True
    else:
        if pos_usuario[0] < pos_tesoro[0]:
            print("El tesoro está más abajo.")
        elif pos_usuario[0] > pos_tesoro[0]:
            print("El tesoro está más arriba.")
        if pos_usuario[1] < pos_tesoro[1]:
            print("El tesoro está más a la derecha.")
        elif pos_usuario[1] > pos_tesoro[1]:
            print("El tesoro está más a la izquierda.")
        return False


# SUBPROGRAMA para el menu interactivo


def menu_interactivo():
    nombre = input("\n Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    nivel = int(input("Ingresa el nivel que deseas jugar (1, 2 o 3): "))

    f = open("jugador_info.txt", "w")
    try:
        f.write(f"Nombre: {nombre}\n")
        f.write(f"Edad: {edad}\n")
        f.write(f"Nivel: {nivel}\n")
    finally:
        f.close()

    return nombre, nivel


# SUBPROGRAMA para imprimir la matriz de ejemplo


def imprimir_ejemplo_matriz(matriz):
    print('\n\n\n')
    tamano = len(matriz)
    # Definir el ancho de cada columna
    ancho_columna = 3

    # Imprimir los índices de las columnas
    encabezado = " " * ancho_columna + \
        "".join([f"{i:>{ancho_columna}}" for i in range(tamano)])
    print(encabezado)

    for i in range(tamano):
        # Imprimir el índice de la fila seguido de la fila de la matriz
        fila = f"{i:>{ancho_columna}}" + \
            "".join([f"{elem:>{ancho_columna}}" for elem in matriz[i]])
        print(fila)
    print('\n\n\n')

# SUBPROGRAMA para inicializar la matriz(tesoro)


def inicializar_matriz(tamano):
    return [['x' for _ in range(tamano)] for _ in range(tamano)]

# SUBPROGRAMA para actualizar la matriz de ejemplo con una 'o' en la posición del usuario


def actualizar_matriz(matriz, fila, columna):
    matriz[fila][columna] = 'o'

# SUBPROGRAMA principal


def main():
    os.system('cls')
    mostrar_codigo_ascii_bienvenida()
    niveles = {
        1: ('nivel1.txt', 5),
        2: ('nivel2.txt', 10),
        3: ('nivel3.txt', 25)
    }

    nombre, nivel = menu_interactivo()
    archivo, tamano = niveles[nivel]

    print(f"Nivel {nivel}")
    matriz_ejemplo = inicializar_matriz(tamano)
    imprimir_ejemplo_matriz(matriz_ejemplo)
    matriz = leer_mapa(archivo)
    if matriz is None:
        return

    pos_tesoro = buscar_tesoro(matriz)
    if pos_tesoro is None:
        print("Error: No se encontró el tesoro en el mapa.")
        return

    vidas = 5
    encontrado = False
    while not encontrado and vidas > 0:
        pos_usuario = pedir_coordenadas(tamano)
        encontrado = dar_pistas(pos_usuario, pos_tesoro)
        if not encontrado:
            vidas -= 1
            print(f"Te quedan {vidas} vidas.")
            actualizar_matriz(matriz_ejemplo, pos_usuario[0], pos_usuario[1])
            imprimir_ejemplo_matriz(matriz_ejemplo)
    if vidas == 0:
        mostrar_codigo_ascii_perdedor()
    with open("jugador_info.txt", "a") as f:
        if encontrado:
            f.write("Resultado: Gano\n")
        else:
            f.write("Resultado: No gano\n")


main()
