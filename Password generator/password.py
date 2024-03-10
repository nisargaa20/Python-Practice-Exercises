import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','$','#','^','%','&','*']

n_letters = int(input("How many letters do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))

password_list = []

for _ in range(n_letters):
    char = random.choice(letters)
    password_list.append(char)

for _ in range(n_symbols):
    char = random.choice(symbols)
    password_list.append(char)

for _ in range(n_numbers):
    char = random.choice(numbers)
    password_list.append(char)

random.shuffle(password_list)

password = "".join(password_list)
print(password)
