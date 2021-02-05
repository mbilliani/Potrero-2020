def dado():
    import random

    print("Bienvenid@s al juego del dado")

    dado=[1,2,3,4,5,6]

    p1=input("Ingrese el nombre del jugador 1: ")
    p2=input("Ingrese el nombre del jugador 2: ")


    juega_otra_vez = "si"

    while True:
        juega_otra_vez == "si" or juega_otra_vez == "s"
        print("\nTirando los dados...\n Los números son...")

        j1 = random.choice (dado)
        j2 = random.choice (dado)

        if j1 == j2:
            print("{} sacó {} y {} sacó {}, por lo tanto esto es ¡EMPATE!".format(p1,j1,p2,j2))
        elif j1 > j2:
            print("{} sacó {} y {} sacó {}, ¡{} ganaste!".format(p1,j1,p2,j2,p1))
            return
        else:
            print("{} sacó {} y {} sacó {}, ¡{} ganaste!".format(p1,j1,p2,j2,p2))

        
        juega_otra_vez=input("Tira los dados otra vez?")

def quince():
    import random

    print("Bienvenid@s al juego del quince")

    cartas=[1,2,3,4,5,6,7,8,9,10]
    pierde=[15]


    p1=input("Ingrese el nombre del jugador 1: ")
    p2=input("Ingrese el nombre del jugador 2: ")


    juega_otra_vez = "si"

    while True:
        juega_otra_vez == "si" or juega_otra_vez == "s"
        print("\nMezclando las cartas... \n    Repartiendo las cartas...\n")

        j1 = random.sample(cartas,3)
        j2 = random.sample(cartas,3)
        print("\n{} sacó {} \ny {} sacó {}".format(p1,j1,p2,j2))

        if j1 == j2:
            print("{} sacó {} y {} sacó {}, por lo tanto esto es ¡EMPATE!".format(p1,j1,p2,j2))
        elif j1 >= pierde:
            print("{} sacó más de 15 en total, ¡{} perdiste!".format(p1,p1))
        elif j2 >= pierde:
            print("{} sacó más de 15 en total, ¡{} perdiste!".format(p2,p2))
        elif j1 > j2:
            print("{} sacó {} y {} sacó {}, ¡{} ganaste!".format(p1,j1,p2,j2,p1))
            return
        else:
            print("{} sacó {} y {} sacó {}, ¡{} ganaste!".format(p1,j1,p2,j2,p2))
  
        
        juega_otra_vez=input("Barajamos las cartas otra vez?")


#while i <= 3:
#player1card.append(random.randint(1,10))
#player2card.append(random.randint(1,10))
#i = i + 1

#for i in player1card:
#suma = i + suma


def ppt():
    import random

    print("Bienvenid@s al juego de 'Piedra, Papel o Tijera'")

    op = ["piedra", "papel", "tijeras"]

    juega_otra_vez = "si"

    while True:
        juega_otra_vez == "si" or juega_otra_vez == "s"
        p1 = input("Escriba el nombre del jugador 1: ")
        p2 = input("Escriba el nombre del jugador 2: ")
    
        j1 = random.choice(op)
        j2 = random.choice (op)

        print("\n Piedra... \n  Papel... \n   o Tijera... \n \nEl respultado es...")
    
        if j1 == j2:
            print("empate, ambos eligieron {}".format(j1))
        elif j1 == "piedra" and j2 == "tijeras":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "tijeras" and j2 == "papel":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "papel" and j2 == "piedra":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
            return
        else:
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p2))

        juega_otra_vez=input("Jugamos otra vez?")

def pptls():
    import random
    
    print("Bienvenid@s a Piedra, Papel, Tijera, Lagarto o Spock")
    op = ["piedra", "papel", "tijeras", "lagarto", "spock"]

    juega_otra_vez = "si"

    while True:
        juega_otra_vez == "si" or juega_otra_vez == "s"
        p1 = input("Escriba el nombre del jugador 1: ")
        p2 = input("Escriba el nombre del jugador 2: ")
    
        j1 = random.choice(op)
        j2 = random.choice (op)

        print("\nPiedra... \n Papel... \n  Tijera... \n   Lagarto... \n    o Spock... \n \nEl resultado es...")
    
        if j1 == j2:
            print("empate, ambos eligieron {}".format(j1))
        elif j1 == "piedra" and j2 == "tijeras":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "tijeras" and j2 == "papel":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "papel" and j2 == "piedra":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "piedra" and j2 == "lagarto":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "tijeras" and j2 == "lagarto":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "papel" and j2 == "spock":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "lagarto" and j2 == "papel":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "lagarto" and j2 == "spock":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "spock" and j2 == "piedra":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
        elif j1 == "spock" and j2 == "tijeras":
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p1))
            return
        else:   
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p2))
        juega_otra_vez=input("Jugamos otra vez?")
