import datetime

def day_of_week(day, month, year):
    return datetime.date(year, month, day).strftime("%A")

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def age(birth_day, birth_month, birth_year):
    today = datetime.date.today()
    return today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

def display_birth_date(day, month, year):
    return f"{day:02d} {month:02d} {year}"

# Ввод данных от пользователя
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

print(f"День недели: {day_of_week(day, month, year)}")
print(f"Високосный год: {'Да' if is_leap_year(year) else 'Нет'}")
print(f"Возраст: {age(day, month, year)} лет")
print(f"Дата рождения: {display_birth_date(day, month, year)}")
