#Print characters from a string that are present at even index number

input_string = "Hello, World!"

even_index_characters = ""

for index in range(len(input_string)):
    if index % 2 == 0:
        even_index_characters += input_string[index]

print("Characters at even index positions:", even_index_characters)


'''user input
input_string = input("Enter a string: ")

even_index_characters = ""

for index, char in enumerate(input_string):
    if index % 2 == 0:
        even_index_characters += char

print("Characters at even index positions:", even_index_characters)

'''
