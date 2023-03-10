from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = 0
        self.total_score = 0
        self.generation_chance = 20
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-425, 250)
        self.write(f'Level: {self.level}', False, 'center', ('times', 30, 'normal'))
        self.goto(425, 250)
        self.write(f'Coins: {self.score}', False, 'center', ('times', 30, 'normal'))
        self.goto(425, 230)
        self.write(f'Total Coins: {self.total_score}', False, 'center', ('times', 15, 'normal'))

    def new_level(self):
        self.level += 1
        self.score = 0
        self.generation_chance -= 1
        self.update_score()

    def pregame(self):
        self.goto(0, 270)
        self.write(f'Collect 5 coins to advance a level. Good luck!', False, 'center', ('times', 20, 'normal'))

    def game_over(self):
        with open('high_level.txt') as file:
            high_level = file.read()
        with open('high_coins.txt') as file:
            high_coins = file.read()
        self.goto(0, 75)
        self.write(f'GAME OVER', False, 'center', ('times', 30, 'normal'))
        self.goto(0, 0)
        self.write(f'You made it to level {self.level}', False, 'center', ('times', 30, 'normal'))
        self.goto(0, -75)
        self.write(f'Current high score: {high_level}', False, 'center', ('times', 30, 'normal'))
        self.goto(0, -125)
        self.write(f'Most coins collected: {high_coins}', False, 'center', ('times', 30, 'normal'))
