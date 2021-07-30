"""
 *****************************************************************************
   FILE:  bots.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 9

   DATE: 4 November 2017

   DESCRIPTION: Use pseudo-graphical objects to control the movement of graphics
                on a window

 *****************************************************************************
"""

from cs110graphics import *

import random 

class Bot(object):
    def __init__(self, win, width, center, direction = 'east', speed = 20):
        ''' Initialize the Bot object with necessary attributes '''
        self._window = win
        self._width = width
        self._center = center
        self._direction = direction
        self._speed = speed

        # these attributes are the individual coordinates of the center. cx is
        # the x coordinate and cy is the y coordinate
        self._cx = self._center[0]
        self._cy = self._center[1]

        # call the robot function to make the bot as a pseudo-graphical object
        self._parts = Robot(win, width, center)
        
    def add_to_window(self):
        ''' add the robot to the window using the list returned by the function
            that created the pseudo-graphical object '''
        for part in self._parts:
            self._window.add(part)
    
    def add_handler(self, handler):
        for part in self._parts:
            part.add_handler(handler)
            
    def move(self):
        ''' make the bot move speed pixels in a direction and change the center
            so collision detection works properly '''
        # this series of if statements moves the bot in the correct direction.
        # this also changes the center of each bot so that collision detection
        # works properly. the body of each if statement moves the pseudo-
        # graphical object then updates where the center should be
        
        # these are the vertical directions:
        if self._direction == 'north':
            for part in self._parts:
                part.move(0, -self._speed)
            self._cy -= self._speed
            self._center = (self._cx, self._cy)
        if self._direction == 'south':
            for part in self._parts:
                part.move(0, self._speed)
            self._cy += self._speed
            self._center = (self._cx, self._cy)

        # these are the horizontal directions:
        if self._direction == 'east':
            for part in self._parts:
                part.move(self._speed, 0)
            self._cx += self._speed
            self._center = (self._cx, self._cy)
        if self._direction == 'west':
            for part in self._parts:
                part.move(-self._speed, 0)
            self._cx -= self._speed
            self._center = (self._cx, self._cy)

    def turn_left(self):
        ''' make the bot turn left. north becomes west, west becomes south, etc.
            '''
        # this is a list of directions for indexing to allow the turning
        # mechanic to function properly
        directions = ['north', 'east', 'south', 'west']

        # this finds the index number of the current direction so it can be
        # modified to make the bot turn left
        index_no = directions.index(self._direction)

        # this calculates what the index number of the new direction will be
        left = index_no - 1

        # the purpopose of this if statement is to ensure that the new index
        # number always exists in the list and the bot can always turn left
        if left < 0:
            left = 3

        #set the direction of the bot to be 90 degrees to the left
        self._direction = directions[left]

        # lastly, move the controller to indicate the current direction of the
        # bot
        self._parts[1].move_to(self._center)

        # this series of if statements moves the controller of the bot to the
        # correct spot within the bot to indicate the bot's current direction
        
        # these are the vertical directions
        if self._direction == 'north':
            self._parts[1].move_to(self._center)
            self._parts[1].move(0, -self._width // 4)
        if self._direction == 'south':
            self._parts[1].move_to(self._center)
            self._parts[1].move(0, self._width // 4)

        # these are the horizontal directions:
        if self._direction == 'east':
            self._parts[1].move_to(self._center)
            self._parts[1].move(self._width // 4, 0)
        if self._direction == 'west':
            self._parts[1].move_to(self._center)
            self._parts[1].move(-self._width // 4, 0)

    def turn_right(self):
        ''' make the bot turn right. north becomes east, east becomes south,
            etc. '''
        # this is a list of directions for indexing to allow the turning
        # mechanic to function properly
        directions = ['north', 'east', 'south', 'west']

        # this finds the index number of the current direction so it can be
        # modified to make the bot turn right
        index_no = directions.index(self._direction)

        # this calculates what the index number of the new direction will be
        right = index_no + 1

        # the purpopose of this if statement is to ensure that the new index
        # number always exists in the list and the bot can always turn right
        if right > 3:
            right = 0

        #set the direction of the bot to be 90 degrees to the right
        self._direction = directions[right]

        # lastly, move the controller to indicate the current direction of the
        # bot
        self._parts[1].move_to(self._center)

        # this series of if statements moves the controller of the bot to the
        # correct spot within the bot to indicate the bot's current direction
        
        # these are the vertical directions
        if self._direction == 'north':
            self._parts[1].move_to(self._center)
            self._parts[1].move(0, -self._width // 3)
        if self._direction == 'south':
            self._parts[1].move_to(self._center)
            self._parts[1].move(0, self._width // 3)

        # these are the horizontal directions:
        if self._direction == 'east':
            self._parts[1].move_to(self._center)
            self._parts[1].move(self._width // 3, 0)
        if self._direction == 'west':
            self._parts[1].move_to(self._center)
            self._parts[1].move(-self._width // 3, 0)
    
    def speed_up(self):
        ''' increase the speed of the bot by a set amount '''
        self._speed += 15

    def slow_down(self):
        ''' decrease the speed of the bot by a set amount '''
        self._speed -= 15
    
    def crash(self):
        ''' cause an obvious, visual chage to the bot to indicate that a crash
            occurred '''
        # set the depth of the controller to be below the chassis as if the bot 
        # had flipped over from the impact of the crash
        self._parts[1].set_depth(50)
        

    def uncrash(self):
        ''' restore the bot to its state before the effect from the crash method
        '''
        self._parts[1].set_depth(30)

    def get_width(self):
        ''' return the width of the bot '''
        return self._witdh

    def get_center(self):
        ''' return the center of the bot '''
        return self._center

    def overlaps(self, other):
        ''' check to see if the bots overlap at all '''
        # this variable is the horizontal bounds of the self bot
        selfHoriz = [self._cx + (self._width // 2),
                     self._cx - (self._width // 2)]

        # this variable is the horizontal bounds of the other bot 
        otherHoriz = [other._cx + (other._width // 2),
                     other._cx - (other._width // 2)]

        # this variable is the vertical bounds of the self bot
        selfVert = [self._cy + (self._width // 2),
                     self._cy - (self._width // 2)]

        # this variable is the vertical bounds of the other bot 
        otherVert = [other._cy + (other._width // 2),
                     other._cy - (other._width // 2)]

        # these variables represent whether there is an overlap in each of the
        # horizontal and vertical values and is a boolean value. these will be
        # used again later
        horizOver = False
        vertOver = False

        # the purpose of this if statement is to see if there is a possible
        # overlap on the horizontal bounds
        if selfHoriz[0] > otherHoriz[1] or selfHoriz[1] < otherHoriz[0]:
            horizOver = True

        # the purpose of this if statement is to see if there is a possible
        # overlap on the vertical bounds
        if selfVert[0] > otherVert[1] or selfVert[1] < otherVert[0]:
            vertOver = True

        # this if statement returns True only if there is an overlap in both the
        # vertical and horizontal bound spaces
        if horizOver and vertOver:
            return True

        return False

        
class BotHandler(EventHandler):
    def __init__(self, bot):
        EventHandler.__init__(self)
        self._bot = bot

    def handle_mouse_release(self, event):
        ''' tell the bot what to do when clicked on '''
        MoT = random.randrange(2) # this variable is Move or Turn

        # this if/else statement uses a % to determine whether the bot is
        # going to move or turn
        if MoT % 2 == 0:
            self._bot.move()
        else:
            LoR = random.randrange(2) # this variable is Left or Right

            # this if/else statement uses a % to determine which direction the
            # bot is going to turn
            if LoR % 2 == 0:
                self._bot.turn_left()
            else:
                self._bot.turn_right()

def Robot(win, width, center):
    ''' create a pseudo-graphical object to move all the pieces of a bot in a
        unified manner. this also 'builds' the bot '''
    # the chassis is the main unit of the bot and will have a higher depth
    chassis = Square(win, width, center,)
    chassis.set_depth(30)
    chassis.set_fill_color('gray')

    # the controller is the 'brain' or 'eye' of the robot and will have a lower
    # depth so that it can be seen and animated. it will also be distinguished
    # by having a different color than the chassis
    controller = Circle(win, width // 4, center)
    controller.set_depth(20)
    controller.set_fill_color('blue')

    # return a list of the the components to be moved in a unified manner
    return [chassis, controller]
            
def program(win):
    # change this as you see fit!
    bot = Bot(win, 100, (75, 75))
    bot.add_to_window()
    bot.add_handler(BotHandler(bot))

    bot2 = Bot(win, 50, (300, 300))
    bot2.add_to_window()
    bot2.add_handler(BotHandler(bot2))


def main():
    StartGraphicsSystem(program)

if __name__ == "__main__":
    main()
