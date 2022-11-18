from Persona import *
class Estudiante(Persona):
    def __init__(self, nombre, celular, direccion):
        super().__init__(nombre, celular, direccion)
    
    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self,direccion):
        self.direccion=direccion