# Завдання 1
hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Введіть ціле число для заміни середнього числа в списку: "))
hat_list.pop()
print("Довжина списку:", len(hat_list))

print(hat_list)

# Завдання 2
# Крок 1
n = int(input("Введіть кількість елементів у списку: "))
arr = []

for i in range(n):
    element = int(input(f"Введіть елемент {i+1}: "))
    arr.append(element)

# Крок 2
n = len(arr)
for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        break

print("Відсортований список:", arr)

# Завдання 3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("The list with unique elements only:")
print(unique_list)

# Завдання 4
chessboard = [["_"] * 8 for _ in range(8)]

chessboard[0][0] = "T"
chessboard[0][7] = "T"
chessboard[7][0] = "T"
chessboard[7][7] = "T"

for i in chessboard:
    print(i)