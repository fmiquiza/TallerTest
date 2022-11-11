class Persona:
    def __init__(self,nombre ,celular):
        self.nombre=nombre
        self.celular=celular
    
    def getNombre(self):
        return self.nombre
    def getCelular(self):
        return self.celular

    def setNombre(self,nombre):
        self.nombre=nombre 
    def setCelular(self,celular):
        self.celular=celular
