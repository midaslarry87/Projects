import sys
import os

directory = r"C:\Users\root\Documents\MyProjects\cs50"


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

file1 = sys.argv[1]

if len(sys.argv) == 2 and not file1.endswith(".py"):
    sys.exit("Not a python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

print(os.path.dirname(os.path.abspath(__file__)))




