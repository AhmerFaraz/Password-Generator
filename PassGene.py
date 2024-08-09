import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spe_symbols = ['!', '#', '$', '%', '&', '*', '_', '+']

print("Welcome to the password generator !!!")

r_alpha = int(input("How many alphabets you want in your password:- \n"))
r_number = int(input("How many numbers you want in your password:- \n"))
r_special_symbol = int(input("How many special characters you want in your password:- \n"))

password_list = []

for x in range(r_alpha):
    random_alpha = random.randint(0, 51)
    a = alphabets[random_alpha]
    password_list.append(a)

for x in range(r_number):
    random_number = random.randint(0, 9)
    a = numbers[random_number]
    password_list.append(a)

for x in range(r_special_symbol):
    random_special = random.randint(0, 7)
    a = spe_symbols[random_special]
    password_list.append(a)

random.shuffle(password_list)

password = ""
for x in password_list:
    password += x

print(f"The Password is:- {password}")