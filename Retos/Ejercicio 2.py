import matplotlib.pyplot as plt
import numpy as np

def ciclo(f,x1,x2,aux):
    for i in aux:
        secant(f, x1, x2, i)
        
def secant(f, x1, x2, tol):
    error = 1e3
    acum = []
    iteraciones = [] 
    n = 0
    x3 = 0
    while error > tol:
        x3 = x1 - ((x2 - x1) / (f(x2) - f(x1))) * f(x1)
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        acum.append(error)
        #print(error)
        iteraciones.append(n)
        n += 1
    print("Solucion Aproximada: {:.20f}".format(x3))
    print("Numero de iteraciones: {:d}".format(n))

    plt.plot(iteraciones,acum)
    plt.xlabel('Iteaciones')
    plt.ylabel('Error')
    plt.title('METODO DE SECANTE CON ' + str(tol)) 
    plt.show()

def secantXY(f, g, x1, x2, y1, y2, tol):
    arreglo = []
    errorx = 1e3
    errory = 1e3
    acum = []
    iteraciones = [] 
    n = 0
    x3 = 0
    y3 = 0
    while errorx > tol and errory > tol:
        x3 = x1 - ((x2 - x1) / (f(x2,y2) - f(x1,y1))) * f(x1,y1)
        y3 = y1 - ((y2 - y1) / (g(x2,y2) - g(x1,y1))) * g(x1,y1)
        x1 = x2
        x2 = x3
        y1 = y2
        y2 = y3
        errorx = abs(f(x3,y3))
        errory = abs(g(x3,y3))
        acum.append(errorx)
        #print(error)
        iteraciones.append(n)
        n += 1
        arreglo = np.append(arreglo,[n,y3])
    print("Solucion AproximadaX: {:.20f}".format(x3))
    print("Solucion AproximadaY: {:.20f}".format(y3))
    print("Numero de iteraciones: {:d}".format(n))
    print(arreglo)

    plt.plot(arreglo)
    plt.xlabel('Iteraciones')
    plt.ylabel('Solucion en y')
    plt.title('Metodo de la secante con ' + str(tol)) 
    plt.show()
    
"""-----------------------------------------------------------
Pruebas
-----------------------------------------------------------"""

def fun(x):
    return x**3 - (2*x**2) + (4*x)/3 - (8/27)

def fun2(x,y):
    return x**2+x*y-10

def fun3(x,y):
    return y+3*x*y**2-57

secantXY(fun2, fun3, 1.5, 10, 3.5, 10, 10e-4)
  
    