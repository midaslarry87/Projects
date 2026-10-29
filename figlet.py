import pyfiglet
import sys

req = input("Input: ")

print(len(sys.argv))

if len(sys.argv) <= 2:
    output = pyfiglet.figlet_format(req)

    print("Output:" "\n" + output)

elif len(sys.argv) > 2 and (sys.argv[1]) == "-f" or (sys.argv[1]) == "--font":
    output = pyfiglet.figlet_format(req, font=sys.argv[2])

    print("Output: " + "\n" + output)

# elif len(sys.argv) > 2 and (sys.argv[1]) == (sys.argv[1]):
#     output = pyfiglet.figlet_format(req, font=sys.argv[2])

#     print(output)

elif len(sys.argv) > 1 and (sys.argv[1]) != "-f" or (sys.argv[1]) != "--font":
    print("I am exiting")
    sys.exit()

# else:
#     sys.exit
# print(m)

# print((sys.argv[1]))