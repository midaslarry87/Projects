import random

password = ""
fPassword = ""

alphLo = "abcdefghijklmnopqrstuvwxyz"
alphUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "0123456789"

specialSyn = "!@#$%^&*()-_=+[]{}|;:"

print("Select password level: ")

level = int(input("Pick level 1 - 20: "))

for _ in range(level):

    password += random.choice(alphLo)
    password += random.choice(alphUp)
    password += random.choice(specialSyn)
    password += random.choice(numb)

    fPassword += random.choice(password)

print(password)

print(fPassword)