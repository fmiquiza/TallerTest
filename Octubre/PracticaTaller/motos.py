# el libro puede tener un regalo c
# hacer con sus datos con nombres y heredar de un aclase y ponr valores a la clase 
# o a cada perona


def menu():
    menu="""
    ***MENU DE OPCIONES***
    [1] create
    [2] read
    [3] update
    [4] delete
    [5] salir 
    """
    return menu
def main():
    motos=[]
    while True:
        opciones=int(input(menu()))
        if (opciones==1):
            marca=input("marca: ")
            modelo=input("modelo: ")
            placa=input("placa: ")
            motos=motos(modelo, marca, placa)
            motos.append(motos)
            
        elif(opciones==2):
            count=0
            for i in motos:
                count+=1
                print("--- \n ---", count)

       



#"""class motos():
#    def __init__(self, marca, modelo, placa):
 #       self.marca=marca
 #       self.modelo=modelo
  #      self.placa=placa
#
# def __str__(self):
 #       return"""