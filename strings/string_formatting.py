a = 5
b = 10
sum = a+b

#normal formatting
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a, b, sum))

#index based formatting
print("sum of {1} & {0} is {2}".format(a, b, sum))

#value based formatting
print("value of vars {a} & {b}".format(a=10, b=4))

# f-strings => literal string interpolation
print(f"avg of {a} & {b} is {(a+b)/2}")


