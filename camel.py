
getName = input("camelCase: ")


if getName.title():
    for n in getName:
        getSmall = n.lower()
        if n in n.upper():

            getReplace = n.replace(n, "_")
            # adWords = getSmall.join(getReplace)

             #.join(getReplace)
            print(getReplace)
        print(getSmall)
        # print(adWords)
            
    
    mysplit = getName.split()
    print("snake_case:", getSmall)
    #print("snake_case:", getName)
    print(mysplit)


