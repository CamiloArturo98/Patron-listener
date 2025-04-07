import csv

def filtrar_csv(nombre_archivo, columna, valor_minimo):
    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            print(f"Filas donde {columna} > {valor_minimo}:")
            for fila in lector:
                if fila[columna] and int(fila[columna]) > valor_minimo:
                    print(fila)
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except KeyError:
        print(f"La columna '{columna}' no existe.")
    except Exception as e:
        print("Error:", e)

# Ejecutar la función
filtrar_csv("datos.csv", "edad", 30)
