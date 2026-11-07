
import requests
import sys
import json

myKey = "98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

myFile = r"C:\Users\root\Documents\jsonfile.json"

bitcoinPrice = []

try:

    if len(sys.argv) == 1:
        print("missing command-line argument")
        sys.exit()

    elif (sys.argv[1].isalpha()):
        print("command line argument is not a number")
        sys.exit()

    amount = float(sys.argv[1])

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="

    urlReal = "https://rest.coincap.io/v3/assets?search=bitcoin&apiKey=98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

    r = requests.get(urlReal, amount)

    myJson = r.json()

    for m in myJson["data"]:
        dataName = (m["name"])
        dataPrice = m["priceUsd"]

        bitcoinPrice.append(dataPrice)

        # print(dataName +":" +" "+ dataPrice)

    bitcoinP = bitcoinPrice[0]

    bitcoinAmount = float(bitcoinP) * amount

    bitcoinFraction = f"{bitcoinAmount:,.4f}"

    print("$" + bitcoinFraction)

except:
    pass
