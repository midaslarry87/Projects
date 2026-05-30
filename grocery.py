
groceries = []

items = {}

goods = ()

print(type(groceries))

while True:

    user_input = input()

    if user_input  == "":
        break

    try:

        # prompt = input()

        if user_input != "":

            groceries.append(user_input)

    except ValueError:
        pass

    except TypeError:
        pass


for g in groceries:
    # result = goods.count(groceries)
    result = groceries.count(g)

    # items[result] = g

    items[g] = result

    print(result)
    print(g)

    print(items)