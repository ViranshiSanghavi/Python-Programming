#To count the number of occurrence of each word in a given sentence# Input sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words and count using a dictionary
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

# Print the word frequencies
for word, count in word_count.items():
    print(f"'{word}' appears {count} time(s) in the sentence.")
