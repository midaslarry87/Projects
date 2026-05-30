
groceries = []

my_dic = {}

while True:

    user_input = input().upper()

    if user_input  == "":
        break

    try:

        if user_input != "":

            groceries.append(user_input)

    except ValueError:
        pass

    except TypeError:
        pass

# This is getting the information to be converted to dictionary 

for g in groceries:
   
    result = groceries.count(g)

    my_dic[g] = result

print(my_dic)

# This is for unpacking the dictionary 

for k, v in my_dic.items():
    print(v, k)

