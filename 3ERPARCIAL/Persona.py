class persona:
    def __init__(self,nombre="",apellido="",telefono=0,ci=0,edad=0) :
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.ci=ci
        self.edad=edad
    def añadir(self):
        self.nombre=input("ingrese su nombre:")
        self.apellido=input("ingrese su apellido:")
        self.telefono=int(input("ingrese su telefono:"))
        self.ci=int(input("ingrese su ci:"))
        self.edad=int(input("ingrese su edad:"))
