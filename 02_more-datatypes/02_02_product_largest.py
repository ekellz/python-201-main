# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

#from resources import randlist

list = []

while len(list) < 3:
    try:
        number = int(input("Please enter a number. "))
        list.append(number)
    except ValueError: 
        print("Fix yo entry. ")
#print(list)

largest_number = max(list)
print(f"largest number = {largest_number}")

total_sum = sum(list)
print(f"total sum = {total_sum}")
