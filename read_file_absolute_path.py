'''
simple_programming_

This code opens a file in a read mode with absolute path
Read mode "r" is the default value
Text mode "t" is the default value as well 
'''
# as same as open("d:\\myFolder\text_file.txt") 
f = open("d:\\myFolder\text_file.txt", "rt") 
# doing something with the file here 
f.close() 
# need to call close function 
# to close the file after use to release the resource   

