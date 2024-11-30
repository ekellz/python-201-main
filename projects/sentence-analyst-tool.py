# user input
# set count to 0
# Loop through sentence (isupp, islower, ignore spaces)

sentence = input("Hello, please enter a senetence. ")
upper_count = 0
lower_count = 0
punt_count = 0

print(sentence)
for char in sentence:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif not char.isalnum() and not char.isspace():
        punt_count += 1

print(sentence)
print(f"Upper: {upper_count}")
print(f"Lower: {lower_count}")
print(f"Punt: {punt_count}")