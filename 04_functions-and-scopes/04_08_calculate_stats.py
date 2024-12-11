# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(numbers):
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
    print(f"Avg: {sum(numbers) / len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    pass

# call the function below here
stats(example_list)
print(stats)