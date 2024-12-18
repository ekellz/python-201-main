# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

list = []

while len(list) < 10:
    try:
        number = int(input("Please enter a number. "))
        list.append(number)
    except ValueError: 
        print("Fix yo entry. ")
print(f"The list = {list}")

list_2 = [list[1], list[3], list[5], list[7], list[9]]
print(f"List_2 = {list_2}")

list_3 = [list[8], list[6], list[4], list[2], list[0]]
print(f"List 3 = {list_3}")