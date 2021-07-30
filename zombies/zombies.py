"""
    In this game, we create a set of dice with varying sides and put them
    randomly on two teams: vampires and zombies. The dice sit in a circular
    arrangement, so that each die has two neighbors. On each game turn, all
    dice are rolled, and if any die's roll is less than a neighboring enemy's
    roll, that die is converted to the other team.

    Each round continues until all dice are vampires or all dice are zombies!

    The game continues until the player indicates a desire to end the game!
"""
# CITE: TA Hours
# DESC: Matt and Candice helped with the style, and Matt helped with the MANY
#       input checks in this program.

import random

class Die():
    """Represents a die for the vampires vs. zombies dice game.
    Each Die has a number of sides, a team, a location, and a value."""

    def __init__(self, sides, team, location, side_up=0):
        """ Constructor. """
        self._sides = sides
        self._team = team
        self._loc = location
        self._side_up = 0

    def roll(self):
        """ We roll a die by choosing a  side_up . """
        self._side_up = random.randint(1, self._sides)

    def get_value(self):
        """ We check the value on the upward-facing side of the die. """
        return self._side_up

    def get_sides(self):
        """ returns the number of sides of the die """
        return self._sides

    def get_team(self):
        """ returns the team that the current die is on """
        return self._team

    def get_loc(self):
        """ returns the location of the die in the list of dice """
        return self._loc

    def change_team(self):
        """ This function should change the die's team. """
        # Copied from the Game class so I have access to this information in
        # an easy to read manner
        team_lst = ['vampire', 'zombie']
        
        # checks to see if the team value is the first in the list of teams
        # and switches it to the other if it is
        if self._team == team_lst[0]:
            self._team = team_lst[1]
            
        # This switches to the first team value if the die is the second
        # team value
        else:
            self._team = team_lst[0]

class Game():
    """Plays the vampires vs. zombies dice game."""

    def __init__(self, num_dice):
        """ Create dice and put them on teams at random.
            This function is provided in full to you."""
        self._num_dice = num_dice
        self._dice = []
        self._turn = 0

        sides_options = [4, 6, 8, 10]
        teams = ['vampire', 'zombie']

        for loc in range(self._num_dice):
            sides = random.choice(sides_options)
            team = random.choice(teams)
            self._dice.append(Die(sides, team, loc))

    def __str__(self):
        """ We print a status report. 
            This function is provided in full to you. """
        to_print = ''
        for die in self._dice:
            this_die = ('die %3i: d%-2i (%7s) rolled %i' %
                        (die.get_loc(), die.get_sides(), die.get_team(),
                        die.get_value()))
            to_print = to_print + this_die + '\n'
        return to_print

    def get_turn(self):
        """ This function should return the turn number of the game. """
        return self._turn

    def increment_turn(self):
        """ This function should add 1 to the turn counter. """
        self._turn += 1

    def roll_all(self):
        """ This function should roll all of the dice. """
        for die in self._dice: # Rolls all the die in self._dice
            die.roll()

    def is_game_over(self):
        """ We check for the end of the game, which happens when
            all dice are vampires or all dice are zombies."""
        # Arbitrarily sets the team to check for equal to the team of the first
        # die
        check = self._dice[0].get_team()
                                         
        for die in self._dice:
            # If any of the die are not the same team as the first die this
            # method returns False
            if die.get_team() != check: 
                return False

        # If all of the die are on the same team this method returns True
        return True

    def update_teams(self):
        """ We see for each die if it should change teams. 
            This function should call  check_battles() . 
            The function does not return anything. Instead, it
            should update the  self._dice  list."""
        switch_lst = Game.check_battles(self)
        
        # check every die and chenge the teams as necessary
        for i in range(len(self._dice)):
            die = self._dice[i] # only here to make the code look nicer
            
            # checks to see if the value in switch_lst that corresponds to the
            # current die is True
            if switch_lst[i]: 
                # calls another method to change the team of the die
                die.change_team() 

    def check_battles(self):
        """ We check the results of all possible battles. 
            This function should call  attack_result() .
            The function should return the list  switch_teams , with
            each entry either True or False. """
        
        switch_teams = []
        for die in self._dice: # check every die in the game
            switch_teams.append(Game.attack_result(self, die))

        return switch_teams # return the list
        

    def attack_result(self, curr):
        """ Called by  check_battles , here we calculate the result
            of each battle, returning if the die should switch teams.
            The function should return:
                True   if current die should switch teams and
                False  otherwise """
        
        # make a list of the dice that need to be checked against the current
        # die
        dice_lst = []
        num = self._dice.index(curr)
        before = num - 1
        after = num + 1
        
        # gets the final index number instead of the length
        if after > len(self._dice) - 1: 
            after = 0
        dice_lst.append(self._dice[before])
        dice_lst.append(self._dice[after])

        # check to see if either of the dice are on the same team as the current
        # die and remove them if so
        for die in dice_lst:
            if die.get_team() == curr.get_team():
                dice_lst.remove(die)

        # check all neessary dice against the current die to see if the current
        # die is forced to change teams
        for die in dice_lst:
            if die.get_value() > curr.get_value():
                return True
            
        # only executes if the current die has a higher value than the
        # neighboring dice that are of the opposite team
        return False 

    def get_winning_team(self):
        """ Returns the team of the first die. This is intended only to be used
            to check the results of the war and see if the player won their bet.
            It is not called by anything else. """
        return self._dice[0].get_team()

def is_number(string):
    ''' checks to see if a string is a number '''
    # checks every character in the string to see if it is a character in the
    # alphabet and returns false if it finds the character in the alphabet
    for i in range(len(string)):
        if string[i] not in '1234567890':
            return False
    return True

def valid_bet(bet, plants):
    ''' This is a recursive function thatchecks to see if a bet is valid.
        This function forces the user to enter a valid wager. '''
    # This if statement checks to see if the player has entered a number and
    # sets a variable called wager equal to the entered bet as an integer
    if is_number(bet):
        wager = int(bet)
        
        # this if statement checks to see if the wager is invalid
        if wager == 0 or wager > plants:
            print('Your previous wager was invalid.', end = ' ')
            bet = input('Please enter another wager: ')
            
            # this if returns True only runs once the player has entered a valid
            # wager
            return valid_bet(bet, plants)
        return (True, bet)
    
    # this else statement tells the player that the value they have entered is
    # not valid only after checking to ensure that the value is not a number
    else:
        print('Your previous wager was invalid.', end = ' ')
        bet = input('Please enter another wager: ')
        return valid_bet(bet, plants)

def main():
    """ We run the game from here. 
        This function is provided in full to you. """
    
    # explain the rules
    print("You have 500 Plants. Use these to bet on the outcome of the battles")
    print('between the zombies and vampires. You cannot bet more than you have')
    print('and you cannot lose all your Plants. If you do, you will have the')
    print('option to restart with 500 Plants or to quit. You may also quit at')
    print('any time by entering "n" when prompted. Both the zombies and')
    print('the vampires have the same abilities, so there is no team that is')
    print('better than another. Each unit is represented by a die and can')
    print('attack the one immediately before or after it. You will now be')
    print('asked for a number of dice to play the game with. The minimum wager')
    print('is 1 Plant; the maximum is your current number of Plants. Please ')
    print('keep in mind that the more die there are, the longer the round will')
    print('take, and if there are an odd number of die, one side will have an')
    print('advantage. Have fun!')

    cont_game = 'y' # this will be used to continue running the game

    Plants = 500 # this is the ingame currency that the player will use to bet

    # cont_game will be rewritten after every battle
    while cont_game == 'y':
        print()
        
        # Change this number to change how many dice we use.
        dice_count = input('Enter the number of dice to use in the war: ')
        
        # checks to see that the player entered a number
        while not is_number(dice_count):
            dice_count = input("Please enter a valid number of dice: ")
        num_dice = int(dice_count)
        war = Game(num_dice)
        
        # if there is only 1 die the game is ended on turn 0 if there are 0
        # dice th game cannot possibly start
        while num_dice <= 1: 
            num_dice = int(input("Please enter a valid number of dice: "))
        bet = input("Enter a number of Plants to wager on this battle: ")
        
        # this if statement calls a function that checks to see if the wager
        # is valid and sets wager equal to the value of bet as an integer
        wager = int(valid_bet(bet, Plants)[1])
                                            
        team = input("Which team would you like to bet on (vampires or "
                     "zombies)? ")
        
        # this retrieves the team, accounts for typos and makes the search
        # case-insensitive
        bet_team = team[0].lower() 

        # this checks to see if the user entered a team not supported by the
        # game
        while bet_team not in "zv":
            team = input("Please enter a valid team to bet on (vampires or "
                     "zombies)? ")
            bet_team = team[0].lower()

        # this keeps running the game until it finishes
        while not war.is_game_over():
            war.increment_turn()
            war.roll_all()
         
            print('Turn', war.get_turn())
            print(war)
        
            war.update_teams()

        print()
        print('Final status after %i turns:' % war.get_turn())
        print(war)

        # this checks to see if the player bet on the winning team and
        # calculates the number of plants the player currently has accordingly
        if war.get_winning_team()[0].lower() == bet_team:
            Plants += wager
        else:
            Plants -= wager
           
        # This if/else statement checks to see if the player has more than 0
        # plants and asks if the player would like to continue. If the player
        # has 0 Plants, this informs the player of this and asks if the player
        # would like to restart
        if Plants > 0:
            print('You have', Plants, 'Plants.')
            to_continue = input("Would you like to continue? Y/N: ")
            
            # this takes the first letter to account for typos and makes the
            # check to continue case-insensitive
            cont_game = to_continue[0].lower()
            if cont_game == 'n':
                print('You ended with', Plants, 'Plants.')
                
        else:
            print("You've lost all your Plants and cannot wager anything.")
            to_continue = input("Would you like to restart? Y/N: ")
            cont_game = to_continue[0].lower()

            # this checks whether the player wants to continue or not and
            # resets the Plant value if they have lost and would like to
            # continue                                                   
            if cont_game == 'y':
                Plants == 500
    
    print('Exiting...')


if __name__ == "__main__":
    main()
