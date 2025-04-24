#Set
#Set is the collection of unordered items.
#Each element in the set must be unique and immutable
#Repeated elements stored only once
#The set is mutable but the elements in the set are immutable

#Declaration of empty set
set1= set()

set2={1,2,3,2,1,}
print(set2)

#Methods
set2.add("Aniket")
print(set2) #It will add this element to the set
set2.remove(2) #Removes 2 from set
print(set2)
