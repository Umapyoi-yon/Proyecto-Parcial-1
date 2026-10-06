"""Modulo de visualizacion: dispersion de puntos y recta de ajuste."""


"""
Nombre completo: [Juan Manuel Sanchez Castro]
Cuatrimestre: [7mo]
Matrícula: [2403230435]
Asignatura: Ciencia de Datos
Fecha: [5/10/2026]
"""
import matplotlib.pyplot as plt
import numpy as np


def graficar_ajuste(x, y, m, b, ecuacion):
    """Muestra la dispersion de puntos con la recta de ajuste superpuesta.

    Args:
        x, y (np.ndarray): Muestras originales.
        m, b (float): Pendiente e intercepto de la recta.
        ecuacion (str): Texto de la ecuacion a mostrar en la grafica.
    """
    x_recta = np.linspace(np.min(x), np.max(x), 100)
    y_recta = m * x_recta + b

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, y, color="tab:blue", label="Muestras", zorder=3)
    ax.plot(x_recta, y_recta, color="tab:red", label=f"Ajuste: {ecuacion}")

    ax.set_title("Regresion lineal por minimos cuadrados")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()

    plt.tight_layout()
    plt.show()