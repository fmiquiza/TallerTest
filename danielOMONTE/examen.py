class Camiseta:
    
    def __init__(self, precio, marca, talla, color):
        self.precio = precio
        self.marca = marca
        self.talla = talla
        self.color = color
        self.rebajada = False



    def teñir(self, color):
        self.color = color


    def infoCamiseta(self):
        info = f"Camiseta:\nTalla: {self.talla}\nPrecio: {self.precio:.2f}€\nMarca: {self.marca}\n"
        return info



camiseta = Camiseta(19.99, "Gucci", "XL", "Negro")
print(camiseta.infoCamiseta())
print(camiseta.infoCamiseta())

print("\n####################\n")
camisetaAdimas = Camiseta(300, "Adimas", "M", "Rojo")
print(camisetaAdimas.color)
print(camisetaAdimas.marca)
camisetaAdimas.teñir("Verde")
print(camisetaAdimas.color)