#Write a python program to print a specified list after removing the 0th,2nd,4th
#and 5th elements
l1=[1,2,3,4,5,6,7,8,9,0]
print("Original list is",l1)
print("We have to remove 0th->1, 2nd->3, 4th->5, 5th->6")
l1.pop(0)
print("After removal of 0th element, now list is:",l1)
l1.pop(1)
print("Now remove 3 from list which is at 1st position of index")
print("After removal of 1st element, new list is:",l1)
l1.pop(2)
print("Now remove 5 from list which is at 2nd position of index")
print("After removal of 2nd element, new list is:",l1)
l1.pop(2)
print("Now remove 6 from list which is at second position index")
print("After removal of 2nd element,new list is:",l1)
