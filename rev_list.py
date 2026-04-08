# WAP to reverse a list without using built-in functions.
lst = [1, 2, 3, 4, 5, 6]
reversed_lst = []

for idx in range(len(lst) - 1, -1, -1):
    reversed_lst.append(lst[idx])

print("Reversed list:", reversed_lst)
  
  