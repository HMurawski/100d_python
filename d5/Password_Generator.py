import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


print(f"Welcome to the Password Generator")

int_letters = int(input(f"How many letter would you like to have in your password ? "))
int_symbols = int(input(f"How many symbols would you like to have in your password ? "))
int_numbers = int(input(f"How many numbers would you like to have in your password ? "))

password = ""

for l in range(int_letters):
    password += random.choice(letters)

for s in range(int_symbols):
    password += random.choice(symbols)

for n in range(int_numbers): 
    password += random.choice(numbers)


#mixing up the password

password_list = list(password)

random.shuffle(password_list)

password = "".join(password_list)

print(f"Your generated password is: {password}")