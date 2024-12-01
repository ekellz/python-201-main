# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

file_out = open('long_words.txt', 'w')
file_out.write('Once upon a time, there was a princess who loved her kingdom very much. Oh, and supercalifragilisticexpialidocious!')
file_out.close()    


file_in = open('long_words.txt', 'r')
contents = file_in.read()
for word in contents.split():
    if len(word) > 20:
        print(word)
file_in.close()