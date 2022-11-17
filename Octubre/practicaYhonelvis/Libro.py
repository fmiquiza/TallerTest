class Libro:
    def __init__(self,Autor,Editorial,N_paginas=0,):
        self._autor=Autor
        self._editoria=Editorial
        self._Npaginas=N_paginas
    
    def __str__(self):
        return "Autor: "+ self._autor+"\nEditorial: "+self._editoria+"\nN_paginas: "+ str(self._Npaginas)