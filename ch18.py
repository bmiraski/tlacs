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

def recursive_min(a):
    """ Returns the smallest number in a list or list of lists """
    first = True
    min = None
    for x in a:
        if type(x)==type([]):
            val = recursive_min(x)
        else:
            val = x

        if first or val < min:
            min = val
            first = False

    return min

def count(a, wx):
    """ counts the number of times that a appears in wx"""
    num = 0
    for x in wx:
        if type(x) == type([]):
            z = count(a, x)
        else:
            if a == x:
                z = 1
            else:
                z = 0
        num += z
    return num

def flatten(wx):
    final = []
    for x in wx:
        if type(x) == type([]):
            r = flatten(x)
        else:
            r = []
            r.append(x)
        final += r
    return final

def fibno(x):
    if x < 1:
        return "Nice try"
    wx = [0,1]
    if x > 2:
        for i in range(x-2):
            wx.append(wx[i]+wx[i+1])
    return wx[x-1]

def test_suite():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    test(recursive_min([2, 9, [1, 13], 8, 6]) == 1)
    test(recursive_min([2, [[100, 1], 90], [10, 13], 8, 6]) == 1)
    test(recursive_min([2, [[13, -7], 90], [1, 100], 8, 6]) == -7)
    test(recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6]) == -13)
    test(count(2, []) == 0)
    test(count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]]) == 4)
    test(count(7, [[9, [7, 1, 13, 2], 8], [7, 6]]) == 2)
    test(count(15, [[9, [7, 1, 13, 2], 8], [2, 6]]) == 0)
    test(count(5, [[5, [5, [1, 5], 5], 5], [5, 6]]) == 6)
    test(count("a",
               [["this", ["a", ["thing", "a"], "a"], "is"], ["a", "easy"]]) == 4)
    test(flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]]) == [2, 9, 2, 1, 13, 2, 8, 2, 6])
    test(flatten([[9, [7, 1, 13, 2], 8], [7, 6]]) == [9, 7, 1, 13, 2, 8, 7, 6])
    test(flatten([[9, [7, 1, 13, 2], 8], [2, 6]]) == [9, 7, 1, 13, 2, 8, 2, 6])
    test(flatten([["this", ["a", ["thing"], "a"], "is"], ["a", "easy"]]) ==
         ["this", "a", "thing", "a", "is", "a", "easy"])
    test(flatten([]) == [])


#test_suite()
print(fibno(0))
print(fibno(7))
print(fibno(4))
print(fibno(200))

#wn = turtle.Screen()        # Set up the window and its attributes
#wn.bgcolor("lightgreen")

#george=turtle.Turtle()

#snowflake(george, 300)

#cesaro(george, 3, 200)

#cesaro_square(george, 3, 200)

#sierpinski(george,1,200)

#wn.mainloop()
