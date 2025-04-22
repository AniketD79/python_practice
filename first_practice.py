# name= input("Enter name:")

# print(name)
# print(str(len(name))+""+name)
# # print(String(len(name)))
# a=10.8
# b=str(a)
# print(b)

# name="Aniket Nandkishor Darje"
# print(name.count("a"))

marks=99
grade=""
if(marks>=90):
    grade="A"
    print(grade)
elif(marks<90 and marks>=80):
    grade="B"
    print(grade)
elif(marks<80 and marks>=70):
    grade="C"
    print(grade)
else:
    print("Failed")

print("Grade of student is:", grade) #So no need of multiple print statements after each elif or if