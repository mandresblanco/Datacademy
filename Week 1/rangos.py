'''Reto 5 - Rangos cambiantes

Para este reto final juguemos con números. En tu programa pide al usuario ingresar 3 números: 
un límite inferior, un límite superior y uno de comparación.
Si tu número de comparación se encuentra en el rango de los dos límites, imprímelo en pantalla.
En caso de estar por debajo del inferior o arriba del superior, también muéstralo en pantalla y 
pide ingresar otro número para repetir el proceso.'''

import os

def run():
    print('''\nJuguemos con numeros, debes ingresar 3 nummeros:''')

    salir = False
    os.system ("cls")
    Inferior = float(input("Limite Inferior:"))
    Superior = float(input("Limite Superior:"))
    
    if Inferior<Superior:
    
        while not salir:
            

            Comparacion = float(input("Numero de Comparacion:"))
            

            if Comparacion >= Inferior and Comparacion <= Superior:
                print(f'{Comparacion} se encuentra entre {Inferior} y {Superior}.')
                salir =True
            elif Comparacion<Inferior:
                os.system ("cls")
                print('Vuelve a ingresar un valor!\n' )
                print(f'{Comparacion} Se encuentra por debajo del limite inferior {Inferior}')
                # salir = True
            elif Comparacion>Superior:
                os.system ("cls")
                print(f'{Comparacion} Se encuentra por arriba del limite superior {Superior}')
                print('Vuelve a ingresar un valor!\n' )
            

    else:
            print('''\nEl valor del limite inferior debe ser menor que el del limite superior!! \n
Si es que esto es un juego, entonces perdiste.
                ಥ_ಥ''')

if __name__ == '__main__':
    run()