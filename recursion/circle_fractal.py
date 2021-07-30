"""
 *****************************************************************************
   FILE:  circle_fractal.py

   AUTHOR: Nathan Koike

   ASSIGNMENT: Project 7

   DATE: 16 October 2017

   DESCRIPTION: Draws a fractal that resembles an equilateral triangle with
                triangular holes cut out at a 180 degree turn from the base
                triangle at higher levels of its composition and is comprised
                entirely of circles

 *****************************************************************************
"""

import turtle




init_rad = 200 # global variable, provided in the project assignment document


def fractal(t, radius, level):

    t.up() 
    
    heading = t.heading() # stores heading to be used to continue drawing the
                          # circle later
                          
    t.setheading(270) # makes the turtle face down
    
    t.forward(radius)
    
    t.left(90) # orients the turtle so that all circles are drawn with the same
               # initial heading
               
    t.down()
    
    if level == 0: # base case
        
        t.circle(radius)
        t.up()

        t.setheading(90) # sets the heading toward the center of the circle
                         # this will be used to draw circles at higher levels
                         # so this is very important
                         
        t.forward(radius) # moves the turtle back to the center of the circle
        
        t.setheading(heading) # restores the turtle's initial heading. this
                              # allows the turtle to continue drawing where it
                              # started the last circle which is very important
                              # for the fractal to be drawn properly
                              
        t.down()
    else:
        for x in range(3):
            if x == 0:
# CITE: https://docs.python.org/3/library/turtle.html#turtle.circle
# DESC: prodived information about how to use the t.circle() function

                t.circle(radius, 60) # draws 1/6 of a circle. this puts the
                                     # first circle in fractal beyond the main
                                     # circle at a 120 degree spacing from the
                                     # rest of the circles
                                     
            else:
                
                t.circle(radius, 120) # this draws 1/3 of a circle and allows
                                      # the fractal to be completed properly
                                      
            fractal(t, radius/2, level - 1) # this recursion allows the function
                                            # to continue checking the fractal
                                            # pattern and draw a fractal of the
                                            # correct level
                                            
        t.circle(radius, 60) # this draws the remaining 1/6 of the main circle
        
        t.up()
        
        t.setheading(90) # this and the lines following it return the turtle to
                         # the center of the circle it just drew
        t.forward(radius)
        t.setheading(heading)
        t.down()
        


def main():
    t = turtle.Turtle()
    
    t.speed(0) # makes the turtle go fast
    
    fractal(t, init_rad, 4)


if __name__ == "__main__":
    main()
