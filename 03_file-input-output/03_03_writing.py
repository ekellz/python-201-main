# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

import pathlib

input_file_path = '/Users/ericajansen/Documents/codingnomads/python-201-main/03_file-input-output/words.txt'
output_file_path = '/Users/ericajansen/Documents/codingnomads/python-201-main/03_file-input-output/words_reverse.txt'

# Open the file for reading
with open(input_file_path, 'r') as file_in:
    contents = file_in.read()

# Reverse the contents
contents_reversed = contents[::-1]
with open(output_file_path, 'w') as file_out:
    file_out.write(contents_reversed)
    print(contents_reversed)

