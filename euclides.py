print("=================Maximo comun divisor=================")

while True:
    try:
        a=int(input("Ingrese el primer número para calcular su Maximo común divisor: "))
        b=int(input("Ingrese el segundo número para calcular su máximo común divisor: "))

        if a>b:
            a=a
            b=b
        else:
            temp=a
            a=b
            b=temp
        
        
        while not(a%b==0):
            b=a%b

        print(f"El maximo comun divisor es: {b}")



    except:

        print("Usted ha digitado un número que no es entero")