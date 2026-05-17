

strVowels = "A, E, I O, U"


myString = input("Input: ")


newWords = ""

for i in myString:
    # print(i)
    if i not in strVowels.lower():
        # print(i)
        #i.replace(i, "")
        #newWords += i.replace(i, "")
        newWords += i

print("Output:", newWords)

