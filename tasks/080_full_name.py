user_name = input("Enter your name, please: ")
print(len(user_name))
user_surname = input("Enter your surname, please: ")
print(len(user_surname))
full_name = (f"{user_name} {user_surname}")
print(f"{full_name}\n{len(full_name)}")