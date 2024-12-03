# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.


import pathlib

file_path = pathlib.Path('/Users/ericajansen/Documents/codingnomads/python-201-main/03_file-input-output/words.txt')
output_file_path = pathlib.Path('/Users/ericajansen/Documents/codingnomads/python-201-main/03_file-input-output/new_words.txt')

# Open the file for reading
with file_path.open('r') as file_in:
    contents = file_in.read()

with output_file_path.open('w') as file_out:
    file_out.write(contents)
    print(contents)