from unit_tester import test
import string
import urllib.request
import wordtools
import time

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    
# def print_point(pt):
#     print("({0}, {1})".format(pt.x, pt.y))

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

def test_suite():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

p=Point(3,4)
str(p)
print(p)



#test_suite()

