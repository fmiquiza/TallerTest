from persona import Persona

class Estudiante():
    def __init__(self,persona,colegio,curso,materias):
        self.colegio=colegio
        self.curso=curso
        self.materias=materias
    
    def super__init__(self,nombre,apellido,persona,colegio,curso,materias):
        self.nombre=nombre
        self.apellido=apellido

    def setColegio(self):
        self.colegio=input("Colegio: ")
    
    def setCurso(self):
        self.curso=input("Curso: ")

    def setMaterias(self):
        self.materias=input("Materias: ")

    def __str__(self):
        return "\nColegio: "+self.colegio+"\nCurso: "+self.curso+"\nMaterias: "+self.materias