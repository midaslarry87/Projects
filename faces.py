
# This is to show emotions base on messages 

def main():
    global textWord 

    textWord = input()
 
    print(convert())
#convert()

def convert():
    # myStr = input()
    if textWord == "hello":
        return textWord + " " + "\U0001F600"
    else:
        return textWord + " " + "\U0001F641"

main()

