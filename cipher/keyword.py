"""
 *****************************************************************************
   FILE:        decrypt.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 4

   DATE: 17 September 2017

   DESCRIPTION: create a program that uses keyword decryption to decrypt
   messages

 *****************************************************************************
"""

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def remove_spaces(text):
    """ Given string   text  , build and return a new string with all
    spaces removed.  For example, from "Happy birthday   to you", return
    "Happybirthdaytoyou" """
    lst = [] # creates a blank list
    for char in text: # goes through every character in the input text
        if (char == ' ') == False: # finds every character that is not a space
            lst.append(char) # adds non-space characters to the blank list
    return lst # returns the list


def subtract(text, key):
    """ Given two uppercase letters of the alphabet, determine and return the
    unencrypted letter from the encrypted_letter was generated using
    key_letter.  For example, when encrypted_letter is "J" and key_letter is
    "R", return "S". """
    key_used = key[0:len(text)] # shortens string that was intentionally made
    							# to be too long
    for i in range (0, len(text)): # goes through every index position in the
    							   # the text
        text[i] -= abc.index(key_used[i]) # subtracts the index number of the
                                          # current character in the long key
                                          # in the alphabet from the current
                                          # number in the index location in the
                                          # list of numbers after the addition
                                          # that happens in the decrypt function
    return text # returns the corrected list of indicies
    

def decrypt(text, key):
    """ For each letter in   text  , determine the letter from which it was 
    encrypted using   key  . Build and return the string of these letters."""
    lst = [] # creates a blank lisit
    message_lst = [] #creates a blank list that will be used to make a final
                     # string
    keyMult = key * 16 # makes the key repeat a number of times larger than what
                       # should be necessary
                       # this is also a power of 2 because I like powers of 2
    blank = '' # creates a blank string
    for char in text: # goes through every character in the text
        lst.append(abc.index(char)) # adds the alphabetical index of each
                                    # character to the first blank list
    for i in range(0, len(lst)): # goes through every index in the list
        if lst[i] < abc.index(keyMult[i]): # checks to see if the value in the
                                           # list is less than the value of the
                                           # value of the alphabetical index of
                                           # the current character in the key
                                           # this happens because the minimum
                                           # value a character could have if
                                           # it didn't require the use of % to
                                           # encrypt is the value of the
                                           # character used to encrypt it
                                           # if the value is less than this
                                           # it means that the value was
                                           # obtained by using % 26
                                           # and must therefore be reversed by
                                           # adding 26
            lst[i] += 26 # adds 26 to the current list value
    subtracted = subtract(lst, keyMult) # calls the subtract function
    for i in subtracted: # goees through every index value stored in the result
                         # of running the subtracted function
        message_lst.append(abc[i]) # adds the correcponding letter from the abc
                                   # global variable to the predefined blank
                                   # list to be used for storing message data
                                   # the reason this takes the value at the
                                   # char i is because the values in the result
                                   # of subtracted are integer values that
                                   # represent the index number of a letter
                                   # in the global abc string
    message = blank.join(message_lst) # joins the message list with nothing
                                      # separating the characters and builds a
                                      # string to store the data
    return message # returns the string

def report(message, clues): # this was a prewritten function
    """ Print the   message  , and, for each clue in   clues  , if it occurs in 
      message  , indicate so on the output. """
    print("The decrypted message is", message)
    for entry in clues:
        if entry in message:
            print('Clue', entry, 'discovered in', message)


def main(): # this was a prewritten function
    """
    This function is provided in full. Its job is to control
    the flow of the program, and offload the details to the
    other functions.
    """
    captured_text = input('Enter the captured text: ')
    keyword = input('Enter a keyword: ')
    clues = input('Enter the clues separated by one space: ')
    clueList = clues.split();

    # Take all spaces out of the captured text:
    squished_text = remove_spaces(captured_text)

    # Send the captured text for decryption:
    decrypted_text = decrypt(squished_text, keyword)

    # Check the decrypted text for clues that indicate a real message.
    report(decrypted_text, clueList)


# Here we invoke the main function. This code is always included in our
# python programs.
if __name__ == "__main__":
    main()
