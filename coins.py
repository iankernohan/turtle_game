from turtle import Turtle
import random


class Coins:

    def __init__(self):
        self.graveyard = (1000, 1000)
        self.coins = []

    def create_coin(self):
        coin = Turtle('circle')
        coin.penup()
        coin.shapesize(0.5, 0.5)
        coin.color('yellow')
        self.coins.append(coin)
        x_cor = random.randint(-450, 450)
        y_cor = random.randint(-250, 250)
        coin.goto(x_cor, y_cor)

    def capture(self):
        for coin in self.coins:
            coin.goto(self.graveyard)
        self.create_coin()
