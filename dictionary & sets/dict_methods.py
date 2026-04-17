# Dictionary methods
info = {
  "name" : "shanaya",
  "cgpa" : 9.2,
  "subjects" : ["math", "science"],
  3.14 : "PI"
}

dict_keys = info.keys() # returns all keys
print(dict_keys)

print(info.values()) # returns all values

print(info.items()) # returns (key, val) pairs

print(info.get("name")) # returns val acc. to key

info.update({
  "city" : "delhi"}) # adds new item to dictionary

print(info)



