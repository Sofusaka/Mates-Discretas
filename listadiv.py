
listdiv=[1]

try:

    N=int(input("Ingrese un número para calcular sus divisores: "))
    listdiv.append(N)
    A=int((N/2)+1)
    
    for i in range(2, A):
        if N%i==0:
            listdiv.append(i)

    print(f"los divisores de {N} son: {listdiv}")

except:

    print("Usted ha digitado un número que no es entero")