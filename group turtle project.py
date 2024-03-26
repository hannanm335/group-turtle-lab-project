#import turtle library
import turtle

#define shapes with list
valid_shapes = ["classic", "arrow", "turtle", "circle", "square", "triangle"]

#define colors with list
valid_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'black', 'white']

#function to ask the user to choose a shape
def ask_shape_choice():
    answer = turtle.textinput("Shape Choice", "Enter new shape for turtle out of classic, arrow, turtle, circle, square, and triangle: ").lower()

