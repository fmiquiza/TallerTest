input =("ingrese numero de Placas"):
      contador=0
    valores="."
    valoresArro="@"
    valoresNum="#"
    numeroPlaca=str(input("Ingrese el numero de placa:"))
    for i in numeroPlaca:
        contador+=1
    for i in numeroPlaca:
        if i == valores or i==valoresArro or i ==valoresNum:
            print("numero no valido por signo")
    if contador >=5:
        print("ese numero no es valido")

Placas()
