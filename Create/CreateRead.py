#Estudiante Pablo Sebastian Guerrero Quisbert
class Persona:
    def __init__(self):
        self.nombre = ''
        self.apellido = ''
        self.edad = 0
        self.genero = ''
        self.altura = ''
        self.peso = ''
    
    def definirAtributos(self):
        self.nombre = str(input("Ingrese nombre: "))
        self.apellido = str(input("Ingresar apellido: "))
        self.edad = int(input("Ingresar edad: "))
        self.genero = str(input("Ingrese genero: "))
        self.altura = float(input("Ingrese altura: "))
        self.peso = float(input("Ingrese el peso: "))

    def __str__(self):
        return "\nNombre: "+self.nombre+"\nApellido: "+self.apellido+"\nEdad: "+str(self.edad)+"\nGenero: "+self.genero+"\nAltura: "+str(self.altura)+"\nPeso: "+str(self.peso)

class Estudiante(Persona):
    def __init__(self):
        self.estudianteID = ''
        self.colegio = ''
        self.curso = ''
        self.promedio = 0
        self.gestion = 0
    
    def definirEstudiante(self):
        Persona.definirAtributos(self)
        self.estudianteID = str(input("Estudiante ID: "))
        self.colegio = str(input("Colegio: "))
        self.curso = str(input("Curso: "))
        self.peromedio = str(input("Promedio: "))
        self.gestion = str(input("Gestion: "))

    
estudiante = Estudiante()
estudiante.definirEstudiante()
