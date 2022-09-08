class GameBoard:
    def __init__(self, row=3, column=4):
        self.__row = row
        self.__column = column
        self.__board = []

        for i in range(0, row):
            self.__board.append([0]*column)

        self.__board[0][0] = 2
        self.__board[2][1] = 1

    def display(self):
        for i in range(len(self.__board)):
            print(self.__board[i])

        #variante plus concise
        #for i in self.__board:
         #   print(i)





jeu = GameBoard()
jeu.display()
