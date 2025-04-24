dictionary1={
    "professional" : {
        "name" :"Aniket Darje",
        "role" : "Developer",
        "experience" : "1 year"
    }
    ,
    "personal" : {
        "name" : "Aniket Darje",
        "age" : 26,
        "gender" : "Male",
        "interest" : "Music"
    },
    "name" : "Aniket Darje"
}

print(dictionary1.keys()) #Returns all high level keys
print(dictionary1.values()) # Returns all the values
print(dictionary1.items()) #Returns all (key, val) pairs as tuple
print(dictionary1.get("name")) # Returns the value for key we also have one more way to access is dict["key"] but if key is not correct then it will throw an error and if we use get then it will just return none if key is invalid so this way we save our program by avoiding errors.
print(dictionary1.update({"mykey" : "myval"})) # this cant be printed and hence return none
print(dictionary1)
