#Define a function that computes the length of a given list or string
def len_s(s):
    count = 0
    for i in s:
        count += 1
    print("The total length of the string:", count)

s = str(input("Enter a statement: "))
len_s(s)
