"""
 *****************************************************************************
   FILE:        microwave.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 3

   DATE: 9/11/17

   DESCRIPTION: write a program that counds down as a microwave would

 *****************************************************************************
"""


def main():
    """ takes a user input and counts down from that time like a microwave """
    startTime = input('Enter the digits as input to the microwave: ')
    
    '''
    first if statement: checks to see if the input contains a colon
    this knowledge allows the time to be split into minutes and seconds
    splitting the time allows a total time to be calculated so a for loop
    can print the time counting down
    first else statement: allows for the time to be set directly to the input
    if the user did not enter any minutes
    the if statement within the else statement adds a zero if the second count
    falls below 10
    '''
    if ':' in startTime:
        i = startTime.index(':')
        minutes = int(startTime[0: i])
        minutes_in_seconds = minutes * 60
        seconds = int(startTime[(i+1):])
        time = seconds + minutes_in_seconds
        if seconds < 10:
            seconds = '0' + str(seconds)
    else:
        minutes = 0
        seconds = int(startTime)
        time = minutes + seconds
        if seconds < 10:
            seconds = '0' + str(seconds)
    '''
    the for loop prints out the time then enters into an if/else control structure
    the if statement subtracts 1 from the seconds and, contitionally, adds a zero
    to the front of the second counter if it falls below 10
    the else statement subtracts 1 from the minutes and adds 59 to the seconds
    if the seconds reach 0
    '''
    for value in range(time):
        print(str(minutes) + ':' + str(seconds))
        if int(seconds) > 0:
            seconds = int(seconds) - 1
            if seconds < 10:
                seconds = '0' + str(seconds)
        else:
            minutes = minutes - 1
            seconds = int(seconds) + 59
    # prints 0:00 after the for loop ends so the timer comes to a complete stop
    print('0:00')


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
