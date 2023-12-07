#Write a script to sort a dictionary by value(ascending and descending)
# Sample dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

# Sort by values in ascending order
ascending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sort by values in descending order
descending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", ascending_sorted)
print("Descending order:", descending_sorted)



''' user input code:
def sort_dict(d, reverse=False):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

if __name__ == '__main__':
    try:
        user_input = input('Enter a dictionary (key1:value1,key2:value2,...): ')
        user_dict = dict(item.split(':') for item in user_input.split(','))
        sorting_order = input('Enter the sorting order (asc/desc): ')

        if sorting_order == 'asc' or sorting_order == 'desc':
            sorted_dict = sort_dict(user_dict, sorting_order == 'desc')
            print('Sorted Dictionary:', sorted_dict)
        else:
            print('Invalid sorting order. Please enter "asc" for ascending or "desc" for descending.')
    except ValueError:
        print('Invalid input format for the dictionary. Please enter key-value pairs separated by commas.')

#{'date': '4', 'apple': '3', 'cherry': '2', 'banana': '1'}
#{'grape': '2', 'pear': '3', 'orange': '5', 'kiwi': '7'}
'''
