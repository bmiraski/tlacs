from unit_tester import test
import string
import urllib.request
import wordtools
import time
import math

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

    def reflect_x(self):
        """ Returns a new point reflected across the x-axis. """
        return Point(self.x, -1*self.y)

    def slope_from_origin(self):
        """ Returns the slope of a line from the origin to the given point. Note fails if point is located on the y-axis """
        return (self.y/self.x)

    def get_line_to(self, target):
        """ Returns a tuple of the slope and y-intercept given two points """
        slope = ((target.y - self.y)/(target.x - self.x))
        b = self.y - (slope * self.x)
        return (slope, b)

class SMS_store():
    """ Creates an inbox/outbox on a cellphone """

    def __init__(self, contents = []):
        """ create an SMS_store object"""
        self.contents = contents

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        """ adds new unread message to the inbox """
        self.contents.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        """ Returns the number of messages in the inbox """
        return len(self.contents)

    def get_unread_indexes(self):
        """ Returns a list of unread indexes in my_inbox"""
        unread = []
        for x in range(len(self.contents)):
            if not self.contents[x][0]:
                unread.append(x)
        return unread

    def get_message(self, i):
        """ Returns the message at the given index and marks as read """
        self.contents[i] = (True, self.contents[i][1], self.contents[i][2], self.contents[i][3])
        return self.contents[i][1:]

    def delete(self, i):
        """ Deletes the message at index 1 """
        self.contents = self.contents[:i] + self.contents[i+1:]

    def clear(self):
        """ Empties the inbox """
        self.contents = []

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def flip(self):
        oldheight = self.height
        self.height = self.width
        self.width = oldheight

    def contains(self, target):
        return (target.x >= self.corner.x and target.x < (self.corner.x + self.width)) and (target.y >= self.corner.y and target.y < (self.corner.y + self.height))

# def print_point(pt):
#     print("({0}, {1})".format(pt.x, pt.y))

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)

def distance(p1, p2):
    """Returns the distance between two points"""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def circle_from_point(p1, p2, p3, p4):
    """ Returns the center point of a circle defined by four points. Note, this only requires three points. the function checks to see if that fourth point exists on the dircle."""
    d = 2 * (p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y))
    rx = ((p1.x**2 + p1.y**2)*(p2.y-p3.y) + (p2.x**2 + p2.y**2) * (p3.y - p1.y) + (p3.x**2 + p3.y**2) * (p1.y - p2.y))/d
    ry = ((p1.x**2 + p1.y**2)*(p3.x-p2.x) + (p2.x**2 + p2.y**2) * (p1.x - p3.x) + (p3.x**2 + p3.y**2) * (p2.x - p1.x))/d
    center = Point (rx, ry)
    if not math.isclose(distance(p4, center), distance(p2, center)):
        return print("These points are not on the same circle.")
    else:
        return center

def test_suite():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.area() == 50)
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.perimeter() == 30)
    r = Rectangle(Point(100, 50), 10, 5)
    test(r.width == 10 and r.height == 5)
    r.flip()
    test(r.width == 5 and r.height == 10)
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))

test_suite()