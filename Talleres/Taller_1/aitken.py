def Delta2_Aitken(f,g,x1,tol,NO):
        q=[]
        X=[]
        X.append(x1)
        X.append(g(X[0]))
        X.append(g(X[1]))
        i=1
        while i<=NO:
            q.append(X[i+1]-((X[i+1]-X[i])*2/(X[i+1]-2X[i]+X[i])))
            X.append(g(X[i+1]))
            print('%8.4f\t %8.4f\t %8.4f\t %8.4f\t %8.4f\n',X[i],f(X[i]),q[i-1],f(q[i-1]),g(X[i]))
            if i>=2:
                if  abs(q[i-1]-q[i-2])<tol:
                    print('\nq(%2d)= %8.4f\nf(%8.4f)=%8.4f \n' ,i,q[i-1],q[i-1],f(q[i-1]))
                    print('\nProcedimiento terminado satisfactoriamente\n')
                    return
            i=i+1
        print('\nEl metodo fracaso despúes de '+ str(NO))
        print('\nProcedimiento terminado sin exito')