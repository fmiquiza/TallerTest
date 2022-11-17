def opciones():
    print('agenda de contanctos')
    print('*'*50)
    print('selecciona una opcion')
    print('[C]rear contacto')
    print('[L]ista de contacto')
    print('[M]odificar contacto')
    print('[E]liminar contacto')
    print('[B]uscar contacto')
    print('[salir]')
def run():
    opciones()
    command=input()
    command=command.upper()
    