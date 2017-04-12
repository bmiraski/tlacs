from unit_tester import test
import string

def cleanword(word):
    """
    Removes punctuation from the given string and condenses the string
    """
    char = list(word)
    new_word = []
    for i in char:
        if i not in string.punctuation:
            new_word.append(i)
    return "".join(new_word)

def has_dashdash(str):
    """
    Determines if string str has the characters '--' included 
    """
    return len(str.split("--")) > 1

def extract_words(str):
    """
    Extracts the words in lowercase from a string 
    """
    cleanstring = ""
    for a in str:
        if a not in string.punctuation:
            cleanstring += a
        else:
            cleanstring += " "
    lower = cleanstring.lower()
    return lower.split()

def wordcount(word, u):
    """
    Counts the occurrences of a word within a list
    """
    count = 0
    for i in range(len(u)):
        if word == u[i]:
            count += 1
    return count

def wordset(u):
    """
    Returns the set of unique words within a list
    """
    set = []
    new_u = sorted(u)
    for i in new_u:
        if i not in set:
            set.append(i)
    return set

def longestword(u):
    """
    Returns the length of the longest word in a list
    """
    longest = ""
    for i in u:
        if len(i) > len(longest):
            longest = i
    return len(longest)


def test_suite():
    """ 
    Run the suite of tests for code in this module (this file).
    """
    test(cleanword("what?") == "what")
    test(cleanword("'now!'") == "now")
    test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

    test(has_dashdash("distance--but"))
    test(not has_dashdash("several"))
    test(has_dashdash("spoke--"))
    test(has_dashdash("distance--but"))
    test(not has_dashdash("-yo-yo-"))

    test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
        ['now','is','the','time','now','is','the','time','yes','now'])
    test(extract_words("she tried to curtsey as she spoke--fancy") ==
        ['she','tried','to','curtsey','as','she','spoke','fancy'])

    test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
    test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
    test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
    test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

    test(wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"])
    test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
    test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"])

    test(longestword(["a", "apple", "pear", "grape"]) == 5)
    test(longestword(["a", "am", "I", "be"]) == 2)
    test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
    test(longestword([ ]) == 0)


test_suite()