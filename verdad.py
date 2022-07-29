


checklist1=[]
bool=[True,False]


##Función ejercicio 50
def funcion1():
    a=not(not p or q)or r
    return a

def funcion2():
    b=not p or (not q or r)
    return b

###############################
##Funcion ejercicio 51
def funcion3():
     c=(not s or (p and not r))and ((not p or (r or q))and s)
     return c
def funcion4():
    d=p or t
    return d

    
print("------"*4) 
print("TABLAS DE CONJUNCIÓN")
print("------"*4) 
print("P\tQ\tP y Q")
print("------"*4)  
for p in bool:
    for q in bool:
        print(p,q,p and q, sep="\t")
   
print("------"*4) 
print("  ")
######################################
print("------"*4) 
print("TABLAS DE DISYUNCIÓN")
print("------"*4) 
print("P\tQ\tP o Q")
print("------"*4)  
for p in bool:
    for q in bool:
        print(p,q,p or q, sep="\t")
        
print("------"*6) 
######################################
print("------"*6) 
print("TABLA CONDICIONAL")
print("------"*6) 
print("P\tQ\tP entonces Q")
print("------"*6)  
for p in bool:
    for q in bool:
        print(p,q,not p or q, sep="\t")
        
print("------"*6) 



######################################
print("------"*6) 
print("TABLA BIDIMENSIONAL")
print("------"*6) 
print("P\tQ\tP si y solo si Q")
print("------"*6)  
for p in bool:
    for q in bool:
        print(p,q,(not p or q)and(not q or p), sep="\t")
        
print("------"*6) 
######################################

print("------"*6) 
print("===============EJERCICIO 50===============")
print("------"*6) 
print("P\tQ\tR\tEQUIVALENCIA")
print("------"*6)  
for p in bool:
    for q in bool:
        for r in bool:
           eq1=(not funcion1() or funcion2()) and (not funcion2() or funcion1())
           print(p,q,r,eq1, sep="\t")
           checklist1.append(eq1)

print("------"*6) 
if checklist1.count(False)>0:
            print("NO es una tautología")
else:
            print("Es una tautología")


checklist1.clear()
print("------"*9) 
print("====================EJERCICIO 51=====================")
print("------"*9) 
print("P\tQ\tR\tS\tT\tEQUIVALENCIA")
print("------"*9)  
for p in bool:
    for q in bool:
        for r in bool:
            for s in bool:
                for t in bool:
                    eq2=(not funcion3() or funcion4()) and (not funcion4() or funcion3())
                    print(p,q,r,s,t,eq2, sep="\t")
                    checklist1.append(eq2)

print("------"*9) 
if checklist1.count(False)>0:
            print("NO es una tautología")
else:
            print("Es una tautología")


