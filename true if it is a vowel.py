#Write a function that takes a character (i.e. a string of length 1) and return
#true if it is vowel,false otherwise
def find_vowel(s):
    l=['a','e','i','o','u']
    for i in s:
        if i in l:
            print("True")
        else:
            print("False")
s=str(input("Enter a statement: "))
find_vowel(s)
