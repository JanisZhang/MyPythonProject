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

from random import randint

print(randint(1,6))