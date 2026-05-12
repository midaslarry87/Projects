

def main():

    global getName

    getName = input("camelCase: ")

    print("I got here")
def camelCase(main):
    print("I am here")

    if getName.title():
        for n in getName:
            getSmall = n.lower()
            
            if n in n.upper():

                getReplace = n.replace(n, "_")
                # adWords = getSmall.join(getReplace)

                #.join(getReplace)
                return getReplace
                # print(getReplace)
            #print(getSmall)
            
        return getSmall
    print("snake_case:", getSmall)
    #print("snake_case:", getName)
    print("Hi")
# main()

main()

