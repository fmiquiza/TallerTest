#Ejercicio media piramire acendente
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
nroDeFilasPorTeclado = int(input("Ingrese un valor deseada:\n "))

for cadaFila in range(nroDeFilasPorTeclado, 0, -1):
    for cadaColumna in range(1, cadaFila+1):
        print(cadaColumna, end="*_*")
    
    print("\n")
