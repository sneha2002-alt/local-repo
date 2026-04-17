# Merge two dictionaries into one.

dict1 = {
  "a" : 5,
  "b" : 6,
  "c" : 7,
  "d" : 8
}

dict2 = {
  "e" : 25,
  "f" : 16,
  "g" : 47,
  "h" : 58
}

dict1.update(dict2)
print(dict1)