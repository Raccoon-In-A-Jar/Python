class Player:

    def __init__(self, name, row, column):
        self.__name = name
        self.__row = row
        self.__column = column

    def getName(self):
        return self.__name

    def getXCoordinates(self):
        return self.__row

    def getYCoordinates(self):
        return self.__column

    def setXCoordinates(self, x):
        self.__row = x
        return self.__row

    def setYCoordinates(self, y):
        self.__column = y
        return self.__column

    def setCoordinates(self, x, y):
        self.__row = x
        self.__column = y

        return self.__row, self.__column


class Square:

    def __init__(self, element):
        self.__element = element
    """
    element can be assigned the following values:
        0 for corridor
        1 for wall
        2 for player
        3 for key
        """

    def getElement(self, element):
        return element

    def setElement(self, element, value):
        element = value
        return element


class Board:

    def __init__(self, height, width, player, gameBoard):
        self.__height = height
        self.__width = width
        self.__player = player
        self.__gameBoard = gameBoard

    def display(self, height, width, gameboard):

        width = self.__width
        height = self.__height
        gameboard = self.__gameBoard

        for i in range(width):
            for j in range(height):
                if gameboard[i, j] == 0:
                    print(".")
                elif gameboard[i, j] == 1:
                    print("X")
                elif gameboard[i, j] == 2:
                    print("P")
                elif gameboard[i, j] == 3:
                    print("#")
                else:
                    print("ERROR!")

            print("\n")

    def move(self, player, gameboard):

        direction = input("Dans quelle direction souhaitez-vous aller ? ([N]ord, [E]st, [O]uest, [S]ud) -> ")

        xcor = player.getXCoordinates()
        ycor = player.getYCoordinates()

        # Je n'arrive plus à me souvenir de la méthode qui permet de changer la casse d'un caractère ou d'une string...
        # upper(direction) <- c'est pas ça du tout


        while direction != "O" or direction != "E" or direction != "N" or direction != "S":

            print("\n")
            print("Veuillez sélectionner un point cardinal.\n")
            print("\"N\" pour Nord\n\"S\" pour Sud\n\"E\" pour Est\n\"O\" pour Ouest\n")
            direction = input("Dans quelle direction souhaitez-vous aller ? ([N]ord, [E]st, [O]uest, [S]ud) -> ")


        # Dans la partie qui suit, il y a un évident problème dans les vérifications des valeurs
        # que je n'ai pas eu le temps de corriger (comme je n'ai pas eu le temps de finir) :

        # Je pourrais plutôt vérifier que la case de destination soit un mur ou non, mais je redoute d'être hors limites
        # dans certaines situations (qui ne devraient normalement pas se présenter si tout va bien).
        if direction == "N":
            if gameboard[xcor, ycor - 1] != 0 and gameboard[xcor, ycor - 1] != 3:
                print("Vous ne pouvez pas aller par là !")
                direction = input("Dans quelle direction souhaitez-vous aller ? ([N]ord, [E]st, [O]uest, [S]ud) -> ")
            else:
                player.setCoordinates(xcor, ycor - 1)

        elif direction == "S":
            if gameboard[xcor, ycor + 1] != 0 and gameboard[xcor, ycor - 1] != 3:
                print("Vous ne pouvez pas aller par là !")
                direction = input("Dans quelle direction souhaitez-vous aller ? ([N]ord, [E]st, [O]uest, [S]ud) -> ")
            else:
                player.setCoordinates(xcor, ycor + 1)

        elif direction == "E":
            if gameboard[xcor + 1, ycor] != 0 and gameboard[xcor, ycor - 1] != 3:
                print("Vous ne pouvez pas aller par là !")
                direction = input("Dans quelle direction souhaitez-vous aller ? ([N]ord, [E]st, [O]uest, [S]ud) -> ")
            else:
                player.setCoordinates(xcor + 1, ycor)

        elif direction == "O":
            if gameboard[xcor - 1, ycor] != 0 and gameboard[xcor, ycor - 1] != 3:
                print("Vous ne pouvez pas aller par là !")
                direction = input("Dans quelle direction souhaitez-vous aller ? ([N]ord, [E]st, [O]uest, [S]ud) -> ")
            else:
                player.setCoordinates(xcor - 1, ycor)

    def victory(self, width, height, gameboard):

        width = self.__width
        height = self.__height
        gameboard = self.__gameBoard

        for i in range(width):
            for j in range(height):
                if 3 not in gameboard:
                    endgame = True
                else:
                    endgame = False

        return endgame

"""[[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,0,1,1,1,1,0,1],
[1,0,1,0,0,0,0,1,0,1],
[1,0,1,0,1,1,1,1,0,1],
[1,0,0,0,0,0,0,1,0,1],
[1,0,1,1,1,1,1,1,0,1],
[1,3,1,0,0,0,1,0,0,1],
[1,1,1,0,1,0,1,1,0,1],
[1,3,0,0,1,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]]

row then line
"""