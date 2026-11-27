import sys
import os

directory = r"C:\Users\HafeezTukuru\Downloads\Projects"

#print(os.path.dirname(os.path.abspath(directory)))

#fileName = (sys.argv[1])
#print(sys.argv[0])

#print(type(sys.argv[1]))

#print(os.path.isdir(directory))

#print(os.path.abspath(directory))

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
counter = 0

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

file1 = sys.argv[1]

if len(sys.argv) == 2 and not file1.endswith(".py"):
    sys.exit("Not a python file")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

for check in d:
    #print(check)
    if sys.argv[1] == check:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            print(type(lines))
            print(lines)
            for line in lines:
                #ln = line.strip().split(",")
                #if l
                print(line)
                counter += 1
            #print(ln)
        break

for sCheck in d:
    if sys.argv[1] not in check:
        sys.exit("file does not exist")







