# Dictionary
info = {
  "key" : "value",
  "name" : "Sneha",
  "subjects" : ["python", "C", "Java"],
  "topics" : ("dict", "set"),
  "age" : "35"
}

print(info)
print(type(info))

# key cannot be of datatype list and dictionary

# Accessing each element of dictionary
print(info["name"])
print(info["key"])
print(info["subjects"])
print(info["age"])

# Dictionary is mutable, we can change values
info["name"] = "Rahul"
print(info["name"])

info["surname"] = "Aggarwal"
print(info)

# Empty dictionary can also be created
null_dict = {}
print(null_dict)

# Nested dictionary
student = {
  "name" : "Rahul kumar",
  "subjects" : {
    "phy" : 97,
    "chem" : 98,
    "math" : 95
  }
}

print(student)
print(student["subjects"])
print(student["subjects"]["chem"])