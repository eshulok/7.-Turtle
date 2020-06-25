#We need to tell Python that we want to use the turtle library
#We do this with an import statement
import turtle as t

#think of t as the turtle, or a pen
#the turtle has a location and a direction, that is indicated by an arrow as it moves
#it starts off in the middle of the canvas and facing right

#tell the turtle to move forward 100 pixels
t.forward(100)
#the code above creates a line 100 pixels long from the center of the canvas towards the right of the screen.

#tell the turtle to turn left 90 degrees
t.left(90)
#if you comment out all the code below, you will see that the line above changes the direction of the arrow, but not its position

#give instructions to the turtle to complete a square
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

#you can also move the turtle in the direction opposite of where it is facing by going backward
t.backward(50)

#clear the canvas and leave the turtle in its last position
t.clear()

#the following line will begin from where the turtle was before clearing the screen
t.forward(100)

#to clear the screen and put the turtle back at its default position in the center of the screen, use reset
t.reset()

#to move the turtle without drawing a line, pick it up
#the following line is like lifting a pen off the paper
t.up()

#now move the turtle with the same commands as before but now it moves without making a line
t.forward(50)

#now put the turtle back down
t.down()

#now move the turtle again and it draws a line
t.left(90)
t.forward(100)

#now lift the turtle up and create a line parallel to the first that is 20 pixels away
t.up()
t.left(90)
t.forward(20)
t.down()
t.left(90)
t.forward(100)