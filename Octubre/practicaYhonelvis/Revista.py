from Libro import *
class Revista(Libro):
    def __init__(self, Autor, Editorial, N_paginas=0, Portada=""):
        super().__init__(Autor, Editorial, N_paginas)
        self._Portada=Portada
    def __str__(self):
        return super().__str__()+"\nportada: "+ self._Portada