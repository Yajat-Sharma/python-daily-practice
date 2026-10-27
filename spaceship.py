import os
import random
import turtle

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spritshape, color, startx, starty):
        super().__init__(shape=spritshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.move_speed = 1   # custom variable (safe)

# Create player
player = Sprite("triangle", "white", 0, 0)


delay = input("Press Enter to finish...")