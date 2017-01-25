
#import turtle

#def draw_multicolor_square(t, sz):
#    """Make turtle t draw a multi-color square of sz."""
#    for i in ["red", "purple", "hotpink", "blue"]:
#        t.color(i)
#        t.forward(sz)
#        t.left(90)

#wn = turtle.Screen()        # Set up the window and its attributes
#wn.bgcolor("lightgreen")

#tess = turtle.Turtle()      # Create tess and set some attributes
#tess.pensize(3)

#size = 20                   # Size of the smallest square
#for i in range(15):
#    draw_multicolor_square(tess, size)
#    size = size + 10        # Increase the size for next time
#    tess.forward(10)        # Move tess along a little
#    tess.right(18)          #    and give her some turn

#wn.mainloop()

#def final_amt(p, r, n, t):
#    """
#   XZ   Apply the compound interest formula to p
#       to produce the final amount.
#    """
#
#    a = p * (1 + r/n) ** (n*t)
#    return a         # This is new, and makes the function fruitful.#

# now that we have the function above, let us call it.
#toInvest = float(input("How much do you want to invest?"))
#fnl = final_amt(toInvest, 0.08, 12, 5)
#print("At the end of the period you'll have", fnl)

import turtle

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, fill, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr, fill)
    t.pensize(sz)
    return t

def draw_square(t, sz):
    """
    Draws a square and then moves away from the square
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)
    
def move(t, sz, angle):
    """
    Moves a turtle
    """
    #t.penup()
    t.forward(sz)
    t.right(angle)
    #t.pendown()

def draw_poly(t, n, sz):
    """
    draws a regular polygon with n sides
    """
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_equitriangle(t, sz):
    """
    draws an equilateral triangle
    """
    draw_poly(t, 3, sz)

def draw_spiral(t, angle, lines):
    """
    draws a spiral rotating through the angles
    """
    sz = 1
    for i in range(lines):
        t.forward(sz)
        t.right(angle)
        sz=sz+2

def sum_to(n):
    """
    sums the integers up to n
    """
    a=0
    next=0
    for i in range(n):
        next=next+1
        a=a+next
    return a

def area_of_circle(r):
    """
    calculates the area of a circle of radius r
    """
    a = 3.14159*r**2
    return a

def draw_star(t):
    """
    Makes turtle t draw a star of size 100
    """
    for i in range(5):
        t.forward(100)
        t.right(144)

def change_fill(t,height):
    """
    changes the color of the turtle fill based on the height of the bar
    """
    if height>200:
        t.color("blue","red")
    elif height>=100 and height < 200:
        t.color("blue","yellow")
    else:
        t.color("blue","green")


def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    change_fill(t,height)
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)     # Draw up the left side
    
    if height >= 0:
        t.write('  ' + str(height))
    else:
        t.penup()
        t.forward(-15)
        t.write('  ' + str(height))
        t.forward(15)
        t.pendown()    

    t.right(90)
    t.forward(40)         # Width of bar, along the top
    t.right(90)
    t.forward(height)     # And down again!
    t.left(90)            # Put the turtle facing the way we found it.
    t.end_fill()             # Added this line
    t.penup()
    t.forward(10)         # Leave small gap after each bar
    t.pendown()

def hyp(a,b):
    """
    Returns the length of the hypotenuse of a right triangle
    """
    h2=a**2 + b**2
    h=h2**0.5
    return h

def is_rightangled(a,b,c):
    if c>a and c>b:
        if abs((c**2)-(a**2+b**2))<0.000001:
            t=True
        else:
            t=False
    elif a>b and a>c:
        if abs((a**2)-(b**2+c**2))<0.000001:
            t=True
        else:
            t=False
    else:
        if abs((b**2)-(a**2+c**2))<0.000001:
            t=True
        else:
            t=False

    return t


def day_name(x):
    """
    Returns the name of the day given the number of the day in the week
    """
    if x==0:
        day="Sunday"
    elif x==1:
        day="Monday"
    elif x==2:
        day="Tuesday"
    elif x==3:
        day="Wednesday"
    elif x==4:
        day="Thursday"
    elif x==5:
        day="Friday"
    else:
        day="Saturday"
    return day

def leaving(start, dur):
    """
    Calculate the day that a person will return
    """
    adj=dur%7
    end_raw=start+adj
    end=end_raw%7+start
    ret=day_name(end)
    return ret

def grade(mark):
    """
    Return the Grade given the score on the exam
    """
    if mark >=75:
        grade="First"
    elif mark >= 70 and mark < 75:
        grade="Upper Second"
    elif mark >= 60 and mark < 70:
        grade="Second"
    elif mark >= 50 and mark < 60:
        grade="Third"
    elif mark >= 45 and mark < 50:
        grade="F1 Supp"
    elif mark >= 40 and mark < 45:
        grade="F2"
    else:
        grade="F3"
    return grade

#xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

#for i in xs:
#    print("If you score a " + str(i) + ", your grade will be " + grade(i) + ".")

#a=float(input("Enter the length of one side: "))
#b=float(input("Enter the length of a second side: "))
#c=float(input("Enter the length of the last side: "))

#if is_rightangled(a,b,c)==True:
#    print("You have a right triangle! Huzzah!")
#else:
#    print("You have lost the battle.")

import math
a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)



#start=int(input("On what day are you leaving?" ))
#dur=int(input("How many nights will you be gone?" ))

#print

#num=int(input("What number day would you like to look up? "))

#if start<0 or start>6 or dur<0:
#    print("You must live on Mars.")
#else:
#    print("You will return on a " + leaving(start,dur))





#radius = float(input("What is the radius of the circle? "))
#print("The area of your circle is",area_of_circle(radius))

#numbers = int(input("How many numbers would you like to add? "))
#print("Your total is",sum_to(numbers))

#wn = make_window("lightgreen", "Bars")
#tess = make_turtle("blue", "red", 2)

#xs = [48, -20, 117, 200, 240, 160, -50, 260, 220]

#for v in xs:              # Assume xs and tess are ready
#    draw_bar(tess, v)

#for i in range(5):
#    draw_star(tess)
#    move(tess, 350, 144)

#draw_equitriangle(tess, 40)

#draw_spiral(tess, 89, 100)

#for t in range(20):
#    draw_poly(tess, 4, 80)
#    tess.left(18)



#size=20
#for t in range(5):
#    draw_square(tess, size)
#    move(tess, 10)
#    size=size+20


#wn.mainloop()


