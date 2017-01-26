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

b = ("Ben","Miraski",40)
def is_old(tup):
    (first,last,age)=tup
    result = ""
    if age>=40:
        result = "Yes, you are old"
    else:
        result =  "Nope, not old yet"
    return result

print(is_old(b))

def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(count_letters("banana", "a")== 3)

#test_suite() 








