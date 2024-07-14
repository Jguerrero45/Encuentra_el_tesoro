# SUBPROGRAMA para buscar el tesoro en la matriz

def buscar_tesoro(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                return (i, j)
    return None
