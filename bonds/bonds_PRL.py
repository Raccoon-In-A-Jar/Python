stellar = [2, 5, 1, 3, 3, 5, 4, 6, 4, 6, 3, 6]

# Jump position:
jumpy = 0
# Jump count:
jumpCount = 0


def boing(listy, jumpinou, counter):

    # Jump value:
    jumping = listy[jumpinou]

    if (jumpinou+jumping) > len(listy):
        print("Dernier saut : saut n° " + str(counter+1) + "\n")
        lastCall = len(listy) - jumpinou - 1
        print("Valeur = " + str(lastCall))
        print("Position : " + str(jumpinou+jumping - 2))
        # print(lastCall + (jumping+jumpinou))

        return 0

    print("Position : " + str(jumpinou))
    print("Valeur = " + str(jumping))
    # print(jumpinou+jumping)
    print("Saut n° " + str(counter+1) + "\n")

    return boing(listy, jumpinou=jumpinou + jumping, counter=counter + 1)


boing(stellar, jumpy, jumpCount)












