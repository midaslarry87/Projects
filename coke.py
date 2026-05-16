
amount = 50

print("Amount Due:", amount)

payment = int()

# print("This is the payment outside the loop: ", payment)

account = 0

while True:

    pay = int(input("Insert Coin: "))

    account += pay

    #print(account)

    if account < amount:
        balance = amount - account 
        print("Amount Due: ", balance)


    elif account == amount:
        balance = amount - account
        print("change Owed: ", balance)

        break

    else:
        
        break

  