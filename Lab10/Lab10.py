from cs110graphics import *


class Robot():
    """ A robot has a body and can move around within the graphics window. """


    def __init__(self, win, size, center, body, body_fill, eye_fill, direction):
        """ The robot Constructor. """

        self._win = win
        self._size = size
        self._center = center 
        self._dir = direction

        outline = Square(self._win, self._size, self._center)
        outline.set_fill_color(body_fill)

        # The robot's eye is proportional to the size of its outline.
        eye = Square(self._win, round(self._size / 3), self._center)
        eye.set_fill_color(eye_fill)

        self._body = [outline, eye]


    def move_eye(self):

        """ You will write this code, which should shift the robot's eye
            in accordance with the direction the robot is facing. """

        cx = self._center[0]
        cy = self._center[1]
        shift = self._size / 5 # how far the eye shifts

        if self._dir == 0:
            self._body[1].move_to((cx, cy))
        elif self._dir == 1:
            self._body[1].move_to((cx, int(cy - shift)))
        elif self._dir == 2:
            self._body[1].move_to((int(cx + shift), cy))
        elif self._dir == 3:
            self._body[1].move_to((cx, int(cy + shift)))
        elif self._dir == 4:
            self._body[1].move_to((int(cx - shift), cy))



    def set_direction(self, direction):

        """ Simply sets the direction for the robot, with 1 = up,
            2 = right, 3 = down, 4 = left. """

        self._dir = direction


    def add_robot(self, win):

        """ Add a robot to the window  win . """
        
        for obj in self._body:
            win.add(obj)


    def move_all(self, dx, dy):

        """ Move all objects in the list  objects. """

        for obj in self._body:
            obj.move(dx, dy)


    def get_size(self):

        """ Returns the size (the side length) of the robot. """

        return self._size



def begin(win):

    """ This function is akin to a main() function. """

    # When we run the graphics package, there must be a yield statement
    # somewhere in the program.
    yield 1

    # We create and then add a robot named Ava to our graphics window.
    Ava = Robot(win, 30, (100, 100), [], 'yellow', 'blue', 0)
    Ava.set_direction(2)
    Ava.move_eye()
    Ava.add_robot(win)

    # create and add a robot named Eve to the window
    Eve = Robot(win, 30, (301, 100), [], 'white', 'green', 0)
    Eve.set_direction(4)
    Eve.move_eye()
    Eve.add_robot(win)

    for _ in range(28):
        Ava.move_all(3, 0)
        Eve.move_all(-3, 0)
        yield 17




def program(win):
    RunWithYieldDelay(win, begin(win))


if __name__ == '__main__':
    StartGraphicsSystem(program)
