# Convert a string to a tuple and print out the result.
# What do you see? 
    #-> it separated every letter out
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?
    # -> They seem to be the same

string = "codingnomads"

for char in string:
    print(char)

convert = tuple(string)
#for char in convert:
    #print(char)
