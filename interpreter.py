
def ConvString():
    getCal = input("Expression: ")

    expression = eval(getCal)

    print(f"{expression:.1f}")

ConvString()
