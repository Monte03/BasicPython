# Завдання 1
numbers = [20, 12, 17, 1, 3, 7, 140, 18, 36]
numbers_tuple = tuple(numbers)

n = int(input("Введіть число n: "))
result = [num for num in numbers_tuple if num < n]
print(n, ":", result)

# Завдання 2
strings_tuple = ("apple", "banana", "cherry")
result = ", ".join(strings_tuple)
print(result)

# Завдання 3
library = {
    "1984": {"author": "George Orwell", "year": 1949, "pages": 328},
    "To Kill a Mockingbird": {"author": "Harper Lee", "year": 1960, "pages": 281},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "year": 1925, "pages": 180},
    "War and Peace": {"author": "Leo Tolstoy", "year": 1869, "pages": 1225}
}

book_name = input("Введіть назву книги: ")

if book_name in library:
    book_info = library[book_name]
    print(f"Інформація про книгу '{book_name}':")
    print(f"Автор: {book_info['author']}")
    print(f"Рік видання: {book_info['year']}")
    print(f"Кількість сторінок: {book_info['pages']}")
else:
    print(f"Книга '{book_name}' не знайдена в бібліотеці.")

# Завдання 4
students = {
    "Ivanov": ("Ivan", 21, "Computer Science"),
    "Petrov": ("Petr", 22, "Mathematics"),
    "Sidorov": ("Alex", 20, "Physics"),
    "Kovalenko": ("Olga", 23, "Biology")
}

last_name = input("Введіть прізвище студента: ")
if last_name in students:
    student_info = students[last_name]
    print(f"Інформація про студента {last_name}:")
    print(f"Ім'я: {student_info[0]}")
    print(f"Вік: {student_info[1]}")
    print(f"Спеціальність: {student_info[2]}")
else:
    print(f"Студент з прізвищем '{last_name}' не знайдений.")

# Завдання 5
phone_book = {
    "Ivanov": ["+380501234567", "+380501111111"],
    "Petrov": ["+380631234567"],
    "Sidorov": ["+380991234567", "+380501234567"]
}

def add_phone_number(contact_name, phone_number):
    if contact_name in phone_book:
        phone_book[contact_name].append(phone_number)
        print(f"Номер телефону {phone_number} додано до контакту {contact_name}.")
    else:
        print(f"Контакт {contact_name} не знайдено у телефонній книзі.")

add_phone_number("Ivanov", "+380671234567")

print("\nТелефонна книга:")
for contact, numbers in phone_book.items():
    print(f"{contact}: {', '.join(numbers)}")