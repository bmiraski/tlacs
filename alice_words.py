import string
import time

t0=time.clock()

f = open("AliceInWonderland.txt", "r")
txt = f.readlines()
f.close()

alice_wrds = {}
for x in txt: # loop over each line in the text
    alpha = ""
    for char in x: # read the characters in the string and replace the punctuation with spaces
        if char not in string.punctuation:
            alpha = alpha + char
        else:
            alpha = alpha + " "
    words = alpha.lower().split() # split the lowercase line into its associated words
    for word in words: # loop over each word in the line
        alice_wrds[word] = alice_wrds.get(word, 0) + 1 # add to the dictionary of words

print(alice_wrds["alice"])

max_word = ""
max_lng = 0
for k in alice_wrds:
    if len(k) > max_lng:
        max_word = k
        max_lng = len(k)
print("The longest word,",max_word+",","has",max_lng,"characters")

word_list = list(alice_wrds.items())  # generate a list from the dictionary

word_list.sort() # sort that list

# Then write to a file in the preferred format

g = open("alice_words.txt", "w")
g.write("{0:<18}{1:<5}\n".format("Word","Count"))
g.write("=======================\n")
for (x,y) in word_list:
    g.write("{0:<18}{1:<5}\n".format(x,y))
g.close()

t1 = time.clock()

print("That took {0:.2f} secs.".format(t1-t0))