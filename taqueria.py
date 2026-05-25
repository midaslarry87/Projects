
menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
       }


pay = input("Item: ").title()

for m in menu.items():
    #print(m)
    if pay in m:
        print(menu.get(pay)) 
    # print(m)

# while True:

#     pay = input("Item: ").title()


#     for m in menu:
#         print(m)





