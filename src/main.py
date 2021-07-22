class TicTacToe:
    def __init__(self, player, ai):
        self.board = {
            1 : ' ', 2 : ' ', 3 : ' ',
            4 : ' ', 5 : ' ', 6 : ' ',
            7 : ' ', 8 : ' ', 9 : ' ',
        }
        self.player = player
        self.ai = ai
        self.finish = False
    
    def printBoard(self):
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print("-+-+-")
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6])
        print("-+-+-")
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9])
    
    def isFull(self):
        for key in self.board.keys():
            if(self.board[key] == ' '):
                return False
        return True

    def insert(self, char, position):
        if(self.board[position] == ' '):
            self.board[position] = char
            return True
        else:
            print("Can't insert to that position")
            return False

    def check_finish(self):
        for i in range(3):
            if (
                self.board[1 + 3 * i] == self.board[2 + 3 * i] 
                and 
                self.board[2 + 3 * i] == self.board[3 + 3 * i]
            ):
                if self.board[1 + 3 * i] == self.ai:
                    print("AI WINS")
                    self.finish = True
                    return
                if self.board[1 + 3 * i] == self.player:
                    print("Player WINS")
                    self.finish = True
                    return
        
        for j in range(3):
            if (
                self.board[0 * 3 + (j + 1)] == self.board[1 * 3 + (j + 1)] 
                and 
                self.board[1 * 3 + (j + 1)] == self.board[2 * 3 + (j + 1)]
            ):
                if self.board[0 * 3 + (j + 1)] == self.ai:
                    print("AI WINS")
                    self.finish = True
                    return
                if self.board[0 * 3 + (j + 1)] == self.player:
                    print("Player WINS")
                    self.finish = True
                    return 
        
        if self.board[7] == self.board[5] and self.board[5] == self.board[3]:
            if self.board[7] == self.ai:
                print("AI WINS")
                self.finish = True
                return
            if self.board[7] == self.player:
                print("Player WINS")
                self.finish = True
                return                 

        if self.board[1] == self.board[5] and self.board[5] == self.board[9]:
            if self.board[1] == self.ai:
                print("AI WINS")
                self.finish = True
                return                
            if self.board[1] == self.player:
                print("Player WINS")
                self.finish = True
                return 
        
        if self.isFull():
            print("TIE")
            self.finish = True
            return

        self.finish = False
        return
    
    def evaluate(self, depth):
        for i in range(3):
            if (
                self.board[1 + 3 * i] == self.board[2 + 3 * i] 
                and 
                self.board[2 + 3 * i] == self.board[3 + 3 * i]
            ):
                if self.board[1 + 3 * i] == self.ai:
                    return 100
                if self.board[1 + 3 * i] == self.player:
                    return -100
        
        for j in range(3):
            if (
                self.board[0 * 3 + (j + 1)] == self.board[1 * 3 + (j + 1)] 
                and 
                self.board[1 * 3 + (j + 1)] == self.board[2 * 3 + (j + 1)]
            ):
                if self.board[0 * 3 + (j + 1)] == self.ai:
                    return 100
                if self.board[0 * 3 + (j + 1)] == self.player:
                    return -100
        
        if self.board[7] == self.board[5] and self.board[5] == self.board[3]:
            if self.board[7] == self.ai:
                return 100 
            if self.board[7] == self.player:
                return -100

        if self.board[1] == self.board[5] and self.board[5] == self.board[9]:
            if self.board[1] == self.ai:
                return 100
            if self.board[1] == self.player:
                return -100
        
        return 0

    def minimax(self, depth, isMaximizing):
        score = self.evaluate(depth)
                
        if score == 100 or score == -100:
            return score
        
        if self.isFull():
            return 0

        if(isMaximizing):
            bestScore = float("-inf")
            for key in self.board.keys():
                if(self.board[key] == ' '):
                    self.board[key] = self.ai
                    score = self.minimax(depth + 1, not(isMaximizing))
                    self.board[key] = ' '
                    bestScore = max(bestScore, score)
                        
            return bestScore
        
        else:
            bestScore = float("inf")
            for key in self.board.keys():
                if(self.board[key] == ' '):
                    self.board[key] = self.player
                    score = self.minimax(depth + 1, not(isMaximizing))
                    self.board[key] = ' '
                    bestScore = min(bestScore, score)

            return bestScore

    def playerMove(self):
        valid_input = False
        
        while(not(valid_input)):
            position = int(input("Enter position for '{}': ".format(self.player)))
            valid_input = self.insert(self.player, position)

        self.printBoard()
        self.check_finish()
        print()
    
    def aiMove(self):
        bestScore = float("-inf")
        bestPosition = 0
        for key in self.board.keys():
            if(self.board[key] == ' '):
                self.board[key] = self.ai
                score = self.minimax(0, False)   
                self.board[key] = ' '
                if score > bestScore:
                    bestScore = score
                    bestPosition = key
        

        
        self.insert(self.ai, bestPosition)
        self.printBoard()
        self.check_finish()

        print()

if __name__ == "__main__":
    game = TicTacToe(player="O", ai="X")
    counter = 0

    print("Enter number 1 - 9\n")

    while(not(game.finish)):
        if(not(game.finish)):
            game.aiMove()
        if(not(game.finish)):
            game.playerMove()