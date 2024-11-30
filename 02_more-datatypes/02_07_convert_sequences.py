# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
to_tuple = tuple(string)
print(type(to_tuple))
to_list = list(to_tuple)
print(type(to_list))
for char in to_list:
    if char == "c":
        change_letter = list(to_list)
        change_letter[to_list.index(char)] = "k"
        break
print(change_letter)
change_back = tuple(change_letter)
print(type(change_back))
