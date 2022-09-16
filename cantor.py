from re import I


print("=======================Algoritmo de Cantor========================")
n=1

try:

    while n!=0:
        n=int(input("\nIngrese un número para calcular su descomposición factorial:"))
        k=n
        i=2
        listres=[]
        listi=[1]
        while(i<=n):
            n1=n%i
            n=n//i
            
            
            listres.append(n1)
            listi.append(i)
            i+=1
        
        listres.append(n)


        print(f"la expansión de Cantor del entero {k} es: ")
        for m in range (len(listi)):
            if m in range (0,len(listi)-1):

                print(f"{listi[m]}!({listres[m]})", end="+")
            else:
                print(f"{listi[m]}!({listres[m]})", end="")
    
except:
    print("Por favor, ingrese numeros enteros.")
