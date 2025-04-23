

#Code that takes two numbers and an operator from the user and performs the operation accordingly
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=input("Select operation  you want to perform: + - * /")
if (c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
else:
    print("Please select appropriate operation from above!")