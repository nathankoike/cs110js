class Building():
    """ The Building class contains Elevator objects. """

    def __init__(self, num_elevators = 1, top_floor = 1):
        # The Building begins with this attribute:
        self._num_elevators = num_elevators
        self._top_floor = top_floor

        # We create the elevators just once, so we include that
        # code in the __init__ method. First, we create an empty
        # list into which we will place our Elevator objects:
        self._elevs = []

        # Now we fill the list with those Elevator objects.
        # All elevators start on the first floor with no current
        # direction, no goal, no buttons pushed.
        for elev in range(num_elevators):
            self._elevs.append(Elevator(elev, 1, 'up', False, 0, []))

    def __str__(self):
        # This method prints the current status of all Elevators.
        # We give this job to the Building object because we consider
        # the Building to be the manager of the Elevators.
        full_report = ''
        # (Note: \n is equivalent to 'move to the next line')
        for elev in self._elevs:
            report = '\n +++ Elevator %i +++ \n \n'  % elev.get_number()
            report += ' On floor:           %i \n'   % elev.get_floor()
            report += ' Aimed in direction: %s \n'   % elev.get_dir()
            report += ' Currently moving:   %s \n'   % elev.is_moving()
            report += ' Target floor:       %i \n'   % elev.get_target()
            report += ' Buttons pushed:     %s \n'   % elev.get_buttons()
            full_report += report
        return full_report

    #def move(self, elev, goal):



class Elevator():
    """ Elevator objects are created by a Building object. """

    def __init__(self, number, floor, direction, moving, target, buttons):
        # Each Elevator begins with these attributes:
        self._number = number  # The identification number of the Elevator
        self._floor = number + 1    # The current floor of the Elevator
        self._dir = direction   # The current direction (up / down)
        self._moving = moving   # Boolean that reports if Elevator is moving
        self._target = target   # The floor where the Elevator is heading
        self._buttons = buttons # A list of the buttons that are pushed

    def get_number(self): # this is an accessor
        return self._number

    def get_floor(self): # this is an accessor
        return self._floor

    def get_dir(self): # this is an accessor
        return self._dir

    def get_target(self): # this is an accessor
        return self._target

    def is_moving(self): # this is an accessor
        return self._moving

    def get_buttons(self): # this is an accessor
        return self._buttons

    def toggle_elev(self):
        self._moving = not self._moving

    def set_target(self, goal): # this is a mutator
        self._target = goal

def main():
    """ From main() we create a Building and use its methods to run a
        system of Elevators within it. """

    Science = Building(3, 4)   # Creates a building object called Science that
                            # will have 3 Elevator objects.

    print(Science)          # Calls the __str__ method of Building to give a
                            # status report of all Elevator objects in the
                            # Science object.

    Root = Building(1, 3)

    print(Root)

    Science._elevs[0].toggle_elev()
    print(Science)
    Science._elevs[0].set_target(4)

    turn = 1
    while turn < 6:
        Science._elevs[0].move_elev(Science)
        print('\n=== Turn', turn, '===')
        print(Science)
        turn += 1


if __name__ == '__main__':
    main()