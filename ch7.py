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

def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

def sum_to(n):
    """ Return the sum of 1+2+3 ... n """
    ss  = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss


def num_digits(n):
    if n==0:
        return 1
    else:
        count = 0
        k = abs(n)
        while k != 0:
            count = count + 1
            k = k // 10
        return count
	

def num_zero_and_five_digits(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count
	
	
def count_if_odd(xs):
    """
	Counts the number of odd numbers in a list
	"""
    count=0
    for x in xs:
        if x%2 != 0:
            count += 1
    return count


def sum_if_even(xs):
    """
    Sums only the even numbers in a list
    """
    sum = 0
    for x in xs:
        if x%2 == 0:
            sum += x
    return sum			


def sum_if_negative(xs):
    """
    Sum the negative numbers in the list
    """
    sum=0
    for x in xs:
        if x < 0:
            sum += x
    return sum

	
def count_if_five(xs):
    """
    Counts the number of words in a list of length five
    """
    count = 0
    for x in xs:
        if len(x) == 5:
            count += 1
    return count
	
	
def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end="   ")
    print()

def sum_until_even(xs):
    """
    Sums the numbers in a list until one is even
    """
    sum = 0
    for x in xs:
        if x%2 != 0:
            sum += x
        else:
            break
    return sum	

def green_eggs(xs):
    """
    Counts the words in a list up to and including the first sam
    """
    count = 0
    for x in xs:
        if x == 'sam':
            count += 1
            break
        else:
            count += 1
    return count

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better


def print_triangular_numbers(n):
    """
    Prints the first n triangular numbers
    """
    for i in range(1,n+1):
        sum = 0
        for x in range (1,i+1):
            sum += x
        print(i, "\t", sum)


def is_prime(n):
    """
    determines if a number is prime
    """
    if n==1 or n == 2:
        return True
    else:
        x=2
        while x < n:
            if n%x == 0:
                j=False
                break
            else:
                x += 1
            j=True
        return j
        
        
def drunk_pirate(xs):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    tess=turtle.Turtle()
    tess.color("blue")    
    for (x,y) in xs:
        tess.right(x)
        tess.forward(y)
    wn.mainloop()


def hypotenuse(a):
    return (2*a**2)**0.5


def num_even_digits(n):
    """    
    Counts the number of even digits in a number
    """
    if n==0:
        return 1
    else:
        count = 0
        k = abs(n)
        while k != 0:
            if (k%(k//10))%2 !=0:
                k = k // 10 
            else:
                count = count + 1
                k = k // 10
        return count


def sum_of_squares(xs):
    """
    Returns the sum of squares of a list of numbers in a series
    """
    sum=0
    for x in xs:
        sum += x**2
    return sum


# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

def win_perc(a,b,c):
    """
    Returns the winning percentage for a in a 3-outcome game
    """
    perc = str(round(100*(a/(a+b+c)),2))
    return perc

def ttt():
    """
    Plays 1 to many rounds of tic-tac-toe
    """
    x=""
    comp_score=0
    human_score=0
    draws=0
    turn = True
    while x != "n":
        result = play_once(turn)        
        if result == -1:
            human_score += 1
            print("You win!","\n")
        elif result == 0:
            draws += 1
            print("Game drawn!","\n")
        elif result == 1:
            comp_score += 1
            print("I win!","\n")
        print("Current Score: Human","\t",human_score,"\t","Computer","\t",comp_score,"\t","Draws","\t",draws)
        print("The Human has won ",win_perc(human_score, comp_score, draws)," percent of the games.") 
        turn = not turn
        x = input("Do you want to play again? ")
    print("Goodbye")        





def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([ ]) == 0)
    test(mysum(range(11)) == 55)  # 11 is not included in the list.
    test(sum_to(4) == 10)
    test(sum_to(1000) == 500500)
    test(num_zero_and_five_digits(1055030250) == 7)
    test(count_if_odd([3,8,10,7,19,-3])==4)
    test(count_if_odd([0,2,4,6])==0)
    test(sum_if_even([3,8,10,7,19,-3])==18)
    test(sum_if_even([0,2,4,6])==12)
    test(sum_if_even([1,3,5,7,9,11])==0)	
    test(sum_if_negative([3,8,-10,7,19,-3])==-13)
    test(sum_if_negative([0,2,4,6])==0)
    test(sum_if_negative([-1,3,-5,7,-9,11])==-15)
    test(count_if_five(['This','has','no','five','letter','things'])==0)
    test(count_if_five(['There','are','two','five','letter','items'])==2)	
    test(sum_until_even([1,3,5,7,8,11])==16)
    test(sum_until_even([0,5,3,8,2])==0)
    test(sum_until_even([1,3,5,7,9])==25)
    test(sum_until_even([1,2,4,6,8,11])==1)
    test(green_eggs(['I','will','not','eat','green','eggs','and','ham'])==8)
    test(green_eggs(['sam','i','am'])==1)
    test(green_eggs(['said','sam','i','am'])==2)
    test(is_prime(1))
    test(is_prime(2))
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(num_digits(0) == 1)
    test(num_digits(-12345) == 5)
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(sum_of_squares([2, 3, 4]) == 29)
    test(sum_of_squares([ ]) == 0)
    test(sum_of_squares([2, -3, 4]) == 29)


ttt()

#drunk_pirate([(160, 200), (-43, 100), (270, 80), (-43, 120)])
#drunk_pirate([(-90,200),(30,200),(120,200),(30,200),(90,200),(135,hypotenuse(200)),(-135,200),(225,hypotenuse(200))])

#sqrt(25)
    
#print_triangular_numbers(10)   	
	
	
#print(is_prime(19760910))
#print(is_prime(19800710))
#print(is_prime(19810727))
	
#test_suite() 



#num=int(input("What number day would you like to look up? "))

#if start<0 or start>6 or dur<0:
#    print("You must live on Mars.")
#else:
#    print("You will return on a " + leaving(start,dur))





