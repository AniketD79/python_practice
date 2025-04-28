
#Text files: txt, docx etc
#Binary Files: mp4, jpeg etc
#Read Write Clode Delete
# f= open("file_name", "mode")

#Code
# file1= open("fifth.txt", "r")
# print(file1.read())
# file1.close()

#Modes
# r = read
# w = open for writing, truncating the file first
# x = create a new file and open it for writing
# a = Open for writing, appending to the end of the file if exists
# b = Binary mode
# t = Text mode(ddefault)
# + = Open a disk file for updating(reading and writing)

# f.read() reads entire file
# f.readline() reads one line at a time 

#Another way to open or do operations on file using with syntax

# Code
# with open("fifth.txt", "r") as f:
#     data = f.read()
#     print(data)


#Deleting a file
# 1 Using the os module : 
# Module(like a code library) is a file written by another programmer that generally has a functions we can use.

import os
os.remove("deletefile.txt")