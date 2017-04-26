from unit_tester import test
import string
import urllib.request
import wordtools
import time
import math
import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

def snowflake(t,size):
    """ draws a snowflake """
    for x in range(3):
        koch(t, 2, size)
        t.left(-120)

def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [85, -170, 85, 0]:
           cesaro(t, order-1, size/2)
           t.right(angle)

def cesaro_square(t, order, size):
    """ Draws a cesaro square """
    for x in range(4):
        cesaro(t, order, size)
        t.right(90)

def sierpinski(t, order, size):
    if order == 0:
        for angle in [120, 120, 120]:
            t.forward(size)
            t.left(angle)
    else:
        for x in range(4):
            sierpinski(t, order-1, size/2)
            t.left(60)


def test_suite():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# test_suite()

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")

george=turtle.Turtle()

#snowflake(george, 300)

#cesaro(george, 3, 200)

#cesaro_square(george, 3, 200)

sierpinski(george,1,200)

wn.mainloop()
