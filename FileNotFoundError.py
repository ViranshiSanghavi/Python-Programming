#Write a program that opens a file and handle a FileNotFoundError Exception
#of the file does not exist
try:
    file_name = input("Enter the filename: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")

#Output:- Enter the file name text.txt since it is in the folder
