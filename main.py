import random
from turtle import Turtle, Screen
from bad_things import BadThing
from coins import Coins
from level import Level
import subprocess
import time
import math

"""Screen setup"""
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('grey')
screen.tracer(0)

"""Player setup"""
dude = Turtle('circle')
dude.penup()
dude.color('blue')
dude.shapesize(stretch_len=1.7, stretch_wid=1.7)
dude_start = (0, 0)
dude.goto(dude_start)


"""Functions for moving player"""


def right():
    if dude.xcor() < 490:
        dude.setheading(0)
        dude.forward(20)


def left():
    if dude.xcor() > -490:
        dude.setheading(180)
        dude.forward(20)


def up():
    if dude.ycor() < 290:
        dude.setheading(90)
        dude.forward(20)


def down():
    if dude.ycor() > -290:
        dude.setheading(270)
        dude.forward(20)


"""Objects on screen and variables"""
level = Level()
bad_thing = BadThing()
coin = Coins()
new_coin = coin.create_coin()
generation_chance = 20
level.pregame()

game_on = True
while game_on:
    time.sleep(.1)
    screen.update()

    """Starting position for bad things"""
    left_side = (-525, random.randint(-300, 300))
    right_side = (525, random.randint(-300, 300))
    top_side = (random.randint(-500, 500), 325)
    bottom_side = (random.randint(-500, 500), -325)
    if level.level == 1:
        bad_thing.start_position = right_side
    elif level.level == 2:
        bad_thing.start_position = random.choice([right_side, left_side])
    elif level.level == 3:
        bad_thing.start_position = random.choice([right_side, left_side, top_side])
    else:
        bad_thing.start_position = random.choice([right_side, left_side, top_side, bottom_side])

    """Controlled generation of bad things"""
    random_num = random.randint(1, level.generation_chance)
    if random_num == 1:
        bad_thing.create_bad_thing()

    """Control the sides that bad things generate from"""
    if level.level == 1:
        bad_thing.right_fire()
    elif level.level == 2:
        bad_thing.right_fire()
        bad_thing.left_fire()
    elif level.level == 3:
        bad_thing.right_fire()
        bad_thing.left_fire()
        bad_thing.top_fire()
    else:
        bad_thing.right_fire()
        bad_thing.left_fire()
        bad_thing.top_fire()
        bad_thing.bottom_fire()

    """Detect collision with coin"""
    for i in coin.coins:
        if i.distance(dude) < 20:
            coin.capture()
            level.score += 1
            level.total_score += 1
            level.update_score()

    """Detect player collision with bad thing"""
    for thing in bad_thing.bad_things:
        if thing.distance(dude) < 15:
            game_on = False
            with open('high_level.txt') as file:
                high_level = int(file.read())
                if level.level > high_level:
                    with open('high_level.txt', 'w') as file2:
                        file2.write(f'{level.level}')
            with open('high_coins.txt') as file:
                high_coin = int(file.read())
                if level.total_score > high_coin:
                    with open('high_coins.txt', 'w') as file2:
                        file2.write(f'{level.total_score}')
            level.game_over()
            subprocess.call(['afplay', 'stay-retro-124958.wav'])

    """Advance a level"""
    if level.score == 5:
        level.new_level()

    """Keys to move player"""
    screen.listen()
    # screen.onclick(shoot)
    screen.onkey(right, 'Right')
    screen.onkey(left, 'Left')
    screen.onkey(up, 'Up')
    screen.onkey(down, 'Down')


screen.exitonclick()
