from name_function import get_formatted_name

print("Enter 'q' to quit")
while True:
    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == "q":
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"Your name is {formatted_name}")