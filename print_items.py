# WAF to print all items recursively from the list.
def print_list(list, idx = 0):
  if(idx == len(list)):
    return
  print(list[idx])
  print_list(list, idx+1)
  
fruits = ["apple", "mango", "banana", "kiwi", "guava", "litchi", "apricot", "papaya", "peach", "pear", "grapes"]  

print_list(fruits)