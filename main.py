# Password Generator Project
import random
import support
letters= support.letters
numbers= support.numbers
symbols=support.symbols


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''
for i in range(1, nr_letters + 1):
    i = random.choice(letters)
    password += i
for l in range(1, nr_symbols + 1):
    l = random.choice(symbols)
    password += l
for t in range(1, nr_numbers + 1):
    t = random.choice(numbers)
    password += t
print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for i in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for l in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

for t in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)
print(password)
New_password = ''
for i in password:
    New_password += i
print("Your new password is : ", New_password)
