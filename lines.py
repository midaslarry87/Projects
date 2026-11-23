import sys
import os

directory = r"C:\Users\root\Documents\MyProjects\cs50"

print(os.path.dirname(os.path.abspath(directory)))

#fileName = (sys.argv[1])
#print(sys.argv[0])

#print(type(sys.argv[1]))

#print(os.path.isdir(directory))

print(os.path.abspath(directory))

d = os.listdir(directory)

# for check in d:
#     if check == fileName:
#         pass
#     else:
#         sys.exit("File does not exist")

    #print(check)
    # if check not in sys.argv[1]:
    #     sys.exit("File does not exist")


#print(d)

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

file1 = sys.argv[1]

if len(sys.argv) == 2 and not file1.endswith(".py"):
    sys.exit("Not a python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

for check in d:
    print(check)
    # if check is file1:
    #     pass
    # else:
    #     sys.exit("File does not exist")







