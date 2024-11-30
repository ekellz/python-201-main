# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1. Convert to a different data type
list_ = list(set(list_))
print(list_)

# 2. Use a loop and a second list to solve it more manually
for item in list_:
    if list_.count(item) > 1:
        list_.remove(item)
print(list_)