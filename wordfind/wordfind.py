"""
 *****************************************************************************
   FILE:        wordfind.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 5

   DATE: 30 September 2017

   DESCRIPTION: Case-insensitively find words in a grid in all 8 directions

 *****************************************************************************
"""

def printGrid(grid):
    """ Display the grid in a nice way """


    for row in grid:

        line = ''

        for i in range(len(row)):

            line += '' + row[i] + '  '

        print(line)


    print()
    
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def wordfind(grid, words):
    """ For each word in words, if possible, find it once in the grid, case 
        insensitive.  Convert those found letters in the grid 
        to upper-case."""
    

    first_coords = first(grid, words)

    found = find(grid, first_coords, words)


    
    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def dimensions(grid):
    '''
    returns the dimensions of the grid
    '''



    r = len(grid) # the number of lists in the list of lists is the number of
                  # rows

    c = len(grid[0]) # the length of each list within the larger list is the
                     # number of columns



    return r, c

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def first(grid, words):
    ''' returns the coordinates of the first letter of allthe words that may be
    contained within the grid '''


    coords = [] # this blank list will be a list of tuples that are the
                # coordinates (rows, columns) of all possible first letters of
                # words that could exist within the grid

    r, c = dimensions(grid)

    for word in words: # goes through every word

        for y in range(r): # checks every row

            for x in range(c): # checks every column

                if grid[y][x] == word[0]: # if the grid at any point contains a
                                          # possible start to a word

                    tup = y, x # assign those coordinates to a tuple

                    coords.append(tup) # and add that tuple to the list of
                                       # coordinates



    return coords
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def left(grid, first_coords, words):
    '''
    checks to see if the word can exist moving left of the initial coordinate
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "west" direction of their initial letter

    this function has an added purpose: to check one letter words

    this also capitalizes all words found
    '''


    found = 0

    for i in first_coords: # checks all words that could possibly exist in the
                           # grid

        r, c = i # stores the coordinates of the first letter as a tuple

        counter = 0

        string = ''

        for word in words: # checks all the words

            if len(word) > 1: # checks all words longer than 1 letter

                if c - 1 >= 0: # checks to see if the word could exist in the
                               # given direction

                    if grid[r][c - 1].lower() == word[1]: # checks to see if
                                                          # the letter in the
                                                          # given direction is
                                                          # the second letter
                                                          # of the word

                        counter = len(word)

                        for x in range(counter): # generates a string equal in
                                                 # length to the length of the
                                                 # word assuming that a string
                                                 # that long can even exist in
                                                 # the direction

                            if c - x >= 0: # checks to see if there is a letter
                                           # in the direction

                                string += grid[r][c - x] # adds a letter to the
                                                         # blank string assigned
                                                         # earlier

                if word in string.lower(): # checks to see if a word is in the
                                           # string if the string were entirely
                                           # lowercase

                    found += 1 # if a word is found, add 1 to found

                    for x in range(counter):

                        if c - x >= 0:

                            grid[r][c - x] = grid[r][c - x].upper() # makes the
                                                                    # letters in
                                                                    # a found
                                                                    # word
                                                                    # uppercase

            else: # words exculsively with one-letter words

                found += 1 # adds 1 to found

                grid[r][c] = grid[r][c].upper() # capitalizes the letter



    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def right(grid, first_coords, words):
    '''
    checks to see if the word can exist moving right of the initial coordinate
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "east" direction of their initial letter

    this also capitalizes all words found

    most of the logic has been explained previously, so comments from here on
    will be more sparse and less wordy
    '''


    found = 0

    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            if c + 1 < len(grid[0]): # goes to the right

                if grid[r][c + 1].lower() == word[1]:

                    counter = len(word)

                    for x in range(counter):

                        if c + x < len(grid[0]):

                            string += grid[r][c + x]

            if word in string.lower():

                found += 1

                for x in range(counter):

                    if c + x < len(grid[0]):

                        grid[r][c + x] = grid[r][c + x].upper()



    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def up(grid, first_coords, words):
    '''
    checks to see if the word can exist moving up from the initial coordinate
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "north" direction of their initial letter

    this also capitalizes all words found

    most of the logic has previously been explained
    '''


    found = 0

    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            if r > 0:

                if grid[r - 1][c].lower() == word[1]: # goes up the grid with
                                                      # the initial letter being
                                                      # the bottom of the search

                    counter = len(word)

                    for x in range(counter):

                        if r > 0:

                            string += grid[r - x][c]

            if word in string.lower():

                found += 1

                for x in range(counter):

                    if r > 0:

                        grid[r - x][c] = grid[r - x][c].upper()



    return found
                              
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def down(grid, first_coords, words):
    '''
    checks to see if the word can exist moving left of the initial coordinate
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "west" direction of their initial letter

    this also capitalizes all words found

    most of the logic has previously been explained
    '''


    found = 0

    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            if r < len(grid) - 1:

                if grid[r + 1][c].lower() == word[1]: # goes down from the
                                                      # initial letter

                    counter = len(word)

                    for x in range(counter):

                        if r + x < len(grid):

                            string += grid[r + x][c]

            if word in string.lower():

                found += 1

                for x in range(counter):

                    if r + x < len(grid):

                        grid[r + x][c] = grid[r + x][c].upper()



    return found
                              
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def diagonal_ULR(grid, first_coords, words):
    '''
    checks to see if the word can exist moving diagonally, with the initial
    coordinate being the top left, and the moving downward toward the right
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "south-east" direction of their initial letter

    this also capitalizes all words found

    most of the logic has previously been explained
    '''


    found = 0

    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            if (r + 1 < len(grid)) and (c + 1 < len(grid[0])): # goes diagonally
                                                               # with the
                                                               # initial letter
                                                               # being the top
                                                               # left and moving
                                                               # down and to the
                                                               # right

                if grid[r + 1][c + 1].lower() == word[1]:

                    counter = len(word)

                    for x in range(counter):

                        if (r + x < len(grid)) and (c + x < len(grid[0])):

                            string += grid[r + x][c + x]

            if word in string.lower():

                found += 1

                for x in range(counter):

                    if (r + x < len(grid)) and (c + x < len(grid[0])):

                        grid[r + x][c + x] = grid[r + x][c + x].upper()



    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def diagonal_URL(grid, first_coords, words):
    '''
    checks to see if the word can exist moving diagonally, with the initial
    coordinate being the top right, and the moving downward toward the left
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "south-west" direction of their initial letter

    this also capitalizes all words found

    most of the logic has previously been explained
    '''


    found = 0

    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            if (r + 1 < len(grid)) and (c - 1 > 0): # goes diagonally with the
                                                    # initial letter being the
                                                    # top right and moving
                                                    # down and to the
                                                    # left

                if grid[r + 1][c - 1].lower() == word[1]:

                    counter = len(word)

                    for x in range(counter):

                        if (r + x < len(grid)) and (c - x > 0):

                            string += grid[r + x][c - x]

            if word in string.lower():

                found += 1

                for x in range(counter):

                    if (r + x < len(grid)) and (c - x > 0):

                        grid[r + x][c - x] = grid[r + x][c - x].upper()



    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def diagonal_DLR(grid, first_coords, words):
    '''
    checks to see if the word can exist moving diagonally, with the initial
    coordinate being the bottom left, and the moving upward toward the right
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "north-east" direction of their initial letter

    this also capitalizes all words found

    most of the logic has previously been explained
    '''


    found = 0

    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            if (r - 1 > 0) and (c + 1 < len(grid[0])): # goes diagonally with
                                                    # the initial letter being
                                                    # the bottom left and moving
                                                    # down and to the right

                if grid[r - 1][c + 1].lower() == word[1]:

                    counter = len(word)

                    for x in range(counter):

                        if (r - x > 0) and (c + x < len(grid[0])):

                            string += grid[r - x][c + x]

            if word in string.lower():

                found += 1

                for x in range(counter):

                    if (r - x > 0) and (c + x < len(grid[0])):

                        grid[r - x][c + x] = grid[r - x][c + x].upper()




    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def diagonal_DRL(grid, first_coords, words):
    '''
    checks to see if the word can exist moving diagonally, with the initial
    coordinate being the bpttom right, and the moving upward toward the left
    and, if so, checks to see if it does exist and returns a value of how many
    words exist in the "north-west" direction of their initial letter

    this also capitalizes all words found

    most of the logic has previously been explained
    '''


    found = 0


    for i in first_coords:

        r, c = i

        counter = 0

        string = ''

        for word in words:

            for i in range(len(word)):

                if (r - 1 >= 0) and (c - 1 < len(grid[0])):# goes diagonally
                                                    # with the initial letter
                                                    # being the bottom right and
                                                    # moving up and to the left

                    if grid[r - 1][c - 1].lower() == word[1]:

                        counter = len(word)

                        for x in range(counter):

                            if (r - 1 >= 0 and c - 1 < len(grid[0])
                                and r - counter >= 0 and c - counter >= 0):

                                string += grid[r - x][c - x]

            lower = string.lower()

            if word in lower:

                found += 1

                for x in range(counter):

                        if (r - 1 >= 0 and c - 1 < len(grid[0])
                            and r - counter >= 0 and c - counter >= 0):

                            grid[r - x][c - x] = grid[r - x][c - x].upper()



    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def find(grid, first_coords, words):



    found = 0



    found += up(grid, first_coords, words)

    found += down(grid, first_coords, words)

    found += left(grid, first_coords, words)

    found += right(grid, first_coords, words)

    found += diagonal_URL(grid, first_coords, words)

    found += diagonal_ULR(grid, first_coords, words)

    found += diagonal_DRL(grid, first_coords, words)

    found += diagonal_DLR(grid, first_coords, words)




    return found

# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
def main():
    """ The main program is just for your own testing purposes.
        Modify this in any way you wish.  It will not be graded. """
    
    myGrid = [['j', 'm', 'w', 'e'],
              ['e', 'e', 'p', 'p'],
              ['q', 'o', 'x', 'u'],
              ['w', 'w', 'e', 'd'],
              ['w', 'g', 'j', 'o']]
    words = ['wed', 'meow', 'jexd', 'wwxp']
    count = wordfind(myGrid, words)
    printGrid(myGrid)
    print(count)

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
