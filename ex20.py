# create a .txt file in the same folder, and add it to the run script
# in powershell ( python ex20.py test.txt)

#On line 16 we have what's called an "import". 
#This is how you add features to your script 
#from the Python feature set. Rather than give 
#you all the features at once, Python asks you 
#to say what you plan to use. This keeps your 
#programs small, but it also acts as documentation 
#for other programmers who read your code later.
#The argv is the "argument variable", a very standard 
#name in programming, that you will find used in 
#many other languages. This variable holds the 
#arguments you pass to your Python script when you run it. 

from sys import argv

#This line "unpacks" argv so that, rather than holding all 
#the arguments, it gets assigned to four variables you can
#work with: script, first, second, and third. This may look 
#strange, but "unpack" is probably the best word to describe 
#what it does. It just says, "Take whatever is in argv, 
#unpack it, and assign it to all of these variables on the left in order."

script, input_file = argv

#"def" its a function. 
#Functions do three things:
#They name pieces of code the way variables name strings and numbers.
#They take arguments the way your scripts take argv.
#Using #1 and #2 they let you make your own "mini scripts" or "tiny commands".
#You can create a function by using the word def in Python. I'm going to have you mak

#The f is variable related to the (f)ile 
def print_all(f):
    print f.read()

# seek function definition: "http://stackoverflow.com/questions/11696472/seek-function"	
def rewind (f):
    f.seek(0)

#The method readline()reads one entire line from the file. 
#A trailing newline character is kept in the string. 
#If the size argument is present and non-negative, 
#it is a maximum byte count including the trailing newline 
#and an incomplete line may be returned.	

def print_a_line(line_count, f):
    print line_count, f.readline()

# this line is calling the .txt file in the folder 	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Now let's print three lines:"
#takes the first line and add 1 in the left column
current_line = 1
print_a_line(current_line, current_file)
#add something else to that column
current_line = current_line + 1
print_a_line(current_line, current_file)
#and again
current_line = current_line + 1 
print_a_line(current_line, current_file)
