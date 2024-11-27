# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list = ["go", 1, 5, "get", "go", 1, 5, "get", "yo"]
unique_list = set(list)
print(f"Unique list = {unique_list}")