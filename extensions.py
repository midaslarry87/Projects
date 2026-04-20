
imageFile = "gif", "jpg", "png", "jpeg"
applicationFile = "pdf", "zip"
textFile = "text"

newfileName = ""

#fileName = input("File name: ").lower()

fileTypeName = input("File name: ").strip().split(".")

print(fileTypeName[0])
print(fileTypeName[1])


fileTypeName

if fileTypeName[1] in imageFile:
    print("image/",fileTypeName[1])

elif fileTypeName[1] in applicationFile:
    print("application/",fileTypeName[1])

print(fileTypeName)    