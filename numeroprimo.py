import math


def primos(n):

    for i in range (2,n-1):
        if n%i==0:
            return False

    return True

try: 
    N=int(input("Digite un numero entero positivo: "))
    if N<0:
        print("Usted ha ingresado un numero negativo")

    
    if primos(N)==True:

        print("Es un números primo")
    else:
        print("Es un número compuesto")


except:

    print("Usted ha ingresado un caracter que no es entero ")
