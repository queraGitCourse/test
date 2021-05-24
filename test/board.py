class board:
    def __init__(self):
        self.theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                    '4': ' ' , '5': ' ' , '6': ' ' ,
                    '1': ' ' , '2': ' ' , '3': ' ' }

    def printBoard(self):
        print(self.theBoard)

    def resetBoard(self):
        self.theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                    '4': ' ' , '5': ' ' , '6': ' ' ,
                    '1': ' ' , '2': ' ' , '3': ' ' }