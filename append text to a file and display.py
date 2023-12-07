#Append text to a file and display
def main():
    f = open("text.txt", "a")
    f.write("Welcome to Python")
    f.close()

if __name__ == "__main__":
    main()
#Note:- Output will be displayed in the created text.txt file as (Welcome to Python)
