#def quince():
import random

print("Bienvenid@s al juego del quince")

cartas=[1,2,3,4,5,6,7,8,9,10]
pierde=15


p1=input("Ingrese el nombre del jugador 1: ")
p2=input("Ingrese el nombre del jugador 2: ")


juega_otra_vez = 'si'

while juega_otra_vez != 'no' and juega_otra_vez != 'n':
    print("\nMezclando las cartas...\nRepartiendo las cartas...\n")

    j1 = random.sample(cartas,3)
    j2 = random.sample(cartas,3)
    print("\n{} sacó {} \ny {} sacó {}".format(p1,j1,p2,j2))
    pj1 = 0
    pj2 = 0
    pj1 += sum(j1)
    pj2 += sum(j2)
    
    if pj1 == pj2:
        print("{} sacó {}, que son {}, y {} sacó {} que son {}, por lo tanto esto es ¡EMPATE!".format(p1,j1,pj1,p2,j2,pj2))
    elif pj1 >= pierde:
        print("{} sacó {}, más de 15 en total, ¡{} perdiste!".format(p1,pj1,p1))
    elif pj2 >= pierde:
        print("{} sacó más de 15 en total, ¡{} perdiste!".format(p2,pj2,p2))
    elif pj1 > pj2:
        print("{} sacó {} con total de {}, y {} sacó {} con total de {}, ¡{} ganaste!".format(p1,j1,pj1,p2,j2,pj2,p1))
    else:
        print("{} sacó {} con total de {}, y {} sacó {} con total de {}, ¡{} ganaste!".format(p1,j1,pj1,p2,j2,pj2,p2))
    juega_otra_vez=input("Barajamos las cartas otra vez? ")


#while i <= 3:
#player1card.append(random.randint(1,10))
#player2card.append(random.randint(1,10))
#i = i + 1

#for i in player1card:
#suma = i + suma
