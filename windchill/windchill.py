"""
 *****************************************************************************
   FILE:        windchill.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: windchill

   DATE: 8/28/17

   DESCRIPTION: this is a program to find the windchill factor with a user defined air temperature and wind speed

 *****************************************************************************
"""


def main():
    """ finding windchill given two user inputs """
    print("Welcome to the windchill calculator!")
    temp = float(input("Enter the temperature: "))
    speed = float(input("Enter the wind speed: "))
    # CITE: http://www.onlineconversion.com/windchill.htm
    # DETAILS: the formula for finding wind chill given a temperature and wind speed from a free, online conversion website
    chill = (((0.6215 * temp) + 35.74) - (35.75 * (speed**0.16)) + (0.4275 * temp * (speed**0.16)))
    print("At", temp, "degrees, with a wind speed of", speed, "miles per hour,")
    print("the windchill is:", chill, "degrees")



# this invokes the main function.  It is always included in our python programs
if __name__ == "__main__":
    main()
