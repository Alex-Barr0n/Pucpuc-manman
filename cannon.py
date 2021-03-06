"""Cannon, hitting targets with projectiles.
Alex_score
=======

Angel Afonso
Israel Macías

main
Exercises
1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

from random import randrange
from turtle import *
from freegames import vector

state = {'score': 0}
writer = Turtle(visible=False)
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
background = bgcolor('magenta')

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'green')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(10, 'blue')

    update()

def move():
    "Move ball and targets."
    writer.undo()
    writer.up()
    writer.goto(160, 160)
    writer.down()
    writer.color('black')
    writer.write(state['score'])

    # Generate a new target at random times
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # Move the existing targets
    for target in targets:
        target.x -= 0.9

    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.5
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    for target in dupe:
        if abs(target - ball) > 14:
            targets.append(target)
        else:
            state['score'] += 1
            #score+=1 
    draw()


    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

