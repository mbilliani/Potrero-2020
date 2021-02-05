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
        else:
            print("{} sacó {} y {} sacó {}, ¡{} ganaste!".format(p1,j1,p2,j2,p2))

        
        juega_otra_vez=input("Tira los dados otra vez?")
