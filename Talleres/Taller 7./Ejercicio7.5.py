"""-----------------------------------------------------------
Ejercicios
Cristian Contreras
Kevin Garzon
-----------------------------------------------------------"""

from scipy import integrate
import numpy as arreglo
from scipy.interpolate import lagrange

#Datos dados
x=arreglo.array([0 , 0.2, 0.4, 0.6, 0.8])
y=arreglo.array([3.592, 3.110, 3.017, 2.865, 2.658])
a = 0
b = 0.8
tam = 15

#Creacion del polinomio
funcion=lagrange(x,y)

#Punto A
#Metodo de trapecios
def integral_trapecios(funcion,a,b,p):
    r = (b-a)/p
    s = 0
    for i in range(1,p):
        s = s+funcion(a+i*r)
    t = r/2*(funcion(a)+2*s+funcion(b))

    return t

#Punto B
#Metodo de simpson
def integral_simpson(funcion,a,b,p):
    r = (b-a)/p
    y = 0
    x = a
    for i in  range(1, p):      
        y = y+2*(i%2+1)* funcion(x+i*r)
    y = r/3 * (funcion(a)+y+funcion(b))
    return y
       
#Impresiones
print('\n Trapecios :')
for i in range(1, tam+1):
    print( i,'  ', integral_trapecios(funcion,a, b, i))
print('\n \n Simpson : ')
for j in range(1, tam+1):
    print( j,'  ', integral_simpson(funcion, a, b, j))
    
#Punto C
romberg = 2
print('\n \n Romberg Segundo Grado :', integrate.romberg(funcion, a, b, divmax=romberg))