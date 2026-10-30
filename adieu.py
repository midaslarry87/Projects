
myString = "Adiue, adieu, to "

nameList = []

lastWord =""

while True:

    try:
        names = input("Name: ")
        nameList.append(names)


    except EOFError:
        break

for n in nameList:
    print(n)
    if n in nameList[-1]:
        lastWord += n
    myString += n + " "


print(nameList)
print(myString + "and " + lastWord)