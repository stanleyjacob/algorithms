
class TicTacToe:
    def __init__(self):
        self.grid = [[None for i in range(3)] for j in range(3)]
        self.is_player_one = True
        self.game_done = False
        self.winner = None
        
    def move(i, j):
        if self.game_done:
            return
        if self.grid[i][j]:
            self.grid = 'x'
        else:
            self.grid = 'o'
        self.is_player_one = not self.is_player_one
        game_over_check()
   
   def game_over_check():
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][0]:
                self.winner = self.grid[0][0]
                return True
            
            elif self.grid[0][i] == self.grid[0][i] == self.grid[0][i]:
                self.winner = self.grid[0][0]
                return True
                
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            self.winner = self.grid[0][0]
            return True         
        return False
