def suma():
        n=[]
        resultado=0
        while True:
                num=input('Ingrese un número (para finalizar la función presione "ENTER"): ')
                try:
                    num=int(num)
                    n.append(num)
                    print(n)
                except:
                        if num=='':
                            for x in n:
                                    resultado+=x
                            print(resultado)
                            return
                        else:
                                input('ERROR, presione "ENTER" para continuar')
def resta(lista, n):
        if lista == [] :
                return n
        else:
                return restar(lista[1:], n) - lista[0]

        lista=[1,2,3,4,5]
        print(restar(lista, 100))




#        n=[]
#        n2=[]
#        while True:
#                num=input('Ingrese un número (para finalizar la función presione "ENTER"): ')
#                try:
#                    num=int(num)
#                    n.append(num)
#                    print(n)
#                except:
#                        if num=='':
#                            for x in n:
#                                    return restar(n[1:], n2)-n[0]
#                            print(resultado)
#                            return
#                        else:
#                                input('ERROR, presione "ENTER" para continuar')        
def multiplicacion():
          n=[]
          resultado=1
          while True:
                num=input('Ingrese un número (para finalizar la función presione "ENTER"): ')
                try:
                    num=int(num)
                    n.append(num)
                    print(n)
                except:
                        if num=='':
                            for x in n:
                                    resultado*=x
                            print (resultado)
                            return
                        else:
                                input('ERROR, presione ENTER para continuar')

def division():
        n1=int(input('Ingrese su primer número(cuando finalice presione "ENTER"): '))
        n2=int(input('Ingrese su segundo número (cuando finalice presione "ENTER"): '))

        if n2 != 0:

                d = n1 / n2
                print(d)
                return
        else:
                print('Ingresaste un 0(cero) y no se puede dividir por 0 :(')

def potencia():
        n1=int(input('Ingrese su primer número(cuando finalice presione "ENTER"): '))
        n2=int(input('Ingrese su segundo número(cuando finalice presione "ENTER"): '))

        if n2 != 0:
                d = n1 ** n2
                print (d)
                return
        elif n2 == 0:
                print('Ingresaste un 0(cero) y cualquier número elevado a la cero será 1(uno).')
        else:
                print('ERROR. Intentalo nuevamente')

def raiz():
        n1=int(input('Ingrese su primer número(cuando finalice presione "ENTER"): '))
        n2=int(input('Ingrese el número de la raíz(cuando finalice presione "ENTER"): '))

        if n2 != 0:
                r = n1 ** (1/n2)
                print (r)
                return
        elif n1 == 0:
                print('Ingresaste un 0(cero) y la raíz de este número es él mismo')
        else:
                print('ERROR. Intentalo nuevamente')
