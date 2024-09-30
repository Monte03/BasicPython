# Завдання 1
n = int(input())
print(n >= 100)

# Завдання 2
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

if a > b:
    print(f"Найбільше число: {a}")
else:
    print(f"Найбільше число: {b}")

# Завдання 3
plant = input()

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant}!")

# Завдання 4
income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# Завдання 5
# перша частина
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

# друга частина
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# третя частина
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# Завдання 6
secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while True:
    user_guess = int(input("Введіть своє припущення: "))
    if user_guess == secret_number:
        print("Молодець, магле! Тепер ти вільний")
        break
    else:
        print("Ха-ха! Ви застрягли у моїй петлі!")

# Завдання 7
import time

for i in range(1,6):
    print(f"{i} Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

# Завдання 8
while True:
    word = input("Enter a word: ")

    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

# Завдання 9
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue

    print(letter)

# Завдання 10
word_without_vowels = ""

user_word = input("Введіть слово: ")
user_word = user_word.upper()
for letter in user_word:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue

    word_without_vowels += letter

print(word_without_vowels)

# Завдання 11
blocks = int(input("Введіть кількість блоків: "))

height = 0
blocks_in_layer = 1

while blocks >= blocks_in_layer:
    blocks -= blocks_in_layer
    height += 1
    blocks_in_layer += 1

print("The height of the pyramid:", height)

# Завдання 12
c0 = int(input("Введіть натуральне число: "))

steps = 0

while c0 != 1:
    print(c0)
    
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    
    steps += 1

print(c0)
print("steps =", steps)