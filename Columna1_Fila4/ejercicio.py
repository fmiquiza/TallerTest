lista1=[]
contador=3
while contador>0:
    numero=int(input("ingrese un numero: "))
    for num in range(1,numero+1):
        lista1.append(num)
        print(lista1)
        numero-=numero
    contador-=contador
        

