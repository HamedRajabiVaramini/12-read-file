'''
simple_programming_

This code opens a text file in a read mode
and prints its content
Read mode "r" is the default value
Text mode "t" is the default value as well 
'''
# as same as open("text_file.txt", "rt") 
f = open("text_file.txt")
print(f.read()) # print file content 
f.close() 
# need to call close function 
# to close the file after use to release the resource   

