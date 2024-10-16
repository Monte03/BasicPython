# Завдання 1
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

# Завдання 2
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_in_months[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")


# Завдання 3
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None

    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_in_months[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1:
        return None

    days_in_current_month = days_in_month(year, month)
    if day > days_in_current_month:
        return None

    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    total_days += day
    
    return total_days

print(day_of_year(2000, 12, 31))
print(day_of_year(2024, 3, 1))
print(day_of_year(2019, 1, 1))
print(day_of_year(2016, 2, 29))
print(day_of_year(2016, 12, 31))
print(day_of_year(2021, 7, 15))
print(day_of_year(2020, 2, 30))
print(day_of_year(2020, 13, 1))
print(day_of_year(2020, 4, 31)) 

# Завдання 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

# Завдання 5
def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100000 / 1609.344
    gallons = liters / 3.785411784
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    km_per_gallon = miles * 1.609344
    return (100 / km_per_gallon) * 3.785411784

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

# Завдання 6
def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

print(is_a_triangle(6, 8, 10))
print(is_a_triangle(1, 2, 3))
print(is_a_triangle(5, 5, 5))
print(is_a_triangle(10, 2, 7))
print(is_a_triangle(7, 24, 25))

# Завдання 7
def is_a_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False

    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

print(is_a_right_triangle(6, 8, 10))
print(is_a_right_triangle(1, 2, 3))
print(is_a_right_triangle(5, 5, 5))
print(is_a_right_triangle(10, 2, 7))
print(is_a_right_triangle(7, 24, 25))