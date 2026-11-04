# will continue tomorrow. I am very tired right now solve 3 problems today.

import requests
import sys
import json

myKey = "98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

try:

    if len(sys.argv) == 1:
        print("missing command-line argument")
        sys.exit()
        # print("missing command-line argument")


    elif (sys.argv[1].isalpha()):
        print(type(sys.argv[1]))
        print("command line argument is not a number")
        sys.exit()

    amount = int(sys.argv[1])

    # url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey="

    urlReal = "https://rest.coincap.io/v3/assets?search=bitcoin&apiKey=98e1d73a3b8b520cd33679211e062c9089e1801a9c722d05c15b1b91d7f01739"

    r = requests.get(urlReal, amount)


    # print(json.dumps(r.json, indent=2))
    # jdumps = json.dumps(r.json(), indent=2)
    # print(jdumps)

    print(r.status_code)

    myJson = r.json()

    for m in myJson["data"]:
        # print
        dataName = (m["name"])
        dataPrice = m["priceUsd"]
        # dataPrice = m["priceUsd"]

        print(dataName + " " + dataPrice)

    # if r.status_code == "200":
    #     for b in jdumps["data"][]:
    #         pass


except:
    pass

# print(r.json())

# print(len(sys.argv))
# print(sys.argv[1])