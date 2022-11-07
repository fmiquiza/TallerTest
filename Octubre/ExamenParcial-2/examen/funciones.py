def numeroCaracteres(matricula):
    numeroCaracteres=len(matricula)
    if numeroCaracteres > 8:
        print('La matricula es más larga de lo permitido.')
        exit()

def empiezaConNumero(matricula,numeros):
    if matricula[0] in numeros:
        pass
    else:
        print("La matrícula empieza con un valor inválido.")
        exit()

def tresPrimerosNumeros(matricula,numeros):
    if matricula[1] in numeros and matricula[2] in numeros:
        pass
    else:
        print('La matrícula debe iniciar con 3 números.')
        exit()
        
def valoresInvalidos(matricula,noPermitidos):
    for i in noPermitidos:
        if i in matricula:
            print("Valor no permitido en la matricula.")
            exit()
        else:
            pass

def noMasDe4Numeros(matricula,numeros):
    contador=0
    for i in matricula:
        if i in numeros:
            contador+=1
            if contador >= 5:
                print('La matricula solo puede tener 4 numeros.')
                exit()
            else:
                pass