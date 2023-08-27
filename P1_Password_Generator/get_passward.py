import random 

print("welcome to MyPassword generator! ")

num_letters = int(input("How many letters you want in your Password?\n"))

num_symbols = int(input("How many symbols would you like?\n"))

num_numbers = int(input("How many numbers would you like\n"))

letters = ['a','b','c','d','e','f','A','B','C','D','E','F']

symbols = ['!','@','#','$','%','^','&','*','(',')']

numbers = ['1','2','3','4','5','6','7','8','9','0']

my_password = ''

for lett in range(num_letters):
    select_letter = random.choice(letters)
    my_password = my_password + select_letter

# print(f"your password is : {my_password}")

for sym in range(num_symbols):
    select_symbol = random.choice(symbols)
    my_password = my_password + select_symbol

# print(f"your password is : {my_password}")

for num in range(num_numbers):
    select_number = random.choice(numbers)
    my_password = my_password + select_number

print(f"your password is : {my_password}")

