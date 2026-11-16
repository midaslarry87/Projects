# Import the Random model
import random

# Create a empty string variable as a hold place password and final password
password = ""
fPassword = ""

# Create the string characters
alphLo = "abcdefghijklmnopqrstuvwxyz"
alphUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "0123456789"
specialSyn = "!@#$%^&*()-_=+[]{}|;:"

# Print out the password level
print("Select password level: ")

# Input a level and change it from string to Integer
level = int(input("Pick level 1 - 20: "))

# Loop through the number of level to generate the password characters
for _ in range(level):

    password += random.choice(alphLo)
    password += random.choice(alphUp)
    password += random.choice(specialSyn)
    password += random.choice(numb)

# Random choice the password characters
    fPassword += random.choice(password)

# print(password)
# Print out the final password strings (Characters)
print(fPassword)