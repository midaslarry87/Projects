
amount = 50

print("Amount Due:", amount)

payment = int()


account = 0

while True:

    pay = int(input("Insert Coin: "))

    account += pay


    if account < amount:
        balance = amount - account 
        print("Amount Due: ", balance)



    elif account == amount:
        balance = amount - account
        print("change Owed: ", balance)

        break

    elif account > amount:
        balance = account - amount
        print("Change Owed: ", balance)
        
        break

  