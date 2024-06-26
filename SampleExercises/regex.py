import re

def matchStrings(string):
    pattern = r'\b[a-zA-Z]*ing\b'
    matches = re.findall(pattern, string)
    for match in matches:
        print(match)


def find_words_starting_with_vowels(text):
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
    matches = re.findall(pattern, text)
    return matches

def find_lines_starting_with_vowels(filename):
    pattern = r'^[aeiouAEIOU].*'
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            if re.match(pattern, line):
                print(f"Line {line_number}: {line.strip()}")


string ="I am singing while running to the swimming pool."
matchStrings(string)

text = "An example of an apple and an orange."
words_starting_with_vowels = find_words_starting_with_vowels(text)
print(words_starting_with_vowels)

find_lines_starting_with_vowels("loginfo.log")