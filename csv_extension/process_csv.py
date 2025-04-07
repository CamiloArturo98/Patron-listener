import csv

try:
    with open("datos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        encabezado = next(lector)
        print("Encabezado:", encabezado)
        for fila in lector:
            print("Fila:", fila)
except FileNotFoundError:
    print("Archivo no encontrado.")
