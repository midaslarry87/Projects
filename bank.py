
Greetings = input("Greeting: ").lower().strip()

take = Greetings.replace(",","").split()

print(take[0])

# newGreets = Greetings.removeprefix()

# print(newGreets)
# print(Greetings)

if Greetings == "hello":
    print("$0")


elif Greetings[0].startswith("h") and Greetings != "hello":

    print("$20")


else:
    print("$100")
 
# if Greetings.startswith("hey"):
#     print("$20")


# match Greetings:
#     case "hello" | "Hello":
#         print("$0")






