"""
Homework 7

This file contains a class to manage a clock.
"""


class Clock(object):
    """Stores the time on a clock. Can display in 12-hour or 24-hour format."""

    def __init__(self, hrs, mins, secs):
        """Constructor for Clock. Expects hrs in 24-hour format,
        but starts off in 12-hour format."""
        self._hours = hrs
        self._minutes = mins
        self._seconds = secs

        # If true, displays 24-hour format.
        self._24_hour_format = False

    def __str__(self):
        result = ""
        if self._24_hour_format:
            result += "%02i:%02i:%02i" % (self._hours, self._minutes,
                                          self._seconds)
        else:
            hours = self._hours % 12
            if hours == 0:
                hours = 12

            result += "%02i:%02i:%02i" % (hours, self._minutes, self._seconds)

            if self._hours < 12:
                result += " AM"
            else:
                result += " PM"

        return result

    def tick(self):
        """Moves clock ahead one second."""
        self._seconds += 1

        # Check if need new minute
        if self._seconds >= 60:
            self._seconds = self._seconds % 60
            self._minutes += 1

        # Check if need new hour and day
        if self._minutes >= 60:
            self._minutes = self._minutes%60
            self._hours += 1
        if self._hours >= 24:
            self._hours = self._hours % 24

    def toggle_24_hour_format(self):
        """Toggles between 12 and 24 hour format. If clock was in 12-hour
        format, should change to 24-hour format, and vice versa"""

        # 3. YOUR CODE GOES HERE
        self._24_hour_format = True


def main():
    my_clock = Clock(10, 00, 00)

    my_clock.toggle_24_hour_format()

    print(my_clock)

    for _ in range(3000):
    
        my_clock.tick()
        
        print(my_clock)


if __name__ == "__main__":
    main()
