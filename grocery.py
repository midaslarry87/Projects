
groceries = []

my_dic = {}

# goods = ()

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

# This is getting the information to be converted to dictionary 

for g in groceries:
    # result = goods.count(groceries)
    result = groceries.count(g)

    # items[result] = g

    my_dic[g] = result

    # print(result)
    # print(g)

print(my_dic)

# This is for unpacking the dictionary 

for k, v in my_dic.items():
    print(v, k)

