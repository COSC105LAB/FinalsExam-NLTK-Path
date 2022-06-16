import nltk
from nltk.tokenize import word_tokenize
import string
import re
import inflect

def convert_number_to_word(text):
    str_temp = word_tokenize(text)
    str_new = []

    for word in str_temp:
        # If the current word is a digit, convert
        # to number and append into the str_new list
        if word.isdigit():
            temp = inflector.number_to_words(word)
            str_new.append(temp)
        else:
            str_new.append(word)

    # Join the list to form a new string.
    str_temp = ' '.join(str_new)
    return str_temp

input_strip_numbers = input("Enter a sentence with numbers: ")
print(convert(input_strip_numbers))
