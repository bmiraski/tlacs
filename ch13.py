from unit_tester import test
import string
import urllib.request
import wordtools

#myfile = open("test.txt", "w")
#myfile.write("My first file written from Python\n")
#myfile.write("---------------------------------\n")
#myfile.write("Hello, world!\n")
#myfile.close()

#mynewhandle = open("test.txt", "r")
#while True:                            # Keep reading forever
#    theline = mynewhandle.readline()   # Try to read next line
#    if len(theline) == 0:              # If there are no more lines
#        break                          #     leave the loop

#    # Now process the line we've just read
#    print(theline, end="")

#mynewhandle.close()

def reversefile(file):
    """
    Reverses the lines in a file
    """
    f = open(file, "r")
    xs = f.readlines()
    f.close()

    l = len(xs)-1
    new_xs = []
    while l > -1:
        new_xs.append(xs[l])
        l = l-1

    g = open("reversefile.txt", "w")
    for v in new_xs:
        g.write(v)
    g.close()

def snakefile(file):
    """
    creates a file of lines that contain snake
    """
    f = open(file, "r")
    xs = f.readlines()
    f.close()

    snakelines = []
    for i in xs:
        if "snake" in i:
            snakelines.append(i)

    g = open("snakefile.txt", "w")
    for v in snakelines:
        g.write(v)
    g.close()

def numberlines(file):
    """
    Returns a copy of a file with all lines numbered
    """
    f = open(file, "r")
    xs = f.readlines()
    f.close()

    numlines = []
    layout = "{0:>5} {1}"
    for i in range(len(xs)):
        num = layout.format(i+1, xs[i])
        numlines.append(num)

    g = open("linenumbers.txt", "w")
    for v in numlines:
        g.write(v)
    g.close()

def nolines(file):
    """
    Removes line numbers from files
    """
    f = open(file, "r")
    xs = f.readlines()
    f.close()

    nonum = []
    for i in range(len(xs)):
        s = xs[i]
        short = s[6:]
        nonum.append(short)

    g = open("nonum.txt","w")
    for v in nonum:
        g.write(v)
    g.close()

#url = "https://en.wikipedia.org/wiki/Cobra"
#destination_filename = "cobra.txt"

#urllib.request.urlretrieve(url, destination_filename)

#reversefile("test.txt")

#snakefile("cobra.txt")

#numberlines("ch7.py")

nolines("linenumbers.txt")