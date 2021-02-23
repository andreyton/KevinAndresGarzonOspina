import matplotlib.pyplot as plt

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
        iteraciones.append(n)
        n += 1
    print("Tolerancia:" + str(tol))
    print("Solucion Aproximada: {:.20f}".format(x3))
    print("Numero de iteraciones: {:d}".format(n))
    print(" ")

    plt.plot(iteraciones,acum)
    plt.xlabel('Iteaciones')
    plt.ylabel('Error')
    plt.title('METODO DE SECANTE')
    plt.show()