# print('Hello Python world')
# message = 'Hello Python world'
# print(message)
# message = message.upper()
# print(message)

# name = 'janis zhang'
# print(name.title())

# firstname = 'janis'
# lastname = 'zhang'
# fullname = f'{firstname} {lastname}'
# print(fullname)
# greeting = f'Hello,Miss {lastname.title()}'
# print(greeting)

# print('\tHello \nWorld!')

# message = '  tes tA BCD'
# print(message.rstrip())
# print(message.lstrip())
# print(message.strip())

# nostarch_url = 'https://nostarch.com'
# print(nostarch_url.removeprefix('https://'))
# print(nostarch_url.removesuffix('.com'))
# message = 'python_notes.txt'
# print(message.removesuffix('.txt'))

# print(0.2+0.1)
# print(0.2+0.2)
# print(4/2)
# print(1+2.0)
# print(2*3.0)

# universe_age = 14_000_000_000_000
# print(universe_age)

# x,y,z = 34,11,33
# print(x)

# MAX_CONNECTIONS = 5000
# print(MAX_CONNECTIONS)
# MAX_CONNECTIONS = 99
# print(MAX_CONNECTIONS)

"""
test
"""

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[-1])
# print(bicycles)
# print(bicycles[0])
# print(bicycles[-1])
# print(len(bicycles))
# print(bicycles[0:2])
# print(bicycles[2:4])
# print(bicycles[2:])
# print(bicycles[::2])
# print(bicycles[::-1])
# print(bicycles[0].title())

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(f'My first bicycle was a {bicycles[0].title()}')

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles = []
# motorcycles.append('ducati')
# motorcycles.append('honda')
# motorcycles.append('jackal')
# print(motorcycles)
#
# motorcycles.insert(1, 'suzuki')
# print(motorcycles)
#
# del motorcycles[0]
# print(motorcycles)
# motorcycles.pop()
# # motorcycles.pop(1)
# print(motorcycles)
# motorcycles.remove('honda')
# print(motorcycles)

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# for bicycle in bicycles:
#     if len(bicycles) >1:
#         print(bicycle)
#         print('Too many bicycles')
#         bicycles.remove(bicycle)
# print(bicycles)

# cars = ['bmw', 'toyota', 'audi', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars))
# print(cars)
# print(sorted(cars, reverse=True))
# cars = ['bmw', 'toyota', 'audi', 'subaru']
# cars.reverse()
# print(cars)

# for value in range(1,5):
#     print(value)

# numbers = list(range(1,11))
# print(numbers)
# numbers = list (range(2,11,2))
# print(numbers)

# squares = []
# for number in range(1, 11):
#     square = number ** 2
#     squares.append(square)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# squares = [value**2 for value in range(1,11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# # 输出名单上最后三名队员的名字
# print(players[-3:])
# for player in players[:3]:
#     print(player.title())

# my_food = ['apple', 'banana', 'cherry']
# friend_foods = my_food[:]
# print(friend_foods)
# friend_foods = my_food[-2:]
# friend_foods.append('carrot')
# print(friend_foods)

# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])
#
# dimensions[0] = 250

# # 遍历
# for value in dimensions:
#     print(value)
#
# dimensions = (40, 50)
# print(dimensions[0])

# cars = ['bmw', 'subaru', 'toyota']
#
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'audi'
# print(car == 'Audi')
# print(car.upper() == 'Audi'.upper())

# age_0 = 22
# age_1 = 8
# print( age_0 > 10 and age_0 < 20)

# requested_toppings = ['mushrooms', 'extra cheese', 'onions']
# print('test' in requested_toppings)
# print('test' not in requested_toppings)
#
# requested_toppings = ['mushrooms', 'extra cheese', 'onions']
# print('mushrooms' in requested_toppings)

# can_edit = False
# print(can_edit)
#
# car = 'subaru'
# print('I predict True')
# print(car == 'subaru')
#
# print(car == 'audi')
# print('I predict False')

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#    price = 100
# else:
#     price = 200
# print(price)

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# requested_toppings = []
#
# if requested_toppings:
#     for item in requested_toppings:
#         if item == 'green peppers':
#             print("sorry,we don't have green peppers")
# else:
#     print("plain pizza")

# list = [value for value in range(1, 10)]
#
# if list:
#    for value in list:
#         if value == 1:
#             result = str(value) + 'st'
#         elif value == 2:
#             result = str(value) + 'nd'
#         elif value == 3:
#             result = str(value) + 'rd'
#         else:
#             result = str(value) + 'th'
#         print(result)

# alien_0 = {'color': 'blue', 'weight': 100}
# print(alien_0['color'])
# print(alien_0['weight'])
# alien_0 = {}
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")
# print(alien_0)
# del alien_0['x_position']
# print(alien_0)

# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['point'])
#
# print(alien_0.get('point', 'No this value'))


# user_0 = {
# 	'username':'efermi',
# 	'first':'enrico',
# 	'last':'fermi'
# }

# for key,value in user_0.items():
# 	print(f'key is {key}')
# 	print(f'value is {value}')

# for key in user_0.keys():
# 	print(key.title())

# favorite_language = {
# 	'Test1':'Japanese',
# 	'Test2':'Chinese',
# 	'phil':'English'
# }
# friends = ['phil', 'sarah']

# for name in favorite_language.keys():
# 	print(f'Hi {name.title()}')

# 	if name in friends:
# 		language = favorite_language[name].title()
# 		print(f'Nice to meet you, {name}!, I see you love {language}')

# 	if name not in friends:
# 		print(f'{name} not my friends.')

# favorite_language = {
# 	'jen':'python',
# 	'sarah':'c',
# 	'edward':'rust',
# 	'phil':'pyhton'
# }

# for name in sorted(favorite_language.keys()):
# 	print(f'{name.title()}, thank you for taking the poll.')

# for value in sorted(favorite_language.values()):
# 	print(f'{value}')

# favorite_language = {
# 	'jen':'python',
# 	'sara':'c',
# 	'edward':'rust',
# 	'phil':'python',
# 	'sarah':'c',
# }

# for language in set(favorite_language.values()):
# 	print(language.title())

# sara_favorite_language = {'java','rust','c'}
# favorite_language = {
# 	'jen':'python',
# 	'sara':sara_favorite_language,
# 	'edward':'rust',
# 	'phil':'python',
# 	'sarah':'c',
# }

# # find sara's favorite language
# for name in favorite_language.keys():
# 	if name == 'sara':
# 		print(favorite_language[name])

# aliens = []

# for alien_number in range(30):
# 	new_ailen = {'color':'green','points':5,'speed':'slow'}
# 	aliens.append(new_ailen)

# for alien in aliens[:5]:
# 	print(alien)

# print(f'Total number of ailens: {len(aliens)}')

# # 修改外星人

# for alien in aliens[:3]:
# 	if alien['color'] == 'green':
# 		alien['color'] = 'yellow'
# 		alien['speed'] = 'fast'
# 		alien['points'] = 10

# for alien in aliens[:5]:
# 	print(alien)

# pizza = {
# 	'crust':'thick',
# 	'toppings':['mushrooms','extra cheese']
# }

# print(f"You ordered a {pizza['crust']} -crust pizza")

# for topping in pizza['toppings']:
# 	print(f'\t{topping}')

# favorite_language = {
# 	'jen':['python','rust'],
# 	'sara':['rust','go'],
# 	'phil':['python','haskell'],
# 	'sarah':['c'],
# }


# for name,languages in favorite_language.items():
# 	if len(languages) >1:
# 		print(f"{name.title()}'s favorite languages are:")
# 	else:
# 		print(f"{name.title()}'s favorite languages is:")

# 	for language in languages:
# 		print(f'\t{language.title()}')

# message = input("tell me something, i'll print it\n")
# print(message)

# prompt = "What's your name?\n"
# message = input(prompt)
# print(f'Hello, {message}')

# prompt = "What's your age?\n"
# age = input(prompt)

# if int(age) > 18:
# 	print('teenager')
# else: 
# 	print('child')


# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# 	current_number+=1


# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []

# while unconfirmed_users:
# 	current_user = unconfirmed_users.pop()

# 	print(f"Verifying user: {current_user.title()}")
# 	confirmed_users.append(current_user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())


# pets = ["cat", "dog", "mouse", "rabbit", "cat"]
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)


















