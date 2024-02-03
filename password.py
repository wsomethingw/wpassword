from random import randint

choice = int(input("Введите длину пароля: "))
choice_num_chr = input("Делать ли фильтрацию по цифрам? (y/n): ")

if choice_num_chr.lower() == "y":
    choice_num_chr = True
elif choice_num_chr.lower() == "n":
    choice_num_chr = False
else:
    print("You must only enter y or n")
    exit()

password = ""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "0123456789"

if choice_num_chr:
    chars += nums

if choice <= 0:
    print("Длина пароля должна быть больше 0")
    exit()

for _ in range(choice):
    password += chars[randint(0, len(chars) - 1)]

print(password)
