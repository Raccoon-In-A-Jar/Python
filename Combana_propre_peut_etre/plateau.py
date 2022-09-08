class Plateau:
    def __init__ (self, x = 10):
        self.__plateau = [["."] *x] *x
        self.__taille = x

    def getCase(self, ligne, colonne):
        return self.__plateau [ligne][colonne]
    
    def setCase(self, ligne, colonne, char):
        self.__plateau[ligne][colonne] = char

    def getTaille(self):
        return self.__taille

    def getPlateau(self):
        return self.__plateau