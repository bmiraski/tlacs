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

def count_letters(word, char):
    """
    Returns the number of times a character appears in a word
    """
    count = 0
    z=0
    while word.find(char,z) != -1:
        z = word.find(char,z) + 1
        count += 1
    return count


def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def e_stats(graf):
    """
    Returns a lot of stats about the letter e
    """
    count = 0
    array = remove_punctuation(graf).split()
    for word in array:
        if "e" in word:
            count += 1
    result = 'Your text contains {0} words, of which {1} ({2}%) contain an "e".'
    print(result.format(len(array), count, str(round(100*(count/len(array)),1))))    

def reverse(text):
    """
    Reverses the text in a string
    """
    rev=""
    if len(text)==0:
        return rev
    else:
        lx=len(text)-1
        while lx>=0:
            rev=rev+text[lx]
            lx -= 1
        return rev

def mirror(text):
    """
    Creates a string that is a combination of the string and its mirror image
    """
    mir=text + reverse(text)
    return mir

def remove_letter(a,text):
    """
    Removes the letter a from a string of text
    """
    missing=""
    if len(text)==0:
        return missing
    else:
        lx=len(text)
        i = 0
        while i<lx:
            if a==text[i]:
                i += 1
            else:
                missing = missing + text[i]
                i += 1
        return missing

def is_palindrome(text):
    """
    Determines if a string is a palindrome
    """
    if text==reverse(text):
        return True
    else:
        return False

def count(sub,text):
    times=0
    x=0
    y=len(sub)
    while y <= len(text):
        if sub==text[x:y]:
            times += 1
            x += 1
            y += 1
        else:
            x += 1
            y += 1
    return times

def remove(sub,text):
    x = 0
    y = len(sub)
    result=text
    while y <= len(text):
        if sub!=text[x:y]:
            x += 1
            y += 1
        elif sub==text[x:y]:
            result = text[0:x] + text[y:len(text)]
            return result
    return result

def remove_all(sub,text):
    x = 0
    y = len(sub)
    result=""
    while y < len(text):
        if sub!=text[x:y]:
            result = result + text[x:x+1]
            x += 1
            y += 1
        elif sub==text[x:y]:
            x += len(sub)
            y += len(sub)
    if y >= len(text) and sub !=text[x:y]:
        result = result + text[x:len(text)]
    else:
        result = result    
    return result


def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(count_letters("banana", "a")== 3)
    test(count_letters("George", "b")==0)
    test(count_letters("George", "g")==1)
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    # test(is_palindrome(""))    # Is an empty string a palindrome?
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")
    

#e_stats("""
#Welcome to Google's Python online tutorial. It is based on the introductory Python course offered internally. Originally created during the Python 2.4 days, we've tried to keep the content universal and exercises relevant, even for newer releases. As mentioned on the setup page, this material covers Python 2. While we recommend "avoiding" Python 3 for now, recognize that it is the future, as all new features are only going there. The good news is that developers learning either version can pick up the other without too much difficulty. If you want to know more about choosing Python 2 vs. 3, check out this post.    """)

#prefixes = "JKLMNOPQ"
#suffix = "ack"

#for letter in prefixes:
#    if letter == "O" or letter == "Q":
#        letter += "u"
#    print(letter + suffix)

#ttt()
	
test_suite() 








