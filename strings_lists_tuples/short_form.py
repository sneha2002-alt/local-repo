s = input("Enter name: ")
a = s.split()
updated = []
for word in a[:len(a)-1]: #iterate over all but last
  updated.append(word[0])
updated.append(a[len(a)-1])  
  
print(' '.join(updated))  