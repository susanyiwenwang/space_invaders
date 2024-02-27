from turtle import Screen
from tank import Tank
from spaceship import SpaceShip
from scoreboard import Scoreboard
from asteroid import Asteroid
import time
import random as r

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.title("Space Invaders")
screen.tracer(0)

# create tanks
tank = Tank()
tank.create_tank()

# create spaceships
aliens = SpaceShip()
aliens.create_army()

asteroids = Asteroid()
asteroids.create_asteroids()

# create scoreboard
tanks_score = Scoreboard()
scoreboard = Scoreboard()
start = Scoreboard()
start.start_intro()


def start_game():
    start.clear()
    time_lapse = 0.06
    tanks_score.create_tanks_score()
    scoreboard.create_scoreboard()

    game_over = False

    while not game_over:
        if scoreboard.score > 200:
            time.sleep(time_lapse * 0.4)
        elif scoreboard.score > 100:
            time.sleep(time_lapse * 0.6)
        else:
            time.sleep(time_lapse)
        screen.update()

        if tanks_score.lives == 0:
            game_over = True

        # movement and missiles
        if tank.tank_missiles:
            tank.move_missiles()
        if r.randint(0, 8) == 5:
            aliens.shoot_missile()
        if aliens.arsenal:
            aliens.move_missiles()
        if r.randint(1, 18) == 10:
            aliens.move_army()

        # make missiles and ships disappear if hit
        for missile in tank.tank_missiles:
            for ship in aliens.army:
                if missile.distance(ship) < 25:
                    # ship.color('red')
                    time.sleep(0.15)
                    aliens.destroy_ship(ship)
                    tank.destroy_missile(missile)
                    scoreboard.add_score(10)

        # make tank disappear if hit
        for missile in aliens.arsenal:
            if missile.distance(tank.tank) < 25:
                tank.change_color()
                time.sleep(0.3)
                tank.new_tank()
                tanks_score.reduce_lives()
                aliens.destroy_missile(missile)
        for ship in aliens.army:
            if ship.distance(tank.tank) < 25:
                tank.new_tank()
                tanks_score.reduce_lives()

        # advance army after three hits
        if aliens.ships_hit == 3:
            aliens.advance_army()
            aliens.ships_hit = 0
        # advance army after five shots
        if tank.num_shots == 5:
            aliens.advance_army()
            tank.num_shots = 0

        # make asteroids disappear if hit
        for rock in asteroids.asteroids:
            for missile in aliens.arsenal:
                if rock.distance(missile) < 20:
                    asteroids.destroy_rock(rock)
                    aliens.destroy_missile(missile)
            for ship in aliens.army:
                if rock.distance(ship) < 20:
                    asteroids.destroy_rock(rock)
            for missile in tank.tank_missiles:
                if rock.distance(missile) < 20:
                    asteroids.destroy_rock(rock)
                    tank.destroy_missile(missile)

        # destroy missiles if hit each other, add points
        for enemy_missile in aliens.arsenal:
            for tank_missile in tank.tank_missiles:
                if enemy_missile.distance(tank_missile) < 10:
                    aliens.destroy_missile(enemy_missile)
                    tank.destroy_missile(tank_missile)
                    scoreboard.add_score(5)

        # if aliens reach bottom, game over
        for ship in aliens.army:
            if ship.ycor() < -300:
                game_over = True

        if len(aliens.army) == 0:
            game_over = True

    tanks_score.game_over()


screen.listen()
screen.onkeypress(fun=tank.move_left, key="Left")
screen.onkeypress(fun=tank.move_right, key="Right")
screen.onkeypress(fun=tank.shoot_missile, key="s")
screen.onkeypress(fun=start_game, key="Return")

screen.mainloop()
