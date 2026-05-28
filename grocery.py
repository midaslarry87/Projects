
groceries = ""

print(type(groceries))

while True:

    user_input = input()

    if user_input  == "":
        break

    try:

        # prompt = input()

        if user_input != "":

            groceries += user_input

        print(groceries)

    except ValueError:
        pass

    except TypeError:
        pass