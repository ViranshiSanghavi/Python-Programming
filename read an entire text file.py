#Write a program to read an entire text file
def file_read(fname):
    try:
        text = open(fname)
        print(text.read())
        text.close()
    except FileNotFoundError:
        print(f"The file '{fname}' was not found.")

file_read('text.txt')

#Note:- Create a text.txt file in the notepad to get the output or else the
#output will be file not found

