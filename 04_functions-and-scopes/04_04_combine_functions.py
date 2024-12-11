# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    return f"Hello, {name}!"

def write_letter(name, text):
    greeting = greet(name)
    goodbye = f"Goodbye, {name}!"
    letter = f"{greeting}\n\n{text}\n\n{goodbye}"
    return letter

letter = write_letter("Erica", "I hope you are well, yo.")
print(letter)
