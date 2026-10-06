"""Modulo de lectura y validacion de datos (x, y) desde archivos .csv o .txt."""


"""
Nombre completo: [Juan Manuel Sanchez Castro]
Cuatrimestre: [7mo]
Matrícula: [2403230435]
Asignatura: Ciencia de Datos
Fecha: [5/10/2026]
"""


import numpy as np

"""Lee muestras (x, y) de un archivo de texto separado por comas.

    El archivo puede tener o no una linea de encabezado (por ejemplo "x,y").

    Args:
        ruta_archivo (str): Ruta del archivo .csv o .txt.

    Returns:
        tuple[np.ndarray, np.ndarray]: Arreglos x e y.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el formato es invalido o hay menos de 2 muestras.
"""
def leer_datos(ruta_archivo):
    
    x_lista, y_lista = [], []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for numero_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if not linea:
                continue  # Se ignoran lineas vacias

            partes = linea.split(",")
            if len(partes) != 2:
                raise ValueError(
                    f"Linea {numero_linea}: se esperaban 2 valores separados por coma."
                )
            try:
                x_lista.append(float(partes[0]))
                y_lista.append(float(partes[1]))
            except ValueError:
                # Si es la primera linea, se asume que es un encabezado
                if numero_linea == 1:
                    continue
                raise ValueError(f"Linea {numero_linea}: valores no numericos.")

    if len(x_lista) < 2:
        raise ValueError("Se necesitan al menos 2 muestras para ajustar una recta.")

    return np.array(x_lista), np.array(y_lista)