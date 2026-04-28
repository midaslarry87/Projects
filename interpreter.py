
# def ConvString():
#     getCal = input("Expression: ")

#     expression = eval(getCal)

#     print(f"{expression:.1f}")

# ConvString()


# My own way of solving this issue 

def getValue ():
    acceptString = input("Expression: ")

    stringSlice = acceptString.split()

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

    print(f"{getCal:.1f}")

getValue()