"""
 *****************************************************************************
   FILE:        alphabet.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 2

   DATE: 9/9/17

   DESCRIPTION: write a program that takes inputs and displays the letters
                that aren't used

 *****************************************************************************
"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    """ takes user inputs and displays unused letters """
    string = input("Enter some text: ")
    # makes the string a list with all capital letters
    upperList = list(string.upper())
    #makes the alphabet a list
    alphaList = list(alphabet)
    for char in upperList:
        if char in alphaList:
            alphaList.remove(char)
    # sets a blank string to join the characters in alphaList without spaces or
    # symbols between the characters
    blank = ''
    # .join is used to condense the list alphaList into a single string
    
    print('Letters not in the text: ' + blank.join(alphaList))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
