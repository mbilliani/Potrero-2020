"""
vacio=input('Ingrese algo: ')
try:
          vacio=int(vacio)
except:
          if vacio == '':
                       input('Presione Enter para continuar...')
          else:
                      print('ERROR! Ingresaste mal un dato, vuelve a intentarlo')
print(vacio)

"""


from juegos import *


while True:
    valor=input('''Bienvenid@s jugadores! Elijan el juego que quieran empezar:

1 - ¡Tira los dados!
2 - Juego del Quince
3 - Piedra, Papel o Tijeras
4 - Piedra, Papel, Tijeras, lagarto o Spock

Ingrese el número de la operación que deseas realizar: ''')
    try:
        valor=int(valor)
        if valor==1:
            print('En breve comienza el juego del dado')
            dado()
        elif valor==2:
            print('En breve comienza el juego del quince')
            quince()
        elif valor==3:
            print('En breve comienza el juego de "Piedra, papel o tijeras".')
            ppt()
        elif valor==4:
            print('En breve comienza el juego de "Piedra, papel, lagarto o spock".')
            pptls()
            break
        else:
            print ('No ingresaste ninguno de los números de los juegos :(')

    except:
            print ('ERROR. OPERACIÓN INVÁLIDA')        
