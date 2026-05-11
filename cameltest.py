#### METHOD 1 ####

# myString = ""

# getName = input("camelCase: ")

# if getName.title():
        
#         for n in getName:
#             getSmall = n.lower()
            
#             if n in n.upper():

#                 getReplace = n.replace(n, "_")
               
#                 myString += getReplace
#                 # print(getReplace)
#             myString += getSmall
            

# print("snake_case: " + myString)

#### METHOD 2 ####

stringWDash = ""
stringNoDash = ""
stringLower = ""

enterCamelCase = input("camelCase: ")

for n in enterCamelCase:
    if n in enterCamelCase.lower():
        stringNoDash += n 
        stringWDash = stringNoDash


for word in enterCamelCase:
    if word in enterCamelCase.upper():
        repL = word.replace(word, "_")
        print(repL)
        stringLower += word.lower()
        stringWDash += repL
        





# for 

print(stringWDash)
print(stringLower)
print(stringNoDash)

print("snake_case: " + stringNoDash)