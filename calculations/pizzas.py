"""
 *****************************************************************************
   FILE:        pizzas.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 2

   DATE: 9/5/17

   DESCRIPTION: calculate equivalent surface area between regular pizzas and
   				super pizzas

 *****************************************************************************
"""


import math

def main():
    """ takes user inputs, stores them, and calculates the amount of "super
    pies" needed to give everyone the same surface area of pizza """
    
    # user inputs information here
    # because of my own laziness and unwillingess to type super when big will
    # suffice, big is used in place of super when possible
    normRad = int(input('What is the diameter of a "standard" size pie? ')) / 2
    normSlices = int(input("How many slices are in a standard size pie? "))
    countSlices = int(input("How many standard slices do you want? "))
    bigRad = int(input("What is the diameter of the pies you will buy? ")) / 2
    bigDia = bigRad * 2

    # calculations start here
    normArea = math.pi * (normRad ** 2)
    sliceArea = normArea / normSlices
    totalArea = sliceArea * countSlices

    # equivalency calculations start here
    bigArea = math.pi * (bigRad ** 2)
    bigNum = int(math.ceil(totalArea / bigArea))
    superNum = str(bigNum)
    superDia = str(int(bigDia))

    # returns print here
    print("You will need to buy", superNum, superDia+'-inch', "diameter pies.")


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
