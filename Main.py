"""Programa principal: regresion lineal por minimos cuadrados.

Uso:
    python main.py [archivo.csv]

Si no se indica archivo, se usa "datos.csv".

Nombre completo: [Juan Manuel Sanchez Castro]
Cuatrimestre: [7mo]
Matrícula: [2403230435]
Asignatura: Ciencia de Datos
Fecha: [5/10/2026]
"""

import sys

from calculo_regresion import (calcular_r_cuadrado, calcular_recta_ajuste,
                               formatear_ecuacion)
from graficas import graficar_ajuste
from lectura_datos import leer_datos


def main():
    ruta = sys.argv[1] if len(sys.argv) > 1 else "datos.csv"

    try:
        x, y = leer_datos(ruta)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return

    m, b = calcular_recta_ajuste(x, y)
    ecuacion = formatear_ecuacion(m, b)

    print(f"Muestras leidas: {len(x)}")
    print(f"Pendiente (m):   {m:.6f}")
    print(f"Intercepto (b):  {b:.6f}")
    print(f"R^2:             {calcular_r_cuadrado(x, y, m, b):.6f}")
    print(f"Ecuacion:        {ecuacion}")

    graficar_ajuste(x, y, m, b, ecuacion)


if __name__ == "__main__":
    main()