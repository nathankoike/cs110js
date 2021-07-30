# Skeleton program for Lab 6 (Perkins)

import turtle


def main():
    # The turtle is named  t  here in main(), and you should
    # pass it to each function, where I call the turtle  trixie .
    t = turtle.Turtle()

    # Call functions from here.
    dice(t)

    turtle.mainloop()  # Prevents the screen from closing automatically.


def dots(trixie):
    """
    Argument list:

    trixie = the name of the turtle

    This function draws a palette of dots that is intended to guide
    the viewer to an understanding of the three numbers used when
    colormode = 255.
    """
    trixie.hideturtle()
    trixie.speed('fast')
    for y in range(0, 240, 20):
        for x in range(0, 240, 20):
            trixie.up()
            trixie.goto(x, y)
            trixie.down()
            trixie.color(x, y, 0)
            trixie.dot(20)


def triangles(trixie):
    """
    Argument list:

    trixie = the name of the turtle

    The function's purpose is kept hidden for now, because we
    would like you to decipher it by reading.
    """
    trixie.width(5)
    for x in range(-100, 100, 40):
        draw_equil(trixie, x, 0, 40)
    trixie.hideturtle()


def draw_equil(trixie, x, y, size):
    """
    Argument list:

    trixie = the name of the turtle
    x, y = pixel at the start of drawing
    size = length of one side of the triangle

    The function's purpose is kept hidden for now, because we
    would like you to decipher it by reading.
    """
    trixie.up()
    trixie.goto(x, y)
    trixie.pencolor('black')

    trixie.fillcolor('red')
    trixie.begin_fill()
    trixie.down()
    for i in range(3):
        trixie.forward(size)
        trixie.left(120)
    trixie.end_fill()

def squares(trixie):
    """
    Argument list:

    trixie = the name of the turtle

    Draws 5 squares next to each other, each filled with a color.
    """
    trixie.width(5)
    for x in range(-100, 100, 40):
        draw_square(trixie, x, 0, 40)
    trixie.hideturtle()


def draw_square(trixie, x, y, size):
    """
    Argument list:

    trixie = the name of the turtle
    x, y = pixel at the start of drawing
    size = length of one side of the squares

    draws 5 squares nest to each other, eahc filled with a color
    """
    trixie.up()
    trixie.goto(x, y)
    trixie.pencolor('black')

    trixie.fillcolor('red')
    trixie.begin_fill()
    trixie.down()
    for i in range(4):
        trixie.forward(size)
        trixie.left(90)
    trixie.end_fill()


def nest(trixie, nom):
    """
    Argument list:

    trixie = the name of the turtle
    nom = a number that controls the current pencolor
    """
    if nom > 20:
        trixie.width(5)
        trixie.pencolor(nom, nom, nom)
        trixie.up()
        trixie.home()
        trixie.setheading(270)
        trixie.forward(nom // 2)
        trixie.right(90)
        trixie.forward(nom // 2)
        trixie.left(180)
        trixie.down()
        trixie.setheading(0)
        for _ in range(4):
            trixie.forward(nom)
            trixie.left(90)

        nest(trixie, nom - 20)


def dice(trixie):
    number = int(input('Enter a number from 1 to 6: '))
    # Feel free to tinker with these settings:
    pip_size = 12 
    trixie.width(5)
    draw_square(trixie, 0, 0, 60)
    trixie.pencolor('black')

    center = (30,30)
    corners = [(15, 15), (15, 45), (45, 15), (45, 45)]
    two_corners = [(15, 15), (45, 45)]
    middle = [(15, 30), (45, 30)]
    locations = []
    if number % 2 == 1: 
        locations.append(center)
        if number == 3:
            for i in two_corners:
                locations.append(i)
        elif number == 5:
            for i in corners:
                locations.append(i)
    else:
        if number == 2:
            for i in two_corners:
                locations.append(i)
        elif number == 4:
            for i in corners:
                locations.append(i)
        else:
            for i in corners:
                locations.append(i)
            for i in middle:
                locations.append(i)

    draw_pips(trixie, locations, 10)




    trixie.hideturtle()


def draw_pips(trixie, lst, size):
    """
    Argument list:

    trixie = the name of the turtle
    lst = a list of pip locations
    size = the size of each pip

    This function is called by dice() and will draw pips at
    specified locations within a square already drawn by dice().
    """
    for entry in lst:
        trixie.up()
        trixie.goto(entry)
        trixie.down()
        trixie.dot(size)


def hexagon(trixie, size):
    


main()
