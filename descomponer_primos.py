#Descomponer un numero en factores primos





print("====================Descomponer números en factores primos====================")


factor=[]
cont='1'
while cont=='1':
    factor.clear()
    n=int(input("Ingrese un número para calcular sus factores primos: "))
    for i in range (2,n+1):
        while n%i==0:
            factor.append(i)
            n=n/i
    print(factor)    
    cont=input("========================Desea ingresar otro número? Escriba el número correspondiente:======================== \n1.Sí\n2.No\n")
    

print("El programa ha finalizado.")  

