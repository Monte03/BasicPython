import math
# Завдання 1
def gaussian(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

x = float(input("Введіть значення x: "))
mu = float(input("Введіть значення середнього (mu): "))
sigma = float(input("Введіть значення стандартного відхилення (sigma): "))

result = gaussian(x, mu, sigma)

print(f"Значення функції Гауса: {result}")

# Завдання 2
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=", ")

total_apples = john + mary + adam
print("Загальна кількість яблук:", total_apples)

# Завдання 3
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Завдання 4
x =  -1
x = float(x)
y = 3 * (x**3) - 2 * (x**2) + 3**x - 1
print("y =", y)

# Завдання 5
hours  = 2
seconds_per_hour = 3600
print("Hours:", hours)

print("Seconds in Hours:", hours * seconds_per_hour)

print("Goodbye!")

# Завдання 6
a = float(input("Введите первое число (a): "))
b = float(input("Введите второе число (b): "))

print("Результат добавления (a + b):", a + b)
print("Результат вычитания (a - b):", a - b)
print("Результат умножения (a * b):", a * b)

if b != 0:
    print("Результат деления (a / b):", a / b)
else:
    print("Деление на ноль не допускается..")

print("\nThat's all, folks!")

# Завдання 7
x = float(input("Введіть значення для x: "))

y = 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))

print("y =", y)

# Завдання 8
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_minutes = mins + dura

new_mins = total_minutes % 60
extra_hours = total_minutes // 60

new_hour = (hour + extra_hours) % 24

print(f"{new_hour}:{new_mins}")

# Контрольні запитання
x = int(2)
print(x * "5")
# Вівід 55

x = "2"
print(type(x))
#Вивід <class 'str'>


