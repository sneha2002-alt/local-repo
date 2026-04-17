# Set
s = {1, 2, 2, 2, 3, 4, 5}

print(s)

empty_set = set()

# Set Methods

s.add(7)
print(s)

s.remove(2)
print(s)

s.pop()
print(s)

s.clear()
print(s)

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))
print(s1.intersection(s2))

set = {1}

print(type(set))
