import sys

directory = r"C:\Users\root\Documents\MyProjects\cs50"

# print(sys.argv[1])
# print(sys.argv[0])

# print(type(sys.argv[1]))

file1 = sys.argv[1]

# if not file1.endswith(".py"):
#     sys.exit("")


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 2 and not file1.endswith(".py"):
    sys.exit("Not a python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")




