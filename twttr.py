

strVowels = "A, E, I O, U"


myString = input("Input: ")


newWords = ""

for i in myString:
    
    if i not in strVowels.lower():
       
        newWords += i

print("Output:", newWords)

