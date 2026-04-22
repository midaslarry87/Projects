
def main():

    print(cal)

def cal (x, y, z):

    calc = input("Expression: " )
    valid = calc(int(x), y, int(z))

    return valid 

main(cal)