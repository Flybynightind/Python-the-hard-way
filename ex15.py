#import method argv from sys
from sys import argv

#unpack inputs into "script" and "filename"
script, filename = argv

#take the contents of the file passed from the command prompt and assign it to the variable txt
txt = open(filename)

#print out the filename
print "Here's your file %r:" %filename
#print out the results of running the "read" function on the txt variable
print txt.read()
#print a message to the user
print "Type the filename again:"
#take the raw input (with the prompt ">") and assign it to the variable "file_again"
file_again = raw_input("> ")

#open the filenamed in "file_again" and assign it to type
txt_again = open(file_again)

#print the output of the read function on txt_again
print txt_again.read()