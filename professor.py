import random

print("Please Enter a level between 1-4: ")
level = int(input("Level: "))

score = 0
count = 0

while True:

    try:

        x = random.randint(1, 10)
        y = random.randint(1, 10)

        #print(x, y)

        print(x, "+", y, "= ", end="")

        total = int(input())

        #print(type(total))

        result = (x + y)
        #print(type(result))

        print(total, result)

        if total == result:
            score += 1
            continue
        elif total != result:
            count += 1
            print("EEE")
            print(count)
            if count > 2:
                print("Score: ", score)
                break

        else:
            pass

        # I need to fix the issue when using string
        # I need to solve the issue when user answer the question 3 times wrong and the answer
        # should be given
        # and then move on to another question. Answer the remaining questions correctly. Your program should output a score of 9.

        # Run your program with python professor.py. Type 1 and press Enter. Answer all 10 questions correctly. Your program should output a score of 10.

    except:
        pass