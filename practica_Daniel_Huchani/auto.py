#clase padre auto

class Auto():
    def __init__(self,Placa,Marca,Origen):
        self._Placa=Placa
        self._Marca=Marca
        self._Origen=Origen

    
    def __str__(self):
        return "Placa: "+self._Placa+"\nMarca: "+self._Marca+"\nOrigen: "+self._Origen

#auto = Auto("1243SDA","Volvo","Japon")
#print(auto)