aniket=["Aniket",25,"Developer"]
print(aniket)
print(len(aniket))
print(aniket[0])
aniket[2]="Flutter Developer" # We can update the value at the index
print(aniket)

#Slicing of the list
b=[33, 24 , 56 , 76, 83, 99, 27]
print(b[2:5]) # 56, 76, 83
print(b[:]) # prints whole list

#Methods of the list

b.append(77) # will append 77 to the last of the list
print(b)

b.sort() #Will sort the list in the ascending order
print(b)

b.sort(reverse=True) # orts the list in the descending order 
print(b)

b.reverse() # Will reverse the list 
print(b)

b.insert(4, 44) # will insert the element 44 at the index 4
print(b)

b.insert(33, 33) # will insert the element 44 at the index 4
print(b) # If we insert an element at the index which is currenlt not in the range that is exceeds the length of the list, it will add that element at the very end of the list

b.remove(33) #Remove first occurance of element 33
print(b)

b.pop(2) #Removes element at the index 2
print(b)
