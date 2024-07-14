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
