
numero = int(input("Ingrese Numero: "))
listanum = []
for fila in range(numero):
    listanum.append(f"{fila*10+10}")

for fila in range(numero):
    print(" ".join(listanum))
    listanum.pop()