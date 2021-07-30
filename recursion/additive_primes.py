"""
 *****************************************************************************
   FILE:  additive_primes.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 7

   DATE: 16 October 2017

   DESCRIPTION: Determines if something is an additive prime number, a number
                that is prime, and one whose digits' sum is also prime
                decreasing to a single digit number that must also be prime

 *****************************************************************************
"""


def additive_prime(num):
    '''
    checks to see if a number is an additive prime, returns True or False
    '''
    
    if num < 10: # checks to see if the number does not need to have its
                 # digits summed
                 
        return prime(num)
    else:
        if prime(num): # checks to see if the number is a prime. if it is not
                       # it is impossible for that number to be an additive
                       # prime
                       
            digit_sum = sum_of_digits(num)
            
            return additive_prime(digit_sum) # loops through this function until
                                             # a boolean value is returned

        return False # if the body of the previous if statement is not run the
                     # number is automatically not an additive prime

def additive_primes_list(n):
    '''
    returns a list of all additive prime numbers from 1 to n inclusively
    '''
    
    lst = []

    for num in range(2, n + 1): # loops through all the numbers from 2 to n

        if additive_prime(num): # checks to see if the number from the iteration
                                # of the for loop is an additive prime
            
            lst.append(num) # appendss the number to the list if the number is
                            # an additive prime

    return lst
            


def prime(num):
    '''
    checks to see if a number is a prime number, returns True or False
    '''
    
    lst = [] # idea for creating a list to store remainders from a conversation
             # with Ken Fung
             
    if num > 1: # 1, 0, and negative numbers are not considered prime
        
        for x in range(2, num):
            
            remainder = num % (x) # checks to see if there is a remainder when
                                  # dividing the number by anything other than
                                  # 1 and itself
                                  
            lst.append(remainder)
            
        if 0 in lst: # there will only be a 0 in the list of remainders if the
                     # number is evenly devisible by a number other than 1 and
                     # itself
                     
            return False
        
        return True # if there is no 0 in the list of remainders the number is
                    # prime and this function returns True
                    
    return False # if the body of the if statement above is not run the number
                 # is one of the numbers not considered prime

def sum_of_digits(num):
    '''
    sums the digits of a number
    '''
    
    digit_sum = 0
    for i in range(len(str(num))): # goes through every digit in a number
        
        digit_sum += int(str(num)[i]) # adds the values of the digits together
        
    return digit_sum


def main():
    print(additive_primes_list(103))

if __name__ == "__main__":
    main()
