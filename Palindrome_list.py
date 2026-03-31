#WAP to check if a list contains a palindrome of elements
list1=[1,2,1]
list2=[1,2,3]

copy_list1 = list1.copy()
copy_list2 = list2.copy()

copy_list1.reverse()
copy_list2.reverse()

if(list1 == copy_list1):
  print("list1 is palindrome")
else:
  print("Not a palindrome")