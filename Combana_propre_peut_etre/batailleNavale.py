from joueur import *

class BatailleNavale:
    def __init__(self):
        self.__joueurs = []
        
        j1 = input("Pseudo joueur 1 : ")
        while j1 == "":
            j1 = input("Pseudo joueur 1 : ")
            
        j2 = input("Pseudo joueur 2 : ")
        
        while j2 == "":
            j2 = input("Pseudo joueur 2 : ")

        
        self.__joueurs.append(Joueur(j1))
        self.__joueurs.append(Joueur(j2))
        
    def getJoueur(self, i):
        return self.__joueurs[i]

    def tour(self):
        pass

    def afficherPlateau(self):
        print("plateau")

tab = BatailleNavale()