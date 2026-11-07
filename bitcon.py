# will continue tomorrow. I am very tired right now solve 3 problems today.

import requests
import sys
import json

myKey = "98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

myFile = r"C:\Users\root\Documents\jsonfile.json"

bitcoinPrice = []

try:

    # bitcoinPrice = []

    if len(sys.argv) == 1:
        print("missing command-line argument")
        sys.exit()
        # print("missing command-line argument")


    elif (sys.argv[1].isalpha()):
        # print(type(sys.argv[1]))
        print("command line argument is not a number")
        sys.exit()

    amount = float(sys.argv[1])

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="

    urlReal = "https://rest.coincap.io/v3/assets?search=bitcoin&apiKey=98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

    r = requests.get(urlReal, amount)

    # jdumps = json.dumps(r.json(), indent=2)
    # for check in jdumps["data"][0]["name"]:
    #     dataName = check["name"]

    # jLoads = json.loads(r.json())

    # print(jLoads)

    myJson = r.json()

    for m in myJson["data"]:
        # print
        dataName = (m["name"])
        dataPrice = m["priceUsd"]

        bitcoinPrice.append(dataPrice)

        # print(dataName +":" +" "+ dataPrice)

    print("did I get here")

    print("Here is from the list: " + bitcoinPrice[0])

    print(type(bitcoinPrice))

    # bitcoinAmount = bitcoinPrice[0] * amount

    bitcoinP = bitcoinPrice[0]

    bitcoinAmount = float(bitcoinP) * amount

    bitcoionFraction = f"{bitcoinAmount:,.4f}"

    # print(type(bitcoinP))

    print(bitcoionFraction)

    # for w in len(bitcoinPrice):
    #     if
    #     print("This is from the w:" + w)
    #     bitcoinAmount = float(w) * amount

    #     bitFraction = f"{bitcoinAmount:,.4f}"

    #     print("bitcoinCost: " + bitFraction)

    # bitcoinAmount = bitcoinPrice[0] * amount

    # print(type(bitcoinAmount))

    # print(bitcoinAmount)

    # print(type(amount))
    # print(amount)

    # here is addition way to solving the digit number after decimal with commas

    # bitFraction = f"{bitcoinAmount:,.4f}"

    # print("bitcoinCost: " + bitFraction)

    # print(r.status_code)


except:
    pass
