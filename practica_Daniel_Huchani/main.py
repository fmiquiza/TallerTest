#
# Daniel Huchani Huaranca
#

from auto import Auto
from volqueta import Volqueta
def menu():
    menu="""
    <<<------CRUD------>>>
    [1] CREATE
    [2] READ
    [3] UPDATE
    [4] DELETE
    [0] SALIR
>>:"""
    return menu

def main():
    autos = []
    while True:
        opcion= int(input(menu()))
        if(opcion==1):
            placa=input("placa: ")
            marca=input("marca: ")
            origen=input("origen: ")
            auto= Auto(placa,marca,origen)
            autos.append(auto)

        elif(opcion==2):
            count=0
            for i in autos:
                count+=1
                print("\n---> Auto#",count," <---")
                print(i)
                print("+-------------------+")
        elif(opcion==3):
            pass
        elif(opcion==4):
            pass
        elif(opcion==0):
            break
        else:
            print("Opcion no disponible..!")

if __name__=="__main__":
    main()