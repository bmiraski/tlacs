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



def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(count_letters("banana", "a")== 3)

#test_suite() 

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()

tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
        wn.ontimer(advance_state_machine,1000)
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
        wn.ontimer(advance_state_machine,1000)
    else:                    # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
        wn.ontimer(advance_state_machine,1000)

# Bind the event handler to the space key.
wn.ontimer(advance_state_machine, 1000)

#wn.listen()                      # Listen for events
wn.mainloop()







