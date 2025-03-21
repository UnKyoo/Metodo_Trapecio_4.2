#   Codigo que implementa el metodo del trapecio 
#   para aproximar la integral
#   
#
#           Autor:
#   Mendez Cervera Gilbert Alexandrer
#   mendezgilbert222304@outlook.com
#   Version 1.01 : 11/03/2025
#

import numpy as np
import matplotlib.pyplot as plt
"""EJERCICIO #1
def f(x):
    return x**2+3*x+1
"""

"""EJERCICIO #2
# Definimos la función a integrar
def f(x):
    return np.exp(-x**2)
"""
"""EJERCICIO #3
def f(x):
    return np.sin(x)
"""

# Definimos la función a integrar
def f(x):
    return x**2+3*x+1

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral, x, y

"""EJERCICO #1 
# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n = 10,20,50  # Número de subdivisiones
"""
"""EJERCICIO #2 
# Parámetros de integración
a, b = 1, 4  # Intervalo de integración
n = 5,10,15  # Número de subdivisiones
"""
"""EJERCICIO #3
a, b = 0, np.pi  # Intervalo de integración
n = 30,60,90  # Número de subdivisiones
"""

# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n = 10  # Número de subdivisiones

# Cálculo de la integral
integral_approx, x_vals, y_vals = trapezoidal_rule(a, b, n)

# Imprimir el resultado de la integral aproximada
print(f"Integral aproximada con la regla del trapecio: {integral_approx:.6f}")

# Gráfica de la función y la aproximación por trapecios
x_fine = np.linspace(a, b, 100)
y_fine = f(x_fine)  

"""EJERCICIO #1
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = x**2+3*x+1', linewidth=2)
"""
"""EJERCICIO #2
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = e^{-x^2}$', linewidth=2)
"""     
"""EJERCICIO #3
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = \sin(x)$', linewidth=2)
"""
plt.figure(figsize=(8, 5))
plt.plot(x_fine, y_fine, 'r-', label=r'$f(x) = x**2+3*x+1', linewidth=2)
plt.fill_between(x_vals, y_vals, alpha=0.3, color='blue', label="Aproximación Trapecios")
plt.plot(x_vals, y_vals, 'bo-', label="Puntos de integración")

# Etiquetas y leyenda
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.title("Aproximación de la integral con la regla del trapecio")
plt.legend()
plt.grid()

# Guardar la figura
plt.savefig("trapecio.png")
plt.show()

