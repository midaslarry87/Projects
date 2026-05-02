# This is a code for telling user when to eat and what type of food is the person eating during the time of the day 

MorningTime = "7:00" 
AfternoonTime = "12:00" 
NightTime = "18:00" 



def main():

    global askTime

    askTime = input("What time is it? ")
    

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