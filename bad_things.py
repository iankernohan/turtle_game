from turtle import Turtle
import random


class BadThing:
    def __init__(self):
        self.bad_things = []
        self.coordinates = []
        self.start_position = (0, 0)

    def create_bad_thing(self):
        bad = Turtle('square')
        bad.penup()
        bad.pencolor('red')
        self.bad_things.append(bad)
        self.coordinates.append(self.start_position)
        bad.goto(self.start_position)

    def top_fire(self):
        for i in range(len(self.bad_things)):

            # Top Left
            if self.coordinates[i][1] == 325 and self.coordinates[i][0] < -250:
                self.bad_things[i].setheading(random.randint(280, 350))
                self.bad_things[i].forward(20)

            # Top left middle
            elif self.coordinates[i][1] == 325 and self.coordinates[i][0] < 0:
                self.bad_things[i].setheading(random.randint(200, 350))
                self.bad_things[i].forward(20)

            # Top right
            if self.coordinates[i][1] == 325 and self.coordinates[i][0] > 250:
                self.bad_things[i].setheading(random.randint(200, 260))
                self.bad_things[i].forward(20)

            # Top right middle
            elif self.coordinates[i][1] == 325 and self.coordinates[i][0] > 0:
                self.bad_things[i].setheading(random.randint(200, 350))
                self.bad_things[i].forward(20)

    def bottom_fire(self):
        for i in range(len(self.bad_things)):

            # Bottom left
            if self.coordinates[i][1] == -325 and self.coordinates[i][0] < -250:
                self.bad_things[i].setheading(random.randint(10, 80))
                self.bad_things[i].forward(20)

            # Bottom left middle
            elif self.coordinates[i][1] == -325 and self.coordinates[i][0] < 0:
                self.bad_things[i].setheading(random.randint(10, 170))
                self.bad_things[i].forward(20)

            # Bottom right
            if self.coordinates[i][1] == -325 and self.coordinates[i][0] > 250:
                self.bad_things[i].setheading(random.randint(100, 170))
                self.bad_things[i].forward(20)

            # Bottom right middle
            elif self.coordinates[i][1] == -325 and self.coordinates[i][0] > 0:
                self.bad_things[i].setheading(random.randint(10, 170))
                self.bad_things[i].forward(20)

    def left_fire(self):
        for i in range(len(self.bad_things)):

            # Left bottom
            if self.coordinates[i][0] == -525 and self.coordinates[i][1] < -150:
                self.bad_things[i].setheading(random.randint(0, 80))
                self.bad_things[i].forward(20)

            # Left bottom middle
            elif self.coordinates[i][0] == -525 and self.coordinates[i][1] < 0:
                self.bad_things[i].setheading(random.choice([random.randint(0, 80), random.randint(280, 360)]))
                self.bad_things[i].forward(20)

            # Left top
            if self.coordinates[i][0] == -525 and self.coordinates[i][1] > 150:
                self.bad_things[i].setheading(random.randint(280, 360))
                self.bad_things[i].forward(20)

            # Left top middle
            elif self.coordinates[i][0] == -525 and self.coordinates[i][1] > 0:
                self.bad_things[i].setheading(random.choice([random.randint(0, 80), random.randint(280, 360)]))
                self.bad_things[i].forward(20)

    def right_fire(self):
        for i in range(len(self.bad_things)):

            # Right bottom
            if self.coordinates[i][0] == 525 and self.coordinates[i][1] < -150:
                self.bad_things[i].setheading(random.randint(100, 180))
                self.bad_things[i].forward(20)

            # Right bottom middle
            elif self.coordinates[i][0] == 525 and self.coordinates[i][1] < 0:
                self.bad_things[i].setheading(random.randint(100, 260))
                self.bad_things[i].forward(20)

            # Right top
            if self.coordinates[i][0] == 525 and self.coordinates[i][1] > 150:
                self.bad_things[i].setheading(random.randint(180, 260))
                self.bad_things[i].forward(20)

            # Right top middle
            elif self.coordinates[i][0] == 525 and self.coordinates[i][1] > 0:
                self.bad_things[i].setheading(random.randint(100, 260))
                self.bad_things[i].forward(20)
