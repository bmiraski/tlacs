
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


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
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

#radius = float(input("What is the radius of the circle? "))
#print("The area of your circle is",area_of_circle(radius))

#numbers = int(input("How many numbers would you like to add? "))
#print("Your total is",sum_to(numbers))

wn = make_window("lightgreen", "Pretty Pattern")
tess = make_turtle("DeepPink", 2)

for i in range(5):
    draw_star(tess)
    move(tess, 350, 144)

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


wn.mainloop()


