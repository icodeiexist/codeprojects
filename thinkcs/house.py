from gasp import *          # import everything from the gasp library

def draw_house(x):
   Box((x, x), 100, 100)     # the house
   Box((x+35,x ), 30, 50,filled=True,color=color.BLUE)       # the door
   Box((x+20, x+60), 20, 20)       # the left window
   Box((x+60, x+60), 20, 20)       # the right window
   Line((x, x+100), (x+50, x+140))  # the left roof
   Line((x+50, x+140), (x+100, x+100)) # the right roof


begin_graphics()            # open the graphics canvas
draw_house(20)
draw_house(160)
update_when('key_pressed')  # keep the canvas open until a key is pressed
end_graphics()
