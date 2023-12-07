def LastNlines(fname, N):
    with open(fname) as file:
        lines = file.readlines()
        for line in lines[-N:]:
            print(line, end='')

if __name__ == '__main__':
    fname = input('Enter the file name: ')
    try:
        N = int(input('Enter the number of lines to read: '))
        LastNlines(fname, N)
    except FileNotFoundError:
        print('File not found')
    except ValueError:
        print('Invalid input for the number of lines. Please enter a valid integer.')


#File is File1.txt
