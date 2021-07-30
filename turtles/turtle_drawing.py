"""
 *****************************************************************************
   FILE:  turtle_drawing.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 6

   DATE: 6 October 2017

   DESCRIPTION: take user inputs and allow the user to draw using the turtle

 *****************************************************************************
"""

import turtle

distance = 30


def main():
    michelangelo = turtle.Turtle()
    turtle_drawing(michelangelo)


def turtle_drawing(t):
    """ """

    # This allows you to change the value of the global variable distance
    global distance

    print("\nThe commands are: w, a, s, d, color, distance, width, goto, quit")

    user_input = input("Enter a command: ")

    if user_input == "w":
        t.setheading(90)
        t.forward(distance)
    elif user_input == "a":
        t.setheading(180)
        t.forward(distance)
    elif user_input == "s":
        t.setheading(270)
        t.forward(distance)
    elif user_input == "d":
        t.setheading(0)
        t.forward(distance)
    elif user_input == "quit":
        return
    elif user_input == 'color': # allows the user to enter a color as a string
                                # and change the color
        color = input('Enter a color: ') # no str() is necessary because inputs
                                         # are always str by default
        t.color(color)
    elif user_input == 'distance': # allows the user to change how long each
                                   # line segment is
        distance = int(input('Enter a integer: '))
    elif user_input == 'width': # allows the user to change the width of the pen
                                # the turtle uses
        width = int(input('Enter a pen width: '))
        t.width(width)
    elif user_input == 'goto': # allows the user to enter coordinates for the
                               # turtle to move to without drawing a line
        t.up() # raises the pen so the turtle doesn't draw
        x = int(input('Enter an x-coordinate: '))
        y = int(input('Enter an y-coordinate: '))
        t.goto(x, y) # sends the turtle to the specified coordinates
        t.down() # lowers the pen so the turtle can con tinue to draw
        

    turtle_drawing(t)


main()
