# Accept input from the user and make the case insensitive and remove any left, right whitespaces 
Greetings = input("Greeting: ").lower().strip()

# Remove or omit any comma and replace it with no whitespace and split the input into list.
take = Greetings.replace(",","").split()

# check the input if the word is hello 
if take[0] == "hello":
    print("$0")

# check if the beginning of the word start with h and not hello
elif take[0].startswith("h") and take[0] != "hello":

    print("$20")

# print $100 if no word matches hello or start with a word with "h"
else:
    print("$100")

