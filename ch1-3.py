
#total_secs = int(input("How many seconds, in total?"))
#hours = total_secs // 3600
#secs_still_remaining = total_secs % 3600
#minutes =  secs_still_remaining // 60
#secs_finally_remaining = secs_still_remaining  % 60
#
#print("Hrs=", hours, "  mins=", minutes, "secs=", secs_finally_remaining)

#all = "All"
#work = "work"
#not_and = "and"
#no = "no"
#play = "play"
#makes = "makes"
#jack = "Jack"
#a = "a"
#dull = "dull"
#boy = "boy"
#print(all,work,not_and,no,play,makes,jack,a,dull,boy)

#p=10000
#n=12
#r=0.08
#t_input=input("Enter the number of years to compound:")
#t=int(t_input)

#amount = p * ( 1 + r/n )**(n*t)
#print('After',t,'years, you will have $'+ str(amount))

#now=input("What time is it now (24 hour time, hours only): ")
#wait=input("How long should I sleep? ")
#snooze = int(wait)%24
#alarm = (int(now)+snooze)%24
#print("Your alarm will go off at",alarm,"hundred hours")

#import turtle             # Allows us to use turtles
#wn = turtle.Screen()      # Creates a playground for turtles
#alex = turtle.Turtle()    # Create a turtle, assign to alex

#alex.forward(50)          # Tell alex to move forward by 50 units
#alex.left(90)             # Tell alex to turn by 90 degrees
#alex.forward(30)          # Complete the second side of a rectangle

#wn.mainloop()             # Wait for user to close window

#import turtle

#win_color = input("Please enter a background color: ")
#tess_color = input("Please enter a color for your turtle: ")
#pen_size = input("Please enter a pen size: ")

#wn = turtle.Screen()
#wn.bgcolor(win_color)      # Set the window background color
#wn.title("Hello, Tess!")      # Set the window title

#tess = turtle.Turtle()
#tess.color(tess_color)            # Tell tess to change her color
#tess.pensize(int(pen_size))               # Tell tess to set her pen width

#tess.forward(50)
#tess.left(120)
#tess.forward(50)

#wn.mainloop()

#import turtle
#wn = turtle.Screen()         # Set up the window and its attributes
#wn.bgcolor("lightgreen")
#wn.title("Tess & Alex")

#tess = turtle.Turtle()       # Create tess and set some attributes
#tess.color("hotpink")
#tess.pensize(5)

#alex = turtle.Turtle()       # Create alex

#for t in range(3):
#  tess.forward(80)             # Make tess draw equilateral triangle
#  tess.left(120)               # Complete the triangle

#tess.right(180)              # Turn tess around
#tess.forward(80)             # Move her away from the origin

# Assign a list to a variable
#clrs = ["yellow", "red", "purple", "blue"]
#for c in clrs:
#  alex.color(c)
#  alex.forward(50)             # Make alex draw a square
#  alex.left(90)

#wn.mainloop()

#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")
#tess = turtle.Turtle()
#tess.shape("turtle")
#tess.color("blue")

#tess.penup()                # This is new
#size = 20
#for i in range(30):
#   tess.stamp()             # Leave an impression on the canvas
#   size = size + 3          # Increase the size on every iteration
#   tess.forward(size)       # Move tess along
#   tess.right(24)           #  ...  and turn her

#tess.color("red")
#tess.shape("circle")

#wn.mainloop()

#for i in range(1000):
# print("We like Python's turtles!")

#for m in ["January","February","March","April","May","June","July","August","September","October","November","December"]:
#  print("One of the months of the year is",m)

#import turtle
#wn = turtle.Screen()
#wn.bgcolor("blue")

#tess=turtle.Turtle()
#tess.color("white")

#tess.left(3645)

#wn.mainloop()

#xs = [12,10,32,3,66,17,42,99,20]

#total = 1
#for i in xs:
#  total = total * i

#print(total)

#import turtle
#wn = turtle.Screen()
#wn.bgcolor("lightgreen")

#tess=turtle.Turtle()
#tess.color("blue")
#tess.shape("turtle")
#tess.pensize(3)

#tess.stamp()

#for i in range(12):
#  tess.penup()
#  tess.forward(90)
#  tess.pendown()
#  tess.forward(10)
# tess.penup()
# tess.forward(30)
#  tess.stamp()
#  tess.forward(-130)
# tess.right(30)

#name = tess

#print(type(name))

#tess.shape("circle")

#total=0
#for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
#  tess.stamp()
#  tess.left(i)
#  tess.forward(100)
#  total=total+i

#bearing = str(total%360)
#print("The pirate is bearing",bearing,"degrees counter-clockwise from bearing 0") 

#for i in range(3):
#  tess.forward(60)
#  tess.left(120)

#tess.color("yellow")

#for s in range(4):
#  tess.forward(60)
#  tess.left(90)

#tess.color("red")

#for h in range(6):
#  tess.forward(60)
#  tess.left(60)

#tess.color("green")

#for o in range(8):
#  tess.forward(60)
#  tess.left(45)

#wn.mainloop()





