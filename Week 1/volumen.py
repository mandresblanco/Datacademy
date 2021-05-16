'''Reto 4 - Calculadora de volúmenes
Sigamos con matemáticas elementales para no perder la costumbre y retar nuestras habilidades. 
Escribe un programa donde apliques las diferentes fórmulas matemáticas para calcular el volumen 
de un cilindro.
Recuerda que la base del cilindro es un círculo y necesitarás calcular su área. Aplica las fórmulas 
en tu programa recibiendo datos como altura y radio.
Bonus: agrega otras figuras geométricas a tu programa y que el usuario pueda escoger cuál calcular.'''

import os
def Cubo():
        Arista = float(input("Ingresa el valor de la Arista: "))
        Volumen = Arista**3
        print(f'El volumen del cubo es {round(Volumen, 4)}')

def Ortoedro():
    Altura = float(input("Ingresa la Altura: "))
    Ancho = float(input("Ingresa el Ancho: "))
    Largo = float(input("Ingresa el Largo: "))
    Volumen = Altura*Ancho*Largo
    print(f'El volumen del Ortoedro es{round(Volumen, 4)}')
def Cilindro():
    radio = float(input("Ingresa el Radio: "))
    altura = float(input("Ingresa la altura: "))
    Volumen = 3.141592*altura*radio**2
    print(f'El volumen del Cilindro es  {round(Volumen, 4)}')

def Cono():
    radio = float(input("Ingresa el Radio: "))
    altura = float(input("Ingresa la altura: "))
    Volumen = (3.141592*altura*radio**2)/3
    print(f'El volumen del Cono es  {round(Volumen, 4)}')

def Esfera():
    radio = float(input("Ingresa el Radio: "))
    Volumen = (3.141592*4*radio**3)/3
    print(f'El volumen del Esfera es  {round(Volumen, 4)}')

def run():
    os.system ("cls")
    print('''\nBienvenido al Calculador de Volumen 10000, seleccione una figura:''')
    salir = False

    while not salir:
        
        print('''\n
    1. Cubo.\n
    2. Ortoedro.\n
    3. Cilindro.\n
    4. Cono.\n
    5. Esfera.\n
    ''')

        opcion = int(input("Elige una opcion:"))

        if opcion == 1:
            Cubo()
            salir = True
        elif opcion == 2:
            Ortoedro()
            salir = True
        elif opcion == 3:
            Cilindro()
            salir = True
        elif opcion == 4:
            Cono()
            salir = True
        elif opcion == 5:
            Esfera()
            salir = True
        else:
            os.system ("cls")
            print('\nDebes escoger una opcion valida!\n' )
    
if __name__ == '__main__':
    run()