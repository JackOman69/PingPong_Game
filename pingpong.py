class Pong:
    def __init__(self, max_score):
        self.max_score = max_score;
        self.score_one = 0
        self.score_two = 0
        self.odd_int = 0
        self.win_counter = 0
        
    def play(self, ball_pos, player_pos):
        self.odd_int += 1
        if self.score_one == self.max_score:
            self.win_counter += 1
            if self.win_counter % 2 != 0:
                return "Player 1 has won the game!"
            else:
                return "Game Over!"
        if self.score_two == self.max_score:
            self.win_counter += 1
            if self.win_counter % 2 != 0:
                return "Player 2 has won the game!"
            else:
                return "Game Over!"
        if self.odd_int % 2 != 0:  
            if abs(player_pos - ball_pos) <= 3:
                self.score_one += 1
                return "Player 1 has hit the ball!"
            else:
                if self.score_one == self.max_score:
                    return "Player 1 has won the game!"
                return "Player 1 has missed the ball!"
        elif self.odd_int % 2 == 0:
            if abs(player_pos - ball_pos) <= 3:
                self.score_two += 1
                return "Player 2 has hit the ball!"
            else:
                if self.score_two == self.max_score:
                    return "Player 2 has won the game!"
                return "Player 2 has missed the ball!"