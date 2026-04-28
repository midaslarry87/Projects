
# def ConvString():
#     getCal = input("Expression: ")

#     expression = eval(getCal)

#     print(f"{expression:.1f}")

# ConvString()


# My way of solving this issue 

def getValue ():
    acceptString = input("Expression: ")

    stringSlice = acceptString.strip().split()

    print(stringSlice)

    f = float(stringSlice[0])
    g = stringSlice[1]
    h = float(stringSlice[2])

    print(f, g, h)

    if g == '+':
        getCal = f + h
    elif g == '-':
        getCal = f - h

    elif g == '*':
        getCal = f * h

    elif g == '/':
        getCal = f / h 

    # getCal = f"{f + {g} + h}"

    print(type(getCal))

    print(getCal)

getValue()