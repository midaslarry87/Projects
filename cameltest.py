# getName = input("camelCase: ")

# if getName.title():
        
#         for n in getName:
#             getSmall = n.lower()
            
#             if n in n.upper():

#                 getReplace = n.replace(n, "_")
#                 # adWords = getSmall.join(getReplace)

#                 print(getReplace)
#             ansW = getSmall
#             print(ansW)
#         print("snake_case: ", ansW)
            

# print("snake_case:", ansW)

stringWDash = ""
stringNoDash = ""
stringLower = ""

enterCamelCase = input("camelCase: ")

for word in enterCamelCase:
    if word in enterCamelCase.upper():
        repL = word.replace(word, "_")
        print(repL)
        stringLower += word.lower()
        stringWDash += repL
        


for n in enterCamelCase:
    if n in enterCamelCase.lower():
        stringNoDash += n 




print(stringWDash)
print(stringLower)
print(stringNoDash)

print(stringLower,stringWDash, stringNoDash)
print(stringNoDash+stringWDash+stringLower)