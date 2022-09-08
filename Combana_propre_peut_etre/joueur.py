from plateau import *
from bateau import *

class Joueur:
    def __init__ (self, nom):
        self.__nom = nom
        self.__plateau = Plateau()
        self.__flotte = []

        print(self.__nom + " entrez les coordonnées de vos bateaux : \n")
        x = input("x:")
        y = input("y:")
        orientation = input("orientation :")

        while x > 0 and x < self.__plateau.getTaille() - taillebateau :


        self.__flotte.append(PorteAvion())
        self.__flotte.append(Croiseur())
        self.__flotte.append(ContreTorpilleur())
        self.__flotte.append(SousMarin())
        self.__flotte.append(Cuirasse())

            

    def getNom(self):
        return self.__nom
        

    def getPlateau(self):
        return self.__plateau
