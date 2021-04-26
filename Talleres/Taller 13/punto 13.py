# -*- coding: utf-8 -*-
"""
@author: Kevin Garzon - Cristian Contreras

-----------------------------------------------------------
Ejercicio 13
-----------------------------------------------------------"""

import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

#Arreglos
x = np.array([4410000, 4830000, 5250000, 5670000])
y = np.array([1165978, 1329190, 1501474, 1682830])
x2 = np.array([4830000, 5250000, 5670000])
y2 = np.array([1329190, 1501474, 1682830])

fun = spi.interp1d(x, y)
inter2 = spi.lagrange(x2, y2)
inter3 = spi.lagrange(x, y)

#Graficas
plt.plot(x,y,color='darkred',linestyle='--')
plt.plot(x2,y2,color='darkblue',linestyle='--')
plt.plot(5000000,inter3(5000000),marker='X',color='black')
plt.xlabel("Base imponible")
plt.ylabel("Cuota integra")
plt.show()

#Resultados
print("Cuota por impuesto de renta:")
print("interpolacion lineal = {:.20f}".format(fun(5000000)))
print("Interpolacion grado 2 = {:.20f}".format(inter2(5000000)))
print("Interpolacion grado 3 = {:.20f}".format(inter3(5000000)))


