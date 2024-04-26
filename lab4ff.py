#import turtle library
import turtle
import math
import random
import time

special_color_one = ['silver']
special_color_two = ['gold']

# function to set up turtle environment
def environment():
    #set up turtle environment
    screen = turtle.Screen()
    screen.setup(width= 800, height = 800)
    screen.bgcolor('skyblue')

def draw_background():
    pen = turtle.Turtle()
    pen.speed(0) # set the drawing speed to maxium

    # draw the sun rays using a loop
    pen.penup()
    pen.goto(-295, 325)
    pen.pendown()
    pen.pensize(3)
    pen.color("yellow")
    # for loop to draw 12 sun rays
    for _ in range(12):
        pen.forward(90)
        pen.backward(90)
        pen.left(30)
    pen.color("orange")
    pen.left(20)
    for _ in range(12):
        pen.forward(90)
        pen.backward(90)
        pen.left(30)
    # end for
        
    # draw the sun
    pen.penup()
    pen.goto(-285, 275) # position the sun
    pen.pendown()
    pen.begin_fill()
    pen.color("yellow")
    pen.circle(50) # drawing the sun
    pen.end_fill()
    pen.hideturtle()

#draw white cloud
def draw_white_cloud():
    turtle.penup()
    turtle.goto(200, 200)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(120, 220)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(270, 215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(130, 155)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(260, 155)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(170, 140)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

#draw rainy cloud
def draw_rain_cloud():
    turtle.penup()
    turtle.goto(250, 250)
    turtle.speed(0)
    turtle.color("grey")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(20)
    for x in range(1, 15):
        turtle.left(10)
        turtle.forward(10)

    turtle.left(220)
    for y in range(1, 18):
        turtle.left(10)
        turtle.forward(12)

    turtle.left(200)
    for z in range(1, 18):
        turtle.left(10)
        turtle.forward(15)

    turtle.forward(18)
    turtle.left(90)
    turtle.forward(260)
    turtle.end_fill()
    turtle.hideturtle()
"""
def draw_rain():
    # set up rain
    turtle.penup()
    turtle.goto(250, 250)
    turtle.pencolor("dark blue")
    turtle.right(90)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
        turtle.penup()
"""""

#Create function for grass
def draw_grass():
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(-410, -230)
    turtle.pendown()
    for i in range(0, 2):
        turtle.speed(0)
        turtle.fillcolor("green")
        turtle.forward(800)
        turtle.right(90)
        turtle.forward(400)
        turtle.right(90)
    turtle.end_fill()

#Create a function for basic house construction
def draw_red_house():
    turtle.penup()
    turtle.goto(-350, -25)
    turtle.begin_fill()
    for i in range(0, 2):
        turtle.fillcolor("red")
        turtle.penup()
        turtle.pendown()
        turtle.forward(450)
        turtle.right(90)
        turtle.forward(200)
        turtle.right(90)
    turtle.end_fill()


def draw_brown_roof():
    #setting turtle variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-350, -25)
    pen.pendown()
    pen.color('brown')
    pen.begin_fill()
    #for loop to draw the front roof triangle
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()
    #draw side portion of the roof
    pen.begin_fill()
    pen.forward(450)
    pen.left(120)
    pen.forward(100)
    pen.left(60)
    pen.forward(350)
    pen.end_fill()
    pen.hideturtle()
 

def draw_green_roof():
    #setting turtle variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-350, -25)
    pen.pendown()
    pen.color('green')
    pen.begin_fill()
    #for loop to draw the front roof triangle
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()
    #draw side portion of the roof
    pen.begin_fill()
    pen.forward(450)
    pen.left(120)
    pen.forward(100)
    pen.left(60)
    pen.forward(350)
    pen.end_fill()
    pen.hideturtle()
 

def draw_yellow_roof():
    #setting turtle variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-350, -25)
    pen.pendown()
    pen.color('yellow')
    pen.begin_fill()
    #for loop to draw the front roof triangle
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()
    #draw side portion of the roof
    pen.begin_fill()
    pen.forward(450)
    pen.left(120)
    pen.forward(100)
    pen.left(60)
    pen.forward(350)
    pen.end_fill()
    pen.hideturtle()
   
def draw_black_roof_trimming():
    #setting turtle variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('black')
    pen.penup()
    pen.goto(-350, -25)
    pen.pensize(4)
    pen.pendown()
    #for loop to complete the front roof angle trimming
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    #complete side roof portion trimming
    pen.forward(450)
    pen.left(120)
    pen.forward(100)
    pen.left(60)
    pen.forward(350)
    pen.hideturtle()
 

def draw_white_roof_trimming():
    #setting turtle variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('white')
    pen.penup()
    pen.goto(-350, -25)
    pen.pensize(4)
    pen.pendown()
    #for loop to complete the front roof angle trimming
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    #complete side roof portion trimming
    pen.forward(450)
    pen.left(120)
    pen.forward(100)
    pen.left(60)
    pen.forward(350)
    pen.hideturtle()
   
def draw_brown_chimney():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-10, 110)
    pen.pendown()
    pen.color('brown')
    pen.begin_fill()
    #for loop to draw chimney
    for i in range(2):
        pen.forward(40)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()
 

def draw_red_chimney():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-10, 110)
    pen.pendown()
    pen.color('red')
    pen.begin_fill()
    #for loop to draw chimney
    for i in range(2):
        pen.forward(40)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()

def draw_orange_chimney():
    #settings variables
    pen = turtle.Turtle() 
    pen.speed(1)
    pen.penup()
    pen.goto(-10, 110)
    pen.pendown()
    pen.color('orange')
    pen.begin_fill()
    #for loop to draw chimney
    for i in range(2):
        pen.forward(40)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()


def draw_black_chimney_trimming():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('black')
    pen.penup()
    pen.goto(-10, 110)
    pen.pensize(4)
    pen.pendown()
    #for loop to complete chimney trimming
    for i in range(2):
        pen.forward(40)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.hideturtle()    
 

def draw_white_chimney_trimming():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('white')
    pen.penup()
    pen.goto(-10, 110)
    pen.pensize(4)
    pen.pendown()
    #for loop to complete chimney trimming
    for i in range(2):
        pen.forward(40)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.hideturtle()

def draw_windows_purple():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('purple')
    pen.penup()
    pen.goto(-235, -80)
    pen.pensize(4)
    pen.pendown()
    #for loop to complete first window outline 
    for i in range(2):
        pen.forward(70)
        pen.right(90)
        pen.forward(70)
        pen.right(90)
    pen.penup()
    #end loop
    #draw first window inner cross
    pen.goto(-200,-80)
    pen.pendown()
    pen.right(90)
    pen.forward(70)
    pen.penup()
    pen.goto(-235,-115)
    pen.pendown()
    pen.left(90)
    pen.forward(70)
    pen.penup()
    pen.goto(-35, -80)
    pen.pendown()
    #for loop to complete second window outline 
    for i in range(2):
        pen.forward(70)
        pen.right(90)
        pen.forward(70)
        pen.right(90)
    pen.penup()
    #end loop
    #draw second window inner cross
    pen.goto(0,-80)
    pen.pendown()
    pen.right(90)
    pen.forward(70)
    pen.penup()
    pen.goto(-35,-115)
    pen.pendown()
    pen.left(90)
    pen.forward(70)
    pen.penup()
    pen.hideturtle()

def draw_windows_blue():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('blue')
    pen.penup()
    pen.goto(-235, -80)
    pen.pensize(4)
    pen.pendown()
    #for loop to complete first window outline 
    for i in range(2):
        pen.forward(70)
        pen.right(90)
        pen.forward(70)
        pen.right(90)
    pen.penup()
    #end loop
    #draw first window inner cross
    pen.goto(-200,-80)
    pen.pendown()
    pen.right(90)
    pen.forward(70)
    pen.penup()
    pen.goto(-235,-115)
    pen.pendown()
    pen.left(90)
    pen.forward(70)
    pen.penup()
    #2nd window start
    pen.goto(-35, -80)
    pen.pendown()
    #for loop to complete second window outline 
    for i in range(2):
        pen.forward(70)
        pen.right(90)
        pen.forward(70)
        pen.right(90)
    pen.penup()
    #end loop
    #draw second window inner cross
    pen.goto(0,-80)
    pen.pendown()
    pen.right(90)
    pen.forward(70)
    pen.penup()
    pen.goto(-35,-115)
    pen.pendown()
    pen.left(90)
    pen.forward(70)
    pen.penup()
    pen.hideturtle()

def draw_doors_purple():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('purple')
    pen.penup()
    pen.goto(-125, -128)
    pen.pensize(4)
    pen.pendown()
    #for loop to draw doors
    for i in range(2):
        pen.forward(50)
        pen.right(90)
        pen.forward(90)
        pen.right(90)
    pen.penup()
    #draw doorknob
    pen.goto(-82, -180)
    pen.pendown()
    pen.begin_fill()
    pen.circle(2)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()

def draw_doors_blue():
  #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.color('blue')
    pen.penup()
    pen.goto(-125, -128)
    pen.pensize(4)
    pen.pendown()
    #for loop to draw doors
    for i in range(2):
        pen.forward(50)
        pen.right(90)
        pen.forward(90)
        pen.right(90)
    pen.penup()
    #draw doorknob
    pen.goto(-87, -180)
    pen.pendown()
    pen.begin_fill()
    pen.circle(2)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()

def draw_foundation():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-350, -225)
    pen.pensize(4)
    pen.pendown()
    pen.color('dark grey')
    pen.begin_fill()
    #for loop to draw foundation
    for i in range(2):
        pen.forward(450)
        pen.right(90)
        pen.forward(25)
        pen.right(90)
    pen.end_fill()
    pen.hideturtle()

def draw_driveway():
    #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-350, -220)
    pen.pensize(4)
    pen.pendown()
    pen.color('dark grey')
    pen.begin_fill()
    pen.right(60)
    pen.forward(150)
    pen.left(60)
    pen.forward(525)
    pen.left(140)
    pen.forward(200)
    pen.left(40)
    pen.forward(450)
    pen.end_fill()
    pen.penup()
    pen.hideturtle()


# main funciton to call the functions
def main():
    # draw sky
    environment()
    # draw backgroung
    draw_background()
    #screen window
    window = turtle.Screen()
    #ask user for weather
    cloud_color = window.textinput("Will it rain?", "Yes or no")
    if cloud_color == "no":
        draw_white_cloud()
    else:
        draw_rain_cloud()
        #draw_rain()
    draw_grass()
    #draw house
    draw_red_house()
    #draw roof elements
    #creating a screen window
    window = turtle.Screen()
    #asking user for roof color
    roof_color = window.textinput("ROOF COLOR", "Enter brown, green, or yellow:  ")
    if roof_color == "brown":
        draw_brown_roof()
    elif roof_color == "green":
        draw_green_roof()
    else:
        draw_yellow_roof()
    #end if
    #creating a screen window
    window = turtle.Screen()
    #asking for roof trimming color
    roof_trimming_color = window.textinput("ROOF TRIMMING COLOR", "Enter black or white:  ")
    if roof_trimming_color == "black":
        draw_black_roof_trimming()
    else:
        draw_white_roof_trimming()
    #end if
    #creating a screen window
    window = turtle.Screen()
    #asking for chimney color
    chimney_color = window.textinput("CHIMNEY COLOR", "Enter brown, red or orange:  ")
    if chimney_color == "brown":
        draw_brown_chimney()
    elif chimney_color == "red":
        draw_red_chimney()
    else:
        draw_orange_chimney() 
    #end if
    #creating a screen window
    window = turtle.Screen()
    #asking for chimney trimming color
    chimney_trimming_color = window.textinput("CHIMNEY TRIMMING COLOR", "Enter black or white:  ")
    if chimney_trimming_color == "black":
        draw_black_chimney_trimming()
    else:
        draw_white_chimney_trimming()    
    #end if
    
    #asking for windows color
    window_color = window.textinput("WINDOWS COLOR", "Enter purple or blue:  ")
    if window_color == "purple":
        draw_windows_purple()
    else:
        draw_windows_blue()   
    #end if
    #asking for door color
    door_color = window.textinput("DOOR COLOR", "Enter purple or blue:  ")
    if door_color == "purple":
        draw_doors_purple()
    else:
        draw_doors_blue()   
    #end if
    #asking to select house foundation or driveway 
    house_model = window.textinput("FOUNDATION/DRIVEWAY", "Enter house foundation, driveway or none:  ")
    if house_model == "foundation":
        draw_foundation()
    elif house_model == "driveway":
        draw_driveway()
    else:
        pass 
       #settings variables
    pen = turtle.Turtle()
    pen.speed(1)
    pen.penup()
    pen.goto(-150, 40)
    pen.pensize(5)
    pen.pendown()
    pen.color(special_color_one)
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    pen.penup()
    pen.goto(-150, 70)
    pen.color(special_color_two)
    pen.pendown()
    pen.left(40)
    pen.forward(50)
    pen.hideturtle()
    time.sleep(5) 



if __name__ == "__main__":
    main()