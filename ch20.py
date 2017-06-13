from unit_tester import test
import string
import urllib.request
import wordtools
import math
import turtle
import time

def letter_count(s):
    """ counts the letters in a string and places them into a dictionary """
    new_s=""
    for c in s:
        if c not in string.punctuation and c != " ":
            new_s = new_s + c

    letter_counts = {}
    for letter in new_s:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def main():
    sentence = input("Enter a string of characters, like a sentence:")
    letter_list = list(letter_count(sentence.lower()).items())
    letter_list.sort()
    for (x,y) in letter_list:
        print("{0:<4}{1}".format(x,y))

def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit,0) + quantity
    return

# Make these tests work...

def test_suite():
    new_inventory = {}
    add_fruit(new_inventory, "strawberries", 10)
    test("strawberries" in new_inventory)
    test(new_inventory["strawberries"] == 10)
    add_fruit(new_inventory, "strawberries", 25)
    test(new_inventory["strawberries"] == 35)

#test_suite()

#main()