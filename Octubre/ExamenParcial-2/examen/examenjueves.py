from funciones import *
#Recibimos la matricula
matricula=input("Introduzca la matricula:\n>> ")
matricula=matricula.upper()

#valores no permitidos y numeros para verificar
noPermitidos=['#','@','.']
numeros=['1','2','3','4','5','6','7','8','9','0']

#Verificamos que la matricula no sobrepase los 8 caracteres
numeroCaracteres(matricula)

#Verificamos que la matricula empiece con un numero
empiezaConNumero(matricula,numeros)

#Verificamos que por lo menos los 3 primeros valores sean numeros
tresPrimerosNumeros(matricula,numeros)
    
#Por ultimo revisamos si la matricula no contiene valores no permitidos
valoresInvalidos(matricula,noPermitidos)

#Comprobamos que no hay más de 4 numeros en la matricula
noMasDe4Numeros(matricula,numeros)
print('Matricula Correcta')