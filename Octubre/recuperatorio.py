class Estudiante :
    def __init__(self):
        self.__nombre = ""
        self.__direccion = ""
        self.__matricula = ""
        self.__telefono = ""
        self.__listaMateria = []
        
    def Name (self,nombre):
        self.__nombre = nombre

    def setDireccion (self,direccion):
        self.__direccion = direccion

    def setMatricula (self,matricula):
        self.__matricula = matricula

    def setTelefono (self,telefono):
        self.__telefono = telefono

    def setMateria (self,materia):
        self.__listaMateria.append(materia)

    def mostrarDatosPersonales (self):
        print("Nombre: ",self.__nombre)
        print("Dirección: ",self.__direccion)
        print("Matrícula: ",self.__matricula)
        print("Teléfono: ",self.__telefono)

    def mostrarMaterias (self):
        for materia in self.__listaMateria :
            print("Nombre de la Materia: ",materia.getNombre())
            print("Docente de la Materia: ",materia.getDocente())
            print("Horario de la Materia: ",materia.getHorario())