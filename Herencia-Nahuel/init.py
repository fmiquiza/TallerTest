from Estudiante import Estudiante
from Persona import Persona
class Principal:
    def __init__(self) -> None:
        self.registroPersonas=[]
    def Menu(self):
        print("""
        1.Registrar Persona
        2.Salir
        """)
        opcion=str(input("Ingrese una opcion:"))
        while True:
            if opcion=="1":
                self.Registrar()
            elif opcion=="2":
                break
            else:
                print("ingrese un numero mostrado")   

    def Registrar(self):
        nombre=str(input("Ingrese nombre:"))
        celular=str(input("Ingrese numero celular:"))
        direccion=str(input("Ingrese su direccion:"))
        persona=Persona(nombre,celular,direccion)
        self.registroPersonas.append(persona)
        print(self.registroPersonas)    

persona=Principal()
persona.Menu()