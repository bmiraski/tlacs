from unit_tester import test
import string
import urllib.request
import wordtools
import time


def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    for (i, v) in enumerate(xs):
        if v == target:
            return i
    return -1


def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_binary(vocab, w) < 0):
            result.append(w)
    return result


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds


def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:  # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
        #       .format(lb, ub, ub-lb, item_at_mid, target))

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index  # Found it!
        if item_at_mid < target:
            lb = mid_index + 1  # Use upper half of ROI next time
        else:
            ub = mid_index  # Use lower half of ROI next time


def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result


def merge(xs, ys):
    """ merge sorted lists xs and ys. Return a sorted result """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result  # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1


def merge_both(xs, ys):
    """ merge sorted lists xs and ys. Return only items in both """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            return result  # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            return result

        # Both lists still have items, compare item to result.
        if xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            result.append(xs[xi])
            xi += 1
            yi += 1


def merge_first(xs, ys):
    """ compare two lists, only return items that are only in first list """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            return result  # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, compare item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


def bagdiff(xs, ys):
    """ compare two lists, knock out the first of duplicated items """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):  # If xs list is finished,
            return result  # And we're done.

        if yi >= len(ys):  # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, compare item to result.
        if xs[xi] < ys[yi]:
            result.append(xs[xi])
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
        else:
            xi += 1
            yi += 1


def find_unknowns_merge_pattern(vocab, wds):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words from wds that do not occur in vocab.
    """

    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(vocab):
            result.extend(wds[yi:])
            return result

        if yi >= len(wds):
            return result

        if vocab[xi] == wds[yi]:  # Good, word exists in vocab
            yi += 1

        elif vocab[xi] < wds[yi]:  # Move past this vocab word,
            xi += 1

        else:  # Got word that is not in vocab
            result.append(wds[yi])
            yi += 1


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # CXalc the absolute x distance
    return dx == dy  # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True

    return False  # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def flip_x(bd):
    flipx = list(range(8))
    for x in range(8):
        flipx[x] = bd[7 - x]
    return flipx

def turn90(bd):
    turn_ninety = []
    col=0
    while col < len(bd):
        for x in range(len(bd)):
            if bd[x] == col:
                turn_ninety.append(7-x)
                col += 1
    return turn_ninety



def test_suite():
    friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
    test(search_linear(friends, "Zoe") == 1)
    test(search_linear(friends, "Joe") == 0)
    test(search_linear(friends, "Paris") == 6)
    test(search_linear(friends, "Bill") == -1)
    vocab = ["apple", "boy", "dog", "down",
             "fell", "girl", "grass", "the", "tree"]
    book_words = "the apple fell from the tree to the grass".split()
    test(find_unknown_words(vocab, book_words) == ["from", "to"])
    test(find_unknown_words([], book_words) == book_words)
    test(find_unknown_words(vocab, ["the", "boy", "fell"]) == [])
    test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
    test(text_to_words('"Well, I never!", said Alice.') ==
         ["well", "i", "never", "said", "alice"])
    xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]
    test(search_binary(xs, 20) == -1)
    test(search_binary(xs, 99) == -1)
    test(search_binary(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        test(search_binary(xs, v) == i)
    test(remove_adjacent_dups([1, 2, 3, 3, 3, 3, 5, 6, 9, 9]) == [1, 2, 3, 5, 6, 9])
    test(remove_adjacent_dups([]) == [])
    test(remove_adjacent_dups(["a", "big", "big", "bite", "dog"]) ==
         ["a", "big", "bite", "dog"])
    xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    ys = [4, 8, 12, 16, 20, 24]
    zs = xs + ys
    zs.sort()
    test(merge(xs, []) == xs)
    test(merge([], ys) == ys)
    test(merge([], []) == [])
    test(merge(xs, ys) == zs)
    test(merge([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
    test(merge(["a", "big", "cat"], ["big", "bite", "dog"]) ==
         ["a", "big", "big", "bite", "cat", "dog"])
    test(merge_both([1, 2, 3], [3, 4, 5]) == [3])
    test(merge_both(["a", "big", "cat"], ["big", "bite", "cat"]) ==
         ["big", "cat"])
    test(merge_first([1, 2, 3], [3, 4, 5]) == [1, 2])
    test(merge_first(["a", "big", "cat"], ["big", "bite", "dog"]) ==
         ["a", "cat"])
    test(merge_first(["a", "big", "cat"], ["big", "bite", "cat"]) ==
         ["a"])
    test(not share_diagonal(5, 2, 2, 0))
    test(share_diagonal(5, 2, 3, 0))
    test(share_diagonal(5, 2, 4, 3))
    test(share_diagonal(5, 2, 4, 1))
    test(not col_clashes([6, 4, 2, 0, 5], 4))
    test(not col_clashes([6, 4, 2, 0, 5, 7, 1, 3], 7))
    test(col_clashes([0, 1], 1))
    test(col_clashes([5, 6], 1))
    test(col_clashes([6, 5], 1))
    test(col_clashes([0, 6, 4, 3], 3))
    test(col_clashes([5, 0, 7], 2))
    test(not col_clashes([2, 0, 1, 3], 1))
    test(col_clashes([2, 0, 1, 3], 2))
    test(not has_clashes([6, 4, 2, 0, 5, 7, 1, 3]))  # Solution from above
    test(has_clashes([4, 6, 2, 0, 5, 7, 1, 3]))  # Swap rows of first two
    test(has_clashes([0, 1, 2, 3]))  # Try small 4x4 board
    test(not has_clashes([2, 0, 3, 1]))  # Solution to 4x4 case
    test(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]) == [5, 11, 11, 12, 13])
    #test(turn90([6, 4, 2, 0, 5, 7, 1, 3]) == [4, 1, 5, 0, 6, 3, 7, 2])
    #test(turn90([5,2,4,7,0,3,1,6]) == [3,1,6,2,5,7,0,4])


#test_suite()

# bigger_vocab = load_words_from_file("vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} "
#              .format(len(bigger_vocab), bigger_vocab[:6]))

# all_words = get_words_in_book("AliceInWonderland.txt")
# all_words.sort()
# book_words = remove_adjacent_dups(all_words)
# print("There are {0} words in the book. Only {1} are unique.".
#                      format(len(all_words), len(book_words)))
# print("The first 100 words are\n{0}".
#           format(book_words[:100]))

# t0 = time.clock()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.clock()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

# t0 = time.clock()
# missing_words = find_unknown_words(bigger_vocab, book_words)
# t1 = time.clock()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

# all_words = get_words_in_book("AliceInWonderland.txt")
# t0 = time.clock()
# all_words.sort()
# book_words = remove_adjacent_dups(all_words)
# missing_words = find_unknowns_merge_pattern(bigger_vocab, book_words)
# t1 = time.clock()
# print("There are {0} unknown words.".format(len(missing_words)))
# print("That took {0:.4f} seconds.".format(t1-t0))

def main():
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(8))     # Generate the initial permutation
    num_found = 0
    tries = 0
    results = []
    while num_found < 10:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           if bd in results:
               print ("Found a solution, but it was already found!")
           else:
               results.append(bd[:])
               print("Found solution {0} in {1} tries.".format(bd, tries))
               tries = 0
               num_found += 1
    print(results)

t0 = time.clock()
main()
t1 = time.clock()
print("That took {0:.4f} seconds.".format(t1 - t0))

def main_flipx():
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(8))     # Generate the initial permutation
    tries = 0
    solutions=0
    while solutions != 1:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            solutions = 1
    flipx = list(range(8))
    for x in range(8):
        flipx[x] = bd[7-x]
    print (has_clashes(flipx))
    print ("The solution flipped over the x-axis is {}".format(flipx))

# main_flipx()

def main_flipy():
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(8))     # Generate the initial permutation
    tries = 0
    solutions=0
    while solutions != 1:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            solutions = 1
    flipy = list(range(8))
    for x in range(8):
        flipy[x] = 7- bd[x]
    print (has_clashes(flipy))
    print ("The solution flipped over the y-axis is {}".format(flipy))

#main_flipy()

def main_90():
    import random
    rng = random.Random()   # Instantiate a generator

    bd = list(range(8))     # Generate the initial permutation
    tries = 0
    solutions=0
    while solutions != 1:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
            print("Found solution {0} in {1} tries.".format(bd, tries))
            solutions = 1

    print(has_clashes(turn90(bd)))
    print("The solution flipped 90-degrees is {}".format(turn90(bd)))

    print(has_clashes(turn90(turn90(bd))))
    print("The solution flipped 180-degrees is {}".format(turn90(turn90(bd))))

    print(has_clashes(turn90(turn90(turn90(bd)))))
    print("The solution flipped 270-degrees is {}".format(turn90(turn90(turn90(bd)))))

    print("The original solution was {}".format(turn90(turn90(turn90(turn90(bd))))))

#main_90()

def family():
    family = []
    sol = [0,4,7,5,2,6,1,3]
    family.append(sol)
    family.append(flip_x(sol))
    family.append(turn90(sol))
    family.append(flip_x(turn90(sol)))
    family.append(turn90(turn90(sol)))
    family.append(flip_x(turn90(turn90(sol))))
    family.append(turn90(turn90(turn90(sol))))
    family.append(flip_x(turn90(turn90(turn90(sol)))))
    print (family)

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

def lotto():
    import random
    rng=random.Random()
    balls = list(range(1,50))
    rng.shuffle(balls)
    draw = balls[:6]
    return draw

def lotto_match(draw, ticket):
    """returns the number of matches on a lotto ticket"""
    matching_numbers = []
    xi = 0
    yi = 0

    draw.sort()

    while True:
        if xi >= len(draw):  # If draw list is finished,
            return len(matching_numbers)  # And we're done.

        if yi >= len(ticket):  # Same again, but swap roles
            return len(matching_numbers)

        # Both lists still have items, compare item to result.
        if draw[xi] < ticket[yi]:
            xi += 1
        elif draw[xi] > ticket[yi]:
            yi += 1
        else:
            matching_numbers.append(ticket[yi])
            xi += 1
            yi += 1

def lotto_matches(draw, tickets):
    """Returns a list of number of matches given the draw and a list of tickets"""
    matches = []
    for x in tickets:
        matches.append(lotto_match(draw, x))
    return matches

def atleast(num):
    count = 0
    while True:
        drawing = lotto_matches(lotto(), my_tickets)
        for x in drawing:
            if x >= num:
                return count
        count += 1




# print(lotto())


#test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
#test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])


#t0 = time.clock()
#tries3 = 0
#dots = ""
#for x in range(20):
#    tries3 += atleast(3)
#    dots += "."
#    print (dots)
#tries4 = 0
#for x in range(20):
#    tries4 += atleast(4)
#    dots += "."
#    print (dots)
#tries5 = 0
#for x in range(20):
#    tries5 += atleast(5)
#    dots += "."
#    print (dots)
#print ("On average it took {0:.2f} tries to get three matches".format(tries3/20))
#print ("On average it took {0:.2f} tries to get four matches".format(tries4/20))
#print ("On average it took {0:.2f} tries to get five matches".format(tries5/20))
#t1 = time.clock()
#print("That took {0:.4f} seconds.".format(t1 - t0))