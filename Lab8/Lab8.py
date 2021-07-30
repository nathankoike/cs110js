import turtle


def main():

    #greet("Howdy")
    #greet("Hi", "Alice")
    #greet("beep boop", name="robot")

    #print(area_of_rectangle(2))

    #print_triangle(4)

    # Call the functions you are testing here.
    #fractal_main()

    #print(enigma('abcdefghijklmnopqrstuvwxyz'))
    #print(conundrum(3))

    print(reverse('name'))
    print(double_letters("I'M SCREAMING!!!"))


def greet(greeting, name="person"):
    print(greeting, name)


def area_of_rectangle(length, width=0):
    Area = length * width
    if Area == 0:
        Area = length ** 2
    return Area


def print_triangle(rows, char='*'):
    if rows > 0:
        print(rows * char)
        print_triangle(rows - 1, char)


def fractal_main():
    t = turtle.Turtle()
    t.speed(0)

    turtle.tracer(False)

    t.setheading(90)
    fractal(t, 200)

    turtle.update()

    turtle.mainloop()  # Prevents the screen from closing automatically.


def fractal(t, length, level=3):

    TURNS = 20
    ANGLE = 18
    LENGTH_REDUCTION = 1.25

    if level == 0:
        return

    for _ in range(TURNS):
        t.forward(length)
        fractal(t, length / LENGTH_REDUCTION, level - 1)
        t.backward(length)
        t.left(ANGLE)


def enigma(string):
    if string == "":
        return ""
    elif string[0] in "aeiou":
        return string[0] + enigma(string[1:])
    else:
        return enigma(string[1:])


def conundrum(x):
    if x <= 0:
        return 1
    else:
        return conundrum(x - 1) * 2


def reverse(string):
    reversed = ''
    if len(string) > 0:
        reversed += string[-1]
        reversed += reverse(string[:len(string) - 1])
    return reversed

def double_letters(string):
    doubled = ''
    if string[0].isalpha():
        doubled += string[0] * 2
        doubled += double_letters(string[1:])
    elif string[0] == '!':
        doubled += '!' * 3
        doubled += double_letters(string[1:])
    else:
        doubled += string[0]
        doubled += double_letters(string[1:])
    return doubled


main()
