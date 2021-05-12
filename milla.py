'''Reto 3 - Conversor de millas a kilómetros

Imagina que quieres calcular los kilómetros que son cierta cantidad de millas. 
Para no estar repitiendo este cálculo escribe un programa en que el usuario indique una cantidad de millas 
y en pantalla se muestre el resultado convertido a kilómetros.
Toma en cuenta que en cada milla hay 1.609344 Km
Bonus: haz que el usuario pueda escoger entre convertir millas a kilómetros o kilómetros a millas.'''

import os
def mtokm():
        millas = float(input("Ingresa las Millas a convertir: "))
        kilometros = millas/1.609344
        print(f'{millas} Millas son equivalentes a {round(kilometros, 4)} Km')

def kmtom():
    kilometros = float(input("Ingresa los Kilometros a convertir: "))
    millas = kilometros*1.609344
    print(f'{kilometros} Km son equivalentes a {round(millas, 4)} Millas')


def run():
    print('''\nBienvenido al conversor Milla/Kilometro, puedes elegir una de las 2 opciones:''')
    salir = False
    while not salir:
        
        print('''\n
 1. De Millas a Kilometros.\n
 2. De Kilometros a Millas.\n
''')
        opcion = int(input("Elige una opcion:"))

        if opcion == 1:
            mtokm()
            salir = True
        elif opcion == 2:
            kmtom()
            salir = True
        else:
            os.system ("cls")
            print('Debes escoger una opcion valida!\n' )
    
if __name__ == '__main__':
    run()
