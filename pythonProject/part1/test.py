# class Dog:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f'{self.name} is now sitting.')
#
#     def roll_over(self):
#         print(f'{self.name} rolled over!')
#
# my_dog = Dog('Lucky', 3)
#
# my_dog.sit()
# my_dog.roll_over()
# print(my_dog.age)

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         long_name = f"{self.make} {self.model} {self.year}"
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f'This car has {self.odometer_reading} miles on it.')
#
#     def update_odometer(self, mileage):
#         if mileage > self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("you can't roll back an odometer")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
#
# my_new_car.update_odometer(10)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometer(99)
# my_new_car.read_odometer()

# from random import randint
#
# print(randint(1,6))
#
# from random import choice
#
# players = ['carles','michael','florence','eli']
# first = choice(players)
# second = choice(players)
# print(first)
# print(second)


# from pathlib import Path

# path = Path('resources/pi_digits.txt')
# content = path.read_text()
# lines = content.splitlines()
# pi_string = ''
#
# for line in lines:
#     pi_string += line.lstrip()
#
# print(pi_string)
# print(len(pi_string))


# for line in lines:
#     if '323846' in line:
#         print(line)

# print(content)
# print('----')
# print(content.rstrip())

# path = Path('resources/pi_digits.txt')
# content = 'hello world.\n'
# content += 'This is the first line.\n'
# content += 'This is the second line.\n'
# path.write_text( content)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# print("Give me two numbers, and I'll divide them.\n")
# print("Enter 'q' to exit\n")
# while True:
#     first_number = input("first_number:")
#     second_number = input("second_number:")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)

# from pathlib import Path
#
# def count_words(filepath):
#     path = Path(filepath)
#     content = path.read_text()
#     return len(content.split())
#
# print(count_words('resources/pi_digits.txt'))

# from pathlib import Path
# import json
#
# numbers = [2,3,5,7,9,11,13,15,17,19,23]
# contents = json.dumps(numbers)
# path = Path('resources/numbers.json')
# path.write_text(contents)
#
# path = Path('resources/numbers.json')
# contents = path.read_text()
# print(json.loads(contents))

