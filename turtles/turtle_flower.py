"""
 *****************************************************************************
   FILE:  turtle_flower.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: project 6

   DATE: 6 October 2017

   DESCRIPTION: draw a flower with the turtle

 *****************************************************************************
"""

import turtle


def main():
    """Main function to test your functions.
    You may put any code you like here."""

    t = turtle.Turtle()
    t.shape("turtle")
    t.pencolor("blue")

    # Uncomment if you want the turtle to go fast!
    t.speed(0)

    draw_square(t, 50)
    draw_pentagon(t, 50)

    # Uncomment to draw a parallelogram, once implemented
    t.up()
    t.goto(0, -100)
    t.down()
    draw_parallelogram(t, 150, 70, 50)

    # Uncomment to draw a flower
    #t.up()
    #t.goto(200, 200)
    #t.down()
    #t.pencolor("red")
    #draw_flower(t, draw_square, 50, 36)

    # Uncomment to draw a flower with 6 petals, once implemented
    t.up()
    t.goto(-200, 200)
    t.down()
    draw_flower(t, draw_pentagon, 50, 6)

    # Uncomment to draw a flower with your my_petal function, once implemented
    t.up()
    t.goto(-200, -200)
    t.down()
    draw_flower(t, my_petal, 50, 8)

    turtle.mainloop()


def draw_square(t, length):
    """Draws a square with length."""
    for count in range(4): # makes 4 connected line segments
        t.forward(length)
        t.left(90) # makes the angle between each line segment a right angle


def draw_pentagon(t, length):
    """Draws a pentagon with length."""
    for count in range(5): # makes 5 connected line segments
        t.forward(length)
        t.left(72) # makes the turtle turn 72 degrees to the left


def draw_parallelogram(t, length1, length2, angle):
    """Draws a parallelogram. First side has length = length1,
    second side has length = length2, and angle is the angle of
    the first turn the turtle makes."""
    for _ in range(2): # executes the drawing both sides twice
        t.forward(length1) # draws the first side
        t.left(angle) # makes the turtle turn to the left the desired amount
        t.forward(length2) # draws the second length
        t.left(180 - angle) # makes the turtle turn left x many degrees so the
                            # parallelogram has an internal angle of 360 degrees


def draw_flower(t, petal_shape, length, petal_count):
    """Draws a flower with length."""
    for petal in range(petal_count): # loops the body so the flower has the
                                     # desired number of petals
        petal_shape(t, length) # passes the desired shape to a prespecified draw
                               # function written for the shape
        t.left(360/petal_count) # turne the turtle left a proportionately
                                # appropriate amount


def my_petal(t, length):
    """Draws a petal. May or may not use length.
    Note: the turtle must return to its original position and heading
    at the end of drawing the petal; otherwise, this won't work with
    draw_flower at arbitrary positions and headings."""

# a cool pattern
    t.forward(length)
    t.right(120)
    for _ in range(2):
        t.forward(length)
        t.right(60)
    t.left(90)
    for _ in range(2):
        t.forward(length)
        t.right(60)
    t.forward(length)


# Uncomment for another cool pattern
#    for _ in range(3):
#        t.forward(length)
#        t.right(120)
#    t.left(120)
#    for _ in range(2):
#        t.forward(length)
#        t.right(60)
#    t.forward(length)


# Uncomment if you're a real star!
#    for _ in range(5):
#        t.forward(length * 2)
#        t.right(144)

    

if __name__ == "__main__":
    main()
