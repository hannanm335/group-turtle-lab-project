#import turtle library
import turtle
import time

# function to set up turtle environment
def environment():
    #set up turtle environment
    screen = turtle.Screen()
    screen.setup(width= 800, height = 800)
    screen.bgcolor('skyblue')

def draw_sunny_background():
    pen = turtle.Turtle()
    pen.speed(4) # set the drawing speed to maxium

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
    turtle.goto(120, 240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(50, 215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(130, 165)
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

    turtle.penup()
    turtle.goto(70, 140)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(20, 170)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

#rainy background
def rainy_background():
    turtle.bgcolor("light grey")
    turtle.speed(4)

#draw rainy cloud
def draw_rain_cloud():
    turtle.penup()
    turtle.goto(250, 250)
    turtle.speed(4)
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

def draw_rain():
    # set up rain
    turtle.goto(300,250)
    turtle.right(90)
    turtle.pencolor("dark blue")
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    turtle.penup()
    turtle.goto(280, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(260,250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    
    turtle.penup()
    turtle.goto(240, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(220,250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    
    turtle.penup()
    turtle.goto(200, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()

    turtle.goto(200,250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()
    
    turtle.penup()
    turtle.goto(180, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(160, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(140, 250)
    turtle.pendown()
    turtle.penup()

    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(120, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(100, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(80, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(60, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.goto(40, 250)
    turtle.pendown()
    for i in range(10):
        turtle.forward(15)
        turtle.penup()
        turtle.forward(5)
        turtle.pendown()

    turtle.penup()
    turtle.left(90)
    turtle.hideturtle()


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

def thank_you():
    turtle.penup()
    turtle.goto(0,0)
    turtle.hideturtle()
    turtle.clear()
    turtle.write("Group project by Viswa, Adam and Monique", align="center", font=("Arial", 16, "bold"))
    #pause for 2 seconds
    time.sleep(2)
    #clear screen
    turtle.clear()
    turtle.write("Thank you for your time.", align="center", font=("Arial", 16, "bold"))
    #pause for 2 seconds
    time.sleep(2)
    #quit program
    turtle.bye()

# main funciton to call the functions
def main():
    # draw sky
    environment()
    #screen window
    window = turtle.Screen()
    #ask user for weather
    cloud_color = window.textinput("Will it rain?", "Yes or no")
    if cloud_color == "no":
        draw_sunny_background()
        draw_white_cloud()
    else:
        rainy_background()
        draw_rain_cloud()
        draw_rain()
    #draw grass
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
    chimney_color = window.textinput("CHIMNEY COLOR", "Enter brown or red:  ")
    if chimney_color == "brown":
        draw_brown_chimney()
    else:
        draw_red_chimney()
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
    #thank you message
    thank_you()
 

if __name__ == "__main__":
    main()
