"""
 *****************************************************************************
   FILE:  checkerboard.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 6

   DATE: 6 Octuber 2017

   DESCRIPTION: Use turtle graphics to draw a checkerboard

 *****************************************************************************
"""

import turtle


def main():
    t = turtle.Turtle()
    t.speed(0)
    # draw_square(t, 100)
    t.up()
    t.goto(-200, -200)
    t.down()
    draw_checkerboard(t, 50, 8, (60, 60, 0))

    t.up()
    t.left(30)
    t.forward(50)
    t.down()
    draw_checkerboard(t, 10, 10, "blue")

    turtle.mainloop()


def draw_square(t, length):
    """Use t to draw a square with length."""

    for count in range(4):
        t.forward(length)
        t.left(90)
    t.forward(length) # this moves the turtle over so the next square is drawn
                      # one length to the right to prevent overlapping and
                      # removing squares


def draw_checkerboard(t, length, squares_per_side, color):
    """ uses the draw_square function to draw a checkerboard """

    
    for i in range(squares_per_side): # counts the number of rows drawn
        t.down()
        if i % 2 == 0: # uses the number of previously drawn rows to determine
                       # the lead square's color
            for _ in range(squares_per_side // 2): # draws the row. the reason
                                                   # this uses integer division
                                                   # is it is impossible to draw
                                                   # a fraction of a row. the
                                                   # reason the denominator is 2
                                                   # is because the body of the
                                                   # loop draws 2 squares each
                                                   # time it executes
                t.color(color)
                t.begin_fill()
                draw_square(t, length)
                t.end_fill()
                t.begin_fill()
                t.color('white')
                draw_square(t, length)
                t.end_fill()
        else:
            for _ in range(squares_per_side // 2):
                t.color('white')
                t.begin_fill()
                draw_square(t, length)
                t.end_fill()
                t.begin_fill()
                t.color(color)
                draw_square(t, length)
                t.end_fill()

        # this next section of code moves the turtle up one row height because
        # the row drawings start at the bottom of each row and resets the turtle
        # to the left-most edge of the checkerboard
        t.up()
        t.left(180)
        t.forward(length * squares_per_side)
        t.right(90)
        t.forward(length)
        t.right(90)

    # this next section of code moves the turtle to the top left of the
    # checkerboard and draws a black border around the checkerboard
    t.up()
    t.color('black')
    t.right(90)
    t.down()
    draw_square(t, length * squares_per_side)
    t.up()
    t.left(180)
    t.forward(length * squares_per_side)
    t.right(90)
    


main()
