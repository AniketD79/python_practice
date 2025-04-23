dictionary1 = {
  "key1" : "an",
  "age" : 25,
  "married": False,
  "package" : 3.36,
  "list" :["Aniket", "Nandkishor", "Darje"],
  "tuple":("Aniket", "Nandkishor", "Darje"),
  1:"int key",
  True: "bool key",
  tuple: 'tuple as key as it is immutable as keys cannot be changed'
  #dict or lists are mutable so cannot be considered as key as they are mutable
 }
print(dictionary1)
print(type(dictionary1))
print(dictionary1["married"])
#Change value
dictionary1["age"]= 26

print(dictionary1)
# Add new key val
dictionary1["surname"]=  "Darje"
print(dictionary1)

# We also can create a dictionary inside a dictionary
dictionary1["addresses"] ={
    "home" : "Deulgaon Raja",
    "work" : "Pune"
}
print(dictionary1)
print(dictionary1["addresses"]["home"])