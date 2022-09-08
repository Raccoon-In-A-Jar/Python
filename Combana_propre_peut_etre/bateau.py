class Bateau:
    def __init__(self, x, y, orientation):
        self._coordonnee = [x,y]
        self._estcoule = False
        self._orientation = orientation
        self._vie = None
        self._taille = None
        self._lettre = None

    def getLettre(self):
        return self._lettre

    def getTaille(self):
        return self._taille
    
    def getVie(self):
        return self._vie
    
    def decrementation(self):
        self._vie -= 1

    def getEstCoule(self):
        return self.__estcoule

    def couler(self):
        self.__estcoule = True

    def getCoord(self):
        return self.__coordonnee

    def placer(self, x, y, orientation):
        self.__orientation = orientation
        self.__coordonnee = [x][y]


class PorteAvion(Bateau):
    def __init__ (self, x, y, orientation):
        super().__init__(x, y, orientation)
        self._vie = 5
        self._taille = 5
        self._lettre = "p"

class Croiseur(Bateau):
    def __init__ (self, x, y, orientation):
        super().__init__(x, y, orientation)
        self._vie = 4
        self.__taille = 4
        self.__lettre = "c"

class ContreTorpilleur(Bateau):
    def __init__ (self, x, y, orientation):
        super().__init__( x, y, orientation)
        self._vie = 3
        self.__taille = 3
        self.__lettre = "s"

class SousMarin(Bateau):
    def __init__ (self, x, y, orientation):
        super().__init__( x, y, orientation)
        self._vie = 3
        self.__taille = 3
        self.__lettre = "u"

class Cuirasse(Bateau):
    def __init__ (self, x, y, orientation):
        super().__init__( x, y, orientation)
        self._vie = 2
        self.__taille = 2
        self.__lettre = "t"
