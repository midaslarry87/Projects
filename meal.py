# This is a code for telling user when to eat and what type of food is the person eating during the time of the day 

MorningTime = "7:00 - 8:00" 
AfternoonTime = "12:00 - 13:00" 
NightTime = "18:00 - 19:00" 


# Morning = 


def main():

    global askTime
    global spString

    askTime = input("What time is it? ")

    spString = askTime.split(":")

    print(spString[0])
    print(type(spString))

    if spString[0] == "7" or spString[0] == "8":
        print("breakfast time")    

def convert(time):

    

    
    if askTime == MorningTime:
        print("breakfast time")


    elif askTime == AfternoonTime: 
        print("lunch time")

    elif askTime == NightTime:
        print("dinner time")

    else:
        print()

if __name__ == "__main__":

    main()