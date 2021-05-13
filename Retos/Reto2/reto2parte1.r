library(pracma)
library(readxl)

#Made by Oscar Pacheco, Julian Carrillo, Cristian Contreras, Jenifer Medina, Kevin Garzón

temperaturas1 = read_excel("C:/Users/oscar/datos.xls", sheet = "Itatira")

x = seq(1,length(temperaturas1$`Temp. Interna (ºC)`),1)
y = temperaturas1$`Temp. Interna (ºC)`

plot(x,y, type = "line", main = "Datos iniciales", ylab = "Temperatura", xlab = "Indice")

set.seed(0)
selected = rep(1, 720)
eliminate = sample.int(720,720*0.35)
for (e in eliminate) {
  selected[e] = 0
}


newX = c()
newY = c()

j = 1
i = 1


for (o in selected)
{
  if(o == 1)
  {
    newX[i] = x[j]
    newY[i] = y[j]
    i = i + 1
  }
  j = j +1
}


set1 = spline(newX, newY)
funSet1 = splinefun(newX, newY)

plot(x,y, type = "line", main = "Spline", ylab = "Temperatura", xlab = "Indice")
lines(set1, col = "sienna2")

set2 = approx(newX, newY, method = "linear", n = length(newX))
funSet2 = approxfun(newX, newY)

plot(x,y, type = "line", main = "Approx", ylab = "Temperatura", xlab = "Indice")
lines(set2, col = "maroon4")

plot(x,y, type = "line", main = "Splines y Approx", ylab = "Temperatura", xlab = "Indice")
lines(set1, col = "sienna2")
lines(set2, col = "maroon4")


errorSpline = c()
errorInter = c()
errorComb = c()

comb = c()

k = 1

for(var in x)
{
  comb[k] = (funSet1(var) + funSet2(var))/2
  
  errorComb[k] = round(abs(abs((y[k] - comb[k])/y[k])),2)
  errorInter[k] = round(abs((y[k] - funSet2(var))/y[k]),2)
  errorSpline[k] = round(abs((y[k] - funSet1(var))/y[k]),2)
  
  k = k + 1
}

plot(x,y, type = "line", main = "Combinación splines y approx", ylab = "Temperatura", xlab = "Indice ideal")
lines(x, comb, col = "orange")


#print(errorSpline)
#print(errorInter)
#print(errorComb)




cat("VALIDACIÓN CRUZADA")

errorComb[0] = 0
errorComb[1] = 0
errorComb[2] = 0
cat("Con el uso combinado")
cat("Error minimo: (para valores distintos de cero)", min(errorComb[errorComb>0]))
cat("Error medio: (para valores distintos de cero)", median(errorComb[errorComb>0]))
cat("Error maximo: ", max(errorComb))
cat("Cantidad de errores: ", sum(errorComb != 0))
cat("Indice de Jaccard: ", round(sum(errorComb == 0)/ length(x), 4))


errorInter[0] = 0
errorInter[1] = 0
errorInter[2] = 0
cat("Con el uso de la funcion approx") 
cat("Error minimo: (para valores distintos de cero)", min(errorInter[errorInter>0]))
cat("Error medio: (para valores distintos de cero)", median(errorInter[errorInter>0]))
cat("Error maximo: ", max(errorInter))
cat("Cantidad de errores: ", sum(errorInter != 0))
cat("Indice de Jaccard: ", round(sum(errorInter == 0)/ length(x), 4))


cat("Con el uso de la funcion spline")
cat("Error minimo: (para valores distintos de cero)", min(errorSpline[errorSpline>0]))
cat("Error medio: (para valores distintos de cero)", median(errorSpline[errorSpline>0]))
cat("Error maximo: ", max(errorSpline))
cat("Cantidad de errores: ", sum(errorSpline != 0))
cat("Indice de Jaccard: ", round(sum(errorSpline == 0)/ length(x), 4))