import random

password = ""

alphLo = "abcdefghijklmnopqrstuvwxyz"
alphUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

specialSyn = "!@#$%^&*()-_=+[]{}|;:"


print("Select password level: ")


level = int(input("Pick level 1 - 20: "))


for _ in range(level):

    password += random.choice(alphLo)
    password += random.choice(alphUp)
    password += random.choice(specialSyn)

print(password)