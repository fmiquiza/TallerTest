
def validar(listaPlaca):
    for caracter in listaPlaca:
        if caracter == '@':
            print(listaPlaca," #Placa Invalida")
        elif caracter == '.':
            print(listaPlaca," #Placa Invalida")
        elif caracter == '#':
            print(listaPlaca," #Placa Invalida")
        elif caracter == ' ':
            print(listaPlaca,"#Placa Valida")
        elif caracter == '-':
            print(listaPlaca,"#Placa Valida")
        
        
def agregar(numPlaca):
    listaPlaca=[]
    for caracter in numPlaca:
        listaPlaca.append(caracter)
    validar(listaPlaca)


def inicio():
    numPlaca=input("ingrese numero de placa: ")
    agregar(numPlaca)
    

inicio()