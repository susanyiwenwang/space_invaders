from turtle import Turtle
import random
import numpy as np


class Asteroid:
    def __init__(self):
        self.asteroids = []

    def create_asteroids(self):
        x_positions_1 = np.arange(-350, 350, 80).tolist()
        x_positions_2 = np.arange(-290, 410, 80).tolist()
        y_positions = np.arange(-200, 50, 50).tolist()
        for y in y_positions[0::2]:
            for n in range(len(x_positions_1)):
                rock = Turtle()
                rock.shape("circle")
                rock.shapesize(stretch_wid=0.8, stretch_len=1.5)
                rock.penup()
                rock.color("grey")
                rock.setposition(x=x_positions_1[n], y=y)
                self.asteroids.append(rock)
        for y in y_positions[1::2]:
            for n in range(len(x_positions_2)):
                rock = Turtle()
                rock.shape("circle")
                rock.shapesize(stretch_wid=0.8, stretch_len=1.5)
                rock.penup()
                rock.color("grey")
                rock.setposition(x=x_positions_2[n], y=y)
                self.asteroids.append(rock)
        return self.asteroids

    def destroy_rock(self, rock):
        self.asteroids.remove(rock)
        rock.penup()
        rock.goto(0, -800)
