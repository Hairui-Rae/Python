# Practice 2: String counter

text = input("Please input the text:")
letter_count = 0
digit_count = 0

for char in text:
    if char.isalpha():
        letter_count += 1
    if char.isdigit():
        digit_count += 1

print(f"The number of letters is: {letter_count}")
print(f"The number of digits is: {digit_count}")
print(f"The total characters are: {len(text)}")