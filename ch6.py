import turtle
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def day_name(x):
    """
    Returns the name of the day given the number of the day in the week
    """
    if x==0:
        return "Sunday"
    elif x==1:
        return "Monday"
    elif x==2:
        return "Tuesday"
    elif x==3:
        return "Wednesday"
    elif x==4:
        return "Thursday"
    elif x==5:
        return "Friday"
    elif x==6:
        return "Saturday"


def day_num(x):
    """
    Returns the number of the day of the week entered
    """
    if x=="Sunday":
        return 0
    elif x=="Monday":
        return 1
    elif x=="Tuesday":
        return 2
    elif x=="Wednesday":
        return 3
    elif x=="Thursday":
        return 4
    elif x=="Friday":
        return 5
    elif x=="Saturday":
        return 6


def day_add(start, delta):
    """
    Calculate the day that a person will return
    """
    begin=day_num(start)
    adj=delta%7
    end=(begin+adj)%7
#    end=end_raw%7+begin
    return day_name(end)


def turn_clockwise(a):
    """
    Returns the next compass point clockwise
    """
    if a=="N":
        return "E"
    elif a=="E":
        return "S"
    elif a=="S":
        return "W"
    elif a=="W":
        return "N"


def days_in_month(month):
    """
    Returns the number of days in a month
    """
    if month=="February":
        return 28
    elif month=="September" or month=="April" or month=="June" or month=="November":
        return 30
    elif month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December":
        return 31


def to_secs(h,m,s):
    """
    Returns the total number of seconds for a given hours, minutes, seconds
    """
    h_sec=h*3600
    m_sec=m*60
    return int(h_sec+m_sec+s)


def hours_in(sec):
    """
    Returns the whole number of hours in a given number of sec.
    """
    return int(sec//3600)


def minutes_in(sec):
    """
    Returns the whole number of miunutes in a given number of sec.
    """
    return int((sec - (hours_in(sec)*3600))//60)


def seconds_in(sec):
    """
    Returns the whole number of seconds left after hours_in and minutes_in run
    """
    return int(sec - (hours_in(sec)*3600) - (minutes_in(sec)*60))


def compare(a,b):
    """
    Compares two values and returns a predetermined 1,0 or -1
    """
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1


def hypotenuse(a, b):
    """
    Returns the hypotenuse length of a right triangle given the two sides
    """
    return (a**2 + b**2)**0.5


def slope(x1, y1, x2, y2):
    """
    Returns the slope of a line through two points
    """
    delta_y = y2-y1
    delta_x = x2-x1
    return delta_y / delta_x


def intercept(x1, y1, x2, y2):
    """
    Returns the y-intercept of a line through two points. Requires slope
    """
    m = slope(x1, y1, x2, y2)
    return y1 - m*x1


def is_even(n):
    """
    determines if a number passed in is even
    """
    return n%2==0


def is_odd(n):
    """
    Determines is a number passed in is odd
    """
    return not is_even(n)

def is_factor(f, n):
    """
    Determines if f is a factor of n
    """
    return n%f == 0


def is_multiple(m, n):
    """
    Determines if m is a multiple of n
    """
    return is_factor(n, m)


def f2c(t):
    """
    Returns the rounded degree in Celsius for a temperature in Farenheit
    """
    return round(5/9 * (t-32))

def c2f(t):
    """
    Returns the rounded temperature in Farenheit for a temp in Celsius
    """
    return round(9*t/5 + 32)


def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    test(day_num("Halloween") == None)
    test(day_add("Monday", 4) ==  "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433,0,0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    test(is_even(42))
    test(not is_even(7))
    test(is_even(0))
    test(is_even(-6))
    test(not is_even(-13))
    test(not is_odd(18))
    test(is_odd(71))
    test(not is_odd(0))
    test(not is_odd(-14))
    test(is_odd(-21))
    test(is_factor(3, 12))
    test(not is_factor(5, 12))
    test(is_factor(7, 14))
    test(not is_factor(7, 15))
    test(is_factor(1, 15))
    test(is_factor(15, 15))
    test(not is_factor(25, 15))
    test(is_multiple(12, 3))
    test(is_multiple(12, 4))
    test(not is_multiple(12, 5))
    test(is_multiple(12, 6))
    test(not is_multiple(12, 7))
    test(f2c(212) == 100)     # Boiling point of water
    test(f2c(32) == 0)        # Freezing point of water
    test(f2c(-40) == -40)     # Wow, what an interesting case!
    test(f2c(36) == 2)
    test(f2c(37) == 3)
    test(f2c(38) == 3)
    test(f2c(39) == 4)
    test(c2f(0) == 32)
    test(c2f(100) == 212)
    test(c2f(-40) == -40)
    test(c2f(12) == 54)
    test(c2f(18) == 64)
    test(c2f(-48) == -54)


test_suite() 



#num=int(input("What number day would you like to look up? "))

#if start<0 or start>6 or dur<0:
#    print("You must live on Mars.")
#else:
#    print("You will return on a " + leaving(start,dur))





