import random

print("Select password level: ")


level = input("Pick level 1 - 20: ")

alphLo = "abcdefghijklmnopqrstuvwxyz"
alphUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

specialSyn = "!@#$%^&*()-_=+[]\{}|;:"

for _ in range(level):
    password = random.random(alphLo)