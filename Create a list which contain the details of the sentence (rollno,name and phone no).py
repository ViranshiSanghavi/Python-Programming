#Q. Create a list which contain the
#details of the sentence (rollno,name and phone no)
# Initialize an empty list to store details
details_list = []

# Get user input for details
while True:
    roll_no = input("Enter Roll No (or 'q' to quit): ")
    if roll_no == 'q':
        break
    
    name = input("Enter Name: ")
    phone_no = input("Enter Phone No: ")
    
    # Append the details as a sublist to the list
    details_list.append([roll_no, name, phone_no])

# Print the list of details
for details in details_list:
    print(details)

