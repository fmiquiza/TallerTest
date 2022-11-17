from auto import Auto

class Volqueta(Auto):
    def __init__(self,color,capacidad,Placa,Marca,Origen):
        super().__init__(Placa,Marca,Origen)
        self._color=color
        self._capacidad=capacidad
        self._placa=Marca
        self._marca=Marca
        self._origen=Origen

    def __str__(self):
        return "color:"

