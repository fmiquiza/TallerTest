#Integrantes: Juan Carlos Sandy, Wendy Velarde, Limbert Tola
#Ejercicio 1 Columna 1

numero = int(input("Ingrese Numero: "))
listanum = []
for fila in range(numero):
    listanum.append(fila + 1)


for fila in range(numero):
    print(listanum)
    listanum.pop()