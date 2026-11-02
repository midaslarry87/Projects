import random

print("Guess number between 1 to 100...")

count = random.randint(1, 100)

print(count)

while True:

    try:
        level = int(input("Level: "))
        break

    except:
        pass

        # break

while True:

    # level = int(input("Level: "))

    try:

        # level = int(input("Level: "))

        guessNumber = int(input("Guess: "))

        if guessNumber > count:
            print("Too Large!")

        elif guessNumber < count:
            print("Too small!")

        else:
            print("Just right!")
            break

        # print(type(guessNumber))
        # break

    except ValueError:
        pass


