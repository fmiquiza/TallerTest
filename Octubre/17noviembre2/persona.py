class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre 
        self.apellido=apellido

    def setNombre(self):
        self.nombre=input("Nombre: ")

    def setApellido(self):
        self.apellido=input("Apellido: ")

    def __str__(self):
        return "Nombre: "+self.nombre+"\nApellido: "+self.apellido