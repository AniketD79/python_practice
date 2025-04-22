print("Hi")
print("Hello")

#String concatenation
str1= "Aniket"
str2= "Darje"
print(str1+str2)

print(len(str2))
str3= str1 + "  "+ str2
print(str3)
print(str3[5]) # Prints character at 5

        #Slicing
print(str3[2:5]) # prints characters from index 2 to 4

name= "ANIKET"
#This is normal and forward counting
#0 1 2 3 4 5
#A N I K E T
print(name[0:4]) #ANIK
print(name[0: len(name)]) #ANIKET

#Backward counting that is starting from last
# -6 -5 -4 -3 -2 -1
# A   N  I  K  E  T
print(name[-1 : -4 : -1]) #TEK

sentence= "My name is Aniket and I am a Developer"
print(sentence.endswith("r")) #True or false ans is True, it checks whole string's ending to match with "r"
print(sentence.count("a")) #Case sensitive 