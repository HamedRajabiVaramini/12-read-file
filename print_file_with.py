'''
simple_programming_

This code opens a text file in a read mode
and prints its content line by line
while using "with" keyword to take care about 
closing file automatically.
Read mode "r" is the default value
Text mode "t" is the default value as well 
'''
# as same as open("text_file.txt", "rt") 
with open("text_file.txt") as f:
    for line in f: # loop over lines 
        print(line)
# no need to call close function 
# to close the file after use 
# it automatically happens   

