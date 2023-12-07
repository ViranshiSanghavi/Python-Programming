#Palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(user_input, "is a palindrome.")
else:
    print(user_input, "is not a palindrome.")

#Output mom: is a palindrome
    #hello:not a palindrome
#civic, radar, level, rotor,
    
