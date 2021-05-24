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
            move = input()        

            if self.new_board.theBoard[move] == ' ':
                self.new_board.theBoard[move] = self.getSymbolOfPlayer(self.turn)
                self.count += 1
            else:
                continue

            if self.count >= 5:
                if self.new_board.theBoard['7'] == self.new_board.theBoard['8'] == self.new_board.theBoard['9'] != ' ':
                    self.new_board.printBoard() 
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['4'] == self.new_board.theBoard['5'] == self.new_board.theBoard['6'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['1'] == self.new_board.theBoard['2'] == self.new_board.theBoard['3'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['1'] == self.new_board.theBoard['4'] == self.new_board.theBoard['7'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['2'] == self.new_board.theBoard['5'] == self.new_board.theBoard['8'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['3'] == self.new_board.theBoard['6'] == self.new_board.theBoard['9'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break 
                elif self.new_board.theBoard['7'] == self.new_board.theBoard['5'] == self.new_board.theBoard['3'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn              
                    break
                elif self.new_board.theBoard['1'] == self.new_board.theBoard['5'] == self.new_board.theBoard['9'] != ' ':
                    self.new_board.printBoard()
                    self.winner = self.turn
                    break 

            if self.count == 9:
                break      

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
