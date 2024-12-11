# Add type annotations to the three functions shown below.

def multiply(num1, num2): # type: (int, int) -> int
    return num1 * num2

def greet(greeting, name): # type: (str, str) -> str
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def shopping_list(*args): # type: (*str) -> list
    [print(f"* {item}") for item in args]
    return args
