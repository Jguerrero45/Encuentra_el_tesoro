# SUBPROGRAMA para leer la matriz(Mapa)
def leer_mapa(archivo):
    with open(archivo, 'r') as f:
        matriz = [list(map(int, line.strip().split())) for line in f]
    return matriz
