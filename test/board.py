class board:
    def __init__(self):
        self.theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                    '4': ' ' , '5': ' ' , '6': ' ' ,
                    '1': ' ' , '2': ' ' , '3': ' ' }

    def printBoard(self):
        print(self.theBoard['7'] + '|' + self.theBoard['8'] + '|' + self.theBoard['9'])
        print('-+-+-')
        print(self.theBoard['4'] + '|' + self.theBoard['5'] + '|' + self.theBoard['6'])
        print('-+-+-')
        print(self.theBoard['1'] + '|' + self.theBoard['2'] + '|' + self.theBoard['3'])

    def resetBoard(self):
        self.theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                    '4': ' ' , '5': ' ' , '6': ' ' ,
                    '1': ' ' , '2': ' ' , '3': ' ' }