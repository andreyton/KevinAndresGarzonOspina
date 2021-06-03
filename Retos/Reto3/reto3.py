import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def df_dt(x, t, a, b, c, d):
    """Función del sistema en forma canónica"""
    dx = a * x[0] - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    return np.array([dx, dy])
# Parámetros
a = 0.4     
b = 0.0018
c = 0.8
d = 0.0023
# Condiciones iniciales
x0 = 4   # Presas
y0 = 30    # Depredadores
conds_iniciales = np.array([x0, y0])
# Condiciones para integración
tf = 100  #TIEMPO
N = 200 #CANTIDAD DE MUESTRAS
t = np.linspace(0, tf, N)
solucion = odeint(df_dt, conds_iniciales, t, args=(a, b, c, d))

#plt.plot(t, solucion[:, 0], label='presa')
#plt.plot(t, solucion[:, 1], label='depredador')

#PARA GRAFICA DE CICLOS DEL METODO
x_max = np.max(solucion[:,0]) * 1.05
y_max = np.max(solucion[:,1]) * 1.05
x = np.linspace(0, x_max, 25)
y = np.linspace(0, y_max, 25)
xx, yy = np.meshgrid(x, y)
uu, vv = df_dt((xx, yy), 0, a, b, c, d)
norm = np.sqrt(uu**2 + vv**2)
uu = uu / norm
vv = vv / norm
plt.quiver(xx, yy, uu, vv, norm, cmap=plt.cm.gray)
plt.plot(solucion[:, 0], solucion[:, 1])