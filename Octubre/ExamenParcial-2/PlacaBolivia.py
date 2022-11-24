
placasValidas = []
opcion = ""
while opcion.upper() != 'X':
    contLetra = 0
    contNum = 0
    placa = input("Ingrese la placa del vehículo: ")
    if len(placa) == 9:
        for i, item in enumerate(placa):
            if item.isdigit() and (i == 0 or i == 1 or i == 2 or i ==3):
                 contNum += 1
            elif item.isalpha() and (i == 3 or i == 4 or i == 5 or i ==6):
                contLetra += 1
        if (contNum == 4 and contLetra == 3):
            print('Placa válida!')
            placasValidas.append(placa)
        else:
            print('Placa inválida')
    else:
        print("Placa inválida")
 
    opcion = str(input("Presione ENTER para continuar o 'X' para sair:"))

print("### PLACAS VÁLIDAS ENCONTRADAS ###")
for placasCad in placasValidas:
    print(f"Placa:{placasCad}")