
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N09935924
#    Student name: Greyden Scott
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  BUILDING BLOCKS
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "stack_blocks".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a pile of building blocks
#  whose arrangement is determined by data stored in a list which
#  specifies the blocks' locations.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

block_size = 250 # pixels
top_and_bottom_border = 75 # pixels
left_and_right_border = 150 # pixels
canvas_width = (block_size + left_and_right_border) * 2
canvas_height = (block_size + top_and_bottom_border) * 2

#
#--------------------------------------------------------------------#



#-----Functions for Managing the Canvas------------------------------#
#
# The functions in this section are called by the main program to
# set up the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

		# Set up the drawing canvas
		setup(canvas_width, canvas_height)

		# Set the coordinate system so that location (0, 0) is centred on
		# the point where the blocks will be stacked
		setworldcoordinates(-canvas_width / 2, -top_and_bottom_border,
												canvas_width / 2, canvas_height - top_and_bottom_border)

		# Draw as fast as possible
		tracer(False)

		# Colour the sky blue
		bgcolor('sky blue')

		# Draw the ground as a big green rectangle (sticking out of the
		# bottom edge of the drawing canvas slightly)
		overlap = 50 # pixels
		penup()
		goto(-(canvas_width / 2 + overlap), -(top_and_bottom_border + overlap)) # start at the bottom-left
		fillcolor('pale green')
		begin_fill()
		setheading(90) # face north
		forward(top_and_bottom_border + overlap)
		right(90) # face east
		forward(canvas_width + overlap * 2)
		right(90) # face south
		forward(top_and_bottom_border + overlap)
		end_fill()
		penup()

		# Draw a friendly sun peeking into the image
		goto(-canvas_width / 2, block_size * 2)
		color('yellow')
		dot(250)

		# Reset everything ready for the student's solution
		color('black')
		width(1)
		penup()
		home()
		setheading(0)
		tracer(True)
		

# As a debugging aid, mark the coordinates of the centres and corners
# of the places where the blocks will appear
def mark_coords(show_corners = False, show_centres = False):

		# Go to each coordinate, draw a dot and print the coordinate, in the given colour
		def draw_each_coordinate(colour):
				color(colour)
				for x_coord, y_coord in coordinates:
						goto(x_coord, y_coord)
						dot(4)
						write(' ' + str(x_coord) + ', ' + str(y_coord), font = ('Arial', 12, 'normal'))

		# Don't draw lines between the coordinates
		penup()

		# The list of coordinates to display
		coordinates = []

		# Only mark the corners if the corresponding argument is True
		if show_corners:
				coordinates = [[-block_size, block_size * 2], [0, block_size * 2], [block_size, block_size * 2],
											 [-block_size, block_size], [0, block_size], [block_size, block_size],
											 [-block_size, 0], [0, 0], [block_size, 0]]
				draw_each_coordinate('dark blue')

		# Only mark the centres if the corresponding argument is True
		if show_centres:
				coordinates = [[-block_size / 2, block_size / 2], [block_size / 2, block_size / 2],
											 [-block_size / 2, block_size + block_size / 2], [block_size / 2, block_size + block_size / 2]]
				draw_each_coordinate('red')

		# Put the cursor back how it was
		color('black')
		home()


# End the program by hiding the cursor and releasing the window
def release_drawing_canvas():
		tracer(True)
		hideturtle()
		done()
		
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# the building blocks:
#
# 1. The name of the block, from 'Block A' to 'Block D'
# 2. The place to put the block, either 'Top left', 'Top right',
#    'Bottom left' or 'Bottom right'
# 3. The block's orientation, meaning the direction in which the top
#    of the block is pointing, either 'Up', 'Down', 'Left' or 'Right'
# 4. An optional mystery value, 'X' or 'O', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all four blocks.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#

# The following data set doesn't require drawing any blocks
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

arrangement_00 = []

# Each of the following data sets specifies drawing just one block
# in an upright orientation.  You may find them useful when
# creating your individual pieces.

arrangement_01 = [['Block A', 'Bottom left', 'Up', 'O']]
arrangement_02 = [['Block B', 'Bottom right', 'Up', 'O']]
arrangement_03 = [['Block C', 'Bottom left', 'Up', 'O']]
arrangement_04 = [['Block D', 'Bottom right', 'Up', 'O']]

# Each of the following data sets specifies drawing just one block
# in non-upright orientations.  You may find them useful when
# ensuring that you can draw all the blocks facing in different
# directions.

arrangement_10 = [['Block A', 'Bottom left', 'Down', 'O']]
arrangement_11 = [['Block A', 'Bottom right', 'Left', 'O']]
arrangement_12 = [['Block A', 'Bottom left', 'Right', 'O']]

arrangement_13 = [['Block B', 'Bottom left', 'Down', 'O']]
arrangement_14 = [['Block B', 'Bottom right', 'Left', 'O']]
arrangement_15 = [['Block B', 'Bottom left', 'Right', 'O']]

arrangement_16 = [['Block C', 'Bottom left', 'Down', 'O']]
arrangement_17 = [['Block C', 'Bottom right', 'Left', 'O']]
arrangement_18 = [['Block C', 'Bottom left', 'Right', 'O']]

arrangement_19 = [['Block D', 'Bottom left', 'Down', 'O']]
arrangement_20 = [['Block D', 'Bottom right', 'Left', 'O']]
arrangement_21 = [['Block D', 'Bottom left', 'Right', 'O']]

# The following data sets all stack various numbers of
# blocks in various orientations

arrangement_30 = [['Block C', 'Bottom right', 'Up', 'O'],
									['Block D', 'Top right', 'Up', 'O']]
arrangement_31 = [['Block A', 'Bottom left', 'Up', 'O'],
									['Block C', 'Bottom left', 'Up', 'O']]

arrangement_32 = [['Block B', 'Bottom right', 'Up', 'O'],
									['Block D', 'Bottom left', 'Up', 'O'],
									['Block C', 'Top right', 'Up', 'O']]
arrangement_33 = [['Block B', 'Bottom right', 'Up', 'O'],
									['Block D', 'Bottom left', 'Up', 'O'],
									['Block A', 'Top left', 'Up', 'O']]
arrangement_34 = [['Block B', 'Bottom left', 'Up', 'O'],
									['Block A', 'Bottom right', 'Up', 'O'],
									['Block D', 'Top left', 'Up', 'O'],
									['Block C', 'Top right', 'Up', 'O']]

arrangement_40 = [['Block C', 'Bottom right', 'Left', 'O'],
									['Block D', 'Top right', 'Right', 'O']]
arrangement_41 = [['Block A', 'Bottom left', 'Down', 'O'],
									['Block C', 'Bottom left', 'Up', 'O']]

arrangement_42 = [['Block B', 'Bottom right', 'Left', 'O'],
									['Block D', 'Bottom left', 'Left', 'O'],
									['Block C', 'Top right', 'Down', 'O']]
arrangement_43 = [['Block B', 'Bottom right', 'Right', 'O'],
									['Block D', 'Bottom left', 'Left', 'O'],
									['Block A', 'Top left', 'Right', 'O']]
arrangement_44 = [['Block B', 'Bottom left', 'Down', 'O'],
									['Block A', 'Bottom right', 'Left', 'O'],
									['Block D', 'Top left', 'Right', 'O'],
									['Block C', 'Top right', 'Up', 'O']]

arrangement_50 = [['Block B', 'Bottom right', 'Left', 'O'],
									['Block D', 'Bottom left', 'Left', 'O'],
									['Block C', 'Top right', 'Down', 'X']]
arrangement_51 = [['Block B', 'Bottom right', 'Right', 'O'],
									['Block D', 'Bottom left', 'Left', 'O'],
									['Block A', 'Top left', 'Right', 'X']]
arrangement_52 = [['Block B', 'Bottom left', 'Down', 'O'],
									['Block A', 'Bottom right', 'Left', 'O'],
									['Block D', 'Top left', 'Right', 'O'],
									['Block C', 'Top right', 'Up', 'X']]

arrangement_60 = [['Block B', 'Bottom right', 'Left', 'X'],
									['Block D', 'Bottom left', 'Left', 'O'],
									['Block C', 'Top right', 'Down', 'O']]
arrangement_61 = [['Block B', 'Bottom right', 'Right', 'O'],
									['Block D', 'Bottom left', 'Left', 'X'],
									['Block A', 'Top left', 'Right', 'O']]
arrangement_62 = [['Block B', 'Bottom left', 'Down', 'X'],
									['Block A', 'Bottom right', 'Left', 'X'],
									['Block D', 'Top left', 'Right', 'O'],
									['Block C', 'Top right', 'Up', 'O']]

# The following arrangements create your complete image, but
# oriented the wrong way

arrangement_80 = [['Block C', 'Bottom right', 'Left', 'O'],
									['Block D', 'Top right', 'Left', 'X'],
									['Block A', 'Bottom left', 'Left', 'O'],
									['Block B', 'Top left', 'Left', 'O']]

arrangement_81 = [['Block B', 'Bottom right', 'Right', 'X'],
									['Block D', 'Bottom left', 'Right', 'X'],
									['Block A', 'Top right', 'Right', 'O'],
									['Block C', 'Top left', 'Right', 'O']]

arrangement_89 = [['Block A', 'Bottom right', 'Down', 'O'],
									['Block C', 'Top right', 'Down', 'O'],
									['Block B', 'Bottom left', 'Down', 'O'],
									['Block D', 'Top left', 'Down', 'O']]

# The following arrangements should create your complete image
# (but with the blocks stacked in a different order each time)

arrangement_90 = [['Block C', 'Bottom left', 'Up', 'O'],
									['Block D', 'Bottom right', 'Up', 'O'],
									['Block B', 'Top right', 'Up', 'X'],
									['Block A', 'Top left', 'Up', 'O']]

arrangement_91 = [['Block D', 'Bottom right', 'Up', 'X'],
									['Block C', 'Bottom left', 'Up', 'X'],
									['Block A', 'Top left', 'Up', 'O'],
									['Block B', 'Top right', 'Up', 'O']]

arrangement_92 = [['Block D', 'Bottom right', 'Up', 'X'],
									['Block B', 'Top right', 'Up', 'O'],
									['Block C', 'Bottom left', 'Up', 'O'],
									['Block A', 'Top left', 'Up', 'O']]

arrangement_99 = [['Block C', 'Bottom left', 'Up', 'O'],
									['Block D', 'Bottom right', 'Up', 'O'],
									['Block A', 'Top left', 'Up', 'O'],
									['Block B', 'Top right', 'Up', 'O']]

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "stack_blocks" function.
#

# Draw the stack of blocks as per the provided data set
def stack_blocks(arrangement):
	#Configured the color mode to use RGB 255. 
	colormode(255)

	#Draws the background. Orientation indepedent as only requires white background.
	def drawbackGround(block):
		right = 0
		left = 180
		up = 90
		down = 270
		# Reads the position based on the passed block number
		# and sets the starting location based on the result
		if (arrangement[block][1] == "Top left"):
			goto(-250,500)
		elif (arrangement[block][1] == "Top right"):
			goto(0,500)
		elif (arrangement[block][1] == "Bottom left"):
			goto(-250,250)
		elif (arrangement[block][1] == "Bottom right"):
			goto(0,250)
		else:
			return
		# START BACKGROUND
		color('white')
		width(1)
		pendown()
		begin_fill()
		setheading(down)
		forward(250)
		setheading(right)
		forward(250)
		setheading(up)
		forward(250)
		setheading(left)
		forward(250)
		end_fill()
		penup()
		# END BACKGROUND

	# Draws the boarder
	# Calls the start location fucntion to determine starting location
	# Takes several parameters to assist with directions
	def draw_boarder(arrangement, block, left, right, up, down):
		goto_start_location(arrangement, block)
		setheading(up)
		forward(125)
		setheading(left)
		forward(125)
		color("black")
		width(3)
		pendown()
		setheading(down)
		forward(250)
		setheading(right)
		forward(250)
		setheading(up)
		forward(250)
		setheading(left)
		forward(250)
		penup()

	# Positions the turtle at teh starting location for each block
	# Takes the arrangements and current blocks as arguments
	# to determine what the starting location is
	def goto_start_location(arrangement, block):
		if (arrangement[block][1] == "Top left"):
			goto(-125, 375)
		elif (arrangement[block][1] == "Top right"):
			goto(125, 375)
		elif (arrangement[block][1] == "Bottom left"):
			goto(-125, 125)
		elif (arrangement[block][1] == "Bottom right"):
			goto(125, 125)
		else:
			goto(-125,375)

	# Sets the oreintation of the directions based on the orientation
	# specified in the arrangement
	def set_orientation(block):
		if (arrangement[block][2] == "Up"):
			left = 180
			up = 90
			right = 0
			down = 270
		elif (arrangement[block][2] == "Right"):
			left = 90
			up = 0
			right = 270
			down = 180
		elif (arrangement[block][2] == "Down"):
			left = 0
			up = 270
			right = 180
			down = 90
		elif (arrangement[block][2] == "Left"):
			left = 270
			up = 180
			right = 90
			down = 0
		else: 
			left = 180
			up = 90
			right = 0
			down = 270
		# Returns left up right down directions to be passed into a variable
		return [left, up, right, down]
	
######################################################
## START BLOCK A									##
######################################################
	def blockA(block = 0):
		# 1. Draw Background
		drawbackGround(block)
		# 2. Configure Orientation
		directions = set_orientation(block)
		# pass results from orientation to indivudal directions
		left = directions[0]
		up = directions[1]
		right = directions[2]
		down = directions[3]
		# 3. Goto Start Location
		goto_start_location(arrangement, block)
		# 4. Draw the details of the block
		#LAYER 1 RED
		setheading(up)
		forward(125)
		setheading(right)
		forward(125)
		setheading(down)
		forward(50)
		pendown()
		setheading(left)
		color(224, 77, 43) #RGB Google Chrome RED
		begin_fill()
		circle(200, 90)
		setheading(right)
		forward(200)
		setheading(up)
		forward(200)
		end_fill()
		penup()
		#LAYER 2 WHITE
		setheading(down)
		forward(200)
		setheading(up)
		forward(110)
		setheading(left)
		color('white') # Standard White
		begin_fill()
		pendown()
		circle(110, 90)
		setheading(right)
		forward(110)
		setheading(up)
		forward(110)
		end_fill()
		penup()#
		#LAYER 3 BLUE
		setheading(down)
		forward(20)
		setheading(left)
		color(37, 171, 217) #Google Chrome BLUE
		begin_fill()
		pendown()
		circle(90,90)
		setheading(right)
		forward(90)
		setheading(up)
		forward(90)
		pendown()
		end_fill()
		#LAYER 4 GREEN
		penup()
		setheading(up)
		forward(110)
		setheading(left)
		circle(200, 57)
		pendown()
		begin_fill()
		color(113, 210, 117) #Google Chrome GREEN
		circle(200, 33)
		setheading(right)
		forward(90)
		end_fill()
		penup()

		# 5. Draw the Boarder
		draw_boarder(arrangement, block, left, right, up, down)
######################################################
## END BLOCK A							            ##
######################################################		

######################################################
## START BLOCK B 						         	##
######################################################
	def blockB(block = 1):
		# 1. Draw Background
		drawbackGround(block)
		# 2. Configure Orientation
		directions = set_orientation(block)
		left = directions[0]
		up = directions[1]
		right = directions[2]
		down = directions[3]
		# 3. Goto Start Location
		goto_start_location(arrangement, block)
		# 4. Draw the details of the block
		# LAYER 1 YELLOW
		setheading(down)
		forward(125)
		setheading(right)
		forward(75)
		pendown()
		setheading(up)
		color(249, 219, 70) #Google Chrome YELLOW
		begin_fill()
		circle(200, 90)
		setheading(down)
		forward(200)
		setheading(right)
		forward(200)
		end_fill()
		penup()
		#LAYER 2 WHITE
		setheading(left)
		forward(90)
		pendown()
		setheading(up)
		color('white')
		begin_fill()
		circle(110, 90)
		setheading(down)
		forward(110)
		setheading(right)
		forward(110)
		end_fill()
		penup()
		# LAYER 3 BLUE
		setheading(left)
		forward(20)
		setheading(up)
		pendown()
		color(37, 171, 217) #Google Chrome BLUE
		begin_fill()
		circle(90,90)
		setheading(down)
		forward(90)
		setheading(right)
		forward(90)
		end_fill()
		penup()
		# LAYER 4 RED
		forward(110)
		setheading(up)
		circle(200,34)
		pendown()
		begin_fill()
		color(224, 77, 43) #RGB Google Chrome RED
		circle(200, 56)
		setheading(down)
		forward(89)
		setheading(right)
		forward(166)
		penup()
		end_fill()
		# 5. Draw the Boarder
		draw_boarder(arrangement, block, left, right, up, down)
######################################################
## END BLOCK B								        ##
######################################################

######################################################
## START BLOCK C							   		##
######################################################
	def blockC(block = 2):
		# 1. Draw Background
		drawbackGround(block)
		# 2. Configure Orientation
		directions = set_orientation(block)
		left = directions[0]
		up = directions[1]
		right = directions[2]
		down = directions[3]
		# 3. Goto Start Location
		goto_start_location(arrangement, block)
		# 4. Draw the details of the block
		# Layer 1 GREEN
		setheading(up)
		forward(125)
		setheading(left)
		forward(75)
		pendown()
		setheading(down)
		color(113, 210, 117) #Google Chrome GREEN
		begin_fill()
		circle(200, 90)
		setheading(up)
		forward(200)
		setheading(left)
		forward(200)
		end_fill()
		penup()
		# LAYER 2 WHITE
		setheading(right)
		forward(90)
		pendown()
		setheading(down)
		color('white')
		begin_fill()
		circle(110, 90)
		setheading(up)
		forward(110)
		setheading(left)
		forward(110)
		end_fill()
		penup()
		# LAYER 3 BLUE
		setheading(right)
		forward(20)
		pendown()
		setheading(down)
		color(37, 171, 217) #Google Chrome BLUE
		begin_fill()
		circle(90, 90)
		setheading(up)
		forward(90)
		setheading(left)
		forward(90)
		end_fill()
		penup()
		# 5. Draw the Boarder
		draw_boarder(arrangement, block, left, right, up, down)
######################################################
## END BLOCK C								        ##
######################################################

######################################################
## START BLOCK D 						            ##
######################################################
	def blockD(block = 3):
		# 1. Draw Background
		drawbackGround(block)
		# 2. Configure Orientation
		directions = set_orientation(block)
		left = directions[0]
		up = directions[1]
		right = directions[2]
		down = directions[3]
		# 3. Goto Start Location
		goto_start_location(arrangement, block)
		# 4. Draw the details of the block
		# LAYER 1 YELLOW
		setheading(left)
		forward(125)
		setheading(down)
		forward(75)
		pendown()
		setheading(right)
		color(249, 219, 70) #Google Chrome YELLOW
		begin_fill()
		circle(200, 90)
		setheading(left)
		forward(200)
		setheading(down)
		forward(200)
		end_fill()
		penup()
		# LAYER 2 WHITE
		setheading(up)
		forward(90)
		pendown()
		setheading(right)
		color('white')
		begin_fill()
		circle(110, 90)
		setheading(left)
		forward(110)
		setheading(down)
		forward(110)
		end_fill()
		penup()
		# LAYER 3 BLUE
		setheading(up)
		forward(20)
		pendown()
		setheading(right)
		color(37, 171, 217) #Google Chrome BLUE
		begin_fill()
		circle(90, 90)
		setheading(left)
		forward(90)
		setheading(down)
		forward(90)
		end_fill()
		penup()
		# LAYER 4 GREEN
		setheading(down)
		forward(21)
		setheading(right)
		color(113, 210, 117) #Google Chrome Green
		pendown()
		begin_fill()
		circle(110,50)
		# This series of if statements handles the 
		# direction in which the green draws based on 
		# orientation
		if (arrangement[block][2] == "Up"):
			setheading(236)
		elif (arrangement[block][2] == "Right"):
			setheading(146)
		elif (arrangement[block][2] == "Down"):
			setheading(56 )
		elif (arrangement[block][2] == "Left"):
			setheading(326)
		else:
			setheading(236)
		forward(155)
		setheading(up)
		forward(90)
		end_fill()
		penup()
		# 5. Draw the Boarder
		draw_boarder(arrangement, block, left, right, up, down)
######################################################
## END BLOCK D							            ##
######################################################

######################################################
## Drawing the Blocks						        ##
######################################################
	#Set up variables to assist in identifying which blocks are not drawn.
	left_did_not_draw = False
	right_did_not_draw = False
	
	# Reading the arrangment to print the blocks
	# For each block in the arrangement
	for block_item in arrangement:
		# 1. Assign the index of the block to a variable
		block_index = arrangement.index(block_item)
		# For each item in the block
		for the_block in block_item:
			# 2. Check the block title and produce
			# the relevant block based on the title
			# pass the block index to the block
			if the_block == "Block A":
				# Check to see if the block should be drawn
				if block_item[3] != 'X':
					# If it should be drawn, check to see if its top left 
					# or check to see if its Top right
					if left_did_not_draw and block_item[1] == "Top left":
						# if it is top left and the bottom left is missing
						# change the arragnment so it draws at the bottom left position
						arrangement[block_index][1] = "Bottom left"
						blockA(block_index)
					elif right_did_not_draw and block_item[1] == "Top right":
						# if it is top right and the bottom right is missing
						# change the arrangment so it daws at the bottom right position
						arrangement[block_index][1] = "Bottom right"
						blockA(block_index)
					else:
						# if no block is missing underneath then draw block as normal
						blockA(block_index)
				else:
					# if an X is present in the arrangment
					# set the left/right_did_not_draw_boolean to true
					if block_item[1] == "Bottom left":
						left_did_not_draw = True
					elif block_item[1] == "Bottom right":
						right_did_not_draw = True
					else: 
						pass
			elif the_block == "Block B":
				# Check to see if the block should be drawn
				if block_item[3] != 'X':
					# If it should be drawn, check to see if its top left 
					# or check to see if its Top right
					if left_did_not_draw and block_item[1] == "Top left":
						# if it is top left and the bottom left is missing
						# change the arragnment so it draws at the bottom left position
						arrangement[block_index][1] = "Bottom left"
						arrangB(block_index)
					elif right_did_not_draw and block_item[1] == "Top right":
						# if it is top right and the bottom right is missing
						# change the arrangment so it daws at the bottom right position
						arrangement[block_index][1] = "Bottom right"
						blockB(block_index)
					else:
						# if no block is missing underneath then draw block as normal
						blockB(block_index)
				else:
					# if an X is present in the arrangment
					# set the left/right_did_not_draw_boolean to true
					if block_item[1] == "Bottom left":
						left_did_not_draw = True
					elif block_item[1] == "Bottom right":
						right_did_not_draw = True
					else: 
						pass
			elif the_block == "Block C":
				# Check to see if the block should be drawn
				if block_item[3] != 'X':
					# If it should be drawn, check to see if its top left 
					# or check to see if its Top right
					if left_did_not_draw and block_item[1] == "Top left":
						# if it is top left and the bottom left is missing
						# change the arragnment so it draws at the bottom left position
						arrangement[block_index][1] = "Bottom left"
						blockC(block_index)
					elif right_did_not_draw and block_item[1] == "Top right":
						# if it is top right and the bottom right is missing
						# change the arrangment so it daws at the bottom right position
						arrangement[block_index][1] = "Bottom right"
						blockC(block_index)
					else:
						# if no block is missing underneath then draw block as normal
						blockC(block_index)
				else:
					# if an X is present in the arrangment
					# set the left/right_did_not_draw_boolean to true
					if block_item[1] == "Bottom left":
						left_did_not_draw = True
					elif block_item[1] == "Bottom right":
						right_did_not_draw = True
					else: 
						pass
			elif the_block == "Block D":
				# Check to see if the block should be drawn
				if block_item[3] != 'X':
					# If it should be drawn, check to see if its top left 
					# or check to see if its Top right
					if left_did_not_draw and block_item[1] == "Top left":
						# if it is top left and the bottom left is missing
						# change the arragnment so it draws at the bottom left position
						arrangement[block_index][1] = "Bottom left"
						blockD(block_index)
					elif right_did_not_draw and block_item[1] == "Top right":
						# if it is top right and the bottom right is missing
						# change the arrangment so it daws at the bottom right position
						arrangement[block_index][1] = "Bottom right"
						blockD(block_index)
					else:
						# if no block is missing underneath then draw block as normal
						blockD(block_index)
				else:
					# if an X is present in the arrangment
					# set the left/right_did_not_draw_boolean to true
					if block_item[1] == "Bottom left":
						left_did_not_draw = True
					elif block_item[1] == "Bottom right":
						right_did_not_draw = True
					else: 
						pass

#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by stacking your blocks correctly
title('Google Chrome Logo')

# Display the corner and centre coordinates of the places where
# the blocks must be placed
# ***** If you don't want to display the coordinates change the
# ***** arguments below to False
mark_coords(True, True)

### Call the student's function to display the stack of blocks
### ***** Change the argument to this function to test your
### ***** code with different data sets
stack_blocks(arrangement_99)

# Exit gracefully
release_drawing_canvas()

#
#--------------------------------------------------------------------#

