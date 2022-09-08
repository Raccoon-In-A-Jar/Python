liste = [5, 2, 8, 6, 4, 5, 9, 4, 1, 3, 5, 9, 6, 7]


somme1 = 0
somme2 = 0


def naive(maliste, sommej1, sommej2):

    longueur = len(maliste)
    debut = 0
    fin = longueur - 1

    print(longueur)
    print("debut = " + str(debut))
    print("fin = " + str(fin))

    # Si la liste est vide :
    if longueur == 0:
        print("Joueur 1 : " + str(sommej1))
        print("Joueur 2 : " + str(sommej2))

        if sommej1 > sommej2:
            print("Le joueur 1 a gagné.")
        elif sommej2 > sommej1:
            print("Le joueur 2 a gagné.")
        else:
            print("Les joueurs sont ex-aequo.")
        return 0

    # tour du joueur 1 :
    if longueur % 2 == 0:
        if maliste[debut] > maliste[fin]:
            sommej1 += maliste[debut]
            maliste.pop(0)  # supprime le premier élément de la liste

        elif maliste[fin] > maliste[debut]:
            sommej1 += maliste[fin]
            maliste.pop()  # supprime le dernier élément de la liste (par défaut)

        # si les deux valeurs sont égales, on prend celle en i par défaut
        # (bien que l'on pourrait anticiper plusieurs tours si on voulait
        # pousser davantage la complexité) :
        else:
            sommej1 += maliste[debut]
            maliste.pop(0)

        longueur = len(maliste)
        print(maliste)
        print("Somme du joueur 1 = " + str(sommej1))
        return maliste, sommej1, naive(maliste, sommej1, sommej2)

    # tour du joueur 2 :
    elif longueur % 2 != 0:
        if maliste[debut] > maliste[fin]:
            sommej2 += maliste[debut]
            maliste.pop(0)

        elif maliste[fin] > maliste[debut]:
            sommej2 += maliste[fin]
            maliste.pop()

        else:
            sommej2 += maliste[debut]
            maliste.pop(0)

        longueur = len(maliste)
        print(maliste)
        print("Somme du joueur 2 = " + str(sommej2))
        return maliste, sommej2, naive(maliste, sommej1, sommej2)


naive(liste, somme1, somme2)

