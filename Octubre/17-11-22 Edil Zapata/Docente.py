from Estudiante import * 
class Docente(Estudiante):
    def __init__(self,nombre="",apellido="",edad=0,profesion=""):
        super().__init__(nombre,apellido,edad)
        self.profesion=profesion
    def getProfesion(self):
        return self.profesion
    def __str__(self):
        return super().__str__()+"\nProfesion"+self.profesion