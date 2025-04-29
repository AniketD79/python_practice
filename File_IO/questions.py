# list1=["Aniket", "Nandkishor", "Darje"]
# # index=0
# with open("File_IO/pract1.txt", 'a') as f:
#     for i in list1:
#         # if(index<len(list1)):   
#             f.write(i+'\n')
#             # index+=1

# with open("File_IO/pract1.txt", "r") as f:
#       data = f.read()
#       print(data)

# If the file is large, you could read it line by line using:

# python
# Copy
# Edit
# with open("File_IO/pract1.txt", "r") as f:
#     for line in f:
#         print(line.strip())  # .strip() removes the newline character




#QQQQ
# with open("File_IO/pract1.txt", "r") as f:
   
#     count=0
#     for i in f:
      
#          count+=1
# print(count)

# #More clear approach
# with open("File_IO/pract1.txt", "r") as f:
#     lines = f.readlines()
#     print(len(lines))
# f.close()


#QQQQ

from datetime import datetime

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append to file
with open("File_IO/pract1.txt", "+a") as f:
    f.write(timestamp + '\n')

print("Timestamp appended!")





