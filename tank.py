from turtle import Turtle

# TODO: create gun for tank with another turtle
# TODO: create missiles as part of tank


class Tank:
    def __init__(self):
        self.tank = None
        self.gun = None
        self.tank_missiles = []
        self.num_shots = 0

    def create_tank(self):
        new_tank = Turtle()
        new_tank.shape("square")
        new_tank.shapesize(stretch_wid=1, stretch_len=3)
        new_tank.color("blue")
        new_tank.penup()
        new_tank.setposition(x=0, y=-350)
        gun = Turtle()
        gun.shape("square")
        gun.shapesize(stretch_wid=1, stretch_len=0.5)
        gun.color("blue")
        gun.penup()
        gun.setposition(x=0, y=-330)
        self.tank = new_tank
        self.gun = gun
        return self.tank, self.gun

    def move_left(self):
        if self.tank.xcor() > -400:
            self.tank.backward(20)
        if self.gun.xcor() > -400:
            self.gun.backward(20)

    def move_right(self):
        if self.tank.xcor() < 400:
            self.tank.forward(20)
        if self.gun.xcor() < 400:
            self.gun.forward(20)

    def shoot_missile(self):
        coord = self.tank.position()
        missile = Turtle()
        missile.shape("square")
        missile.shapesize(stretch_wid=0.2, stretch_len=1)
        missile.penup()
        missile.setheading(90)
        missile.color("blue")
        missile.setposition(coord)
        self.num_shots += 1
        self.tank_missiles.append(missile)

    def move_missiles(self):
        for missile in self.tank_missiles:
            missile.forward(10)

    def new_tank(self):
        self.tank.penup()
        self.tank.goto(0, -500)
        self.gun.penup()
        self.gun.goto(0, -480)
        # TODO: make animation to show a new tank coming into place
        self.create_tank()

    def change_color(self):
        self.tank.fillcolor("red")

    def destroy_missile(self, missile):
        missile.goto(-600, 0)




