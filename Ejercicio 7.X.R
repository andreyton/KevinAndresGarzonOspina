#Datos---------------------------------------------------------------
f = function(x){
  return(1+sin(exp(3*x)))
}
x = seq(-1, 1, by=0.1)
y = f(x)

#Metodo de simpson -------------------------------------------------
simpson = function(f, a, b, n) {
  Ig = integrate(f,a,b)
  res = Ig$value
  if (n%%2 != 0) stop ("Simpson: n es par!")
  k = (b-a)/n
  x1 = seq(1, n-1, by = 2)
  x2 = seq(2, n-2, by = 2)
  y = f(a+(0:n)*k)
  abs(k/3 * ( f(a) + f(b) + 4*sum (y[x1]) + 2*sum(sum (y [x2]) ) ))
  op = abs(k/3 * ( f(a) + f(b) + 4*sum (y[x1]) + 2*sum (sum (y[x2]) ) ))
  error = abs( res- op)
  cat("Integral metodo de Simpson: ",op, "\n")
  cat("Error metodo de Simpson: ",error, "\n")
}

#Metodo del trapecio ------------------------------------------
trapezoid = function(f, a, b, n) {
  Ig = integrate(f,a,b)
  res = Ig$value
  k = (b-a)/n
  x = seq(a, b, by=k)
  y = f(x)
  s = k * (abs(y[1]/2) + abs( sum(y[2:n])) + abs (y [n+1]/2))
  op = k * (abs(y[1]/2) + abs( sum(y[2:n])) + abs (y [n+1]/2))
  cat(" Integral metodo del trapecio: ",op,"\n")
  error = abs( res - op)
  cat(" Error metodo del trapecio: ",error,"\n")
}

#-----------------------------------------------------
#PRUEBAS
#-----------------------------------------------------
a = -1       
b = 1     
n = 10

trapezoid(f,a,b,n)
simpson(f,a,b,n)

