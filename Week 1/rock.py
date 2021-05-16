'''Reto 2 - Piedra, papel o tijera

Este es un juego en el que nunca fui bueno, pero eso no significa que hacer un programa sea difícil. 
Escribe un programa que reciba como parámetro “piedra”, “papel”, o “tijera” y determine si ganó el 
jugador 1 o el jugador 2.
Bonus: determina que el ganador sea el jugador que gane 2 de 3 encuentros.
Ejemplo:
ppt(“piedra”, “papel”) ➞ “El ganador es el jugador 2'''


def run():
    print('''El jugador debe escoger entre Piedra  O , Papel __ o Tijeras 8< , puede escribir Pi, Pa o Ti 
    si asi lo prefiere, o escribir la parabra completa, gana el mejor de 3!

    ''')
    a,b = 'áéíóúüÁÉÍÓÚÜ','aeiouuAEIOUU'
    k=1
    v1=0
    v2=0
    
    while k==1:  
        p1= input('Seleccion del Jugador 1:').lower()
        trans = str.maketrans(a,b)
        p1=p1.translate(trans)
        p2= input('Seleccion del Jugador 2:').lower()
        trans = str.maketrans(a,b)
        p2=p2.translate(trans)


        if p1.isalpha() and p2.isalpha():


            if p1 == 'pi' or p1 == 'piedra': 
                if p2 == 'pa' or p2 == 'papel':
                    print('''\nO  __  PAPEL GANA A PIEDRA! \n el juador 2 gana 1 punto\n''') 
                    v2 = v2 +1
                elif p2  == 'ti' or p1 == 'tijera':
                    print('''\nO 8<  PIEDRA GANA A TIJERAS! \n el juador 1 gana 1 punto\n''') 
                    v1 = v1 +1
                
                elif p2  == p1:
                    print('O  O  EMPATE!') 
                
                else:
                    print('''El jugador 2 debe elegir
                                Pi o Piedra: O
                                Pa o Papel: __
                                Ti o Tijera: 8<
                                Vuelvan a intentarlo! ''')                


            if p1 == 'pa'or p1 == 'papel': 
                if p2 == 'pi' or p2 == 'piedra':
                    print('''\n__  O  PAPEL GANA A PIEDRA! \n el juador 1 gana 1 punto\n''') 
                    v1 = v1 +1
                elif p2  == 'ti' or p1 == 'tijera':
                    print('''\n__ 8<  TIJERAS GANA A PAPEL! \n el juador 2 gana 1 punto\n''') 
                    v2 = v2 +1
                elif p2  == p1:
                    print('__  __  EMPATE!') 
                else:
                    print('''El jugador 2 debe elegir
                                Pi o Piedra: O
                                Pa o Papel: __
                                Ti o Tijera: 8<
                                Vuelvan a intentarlo! ''')


            if p1 == 'ti' or p1 == 'tijera': 
                if p2 == 'pa' or p2 == 'papel':
                    print('''\n8<  __  TIJERA GANA A PAPEL! \n el juador 1 gana 1 punto\n''') 
                    v1 = v1 +1
                elif p2  == 'pi' or p1 == 'piedra':
                    print('''\n>8 O  PIEDRA GANA A TIJERAS! \n el juador 2 gana 1 punto\n''') 
                    v2 = v2 +1
                
                elif p2  == p1:
                    print('8< >8  EMPATE!') 
                else:
                    print('''El jugador 2 debe elegir
                                Pi o Piedra: O
                                Pa o Papel: __
                                Ti o Tijera: 8<
                                Vuelvan a intentarlo! ''')
            if v1 == 2:
                print(f'GANA EL JUGADOR 1!!! {v1} a {v2}' )
                k=0

            elif v2 == 2:
                print(f'GANA EL JUGADOR 2!!! {v2} a {v1}')
                k=0

        else:
            print('''
            Error, debes ingresar:
            
            Pi o Piedra: O
            Pa o Papel: __
            Ti o Tijera: 8<
            Vuelvan a intentarlo!

            \n
            ''')


if __name__ == '__main__':
    run()