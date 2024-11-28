# user input
# set count to 0
# Loop through sentence (isupp, islower, ignore spaces)

sentence = input("Hello, please enter a senetence. ")
upper_count = set()
lower_count = set()
punt_count = set()

print(sentence)
for char in sentence:
    if char.isupper():
        upper_count.add(char)
    elif char.islower():
        lower_count.add(char)
    elif char.isalpha == False:
        punt_count.add(char)

print(sentence)
print(f"Upper: {upper_count}")
print(f"Lower: {upper_count}")
print(f"Punt: {upper_count}")