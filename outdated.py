
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

d = dates[0]
m = dates[1]
y = dates[2]

print(dates)

print(type(m))
print(type(d))

# print(y,m,d)

takeNewDate = y, m , d 

print(len(d))

print("Before the if statement")

if len(m) != 2 or len(d) != 2:

    print("this is after the if len")
     
    # mm = dates.append(0)

    # mm = dates.insert(0, "0")
    # dd = dates.insert(0, "0")

    z = ""

    twoDigitFormat = z, m, d  

    # print("-0".join(twoDigitFormat))

    conc = "-0".join(twoDigitFormat)

    print("b4 the len")

    print(y)

    # print("".join(twoDigitFormat))

    print(y+(conc))

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



