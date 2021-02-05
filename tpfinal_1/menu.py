"""
vacio=input('Ingrese algo: ')
try:
            vacio=int(vacio)
except:
            if vacio== '':
                      input('Presione Enter para continuar...')
            else:
                      print('ERROR! Ingresaste letras, vuelve a intentarlo')
print(vacio)              

"""


from funciones import *

while True:
        valor=input('''¡Bienvenid@! Lea atentamente las opciones a realizar.
1 - Suma
2 - Resta
3 - Multiplicación
4 - División
5 - Potencia
6 - Raíz
0 - Finalizar

Ingrese el número de la operación que desea realizar: ''')
        try:
                valor=int(valor)
                if valor==1:
                           print ('En breve se ejecutará la Suma')
                           suma()
                elif valor==2:
                           print ('En breve se ejecutará la Resta')
                           resta(lista, n)
                elif valor==3:
                           print ('En breve se ejecutará la Multiplicación')
                           multiplicacion()
                elif valor==4:
                           print ('En breve se ejecutará la División')
                           division()
                elif valor==5:
                           print ('En breve se ejecutará la Potenciación')
                           potencia()
                elif valor==6:
                           print ('En breve se ejecutará la Raíz')
                           raiz()
                elif valor==0:
                           print ('Finalizaste la elección')
                           break
                else:
                           print('No ingresaste ninguno de los números de operación válido. El número que ingreses debe estar entre el 1 y el 6.')

        except:
                print('Error. Operación inválida.')
