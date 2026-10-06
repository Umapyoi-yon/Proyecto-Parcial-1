"""Modulo con la logica de calculo de la regresion lineal por minimos cuadrados."""

"""
Nombre completo: [Juan Manuel Sanchez Castro]
Cuatrimestre: [7mo]
Matrícula: [2403230435]
Asignatura: Ciencia de Datos
Fecha: [5/10/2026]
"""

import numpy as np

"""Calcula las sumatorias necesarias del sistema de ecuaciones normales.

    Returns:
        dict: n, sum_x, sum_y, sum_xy y sum_x2.
"""
def calcular_sumatorias(x, y):
    
    return {
        "n": len(x),
        "sum_x": np.sum(x),
        "sum_y": np.sum(y),
        "sum_xy": np.sum(x * y),
        "sum_x2": np.sum(x ** 2),
    }

"""Calcula la pendiente (m) y el intercepto (b) de la recta y = mx + b.

    Formulas obtenidas al resolver las ecuaciones normales:
        m = (n*Sxy - Sx*Sy) / (n*Sx2 - Sx^2)
        b = (Sy - m*Sx) / n

    Raises:
        ValueError: Si todos los valores de x son iguales (denominador cero).
"""
def calcular_recta_ajuste(x, y):
    
    s = calcular_sumatorias(x, y)

    denominador = s["n"] * s["sum_x2"] - s["sum_x"] ** 2
    if np.isclose(denominador, 0.0):
        raise ValueError("Los valores de x son todos iguales: no hay recta unica.")

    m = (s["n"] * s["sum_xy"] - s["sum_x"] * s["sum_y"]) / denominador
    b = (s["sum_y"] - m * s["sum_x"]) / s["n"]
    return m, b


"""Calcula el coeficiente de determinacion R^2 del ajuste."""
def calcular_r_cuadrado(x, y, m, b):
    y_ajustada = m * x + b
    ss_residual = np.sum((y - y_ajustada) ** 2)
    ss_total = np.sum((y - np.mean(y)) ** 2)
    return 1 - ss_residual / ss_total

"""Devuelve la ecuacion de la recta como texto: y = mx + b."""
def formatear_ecuacion(m, b):
    signo = "+" if b >= 0 else "-"
    return f"y = {m:.4f}x {signo} {abs(b):.4f}"