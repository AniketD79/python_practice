#To craete a file using program if we name and open the file in write mode 
#It will be auto created if not present

#Q1
# with open("auto_created_file.txt", "w") as f:
#     f.write("My name ia Aniket\nThis is an auto generated file")
#     # d=f.read()
#     # print(d)

# with open("auto_created_file.txt", "r") as f1:
#     print(f1.read())

#Q2
# with open("auto_created_file.txt", "r") as f:
#     data=f.read()
#     newdata=data.replace("ia", "is")
#     print(newdata)

#Above will not replace actual file data it will just replace on console and thats it no real data is being replaced.
#But below will
# with open("auto_created_file.txt", "w") as f1:
#    f1.write(newdata)


#Q3

# with open("auto_created_file.txt", "r") as f:
#     data=f.read()
#     if(data.find("AAniket" )!= -1):
#         print("Found")
#     else:
#         print("Not Found")

#Q4

# def check_for_line() :
#     word = "Aniket"
#     data = True
#     line_no = 1
#     with open("auto_created_file.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return -1

# check_for_line()






#Q5
count = 0
with open("sixth_nums.txt", "r") as f:
    data= f.read()
    nums= data.split(",")
    for num in nums:
        if(int(num) % 2==0):
            count +=1
    
    print(count)
    
