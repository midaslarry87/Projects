myString = "Adiue, adieu, to "

nameList = []

lastWord = ""

while True:

    try:
        names = input("Name: ")
        nameList.append(names)


    except EOFError:
        break

if len(nameList) > 2:
    print(len(nameList))

    lastWord += nameList[-1]

    for n in nameList[:-1]:
        print(n)
        myString += n + "," + " "

    print(myString + "and " + lastWord)

elif len(nameList) > 1:

    if nameList[-1] == nameList[-1]:
        lastWord += nameList[-1]

    for n in nameList[:-1]:
        myString += n + " "

    print(myString + "and" + " " + lastWord)

elif len(nameList) == 1:
    print(len(nameList))
    oneWord = "".join(nameList)
    print(myString + oneWord)
