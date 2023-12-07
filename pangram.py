#A pangram is a sentence that contains all the letters of the alphabet at least
#once, for example: The quick brown fox jumps over the lazy dog. Task here is
#to write a function to check a sentence to see if it is a pangram or not.
import string
import sys

if sys.version_info[0] < 3:
    input = raw_input

def ispangram(sentence, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(sentence.lower())

print(ispangram(input('Sentence:')))
