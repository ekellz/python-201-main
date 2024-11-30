# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

points = 0
the_set = set()

while True: 
    get_number = input("Please enter a number: (or type 'quit' to exit) ")

    if get_number == "quit":
        print("You have quit the game.")
        break

    try:
        number = int(get_number)
    except ValueError:
        print("Please enter a valid number.")
        continue
    # Identify the winning condition
    if len(the_set) > 10:
        print("You won!")
        break
    # Counting losing points
    if number in the_set:   
        print("Duplicate number. You lose a point.")
        points -= 1
    # Adding the number to the set
    else:
        the_set.add(number)
        print(the_set)
    # If the user loses 5 points, quit the program
    if points == -5:
        print("You lost!")
        break