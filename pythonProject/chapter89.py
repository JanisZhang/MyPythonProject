# def greet_user(username):
#     print(f'hello {username}')
#
# name = input('What is your name?\n')
# greet_user(name)

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet("dog", "lucky")

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet( pet_name="lucky",animal_type="dog")

# def describe_pet(animal_type, pet_name='xiao gou'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet( pet_name="lucky",animal_type="dog")
# describe_pet( animal_type="dog")

# def get_formatted_name(first_name, last_name):
#     fullname = f'{first_name} {last_name}'
#     return fullname.title()
#
# formatted_name = get_formatted_name('janis', 'zhang')
# print(formatted_name)


# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f'{first_name} {last_name} {middle_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
# formatted_name = get_formatted_name('janis', 'zhang','wang')
# print(formatted_name)
# formatted_name = get_formatted_name('janis', 'zhang')
# print(formatted_name)

# def build_person(first_name, last_name):
#     person = {'first_name': first_name, 'last_name': last_name}
#     return person
#
# musician = build_person('John', 'Doe')
# print(musician)

# def build_person(first_name, last_name, age=None):
#
#     person = {'first_name': first_name, 'last_name': last_name}
#     if age is not None:
#         person['age'] = age
#     return person
# person = build_person('John', 'Smith')
# print(person)
# person = build_person('John', 'Smith', age=25)
# print(person)

# def greet_users(names):
#     for name in names:
#         print(f'Hello {name}')
#
# greet_users(['John', 'Doe', 'Janis'])

# def make_pizza(size, *toppings):
#     print('making a pizza with the following toppings:')
#     print(f'The size is {size}')
#     for topping in toppings:
#         print(topping)
#
# make_pizza(20,'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
# user_profile = build_profile('albert', 'einstein', location='San Francisco')
# print(user_profile)

