import turtle

"""
Program: Turtle Graphics Birthday Cake Drawing
This program uses the turtle module to draw a scene that includes a table, 
a multi-layer cake with customizable colors and dimensions, candles, balloons, 
and decorative letters ('H', 'B', 'D'). The scene elements are customized 
through user input for features like table size, cake layers, frosting, 
candle color, flame size, and balloon colors..
"""

#Parent function
def main():
    """
    Main function to arrange the drawing of the entire scene.
    It calls functions to draw the cake layers, and controls the speed of the turtle.
    """
    turtle.speed(2)
    turtle.screensize(canvwidth=800,canvheight=600, bg='lightblue')
    print("Maintain the canvas size by having the table width be less than 750, and both the table and cake height less than 550.")
    draw_cake_layers() # Draw cake with user input
    print("HAPPY BIRTHDAY TO YOU!")
    print("Click on the window to close the program!")
    turtle.done()

# Base for the table, table legs, and cake
def rectangle(x, y, rotation, width, height, ang, color):
    """
    Draws a rectangle with specified positions, angles, and color.
    Parameters:
    x (int): x-coordinate of the rectangle's center
    y (int): y-coordinate of the rectangle's center
    width/height: how long/tall the rectangle is
    rotation (int): rotation angle of the rectangle
    ang (int): angle of the rotation
    """
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y) # Position of the rectangle
    turtle.pendown()
    turtle.right(rotation)
    turtle.forward(height/2)
    turtle.right(ang)
    turtle.forward(width)
    turtle.right(ang)
    turtle.forward(height)
    turtle.right(ang)
    turtle.forward(width)
    turtle.right(ang)
    turtle.forward(height/2)
    turtle.end_fill()
    
#Table
def draw_table(width, height, color):
    """
    Draws a table.
    
    Parameters:
    width (float): The width of the table.
    height (float): The height of the table.
    color (str): The color of the table.
    """
    # Draws the left leg
    rectangle((-width*5/12),-height, 0, width*5/12, height*5/12, 90, color) # Left leg
    rectangle((width*5/12),-height, -180, width*5/12, height*5/12, -90, color) # Right leg
    rectangle(0, 0, 0, height, width, -90, color) # Table Top

#Cake
def draw_cake_layer(x, y, width, height, color):
    """
    Draws one layer of the cake with specified width, height, and color.

    Parameters:
    x (float): The x-coordinate for positioning the cake.
    y (float): The y-coordinate for positioning the cake.
    width (float): The width of the cake layer.
    height (float): The height of the cake layer.
    color (str): The color of the cake layer.
    """
    rectangle(-x, y, 0, height, width, -90, color)
    
def draw_cake_layers():
    """
    Prompts the user for cake and table parameters and draws the multi-layer cake.
    Adds frosting and a candle on top.
    """
    table_width = float(input("Enter the width of the table: "))
    table_height = float(input("Enter the height of the table: "))
    table_color = input("Enter the color of the table: ")
    # Draws the table
    draw_table(table_width, table_height, table_color)
    
    """
    Asks the user for the amount of layers they would like, and tells them that it should
    be smaller than the table width.
    """
    cake_width = float(input(f"Enter the width of the cake (less than {table_width}): "))
    cake_height = float(input("Enter the height of each cake layer: "))
    """
    Only allows the user to input 10 layers, and if they try to input more than 10,
    it will defult back to 10.
    """
    num_layers = int(input("Enter the number of cake layers (max 10): "))
    if num_layers > 10:
        print("The maximum number of layers is 10. Only the first 10 layers will be drawn.")
        num_layers = 10
    
    """    
    Draw cake layers individually depending on the amount of layers the user wants.
    Asks the user for the color of each layer before drawing it.
    Makes each layer smaller than the previous one by multiplying each layer with smaller and smaller fractions.
    The width of the top-most layer is saved into the new_cake_width variable.
    """    
    new_cake_width = cake_width
    if num_layers >= 1:
        color1 = input("Enter color for layer 1: ")
        draw_cake_layer(0,cake_height, cake_width, cake_height, color1)
    if num_layers >= 2:
        color2 = input("Enter color for layer 2: ")
        draw_cake_layer(0, cake_height*2, cake_width*11/12, cake_height, color2)
        new_cake_width = cake_width*11/12
    if num_layers >= 3:
        color3 = input("Enter color for layer 3: ")
        draw_cake_layer(0, cake_height*3, cake_width*10/12, cake_height, color3)
        new_cake_width = cake_width*10/12
    if num_layers >= 4:
        color4 = input("Enter color for layer 4: ")
        draw_cake_layer(0, cake_height*4, cake_width*9/12, cake_height, color4)
        new_cake_width = cake_width*9/12
    if num_layers >= 5:
        color5 = input("Enter color for layer 5: ")
        draw_cake_layer(0, cake_height*5, cake_width*8/12, cake_height, color5)
        new_cake_width = cake_width*8/12
    if num_layers >= 6:
        color6 = input("Enter color for layer 6: ")
        draw_cake_layer(0, cake_height*6, cake_width*7/12, cake_height, color6)
        new_cake_width = cake_width*7/12
    if num_layers >= 7:
        color7 = input("Enter color for layer 7: ")
        draw_cake_layer(0, cake_height*7, cake_width*6/12, cake_height, color7)
        new_cake_width = cake_width*6/12
    if num_layers >= 8:
        color8 = input("Enter color for layer 8: ")
        draw_cake_layer(0, cake_height*8, cake_width*5/12, cake_height, color8)
        new_cake_width = cake_width*5/12
    if num_layers >= 9:
        color9 = input("Enter color for layer 9: ")
        draw_cake_layer(0, cake_height*9, cake_width*4/12, cake_height, color9)
        new_cake_width = cake_width*4/12
    if num_layers >= 10:
        color10 = input("Enter color for layer 10: ")
        draw_cake_layer(0, cake_height*10, cake_width*3/12, cake_height, color10)
        new_cake_width = cake_width*3/12
    
    # Adding the frosting and the candle on the top-most layer of the cake using its "new width".
    # Divides the new width of the cake by 6, so that the frosting can fit inside the cake.
    frosting(new_cake_width, (new_cake_width/6))
    candle(new_cake_width, new_cake_width/7, cake_height)
    
    # Reverting the turtle to it's original position, and resets the size of the turtle back to '1'.
    turtle.pensize(1)
    turtle.right(90)
    
    # Asks the user for their 4 favorite colors
    ballon1 = input("Enter your favorite color: ")
    ballon2 = input("Enter your 2nd favorite color: ")
    ballon3 = input("Enter your 3rd favorite color: ")
    ballon4 = input("Enter your 4th favorite color: ")
    # Draws 4 balloons with different positions and uses their favorite colors for each balloon.
    balloon(-290, 250, ballon1)  
    balloon(-185, 220, ballon2)  
    balloon(185, 205, ballon3)    
    balloon(290, 250, ballon4)
    """ 
    Draw decorative letters (H, B, D), using the user's favorite color/the color of the first balloon.
    Uses the height of the table, and draws the letters directly 70 pixels under the table.
    """
    draw_H((-table_height)-70, ballon1)
    draw_B((-table_height)-70, ballon1)   
    draw_D((-table_height)-70, ballon1)
    

def frosting(width, r):
    """
    Draws frosting decoration on the topmost cake layer.
    
    Parameters:
    width (float): The width of the frosting.
    r (float): Radius for the frosting curves.
    """
    frost = input("Pick a frosting flavor: Chocolate(c), Vanilla(v), Strawberry(s): ")
    if frost == 'c':
        frost = '#873e23'
    elif frost == 'v':
        frost = 'white'
    elif frost == 's':
        frost = 'pink'
    else:
        print("Invalid input. Defaulting to vanilla frosting.")
        frost = 'white'
    # Draw frosting on top layer
    turtle.forward((width/2))
    turtle.right(-90)
    turtle.fillcolor(frost)
    turtle.pencolor(frost)
    turtle.begin_fill()
    turtle.circle(r,180)
    turtle.left(180)
    turtle.circle(r,180)
    turtle.left(180)
    turtle.circle(r,180)
    turtle.left(180)
    turtle.left(270)
    turtle.forward(width)
    turtle.end_fill()
    
    
def candle(width, candle_width, candle_length):
    """
    Draws a candle on top of the cake with a customizable flame.
    
    Parameters:
    width (float): The width of the top cake layer.
    candle_width (float): The width of the candle.
    candle_length (float): The height of the candle.
    """
    # Center
    turtle.backward(width/2)
    # Candle body
    candle_color = input("Enter the candle color: ")
    turtle.fillcolor(candle_color)
    turtle.pencolor(candle_color)
    turtle.begin_fill() 
    turtle.forward(candle_width/2)
    turtle.right(90)
    turtle.forward(candle_length)
    turtle.right(90)
    turtle.forward(candle_width)
    turtle.right(90)
    turtle.forward(candle_length)
    turtle.right(90)
    turtle.end_fill()

    # Go to flame start
    turtle.penup()
    turtle.right(90)
    turtle.forward(candle_length)
    turtle.left(90)
    turtle.forward((candle_width/2)//1)
    turtle.pendown()

    # Asks the user for the flame segment size
    flame_segments_length = float(input('How big would you like the flame to be: '))
    
    # Draws the candle wick
    turtle.pencolor('black')
    turtle.right(90)
    turtle.forward(flame_segments_length)
    
    # Draws the actual flame
    turtle.pencolor("red")
    turtle.pensize(flame_segments_length)
    turtle.forward(flame_segments_length*0.5)

    turtle.pencolor("orange")
    turtle.pensize(flame_segments_length*0.75)
    turtle.forward(flame_segments_length*0.75)

    turtle.pencolor("yellow")
    turtle.pensize(flame_segments_length*0.5)
    turtle.forward(flame_segments_length)
    
def balloon(x, y, color):
    """
    Draws a balloon at specified coordinates with a given color.
    
    Parameters:
    x (float): The x-coordinate for the balloon.
    y (float): The y-coordinate for the balloon.
    color (str): The color of the balloon.
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(35)  
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(80)  
    turtle.left(90)


def draw_H(y, color):
    """
    Draws the letter 'H' as part of the decorative text.
    """
    turtle.penup()
    turtle.goto(-40, y)
    turtle.pendown()
    turtle.pensize(6)
    turtle.color(color)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)


def draw_B(y, color):
    """
    Draws the letter 'B' as part of the decorative text.
    """
    turtle.penup()
    turtle.goto(0, y)
    turtle.pendown()
    turtle.pensize(6)
    turtle.color(color)
    turtle.setheading(90)  
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-13, 180)
    turtle.left(180)
    turtle.circle(-13, 180)


def draw_D(y, color):
    """
    Draws the letter 'D' as part of the decorative text.
    """
    turtle.penup()
    turtle.goto(30, y)
    turtle.pendown()
    turtle.pensize(6)
    turtle.color(color)
    turtle.setheading(90)  
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-25, 180)

# Run the main function to start drawing
main()
turtle.Screen().exitonclick()