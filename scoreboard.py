from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.lives = 3

    def create_scoreboard(self):
        self.setposition((385, 330))
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)

    def create_tanks_score(self):
        self.setposition((-385, 330))
        self.write(arg=f"Tanks: {self.lives}", move=False, align="center", font=FONT)

    def add_score(self, points):
        self.clear()
        self.score += points
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)

    def reduce_lives(self):
        self.clear()
        self.lives -= 1
        self.write(arg=f"Tanks: {self.lives}", move=False, align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def start_intro(self):
        self.setposition((0, 0))
        self.write(arg=f"Welcome to Space Invaders.\n\n"
                       f"You have three tanks, can move right and left, and shoot at the \n"
                       f"spaceships and their missiles.\n"
                       f"The asteroids are there to protect you, but both you and spaceships \n"
                       f"can destroy them.\n\n"
                       f"After each 100 points the game speeds up.\n"
                       f"After a certain amount of hits, the enemy will advance.\n\n"
                       f"Press 'right' and 'left' to move, 's' to shoot. \n"
                       f"Press 'return' to start. Good luck!", move=False, align="center", font=FONT)

