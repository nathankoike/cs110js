"""
 *****************************************************************************
   FILE:  game.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Final Project

   DATE: 7 November 2017

   DESCRIPTION: Make a board game that interfaces with the player
		exclusively through a GUI

		DISCLAIMER: There are many things I have left to implement. For example:
						using the one other tile if/when the 35 are used up 
							(probably done)
						having a scoreboard 
						a restart button
						determining a winner
							(can be done without the computer)

		rules:
			you must play the tile next to your piece
			your piece SHOULD follow the path to completion. sometimes it does
				sometimes it doesn't. you can do that mentally if python breaks
			last person on the board wins

		step1: select where each player starts by clicking on the colored dots
				when they appear
		step2: select a tile. you may rotate it using the pink button at the
				bottom. then click the space next to the dot whose turn it
				currently is
		step3: close program because it probably broke but will also probably
				work the next time with no modification to it whatsoever
		step4: determine who wins by seeing who is the last to hit the edge

 *****************************************************************************
"""
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
from cs110graphics_v2 import *
import random
import math

# this is the number of rows and columns on a tsuro board
rows = 6
cols = 6

# because this game is played with 2-8 players, these are all the allowed colors
# for a player piece. there is one difference between this and the actual game: 
# there is a player color 'purple' instead of 'gray'. This is because gray will
# be used to set a player's piece inactive and note that on the 'scoreboard'
# displayed to the right of the board 
color_lst = ['black', 'white', 'green', 'blue', 'red', 'yellow', 'orange', 
			 'purple']

# this is an arbitrary variable that serves to store a tile. it is only ever
# used in moving the tile but needs to be accessed by other classes and 
# functions.
stored_tile = 'tile'

# this is the distance between the player space and the center of a space. it
# can be changed by changing the size of the board. 0 is just a placeholder
# value that will be changed upon the initialization of the Game class.
within_range = 0

# this is the hand that holds the tiles used to play the game
hand = []

# this is a list of the coordinates of the centers of the tiles in a
# player's hand
hand_coords = [(748, 225), (748, 350), (748, 475)]

class Game():
	''' control the whole game '''
	def __init__(self, win):
		# access the global variable within_range
		global within_range

		self._win = win
		self._board = Board(self._win)
		self._border_width = self._board.get_border_width()
		self._tile_width = self._board.get_tile_width()
		self._board_width = self._border_width + (self._tile_width * 6)
		within_range = Pythagoras(self._tile_width // 2, self._tile_width // 6)

		# make the spaces
		self._spaces = make_spaces(self._win, self._tile_width, 
									self._border_width, self)

		# make the dragon tile. (698, 250) is a placeholder center
		self._dragon = Dragon_Tile(self._win, self._tile_width, (748, 100), \
									self)

		# make a list of all playable tiles
		self._tiles = make_tiles(self._win, self._tile_width, self)

		# add the tiles to the window
		for tile in self._tiles:
			tile.add_tile_to_win(self._win)

		# the number of players in the game
		self._player_num = 0

		self._deck = self.make_deck()

		# create an attribute to tell if the game is over
		self._over = False

		# create an attribute to count turns
		self._turn  = 0

		# this attribute will be used to count how many players have been
		# eliminated
		self._eliminated_players = 0

		# create the button to rotate tiles
		self._rotate_button = Rotate_Button(self._win, 50, (673, 623))
		self._rotate_text = Text(self._win, 'Rotate', 12, (725, 633))
		self._rotate_text.set_depth(20)

		# create the first screen the player sees
		self._screen = Square(self._win, 1200, (424, 324))
		self._screen.set_fill_color('white')
		self._screen.set_depth(19)
		self._win.add(self._screen)
		self._welcome = Text(self._win, \
			'Welcome to Tsuro! How many players are there?', \
			24, \
			(424, 250))
		add_to_win(self._win, [self._welcome])
		self._welcome.set_depth(0)

		# give the option to select how many players there are
		self._player_buttons = make_player_select(self._win, self)

		# make a list of the players
		self._players = []

		# make a list of the placement buttons
		self._placement_buttons = []

	def continued_init(self):
		''' finish initializing the game '''
		# make the players
		for i in range(self._player_num):
			self._players.append(Player(i, self._win, self))

		# the purpose of this for loop is to place every player on the board
		for player in self._players:
			# make the placement buttons
			self._placement_buttons.append(player_placement(self._win, \
								self._spaces[0].get_center(), self._tile_width,\
								player, self))

	def make_deck(self):
		''' make the deck of tiles to draw from '''
		# create a list of the id numbers of the tiles in the deck in draw
		# order 
		tile_lst = random_List(35)

		# create a blank list to serve as the deck and add all the tiles to the
		# deck in draw order
		deck_lst = []

		# the purpose of this for loop is to add the tiles to the deck in the
		# random order generated above
		for i in tile_lst:
			deck_lst.append(self._tiles[i])

		return deck_lst

	def add_to_deck(self, tile):
		self._deck.append(tile)

	def play_turn(self, space):
		''' control the turns that are played '''
		# access the global variables stored_tile and hand
		global stored_tile

		# find out which player's turn it is
		player_turn = self._turn % self._player_num

		# find out which player played the tile
		player = self._players[player_turn]

		# check to see if the player was eliminated
		if not player._elim:
			# draw tile if possible
			new_dragon_color = player.add_to_hand(self._deck, self._dragon)

			# reassign the color of the dragon tile
			self._dragon.set_color(new_dragon_color)

		# get the position of the player
		player_location = player.get_location()

		# check to see if the space is empty and is within distance of the
		# player
		if (not space._has_tile and
			within_player_range(space.get_center(), player_location)):

			# remove the played tile from the player's hand
			hand.remove(stored_tile)


			# let the space know that it now has a tile on it
			space._has_tile = True

			# move the stored tile to the space
			stored_tile.move_tile_to(space.get_center())

			# disable the space from future play
			space.disable()

			# disable the tile from future play
			stored_tile.disable()

			# deselect the tile in the GUI by resetting the border color
			stored_tile._space.set_border_color('black')

			# find out which player played the tile
			player = self._players[player_turn]

			# get the position of the player
			player_location = player.get_location()

			# this variable determines whether there are more tiles to move to
			more_tiles = True

			# the purpose of this while loop is to move the player until there
			# are no more tiles to move to
			while more_tiles:
				
				# get the position of the player
				player_location = player.get_location()

				# get the ports of the tile that was just played
				tile_ports = stored_tile.get_ports()

				# get the paths
				tile_paths = stored_tile.get_paths()

				# separate the paths into path_start and path_end
				path_start = []
				path_end = []

				# the purpose of these for loops is to separate the paths as the
				# comment above describes
				for path in tile_paths:
					path_start.append(path[0])
				for path in tile_paths:
					path_end.append(path[1])

				# the purpose of this nested for loop is to find which port the
				# player is on then to move the player
				for i in range(len(tile_ports)):
					if player_location == tile_ports[i]:
						# these for loops nested within the larger for loop
						# check to see if the player starts at the beginning or
						# end of a path, both being arbitrarily defined, and
						# moves them to the other side
						for index in range(len(path_start)):
							if i == path_start[index]:
								player.move_player_to(tile_ports[path_end\
														[index]])
						for index in range(len(path_end)):
							if i == path_end[index]:
								player.move_player_to(tile_ports[path_start\
														[index]])
				
				# find the new coordinates of the player
				new_coords = player.get_location()
				
				# check the x coordinate against the boundaries of the board
				# CITE: https://stackoverflow.com/questions/181530/
				#		styling-multi-line-conditions-in-if-statements
				# DESC: provided an example of a multi-line if statement
				if ((player._moved and
					new_coords[0] <= self._border_width) or
					(new_coords[0] >= self._board_width)):
					player.eliminated(self)

				# check the y coordinate against the boundaries of the board
				if ((player._moved and
					new_coords[1] <= self._border_width) or
					(new_coords[1] >= self._board_width)):
					player.eliminated(self)
				
				# check to see if there is another tile to move to
				more_tiles = self.adjacent_tile(new_coords)

				# the purpose of this for loop is to move the player more if
				# possible
				for tile in self._tiles:
					for i in range(len(tile._ports)):
						if player_location == tile_ports[i]:
						# these for loops nested within the larger for loop
						# check to see if the player starts at the beginning or
						# end of a path, both being arbitrarily defined, and
						# moves them to the other side
							for index in range(len(path_start)):
								if i == path_start[index]:
									player.move_player_to(tile_ports[path_end\
															[index]])
							for index in range(len(path_end)):
								if i == path_end[index]:
									player.move_player_to(tile_ports[path_start\
															[index]])

			# check to see if the game has ended
			if self.ended():
				return

			# find out which player does not need to be counted in the next pass
			# to move all the other players
			exempt_player = player._player

			# move the rest of the players
			move_players(space, self, exempt_player)

			# move the next player on
			player = self._players[(player_turn + 1) % self._player_num]
			player.switch_on()

			next_turn(self)

	def get_space_or_tile(self, center_coords, space_lst):
		''' get the space that has those coordinates '''
		for space in space_lst:
			if space.get_center() == center_coords:
				return space
		return 'none'

	def adjacent_tile(self, player_coords):
		''' find out if there is an adjecent tile to the tile the player is
	 		on '''
	 	# access the global variable stored_tile
		global stored_tile

		# split the player coordinates
		px = player_coords[0]
		py = player_coords[1]

		# find the new x and y coordinates of the first theoretical space
		sx = px + (self._tile_width // 2)
		sy = py + (self._tile_width // 6)
		new_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the first direction assuming that there is not a tile there
		if space != 'none':
	 		if space._has_tile:
	 			stored_tile = self.get_space_or_tile(new_center, self._tiles)
	 			return True

	 	# find the new x and y coordinates of the second theoretical space
		sx = px - (self._tile_width // 2)
		sy = py - (self._tile_width // 6)
		new_space_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the second direction assuming that there is not a tile there
		if space != 'none':
	 		if space._has_tile:
	 			stored_tile = self.get_space_or_tile(new_center, self._tiles)
	 			return True

		# find the new x and y coordinates of the third theoretical space
		sx = px + (self._tile_width // 2)
		sy = py - (self._tile_width // 6)
		new_space_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the third direction assuming that there is not a tile there
		if space != 'none':
	 		if space._has_tile:
	 			stored_tile = self.get_space_or_tile(new_center, self._tiles)
	 			return True

		# find the new x and y coordinates of the fourth theoretical space
		sx = px - (self._tile_width // 2)
		sy = py + (self._tile_width // 6)
		new_space_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the fourth direction assuming that there is not a tile there
		if space != 'none':
			if space._has_tile:
				stored_tile = self.get_space_or_tile(new_center, self._tiles)
				return True

		# find the new x and y coordinates of the fifth theoretical space
		sx = px + (self._tile_width // 6)
		sy = py - (self._tile_width // 2)
		new_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the fifth direction assuming that there is not a tile there
		if space != 'none':
	 		if space._has_tile:
	 			stored_tile = self.get_space_or_tile(new_center, self._tiles)
	 			return True

	 	# find the new x and y coordinates of the sixth theoretical space
		sx = px - (self._tile_width // 6)
		sy = py - (self._tile_width // 2)
		new_space_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the sixth direction assuming that there is not a tile there
		if space != 'none':
	 		if space._has_tile:
	 			stored_tile = self.get_space_or_tile(new_center, self._tiles)
	 			return True

		# find the new x and y coordinates of the seventh theoretical space
		sx = px + (self._tile_width // 6)
		sy = py - (self._tile_width // 2)
		new_space_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the seventh direction assuming that there is not a tile there
		if space != 'none':
	 		if space._has_tile:
	 			stored_tile = self.get_space_or_tile(new_center, self._tiles)
	 			return True

		# find the new x and y coordinates of the eighth theoretical space
		sx = px - (self._tile_width // 6)
		sy = py + (self._tile_width // 2)
		new_space_center = (sx, sy)

		# see if there is a tile on the space
		space = self.get_space_or_tile(new_center, self._spaces)

		# check the eighth direction assuming that there is not a tile there
		if space != 'none':
			if space._has_tile:
				stored_tile = self.get_space_or_tile(new_center, self._tiles)
				return True

		return False

	def ended(self):
		if self._eliminated_players < (len(self._players) - 1):
			return False
		return True

class Board():
	''' create the board for the game including borders and spaces '''
	def __init__(self, win, width = 600):
		''' initialize the class for the board with additional
					attributes to pass to to other pseudo-graphical objects to
					make the board complete '''
		self._win = win

		# this will be used to set the total width of the board
		self._width = width

		# this will be used to set the width of the border
		self._border_width = self._width // 25

		# this will be used to set the width of each tile
		self._tile_width = (self._width // 6)

		# center the board along the left edge fo the screen
		self._center = (self._border_width + self._width // 2, 
						self._border_width + self._width // 2)

		# this is the border created as a pseudo-graphical object
		self._border = Border(self._win, self._width, self._border_width, 
							  self._center)

	def get_tile_width(self):
		''' return the width of each square '''
		return self._tile_width

	def get_border_width(self):
		''' return the width of the border '''
		return self._border_width

class Space(EventHandler):
	'''represent all the spaces on the board '''
	def __init__(self, win, space_width, center, game):
		EventHandler.__init__(self)
		self._space_width = space_width
		self._center = center
		self._win = win
		self._game = game
		self._space = space(self._win, self._space_width, self._center)
		self._space.set_depth(30)

		# make the spaces respond to clicks
		self._space.add_handler(self)
		self._active = True
		self._has_tile = False

	def disable(self):
		''' disable the space once clicked '''
		self._active = False

	def get_center(self):
		return self._center

	def handle_mouse_release(self, _):
		# access the global variable stored_tile
		global stored_tile
		# play the turn
		if self._active and not stored_tile._moved:
			self._game.play_turn(self)

class Tile(Space):
	''' create the superclass for all tiles '''
	def __init__(self, win, space_width, center, paths, game):
		Space.__init__(self, win, space_width, center, game)

		# this is a list of tuples of the paths on the tile. each path
		# connects 2 ports. the list is of the 2 ports being connected
		self._paths = paths

		# create the actual pathing used in the game
		self._ports = Ports(self, self._center, self._space_width, self._win)

		# set the background color of the tile to something different from the
		# border and empty spaces
		self._space.set_fill_color('burlywood')

		# make the path graphics
		self._path_graphics = graphics(self._win, self._paths, self._ports)

		# the purpose of this for loop is to add a handler to all the path
		# graphics
		for line in self._path_graphics:
			line.add_handler(self)

		# this is used to control the rotation of each tile
		self._heading = 0

		# see if the tile has moved
		self._moved = False

	def add_tile_to_win(self, win):
		add_to_win(win, [self._space])
		add_to_win(win, self._path_graphics)
		self._space.set_depth(21)

		# the purpose of this for loop is to set the depths of all the lines
		for line in self._path_graphics:
			line.set_depth(20)

	def disable(self):
		self._moved = True

	def move_tile_to(self, goal):
		'''moves the tile and every graphical object related to it '''
		# check to see if the tile has moved
		if not self._moved:
			# split the goal into x and y coordinates
			gx = goal[0]
			gy = goal[1]

			# get the center and split it into x and y coordinates
			cx = self._center[0]
			cy = self._center[1]

			# find the difference in the x and y coordinates
			dx = int(gx - cx)
			dy = int(gy - cy)

			# move the tile
			self._space.move(dx, dy)

			# this moves the locations of all the ports
			for i in range(len(self._ports)):
				px = self._ports[i][0]
				py = self._ports[i][1]
				new_port = ((px + dx), (py + dy))
				self._ports[i] = new_port

			# the purpose of this for loop is to move every line on the tile
			for line in self._path_graphics:
				line.move(dx, dy)

			# move the center
			cx = cx + dx
			cy = cy + dy
			self._center = (cx, cy)

	def rotate(self):
		''' rotate the tile 90 degrees to the right '''
		# rotate which ports are where. this will also change the pathing by
		# passing each path a different set of coordinates. this is a blank list
		# that will be filled with the new ports
		new_ports = []

		# the purpose of this for loop is to reorder the current ports 
		for x in range(len(self._ports)):
			i = (x + 2) % 8
			new_ports.append(self._ports[i])

		# set self._ports to be equal to the new list of ports
		self._ports = new_ports

		# remove the previous lines
		for line in self._path_graphics:
			self._win.remove(line)

		# make new lines
		self._path_graphics = graphics(self._win, self._paths, self._ports)
		for line in self._path_graphics:
			line.add_handler(self)
		for line in self._path_graphics:
			line.set_depth(14)

	def handle_mouse_release(self, _):
		# access the global variable stored_tile
		# CITE: https://stackoverflow.com/questions/12665994/
		#		function-not-changing-global-variable
		# DESC: provided information on how to edit a global variable
		global stored_tile
		# store the tile so that it can be moved
		stored_tile = self

		# check to see if the tile has been moved
		if not self._moved:
			# pop the tile out
			self._space.set_depth(15)
			# the purpose of this for loop is to raise all the lines on the tile
			for line in self._path_graphics:
				line.set_depth(14)

			# create a highlight around the tile
			self._space.set_border_color('green')

	def get_ports(self):
		return self._ports

	def get_paths(self):
		return self._paths

class Player(): # this is not ready yet
	def __init__(self, player_number, win, game):
		''' initialize each player as an object in the Player class '''
		# access the global variable color_lst
		global color_lst

		self._player = player_number
		self._window = win
		self._game = game

		# this will be used to prevent players from being eliminated before they
		# get to play their first turn
		self._moved = False

		# set an arbitrary center to be reassigned later
		self._center = (-100, -100)

		# this references the global variable color_lst that assigns colors to
		# each player's stone based on the index number of the player
		self._color = color_lst[player_number]

		# give the player a stone
		self._stone = Circle(self._window, 10)
		self._stone.set_fill_color(self._color)

		# add the stone to the window but make it invisible
		add_to_win(self._window, [self._stone])
		self._stone.set_depth(100)

		# check to see if the player is on the board
		self._on_board = False

		# check to see if the player is eliminated
		self._elim = False

		# does the player have the dragon tile?
		self._has_dragon = False

	def move_player_to(self, coords):
		''' move the player to the coordinates '''
		self._stone.move_to(coords)
		self._center = coords

		# save the initial coordinates for a comparison
		initial = self._center

		# check to see if the player moved at all
		if initial != self._center:
			self._moved = True

	def eliminated(self, game):
		''' change a player's piece color to 'gray' and remove them from the
			board when they are eliminated '''
		# access the global variable hand
		global hand

		self._elim = True

		# change the color of the player's color to 'gray'
		self._color = 'gray'

		# set the depth of the stone to be below that of the board
		self._window.remove(self._stone)

		# return the player's hand to the deck one at a time so it can be drawn
		# and/or indexed properly
		for card in hand:
			game.add_to_deck(card)
			hand.remove(card)

		# add one to the number of players that have been eliminated
		self._game._eliminated_players += 1

		# the purpose of this if statement is to check to see if the player has
		# the dragon tile and to assign it back to being neutral if he/she does
		if self._has_dragon:
			return 'burlywood'

		# because there is a possible return there needs to be an assignment of
		# some variable
		return self._game._dragon._color

	def get_location(self):
		return self._center

	def add_to_hand(self, deck, dragon):
		''' draw tiles until the hand has 3 tiles in it '''
		# access the global variable hand
		global hand

		# check to see if the deck has at least one tile in it and that the
		# dragon tile is assigned to no one
		if len(deck) > 0:
			# the purpose of this while loop is to make the hand have 3 tiles
			while (len(hand) < 3) and (len(deck) > 0):
				if len(deck) > 1:
					hand.append(deck[0])
					deck = deck[1:]
				else:
					hand.append(deck[0])

		# the purpose of this if statement is to check to see if the dragon tile
		# is assigned to the player. the player only draws one tile here so
		# this had to be a separate statement
		if len(deck) > 0 and (dragon.get_color() == self._color):
			if len(deck) > 1:
				hand.append(deck[0])
				deck = deck[1:]
			else:
				hand.append(deck[0])

			# the dragon tile needs to be reassigned to its neutral color which
			# is why there is a return here
			return 'burlywood'

		# the purpose of this elif statement is to give the player the dragon
		# tile if there are no more tiles to be drawn as long as the dragon tile
		# has not been claimed by another player
		elif dragon.get_color() == 'burlywood':
			return self._color

		# the reason this is returned is because it is used to assign the color
		# of the dragon tile. the assignment of the dragon tile's color happens
		# every turn
		return dragon.get_color()

	def get_color(self):
		return self._color

	def switch_on(self):
		''' move the tiles in the player's hand onscreen '''
		# access the global variables hand and hand_coords
		global hand
		global hand_coords

		for i in range(len(hand)):
			hand[i].move_tile_to(hand_coords[i])

class Dragon_Tile(Space):
	def __init__(self, win, space_width, center, game):
		Space.__init__(self, win, space_width, center, game)
		self._color = 'burlywood'
		self._space.set_fill_color(self._color)

	def get_color(self):
		return self._color

	def set_color(self, color):
		self._color = color

	def handle_mouse_release(self, _):
		'''do nothing. this is here because i created this as a variation on the
		Space class which has its own event handler '''
		arbitrary_value = 0

class Rotate_Button(EventHandler):
	''' create the class for the rotate button '''
	def __init__(self, win, width, center):
		self._width = width
		self._center = center
		self._win = win

		# make the button's shape
		self._button = Square(win, self._width, self._center)
		self._button.set_fill_color('pink')
		self._button.set_depth(30)
		add_to_win(self._win, [self._button])

		# add a handler to the button
		self._button.add_handler(self)

	def handle_mouse_release(self, _):
		''' rotate the selected tile  '''
		global stored_tile

		try:
			stored_tile.rotate()
		except:
			# define an arbitrary value
			arbitrary = 0

class select_button(EventHandler):
	def __init__(self, win, center, player_count, game):
		self._center = center
		self._win = win
		self._player_count = player_count
		self._game = game

		# make the button's shape
		self._button = Circle(win, 25, self._center)
		self._button.add_handler(self)
		self._button.set_fill_color('burlywood')
		self._button.set_depth(10)
		add_to_win(self._win, [self._button])

		# make the text for the buttons
		self._text = Text(self._win, \
			str(self._player_count), \
			18, \
			self._center)
		self._text.set_depth(9)
		self._win.add(self._text)
		self._text.add_handler(self)

	def handle_mouse_release(self, _):
		''' return the number of players and remove the welcome screen and other
			player number buttons from visibility '''
		self._game._screen.set_depth(55)

		# the purpose of this for loop is to set all the player select buttons
		# to be below the blank screen
		for button in self._game._player_buttons:
			button._button.set_depth(60)
			button._text.set_depth(80)

		# set the number of players in the game to be player_count
		self._game._player_num = self._player_count

		# set the depth of the text to be under the screen
		self._game._welcome.set_depth(70)

		self._game.continued_init()

class place_player_button(EventHandler):
	def __init__(self, win, center, player, game):
		self._center = center
		self._win = win
		self._game = game
		self._player = player
		self._color = self._player.get_color()

		# make the button's shape
		self._button = Circle(win, 10, self._center)
		self._button.add_handler(self)
		self._button.set_fill_color(self._color)
		self._button.set_depth(10 + self._player._player)
		add_to_win(self._win, [self._button])

	def handle_mouse_release(self, _):
		''' return the number of players and remove the welcome screen and other
			player number buttons from visibility '''
		# move the player to the location of the button
		self._player.move_player_to(self._center)

		# set the player to be on top
		self._player._stone.set_depth(3)

		# generate a hand for the player
		self._player.add_to_hand(self._game._deck, self._game._dragon)

		self._player.switch_on()

		# the purpose of this for loop is to get rid of all the buttons on the
		# board to reveal the layer of buttons underneath
		for button in self._game._placement_buttons[self._player._player]:
			button._button.set_depth(100)

class Next_button(EventHandler):
	''' the class to advance the turns '''
	def __init__(self, win, text, center, game):
		self._win = win
		self._text = text
		self._game = game

		# make the button
		self._button = Rectangle(self._win, 200, 60, center)

		# add the button and the text to the window
		add_to_win(self._win, [self._button, self._text])

		# set the depths
		self._button.set_depth(1)
		self._text.set_depth(0)

		# set the color of the button
		self._button.set_fill_color('burlywood')

		# add the handlers
		self._button.add_handler(self)
		self._text.add_handler(self)

	def handle_mouse_release(self, _):
		''' remove everything opscuring the game '''
		# access the global variable stored_tile
		global stored_tile

		# remove everything obscuring the game
		self._game._screen.set_depth(53)
		self._win.remove(self._button)
		self._win.remove(self._text)

		# reset the value of stored_tile
		stored_tile = 'tile'


# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# this is the division between classes and functions, some of which call
# call classes
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0


def Border(win, inner_width, border_width, center):
	''' create the border for the board '''
	# this is the outer edge of the border
	edge = Square(win, int(2 * border_width + inner_width), center)
	edge.set_fill_color('wheat')

	# this is the inner playing area of the board
	game_board = Square(win, inner_width, center)
	game_board.set_fill_color('white')
	game_board.set_depth(45)

	# add the pieces of the board to the window
	win.add(edge)
	win.add(game_board)

def space(win, space_width, center):
	''' create all the spaces for the game and add them to the window '''
	# separate center into cx and cy
	cx = center[0]
	cy = center[1]

	# create a space
	new_space = Square(win, space_width, center)
	new_space.set_fill_color('white')

	# set the depth of the new space to be avove the board
	new_space.set_depth(30)

	add_to_win(win, [new_space])

	return new_space

def add_to_win(win, lst):
	for thing in lst:
		win.add(thing)

def random_List(number_of_tiles):
	''' create a random list of id numbers to randomize the shuffle order of
		the deck '''
	# this will store all the numbers as a list
	num_lst = []

	# the purpose of this while loop is to make a unique, ordered list of
	# numbers to serve as id numbers for all the tiles in the deck
	while len(num_lst) < number_of_tiles:
		# generate a random number
		number = random.randrange(number_of_tiles)

		# the purpose of this if statement is to make sure each number is unique
		if number not in num_lst:
			num_lst.append(number)

	return num_lst

def Ports(tile, center, tile_width, win):
	''' create a list of 4 paths connecting 2 ports on a tile together '''
	# break apart the center into cx and cy
	cx = center[0]
	cy = center[1]

	# create all the ports as tuples
	# top ports
	port0 = ((cx - tile_width // 6), (cy - tile_width // 2))
	port1 = ((tile_width // 6 + cx), (cy - tile_width // 2))
	
	# right ports
	port2 = ((tile_width // 2 + cx), (cy - tile_width // 6))
	port3 = ((tile_width // 2 + cx), (tile_width // 6 + cy))
	
	# bottom ports
	port4 = ((tile_width // 6 + cx), (tile_width // 2 + cy))
	port5 = ((cx - tile_width // 6), (tile_width // 2 + cy))
	
	# left ports
	port6 = ((cx - tile_width // 2), (tile_width // 6 + cy))
	port7 = ((cx - tile_width // 2), (cy - tile_width // 6))

	# make a list of ports
	port_lst = [port0, port1, port2, port3, port4, port5, port6, port7]

	# return the list of ports
	return port_lst

def make_spaces(win, tile_width, border_width, game):
	''' make the spaces on the game board '''
	# find the center of the first tile which will be used to find the
	# center of each subsequent space
	cx = border_width + (tile_width // 2)
	cy = border_width + (tile_width // 2)
	
	# create a blank list to store all the spaces in
	spaces = []

	# the purpose of this nested for loop is to make all of the spaces
	# on the board in a grid-like manner
	for row in range(rows):
		for col in range(cols):
			spaces.append(Space(win, tile_width, (cx, cy), game))
			cy += tile_width
		cy = border_width + (tile_width // 2)
		cx += tile_width

	return spaces

def make_tiles(win, length, game):
	''' make all the tiles. this is a lot of repetitive code but it is all
		necessary because each tile was specifically modeled after one that
		exists in the real game. i would not allow the tiles to be randomized
	'''
	# make an empty list to store all the tiles
	lst = []

	# make all the tiles. see docstring for the function for the reason this
	# code is so repetitive
	T1 = Tile(win, length, (748, 200), [(0, 2), (1, 7), (3, 5), (4, 6)], game)
	T2 = Tile(win, length, (748, 200), [(0, 3), (1, 4), (2, 5), (6, 7)], game)
	T3 = Tile(win, length, (748, 200), [(0, 5), (1, 4), (2, 7), (3, 6)], game)
	T4 = Tile(win, length, (748, 200), [(0, 4), (1, 2), (3, 6), (5, 7)], game)
	T5 = Tile(win, length, (748, 200), [(0, 1), (2, 3), (4, 6), (5, 7)], game)
	T6 = Tile(win, length, (748, 200), [(0, 7), (1, 3), (2, 5), (4, 6)], game)
	T7 = Tile(win, length, (748, 200), [(0, 4), (1, 2), (3, 7), (5, 6)], game)
	T8 = Tile(win, length, (748, 200), [(0, 3), (1, 5), (2, 6), (4, 7)], game)
	T9 = Tile(win, length, (748, 200), [(0, 1), (2, 6), (3, 4), (5, 7)], game)
	T10 = Tile(win, length, (748, 200), [(0, 1), (2, 6), (3, 5), (4, 7)], game)
	T11 = Tile(win, length, (748, 200), [(0, 7), (1, 2), (3, 4), (5, 6)], game)
	T12 = Tile(win, length, (748, 200), [(0, 3), (1, 4), (2, 7), (5, 6)], game)
	T13 = Tile(win, length, (748, 200), [(0, 3), (1, 6), (2, 5), (4, 7)], game)
	T14 = Tile(win, length, (748, 200), [(0, 4), (1, 5), (2, 7), (3, 6)], game)
	T15 = Tile(win, length, (748, 200), [(0, 4), (1, 5), (2, 6), (3, 7)], game)
	T16 = Tile(win, length, (748, 200), [(0, 1), (2, 7), (3, 6), (4, 5)], game)
	T17 = Tile(win, length, (748, 200), [(0, 7), (1, 6), (2, 5), (3, 4)], game)
	T18 = Tile(win, length, (748, 200), [(0, 5), (1, 6), (2, 4), (3, 7)], game)
	T19 = Tile(win, length, (748, 200), [(0, 6), (1, 5), (2, 4), (3, 7)], game)
	T20 = Tile(win, length, (748, 200), [(0, 4), (1, 5), (2, 3), (6, 7)], game)
	T21 = Tile(win, length, (748, 200), [(0, 2), (1, 3), (4, 7), (5, 6)], game)
	T22 = Tile(win, length, (748, 200), [(0, 4), (1, 7), (2, 5), (3, 6)], game)
	T23 = Tile(win, length, (748, 200), [(0, 6), (1, 7), (2, 4), (3, 5)], game)
	T24 = Tile(win, length, (748, 200), [(0, 4), (1, 3), (2, 6), (5, 7)], game)
	T25 = Tile(win, length, (748, 200), [(0, 5), (1, 7), (2, 3), (4, 6)], game)
	T26 = Tile(win, length, (748, 200), [(0, 2), (1, 5), (3, 4), (6, 7)], game)
	T27 = Tile(win, length, (748, 200), [(0, 1), (2, 5), (3, 4), (6, 7)], game)
	T28 = Tile(win, length, (748, 200), [(0, 6), (1, 4), (1, 3), (5, 7)], game)
	T29 = Tile(win, length, (748, 200), [(0, 5), (1, 2), (3, 4), (6, 7)], game)
	T30 = Tile(win, length, (748, 200), [(0, 1), (2, 3), (4, 5), (6, 7)], game)
	T31 = Tile(win, length, (748, 200), [(0, 6), (1, 2), (3, 4), (5, 7)], game)
	T32 = Tile(win, length, (748, 200), [(0, 3), (1, 6), (2, 4), (5, 7)], game)
	T33 = Tile(win, length, (748, 200), [(0, 1), (2, 5), (3, 7), (4, 6)], game)
	T34 = Tile(win, length, (748, 200), [(0, 6), (1, 4), (2, 7), (3, 5)], game)
	T35 = Tile(win, length, (748, 200), [(0, 6), (1, 5), (2, 7), (3, 4)], game)

	# add all the tiles to the list. i have that many tiles. thats why this is
	# so repetitive.
	lst.append(T1)
	lst.append(T2)
	lst.append(T3)
	lst.append(T4)
	lst.append(T5)
	lst.append(T6)
	lst.append(T7)
	lst.append(T8)
	lst.append(T9)
	lst.append(T10)
	lst.append(T11)
	lst.append(T12)
	lst.append(T13)
	lst.append(T14)
	lst.append(T15)
	lst.append(T16)
	lst.append(T17)
	lst.append(T18)
	lst.append(T19)
	lst.append(T20)
	lst.append(T21)
	lst.append(T22)
	lst.append(T23)
	lst.append(T24)
	lst.append(T25)
	lst.append(T26)
	lst.append(T27)
	lst.append(T28)
	lst.append(T29)
	lst.append(T30)
	lst.append(T31)
	lst.append(T32)
	lst.append(T33)
	lst.append(T34)
	lst.append(T35)

	# return the list
	return lst

def graphics(win, paths, ports):
	''' create all the graphics for the tile '''
	# break apart all the paths
	p0 = paths[0]
	p1 = paths[1]
	p2 = paths[2]
	p3 = paths[3]

	# make the lines connecting the ports
	l0 = Polygon(win, [ports[p0[0]], ports[p0[1]]])
	l1 = Polygon(win, [ports[p1[0]], ports[p1[1]]])
	l2 = Polygon(win, [ports[p2[0]], ports[p2[1]]])
	l3 = Polygon(win, [ports[p3[0]], ports[p3[1]]])

	# make a list of the lines
	line_lst = [l0, l1, l2, l3]

	# bring all the lines to the front
	for line in line_lst:
		line.set_depth(20)

	# add the lines to the window
	add_to_win(win, line_lst)

	return line_lst

def within_player_range(space_center, player_location):
	''' find out if a space is within the range of a player '''
	# access the global variable within_range
	global within_range

	# split player_location into its components
	px = player_location[0]
	py = player_location[1]

	# split space_center into its components
	sx = space_center[0]
	sy = space_center[1]

	# find dx and dy
	dx = abs(px - sx)
	dy = abs(py - sy)

	# check to see if the hypotenuse of the right triangle formed between the
	# points, using dx and dy as the height, is equal to what it should be if
	# the space were adjacent to the player
	hypotenuse = Pythagoras(dx, dy)

	return hypotenuse == within_range

def Pythagoras(x, y):
	''' compute the Pythagorean Theorem '''
	hypotenuse = math.sqrt((x ** 2) + (y ** 2))

	return hypotenuse

def make_player_select(win, game):
	''' make the buttons to select the number of players '''
	two = select_button(win, (244, 350), 2, game)
	three = select_button(win, (304, 350), 3, game)
	four = select_button(win, (364, 350), 4, game)
	five = select_button(win, (424, 350), 5, game)
	six = select_button(win, (484, 350), 6, game)
	seven = select_button(win, (544, 350), 7, game)
	eight = select_button(win, (604, 350), 8, game)

	# make a list of the buttons
	button_lst = [two, three, four, five, six, seven, eight]

	return button_lst

def player_placement(win, initial_space_center, space_width, player, game):
	''' place the player on the board '''
	# split the initial center of the space
	cx = initial_space_center[0]
	cy = initial_space_center[1]

	# make a list for the buttons
	button_lst = []

	# the putpose of this for loop is to add buttons to every possible starting
	# location for a player
	for row in range(rows):
		# the reason all the checks are in the second for loop is to ensure that
		# all possible buttons are placed as the corners will need 2 sets of the
		# buttons that are created in each if statement
		for col in range(cols):
			# check to see if the space is at the top of the board
			if row == 0: 
				place_one = ((cx - space_width // 6), (cy - space_width // 2))
				place_two = ((space_width // 6 + cx), (cy - space_width // 2))
				button_lst.append(place_player_button(win, place_one, player, \
									game))
				button_lst.append(place_player_button(win, place_two, player, \
									game))
			
			# check to see if the space is at the bottom of the board
			if row == 5: 
				place_one = ((space_width // 6 + cx), (space_width // 2 + cy))
				place_two = ((cx - space_width // 6), (space_width // 2 + cy))
				button_lst.append(place_player_button(win, place_one, player, \
									game))
				button_lst.append(place_player_button(win, place_two, player, \
									game))
			
			# check to see if the space is on the left side of the board
			if col == 0 : 
				place_one = ((cx - space_width // 2), (space_width // 6 + cy))
				place_two = ((cx - space_width // 2), (cy - space_width // 6))
				button_lst.append(place_player_button(win, place_one, player, \
									game))
				button_lst.append(place_player_button(win, place_two, player, \
									game))

			# check to see if the space is on the right side of the board
			if col == 5: 
				place_one = ((space_width // 2 + cx), (cy - space_width // 6))
				place_two = ((space_width // 2 + cx), (space_width // 6 + cy))
				button_lst.append(place_player_button(win, place_one, player, \
									game))
				button_lst.append(place_player_button(win, place_two, player, \
									game))
			
			cx += space_width
		cx = initial_space_center[0]
		cy += space_width

	return button_lst

def move_players(space, game, exempt_player): # this is not done yet
	''' move every player in the game '''
	# access the global variable stored_tile
	global stored_tile 

	# make a list of the players
	player_lst = []
	for player in game._players:
		player_lst.append(player)

	# remove the exempt player
	player_lst.remove(game._players[exempt_player])

	for player in player_lst:
		# this variable determines whether there are more tiles to move to
		more_tiles = True

		# the purpose of this while loop is to move the player until there
		# are no more tiles to move to
		while more_tiles:
			player_location = player.get_location()
			# get the ports of the tile that was just played
			tile_ports = stored_tile.get_ports()

			# get the paths
			tile_paths = stored_tile.get_paths()

			# separate the paths into path_start and path_end
			path_start = []
			path_end = []

			# the purpose of these for loops is to separate the paths as the
			# comment above describes
			for path in tile_paths:
				path_start.append(path[0])
			for path in tile_paths:
				path_end.append(path[1])

			# the purpose of this nested for loop is to find which port the
			# player is on then to move the player
			for i in range(len(tile_ports)):
				if player_location == tile_ports[i]:
					# these for loops nested within the larger for loop
					# check to see if the player starts at the beginning or
					# end of a path, both being arbitrarily defined, and
					# moves them to the other side
					for index in range(len(path_start)):
						if i == path_start[index]:
							player.move_player_to(tile_ports[path_end[index]])
					for index in range(len(path_end)):
						if i == path_end[index]:
							player.move_player_to(tile_ports[path_start[index]])
				
			# find the new coordinates of the player
			new_coords = player.get_location()
				
			# check the x coordinate against the boundaries of the board
			# CITE: https://stackoverflow.com/questions/181530/
			#		styling-multi-line-conditions-in-if-statements
			# DESC: provided an example of a multi-line if statement
			if ((player._moved and
				new_coords[0] <= game._border_width) or
				(new_coords[1] >= game._board_width)):
				player.eliminated(game)

			# check the y coordinate against the boundaries of the board
			if ((player._moved and 
				new_coords[1] <= game._border_width) or
				(new_coords[1] >= game._board_width)):
				player.eliminated(game)
				
			# check to see if there is another tile to move to
			more_tiles = game.adjacent_tile(new_coords)

			# the purpose of this for loop is to move the player more if
			# possible
			for tile in game._tiles:
				for i in range(len(tile._ports)):
					if player_location == tile_ports[i] and tile != stored_tile:
					# these for loops nested within the larger for loop
					# check to see if the player starts at the beginning or
					# end of a path, both being arbitrarily defined, and
					# moves them to the other side
						for index in range(len(path_start)):
							if i == path_start[index]:
								player.move_player_to(tile_ports[path_end\
														[index]])
						for index in range(len(path_end)):
							if i == path_end[index]:
								player.move_player_to(tile_ports[path_start\
														[index]])	

def next_turn(game):
	''' bring up a wait screen to confirm that it is the next player's turn '''
	game._screen.set_depth(2)
	center = (424, 324) # this is the center of the window
	text = Text(game._win, 'Next player', 18, center)
	Next_button(game._win, text, center, game)
	game._turn += 1



# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# main function(s) below this line
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0
# --0----0----0----0----0----0----0----0----0----0----0----0----0----0----0----0


def program(win):
	''' begins the game '''
	# set up the window
	win.set_width(848)
	win.set_height(648)

	# begin the game
	Tsuro = Game(win)

def main():
	StartGraphicsSystem(program)

if __name__ == "__main__":
	main()
