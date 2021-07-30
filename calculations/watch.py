"""
 *****************************************************************************
   FILE:        watch.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 2

   DATE: 9/6/17

   DESCRIPTION: make a program that tells the correct time of an upside down
                watch

 *****************************************************************************
"""


def main():
    """ takes user inputted times and converts them to be correct on an
        upside down watch"""
    # RAW is an unprocessed time
    timeRAW = str(input("What time does your upside-down watch read (hours:minutes)? "))
    # conversions to the corrected time
    timeHrs = int(timeRAW[0:(timeRAW.index(':'))])
    timeMins = int(timeRAW[(timeRAW.index(':'))+1:])
    timeHrs_inMins = 60 * timeHrs
    timeMins_total = timeHrs_inMins + timeMins
    timeMins_fixed = timeMins_total + 390
    # final here refers to the corrected time not the time that will print out
    timeHrs_final = int(timeMins_fixed // 60)
    timeMins_final = int(timeMins_fixed % 60)

    # disp denotes a time that will print
    # this if/else statement exists to return hours in a 12-hour format and can
    # be taken out if a 24-hour format is desired
    if timeHrs_final > 12:
        timeHrs_disp = str(timeHrs_final - 12)
    else:
        timeHrs_disp = str(timeHrs_final)

    timeMins_dispBase = str(timeMins_final)
    zero_timeMins_dispBase = '0'+timeMins_dispBase
    timeMins_disp = zero_timeMins_dispBase[-2:]

    print("The right-side-up time is:", timeHrs_disp + ':' + timeMins_disp)


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
