# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

file_in = open('words.txt', 'r')
contents = file_in.read()
for word in contents.split():
    if 