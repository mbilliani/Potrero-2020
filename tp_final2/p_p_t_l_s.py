def pptls():
    import random
    
    print("Bienvenid@s a Piedra, Papel, Tijera, Lagarto o Spock")
    op = ["piedra", "papel", "tijeras", "lagarto", "spock"]


    while True:
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
        else:   
            print("¡{} sacó {} y {} sacó {}, {} ganaste!".format(p1,j1,p2,j2,p2))
        print("Fin del juego")
