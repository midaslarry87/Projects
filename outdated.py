
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Date should be showing as YYYY-MM-DD

dates = input("Date: ").split("/")

# d = dates[0]
# m = dates[1]
# y = dates[2]

m = dates[0]
d = dates[1]
y = dates[2]



print(dates)

print(type(m))
print(type(d))

# print(y,m,d)

takeNewDate = y, m , d 

print(len(m))
print(len(d))
print(len(y))

print("Before the if statement")

if len(m) != 2 and len(d) != 2:

    print("this is inside the if len")
    
    z = ""

    twoDigitFormat = z, m, d  

    # print("-0".join(twoDigitFormat))

    conc = "-0".join(twoDigitFormat)

    # print("b4 the len")

    # print(y)

    # print("".join(twoDigitFormat))

    print(y+(conc))

# This is the flow for the Months 

elif len(m) != 2:

    z = ""

    mD = z, m

    mDigit = "-0".join(mD)

    print(y)

    print(y + (mDigit) + "-"+ d)

    print("This is mDightPrint: " + mDigit)
    
# This is the flow for the Days 

elif len(d) != 2:

    z = ""

    dD = z, d

    dDigit = "-0".join(dD)

    print("This is mDightPrint: " + dDigit)
    print(y + "-"+ m + dDigit )

else:

    print("This is inside the else ")

    print("-0".join(takeNewDate))

# print(len(m))

print("This is after the if")
    
print(m, d)

# print("-0".join(takeNewDate))

newDate = dates

for check in dates:
    pass

# isoDate = "".join(y)

# print(isoDate)

#print("-0".join(reversed(newDate)))

# for l in months:
#     print(l)



