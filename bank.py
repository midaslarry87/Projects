
Greetings = input("Greeting: ")


if Greetings.startswith("hey"):
    print("$20")

else:
    print("$100")

match Greetings:
    case "hello" | "Hello":
        print("$0")






