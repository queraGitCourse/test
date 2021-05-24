from board import board


class game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = player1
        self.count = 0
        self.new_board = board()
        self.winner = None

    def getSymbolOfPlayer(self, player):
        if player == self.player1:
            return 'X'
        return 'O'

    def start(self):
        while True:
            self.new_board.printBoard()
            print("It's your turn, " + self.turn.name + ". Move to which place? (enter a number between 1 and 9)")

            move = input()        

            if self.new_board.theBoard[move] == ' ':
                self.new_board.theBoard[move] = self.getSymbolOfPlayer(self.turn)
                self.count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Now we will check if player X or O has won,for every move after 5 moves. 
            if self.count >= 5:
                if self.new_board.theBoard['7'] == self.new_board.theBoard['8'] == self.new_board.theBoard['9'] != ' ': # across the top
                    self.new_board.printBoard() 
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['4'] == self.new_board.theBoard['5'] == self.new_board.theBoard['6'] != ' ': # across the middle
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['1'] == self.new_board.theBoard['2'] == self.new_board.theBoard['3'] != ' ': # across the bottom
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['1'] == self.new_board.theBoard['4'] == self.new_board.theBoard['7'] != ' ': # down the left side
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['2'] == self.new_board.theBoard['5'] == self.new_board.theBoard['8'] != ' ': # down the middle
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['3'] == self.new_board.theBoard['6'] == self.new_board.theBoard['9'] != ' ': # down the right side
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break 
                elif self.new_board.theBoard['7'] == self.new_board.theBoard['5'] == self.new_board.theBoard['3'] != ' ': # diagonal
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['1'] == self.new_board.theBoard['5'] == self.new_board.theBoard['9'] != ' ': # diagonal
                    self.new_board.printBoard()
                    self.winner = self.turn
                    break 

            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if self.count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                break      

            # Now we have to change the player after every move.
            if self.turn == self.player1:
                self.turn = self.player2
            else:
                self.turn = self.player1        
        
    def resetGame(self):
            self.new_board.resetBoard()
            self.winner = None
            self.count = 0
            temp = self.player1
            self.player1 = self.player2
            self.player2 = temp
            self.turn = self.player1
