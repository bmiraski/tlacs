import turtle
import sys
import string

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(add_vectors([1, 1], [1, 1]) == [2, 2])
    test(add_vectors([1, 2], [1, 4]) == [2, 6])
    test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    test(scalar_mult(5, [1, 2]) == [5, 10])
    test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    test(dot_product([1, 1], [1, 1]) ==  2)
    test(dot_product([1, 2], [1, 4]) ==  9)
    test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")
    test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

def add_vectors(u, v):
    """
    Adds together the elements of two different lists
    """
    vector=[]
    for i in range(len(u)):
        new_elem = u[i] + v[i]
        vector.append(new_elem)
    return vector

def scalar_mult(s,v):
    """
    Multiplies a vector by a scalar
    """
    vector=[]
    for i in v:
        new_elem = s * i
        vector.append(new_elem)
    return vector

def dot_product(u, v):
    """
    Returns the dot product of two vectors
    """
    dot = 0
    for i in range(len(u)):
        dot = dot + (u[i] * v[i])
    return dot

def replace(s, old, new):
    """
    Replaces the old character with the new character or string in string s
    """
    new_s = new.join(s.split(old))
    return new_s

def swap(x, y):      # Incorrect version
     print("before swap statement: x:", x, "y:", y)
     (x, y) = (y, x)
     print("after swap statement: x:", x, "y:", y)

a = ["This", "is", "fun"]
b = [2,3,4]
print("before swap function call: a:", a, "b:", b)
swap(a, b)
print("after swap function call: a:", a, "b:", b)
    





# test_suite() 