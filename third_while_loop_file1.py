#While loop

#while condition:
 #   statement 
#Keywords
#Break: Used to terminate the loop when encounters break
#Continue: Terminates execution in the current iteration and continues execution of the loop with next iteration
#
#
#
#Below will print 1 to 4 and break when 5
# num=1
# while num<=10:
#     if(num==5):
#         break
#     print(num)
#     num+=1

#Below will skip 4 and print rest all
num=1
while num<=10:
    if(num==4):
        num+=1
        continue
    print(num)
    num+=1