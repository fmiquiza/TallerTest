from Persona import *
class principal(persona):
    def __init__(self, nombre="", apellido="", telefono=0, ci=0, edad=0):
        super().__init__(nombre, apellido, telefono, ci, edad)
    def menu(self):
        opcion=0
        while opcion!= 0:
            print("""1.Añadir cliente:"
                 2.Editar cliente
                 3.eliminar cliente""")
            opcion=input(">>>")
            if opcion==1:
                añadir()
    menu()
                
                
        







    


            