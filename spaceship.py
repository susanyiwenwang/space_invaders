from turtle import Turtle
import numpy as np
import random as r


class SpaceShip:
    def __init__(self):
        self.army = []
        self.move = 0
        self.arsenal = []
        self.ships_hit = 0
        self.y_positions = [100, 150, 200, 250, 300]

    def create_army(self):
        x_positions_1 = np.arange(-350, 350, 80).tolist()
        x_positions_2 = np.arange(-300, 300, 80).tolist()
        for i in self.y_positions[0::2]:
            for n in range(len(x_positions_1)):
                ship = Turtle()
                ship.shape("circle")
                ship.shapesize(stretch_wid=0.8, stretch_len=3)
                ship.penup()
                ship.color("green")
                ship.setposition(x=x_positions_1[n], y=i)
                self.army.append(ship)
        for i in self.y_positions[1::2]:
            for n in range(len(x_positions_2)):
                ship = Turtle()
                ship.shape("circle")
                ship.shapesize(stretch_wid=0.8, stretch_len=3)
                ship.penup()
                ship.color("green")
                ship.setposition(x=x_positions_2[n], y=i)
                self.army.append(ship)
        return self.army

    def move_army_right(self):
        for ship in self.army:
            ship.forward(20)

    def move_army_left(self):
        for ship in self.army:
            ship.backward(20)

    def move_army(self):
        if self.move < 3:
            self.move_army_right()
            self.move += 1
        elif self.move >=3 and self.move < 9:
            self.move_army_left()
            self.move += 1
        elif self.move >=9 and self.move <= 11:
            self.move_army_right()
            self.move += 1
        elif self.move == 12:
            self.move_army_right()
            self.move = 0

    def advance_army(self):
        for ship in self.army:
            ship.setheading(270)
            ship.forward(20)
            ship.setheading(0)

    def shoot_missile(self):
        ship = r.choice(self.army)
        location = ship.position()
        missile = Turtle()
        missile.shape("square")
        missile.shapesize(stretch_wid=0.2, stretch_len=1)
        missile.penup()
        missile.setheading(270)
        missile.color("green")
        missile.setposition(location)
        self.arsenal.append(missile)

    def move_missiles(self):
        for missile in self.arsenal:
            missile.forward(10)

    def destroy_ship(self, ship):
        self.army.remove(ship)
        ship.penup()
        ship.goto(800, 0)
        self.ships_hit += 1


    def destroy_missile(self, missile):
        missile.goto(-700, 0)



