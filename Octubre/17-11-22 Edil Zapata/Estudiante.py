class Estudiante:
    def __init__(self,nombre="",apellido="",edad=0):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def getNombre(self):
        return self.nombreMateria
    def getApellido(self):
        return self.docente
    def getEdad(self):
        return self.anio
    def __str__(self) -> str:
        return "Nombre: "+self.nombre+ "\nApellido: "+self.apellido+"\nEdad: "+str(self.edad)