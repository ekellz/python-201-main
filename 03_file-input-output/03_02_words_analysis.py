# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

import pathlib

file_path = '/Users/ericajansen/Documents/codingnomads/python-201-main/03_file-input-output/words.txt'
# Open the file for reading
with open(file_path, 'r') as file_in:
    contents = file_in.read()

words = contents.split()
sorted_words = sorted(words, key=len)

shortest = sorted_words[0]
min_length = len(sorted_words[0])

for word in sorted_words:
    if len(word) == min_length:
        print(word)

longest = sorted_words[-1]
max_length = len(sorted_words[-1])

for word in sorted_words:
    if len(word) == max_length:
        print(word)

print(f'Total number of words: {len(words)}')


