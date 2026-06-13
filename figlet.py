import sys
import pyfiglet

print(len(sys.argv))

if len(sys.argv) == 2:
    print("Invalid usage")

    sys.exit

stats = input("Input: ")


print("Output: ", "\n" + pyfiglet.figlet_format(stats))

# pyfiglet.figlet_format()