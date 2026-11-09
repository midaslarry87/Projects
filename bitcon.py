import requests
import sys
import json

myKey = "98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

myFile = r"C:\Users\root\Documents\jsonfile.json"

bitcoinPrice = []

try:

    # bitcoinPrice = []
    # check for the command line argument
    if len(sys.argv) == 1:
        print("missing command-line argument")
        sys.exit()

    # check if the command argument is string after the program name
    elif (sys.argv[1].isalpha()):
        print("command-line argument is not a number")
        sys.exit()

    # Change the command arguemnt after the name of the program to be float
    amount = float(sys.argv[1])

    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="

    # assign the URL + APIkey to the variable
    urlReal = "https://rest.coincap.io/v3/assets?search=bitcoin&apiKey=98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

    # use request to get the https response of the webpage
    r = requests.get(urlReal, amount)

    # create the myJson variable to store the jSON from the URL
    myJson = r.json()

    # Create a for loop to iterate on the JSON data to get the name and price
    for m in myJson["data"]:
        # Get the value of the key information from the jSON
        dataName = (m["name"])
        dataPrice = m["priceUsd"]

        # append all the price to the list
        bitcoinPrice.append(dataPrice)

        # print(dataName +":" +" "+ dataPrice)

    # assign the list to a string for the first item in the list
    bitcoinP = bitcoinPrice[0]

    # change the string to float and multiply it and assign to a variable bitcoinAmount
    bitcoinAmount = float(bitcoinP) * amount

    # use the format method to create/use for thousand number , and 4 digit after the .dot
    bitcoinFraction = f"{bitcoinAmount:,.4f}"

    # print the total amount of the bitcoin price
    print("$" + bitcoinFraction)


except requests.RequestException:
    pass
