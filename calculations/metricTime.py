"""
 *****************************************************************************
   FILE:        metricTime.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 2

   DATE: 9/7/17

   DESCRIPTION: a program that converts Earth time to "metric" time

 *****************************************************************************
"""

def main():
    """ takes a user input and converts it to "metric time" through
    calculations """

    timeEarth = input("Enter the time of day in military time (HH:MM:SS): ")
    timeEarth_str = str(timeEarth)

    timeHrs_int = int(timeEarth_str[0:(timeEarth_str.index(':'))])
    timeMins_int = int(timeEarth_str[(timeEarth_str.index(':'))+1:-3])
    timeSec_int = int(timeEarth_str[-2:])

    # unit is seconds
    timeTotal = (timeHrs_int * 3600) + (timeMins_int * 60) + timeSec_int
    # ratio is inverted to prodive something to multiply by instead of divide
    # I felt it was unnecessary to use a variable to represent the amount of
    # seconds in a day because that number is only used once and a variable
    # would be more typing than typing out the actual number
    timeRatio = 100000 / 86400

    # conversions start here
    metricTotal = timeRatio * timeTotal
    metricHrs = metricTotal // 1000
    metric_without_hours = metricTotal - (1000 * metricHrs)
    metricMin = metric_without_hours // 100
    metricSec = metric_without_hours - (metricMin * 100)

    # this finalizes the times that print
    timeHrs = str(int(metricHrs))
    timeMin = str(int(metricMin))
    # these if/elif/else statements exist to take care of cases that a splice
    # cannot take care of with ease (I kept getting 83.33 instead of 08.33)
    if metricSec == 0.00:
        timeSec = '00.00'
    elif metricSec < 10:
        # fixes a bug where it would force the seconds value to be double digit
        timeSec_base = metricSec * 100
        timeSec_round = round(timeSec_base)
        timeSec_str = str(timeSec_round)
        
        timeSec_zero = '0' + timeSec_str[-5:]

        #split seconds into decimal and whole second parts
        timeSec_whole = timeSec_zero[0:2]
        timeSec_dec = timeSec_zero[-2:]
        # rejoin the whole second and the decimal second portions
        timeSec_complete = timeSec_whole + '.' + timeSec_dec
        
        timeSec = timeSec_complete[-5:]
    else:
        timeSec_base = metricSec * 100
        timeSec_round = round(timeSec_base)
        timeSec_str = str(timeSec_round)
        
        timeSec_zero = '0' + timeSec_str[-5:]

        #split seconds into decimal and whole second parts
        timeSec_whole = timeSec_zero[0:3]
        timeSec_dec = timeSec_zero[-2:]
        # rejoin the whole second and the decimal second portions
        timeSec_complete = timeSec_whole + '.' + timeSec_dec
        
        timeSec = timeSec_complete[-5:]
    
    print('The "metric" time is:')
    print(timeHrs + ':' + timeMin + ':' + timeSec)
    
    
# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
