#Set
#Set is the collection of unordered items.
#Each element in the set must be unique and immutable
#Repeated elements stored only once
#The set is mutable but the elements in the set are immutable
#We also can store tuple in set as tuple is immutable
#Declaration of empty set
set1= set()

set2={1,2,3,2,1,}
print(set2)

#Methods
set2.add("Aniket")
print(set2) #It will add this element to the set
set2.remove(2) #Removes 2 from set
print(set2)
print(len(set2))
print(set2.pop()) #Removes any random value from the set
print(set2)

#Union of sets

set3={1,2,3,4,9}
set4={1,4,8,5,6,7}
print(set3.union(set4)) # I noticed it gives ordered output

#Intersection of sets
print(set3.intersection(set4))