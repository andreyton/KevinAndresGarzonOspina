# -*- coding: utf-8 -*-
"""
Reto 2 - AnalisisNumerico

"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#Variables
nombres = []
cont = 0
y1 = 0
x1 = 0
distancias = []
ciudad = ""

coordenadas = pd.read_csv("coordenadas.csv")
print(coordenadas)

for i in coordenadas.iloc[:,2]:
    nombres.append(i)

marco = plt.figure(figsize=(10, 15))
ax = plt.subplot(2, 1, 1)

#Graficas
for x, y in zip(coordenadas.iloc[:,0], coordenadas.iloc[:,1]):
    plt.plot((x,), (y,), 'bo')
    plt.text(x, y, nombres[cont])
    cont = cont + 1
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.title("Coordenadas geograficas")
plt.savefig("Coordenadas geograficas.pdf")

#Encontrar la estación más cercana a Santa Quiteria

for i in range(0, len(coordenadas)):
    if(coordenadas.iloc[i,2]== "Santa Quiteria"):
        x1 = coordenadas.iloc[i,0]
        y1 = coordenadas.iloc[i,1]

a = np.array([x1,y1])
for i in range(0, len(coordenadas)):
    if(coordenadas.iloc[i,2]!= "Santa Quiteria"):
        x2 = coordenadas.iloc[i,0]
        y2 = coordenadas.iloc[i,1]
        b = ([x2, y2])
        distancias.append((coordenadas.iloc[i,2], np.sqrt(np.sum(np.power(b-a, 2)))))
        
print("\n Distancias: ")        
print(distancias)

menor = distancias[0][1]
for i in range(1, len(distancias)):
    if distancias[i][1]<menor:
        menor = distancias[i][1]
        ciudad = distancias[i][0]
        
print("\nLa estacion mas cerca a Santa Quiteria es la estacion " + ciudad)
