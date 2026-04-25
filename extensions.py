
imageFile = "gif", "jpg", "png", "jpeg"
applicationFile = "pdf", "zip"
textFile = "txt"

newfileName = ""

#fileName = input("File name: ").lower()

fileTypeName = input("File name: ").lower().strip().split(".")

print(fileTypeName)

print(fileTypeName[0])
print(fileTypeName[1])


if fileTypeName[1] in imageFile:
    print("image/",fileTypeName[1])

elif fileTypeName[1] in applicationFile:
    print("application/",fileTypeName[1])

elif fileTypeName[1] in textFile:
    print("text/", fileTypeName[1])

else:
    print("Please enter the correct file extension")

# print(fileTypeName)    