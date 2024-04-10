#import turtle library
import turtle
import math
import random

# function to set up turtle environment
def environment():
    #set up turtle environment
    screen = turtle.Screen()
    screen.setup(width= 800, height = 800)
    screen.bgcolor('skyblue')

def draw_background():
    pen = turtle.Turtle()
    pen.speed(0) # set the drawing speed to maxium

    # draw the sun
    pen.penup()
    pen.goto(-200, 200) # position the sun
    pen.pendown()
    pen.begin_fill()
    pen.color("yellow")
    pen.circle(50) # drawing the sun
    pen.end_fill()

    # draw the sun rays using a loop
    pen.penup()
    pen.goto(-200, 250)
    pen.pendown()
    pen.color("yellow")
    # for loop to draw 12 sun rays
    for _ in range(12):
        pen.forward(70)
        pen.backward(70)
        pen.left(30)
    # end for


# main funciton to call the functions
def main():
    # draw sky
    environment()
    # draw background
    draw_background()
    
    


if __name__ == "__main__":
    main()
