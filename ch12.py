import turtle
import sys
import string
import random
import time
import calendar



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
    test(myreplace(",", ";", "this, that, and some other thing") ==
         "this; that; and some other thing")
    test(myreplace(" ", "**",
                   "Words will now      be  separated by stars.") ==
         "Words**will**now**be**separated**by**stars.")


def make_random_ints(num, lower_bound, upper_bound):
   """
     Generate a list containing num random ints between lower_bound
     and upper_bound. upper_bound is an open bound.
   """
   rng = random.Random()  # Create a random number generator
   result = []
   for i in range(num):
      result.append(rng.randrange(lower_bound, upper_bound))
   return result

# print(make_random_ints(5, 1, 13))

def make_random_ints_no_dups(num, lower_bound, upper_bound):
   """
     Generate a list containing num random ints between
     lower_bound and upper_bound. upper_bound is an open bound.
     The result list cannot contain duplicates.
   """
   result = []
   rng = random.Random()
   for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
   return result

# xs = make_random_ints_no_dups(5, 1, 10000000)
# print(xs)
    


def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

#sz = 10000000        # Lets have 10 million elements in the list
#testdata = range(sz)

#t0 = time.clock()
#my_result = do_my_sum(testdata)
#t1 = time.clock()
# print("my_result    = {0} (time taken = {1:.4f} seconds)"
#        .format(my_result, t1-t0))

#t2 = time.clock()
#their_result = sum(testdata)
#t3 = time.clock()
# print("their_result = {0} (time taken = {1:.4f} seconds)"
#        .format(their_result, t3-t2))

def myreplace(old, new, s):
    """ Replace all occurrences of old with new in s. """
    news=" ".join(s.split())
    return new.join(news.split(old))


#cal = calendar.TextCalendar(3)      # Create an instance
# cal.pryear(2012)
#cal.prmonth(2012, 9)

#d = calendar.LocaleTextCalendar(6, "FRENCH")
#d.pryear(2012)

test_suite()