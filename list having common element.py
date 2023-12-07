#Write a program that takes two lists and returns True if they have at least one common member
l1=[1,2,3,4,5,6]
l2=[11,12,13,14,15,6]
for i in l1:
    for j in l2:
        if i==j:
            print("The two lists have atleast one common element")
