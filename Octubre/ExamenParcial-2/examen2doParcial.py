def verificacionPlaca(placa):
    listaPlaca = []
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    verificacion = True

    if len(placa) <= 8 and len(placa) >= 3:
        for i in placa:
            listaPlaca.append(i)

        for i in range(0,3):
            if listaPlaca[i] not in numeros:
                verificacion = False

        if listaPlaca[3] not in numeros:
            if (listaPlaca[3] == ' ' or listaPlaca[3] == '-' or listaPlaca[3] in letras):
                for i in range(4, len(listaPlaca)):
                    if listaPlaca[i] not in letras:
                        verificacion = False
            else:
                verificacion = False

        elif listaPlaca[4] not in numeros:
            if (listaPlaca[4] == ' ' or listaPlaca[4] == '-' or listaPlaca[4] in letras):
                for i in range(5, len(listaPlaca)):
                    if listaPlaca[i] not in letras:
                        verificacion = False
            else:
                verificacion = False
    else:
        return "Longitud de la placa invalida"
    
    if verificacion:
        return 'Placa valida'
    else:
        return 'Placa invalida'

placa = input("Ingrese la placa: ").upper()
print(placa)
print(verificacionPlaca(placa))