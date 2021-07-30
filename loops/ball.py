"""
 *****************************************************************************
   FILE:        ball.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 2

   DATE: 9/10/17

   DESCRIPTION: write a program to calculate the distance traveled by a ball

 *****************************************************************************
"""


def main():
    """ takes inputs and calculates the distance traveled """
    heightStart = float(input('Enter initial height: '))
    bounce1 = float(input('Enter height of first bounce: '))
    bounceCount = int(input('Enter number of bounces: '))
    # the ratio of rebound height to initial height
    # ratio is used to compute the height of each successive bounce
    ratio = bounce1 / heightStart
    
    # bounce is the variable that will be used for the current bounce
    # it starts at a value of bounce1 because the height of the next bounce is
    # computed in the for loop
    bounce = bounce1
    # height starts at heightStart because that is the initial height
    height = heightStart
    for bounces in range(0, (bounceCount - 1)):
        # the reason bounce is multiplied by 2 is because the ball has to
        # travel down and back up
        height += 2 * bounce
        bounce = bounce * ratio
    # the reason the last bounce is added here instead of in the for loop
    # is because there is no rebound on the last bounce
    height += bounce
    # the reason the height is rounded to 2 decimals is because it will
    # eliminate the last decimal place if its value is 0 and it will keep
    # at most 2 decimal places
    print('The total distance the ball traveled is', round(height, 2), 'feet.')

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
