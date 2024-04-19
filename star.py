from turtle import * # Import the turtle module
color("red","yellow")# Set the pen color to red and the fill color to yellow
begin_fill()# Start filling the shape

while True:# Enter an infinite loop
    forward(200)  # Move forward by 200 units
    left(170)# Turn left by 170 degrees
    if abs(pos()) < 1:# Check whether the turtle has returned to its starting position
        break# If so, break out of the loop

end_fill() # Stop filling the shape
done()  # Close the window   
