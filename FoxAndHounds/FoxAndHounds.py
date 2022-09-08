class GameBoard:
    def __init__(self, side):
        self.__side = side
        self.__board = []

        # vérifie si la longueur du côté du plateau est divisible
        # par 4 et, sinon, la réduit à l'entier multiple de 4 inférieur :
        if self.__side % 4 != 0:
            self.__side = (self.__side//4)*4

        # pour pallier un côté éventuellement inférieur à 4 :
        elif self.__side > 4:
            self.__side = 4

        for i in range(0, self.__side):
            self.__board.append([0]*self.__side)

# accesseur pour la valeur du côté du plateau :
    def get_side(self):
        return self.__side

# affichage foireux :
    def display(self):
        show_me = []
        for i in self.__board:
            for j in self.__board:
                if i == -1:
                    show_me.append(['F'])
                    #print("F")
                elif i in (1, self.__side/2):
                    show_me.append([hound])
                    #print(hound)
                else:
                    show_me.append('.')
                    #print(".")

# petite béquille pour (tenter de) « déboguer » l'affichage :
        for k in show_me:
            print(k)

# ce set_case est pour l'instant complètement foireux :
    def set_case(self, i, j):
        if self.__board[i][j] == -1:
            self.__board[i][j] = "F"

        elif self.__board[i][j] == 0:
            self.__board[i][j] = "."

        elif self.__board[i][j] in (1, self.__side/2):
            self.__board[i][j] = str(self.__board)

    def get_case(self, i, j):
        return self.__board[i][j]

    def get_board(self):
        return self.__board



class Hound:
    def __init__(self, x_pos=0, y_pos=0):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def can_move_to(self, board, rowNbr, colNbr):
        pass

    def move(self, board):
        pass

    def can_move(self, board):
        if board[self.__x_pos - 1][self.__y_pos - 1] == 0 or \
                        board[self.__x_pos + 1][self.__y_pos - 1] == 0 or \
                        board[self.__x_pos - 1][self.__y_pos - 1] in board or \
                        board[self.__x_pos + 1][self.__y_pos - 1] in board:
            return True
        else:
            return False


class Fox(Hound):
    def __init__(self, x_pos=0, y_pos=0):
        Hound.__init__(self, x_pos=0, y_pos=0)

    def can_move(self, board):
        if board[self.__x_pos - 1][self.__y_pos - 1] == 0 or \
                        board[self.__x_pos + 1][self.__y_pos - 1] == 0 or \
                        board[self.__x_pos - 1][self.__y_pos - 1] in board or \
                        board[self.__x_pos + 1][self.__y_pos - 1] in board or \
                        board[self.__x_pos + 1][self.__y_pos + 1] == 0 or \
                        board[self.__x_pos - 1][self.__y_pos + 1] == 0 or \
                        board[self.__x_pos + 1][self.__y_pos + 1] in board or \
                        board[self.__x_pos - 1][self.__y_pos + 1] in board:
                return True
        else:
            return False
    # la méthode sans queue ni tête :
    def win(self):
        while True:
            return False


class FoxAndHounds:
    def __init__(self, size=8):
        self.__plateau = GameBoard()
        self.__chiens = []
        self.__renard = Fox()
        size = self.__plateau.get_side()

        hound_count = 1
        for i in range(size/2):
            self.chiens.append(hound_count)
            hound_count += 1

    def play(self):
        while not self.__renard.win():
            print("Bob")
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie
            # déroulement de la partie

        if self.__renard.can_move(self.__plateau.get_board()):
            print("Le renard a gagné !")
        else:
            print("Les chiens de chasse ont gagné !")


jeu = GameBoard(19)
jeu.display()
print(jeu.get_side())

