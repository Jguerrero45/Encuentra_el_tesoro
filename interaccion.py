# SUBPROGRAMA para pedir las coordenadas al usuario


def pedir_coordenadas(tamano):
    while True:
        try:
            fila = int(input("Ingresa la fila: "))
            columna = int(input("Ingresa la columna: "))
            if 0 <= fila < tamano and 0 <= columna < tamano:
                return (fila, columna)
            else:
                print(
                    f"Debes ingresar números enteros entre 0 y {tamano - 1}.")
        except ValueError:
            print("Debes ingresar un número entero.")
