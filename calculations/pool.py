"""
 *****************************************************************************
   FILE:        pool.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 2

   DATE: September 2, 2017

   DESCRIPTION: program to find the time spent filling a pool given the
                dimensions and a rate of flow of water

 *****************************************************************************
"""


def main():
    """ takes user inputs, stores them, and calculates time needed to fill
    a pool with water"""
    length = float(input("Pool length (feet): "))
    wide = float(input("Pool width (feet): "))
    deep = (float(input("Additional depth desired (inches): "))) / 12
    flow = float(input("Water fill rate (gal/min): "))
# CITE: http://www.asknumbers.com/CubicFeetToGallon.aspx
# DETAILS: provides the conversion between cubic feet and gallons
    vol = length * wide * deep * 7.48051948
    # timeRAW is the raw time to fill the pool in minutes
    timeRAW = vol * (1/flow)
    # Stop denotes a variable that is used later and is not in final
    # displayable form
    # RAW from here on denotes a time that is unprocessed to be a Stop time
    timeHrsStop = int(timeRAW // 60)
    timeMinRAW = timeRAW - (timeHrsStop * 60)
    timeMinStop = int(timeMinRAW // 1)
    timeSecRAW = (timeMinRAW - timeMinStop) * 60
    timeSecStop = round(timeSecRAW)

    # converting the Stop times to be useable in the print command
    if timeHrsStop < 100:
        timeHrs = ('0' + str(timeHrsStop))[-2:] + ':'
    else: 
        timeHrs = str(timeHrsStop) + ':'
    timeMin = ('0' + str(timeMinStop))[-2:] + ':'
    timeSec = ('0' + str(timeSecStop))[-2:]

    # final print command
    print('Time: ' + timeHrs + timeMin + timeSec)
    

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
