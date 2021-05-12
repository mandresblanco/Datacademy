'''Reto 1 - Área de un triángulo

Es momento de poner ese conocimiento a la práctica. El área de un triángulo se 
describe de la siguiente manera: 
A = (b * h) / 2 .
Escribe un programa que tome la base y la altura como parámetros y calcule el 
área del triángulo.
Bonus: el programa debe determinar si el triángulo es isósceles, equilátero o escaleno.'''

import os

def tipo(a, b , c):
    if a == b or a == c or c == b:
        if a == b and a == c:
            print('\n'+'El triangulo es Equilatero')
        else:
            print('\n'+'El triangulo es Isoseles')
    else:
        print('\n'+'El triangulo es Escaleno')

def area(b,h):
    a = b*h/2
    print('\n','El area del triangulo es:', a)



k=1

def run():
    
    k=1
    while k==1:
        
        m = int(input('''Selecciona una opcion:
        1. Calcular Area de triangulo ingresando su base y altura:
        2. Determinar el tipo de triangulo ingresando sus lados:
        '''
        ))

        if m == 1:
            b = float(input('Ingresa la Base del triangulo: '))
            h = float(input('Ingresa la Altura del triangulo: '))
           
            if b and h >0:
                area(b,h)
                k=0
            else:
                os.system ("cls")
                print('Todos los valores deben ser positivos!!!'+'\n')

        elif m==2:

            a = float(input('Ingresa el valor del lado A del triangulo: '))
            b = float(input('Ingresa el valor del lado B del triangulo:'))
            c = float(input('Ingresa el valor del lado C del triangulo:'))
            if b and h and c > 0:
                area(b,h)
                k=0
                tipo(a, b, c)
            else:
                os.system ("cls")
                print('Todos los valores deben ser positivos!!!'+'\n')
            

        else:
            os.system ("cls")
            print('Debes elegir 1 o 2!!!!'+'\n')
            # break                        
        
if __name__ == '__main__':
    run()