print("Hello world!")
print("Happy Learning")

#concatenation
str1="hii"
str2="hello"
final_str = str1 + " " + str2 
print(final_str)
print(len(final_str))

#indexing
str = "Happy_Learning"
ch = str[0]
print(ch)

#slicing
print(str[1:5]) #ending index not included
print(str[0:len(str)])
print(str[:])
print(str[:4]) #0 to 4
print(str[5:]) #5 to len(str)

#negative indexing
print(str[-6:-1]) #start from last from -1
print(str[-6:len(str)])