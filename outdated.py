
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

while True:
        
        try:

            # for m in months:
            #      print(m)
        
        # Date should be showing as YYYY-MM-DD

            dates = input("Date: ").split("/")

            # print(dates)
            # print(type(dates))

            # for m in months:
            #      if m in dates:
            #           print(m)
                #  pass
                #  if m in dates.
                 

            # d = dates[0]
            # m = dates[1]
            # y = dates[2]

            m = dates[0]
            d = dates[1]
            y = dates[2]

            takeNewDate = y, m , d 

            # print("Before the if statement")

            if len(m) != 2 and len(d) != 2:
                
                z = ""

                twoDigitFormat = z, m, d  

                # print("-0".join(twoDigitFormat))

                conc = "-0".join(twoDigitFormat)


                print(y+(conc))

                break

            # This is the flow for the Months 

            elif len(m) != 2:

                z = ""

                mD = z, m

                mDigit = "-0".join(mD)

                print(y + (mDigit) + "-"+ d)

                break

                #print("This is mDightPrint: " + mDigit)
                
            # This is the flow for the Days 

            elif len(d) != 2:

                z = ""

                dD = z, d

                dDigit = "-0".join(dD)

                #print("This is mDightPrint: " + dDigit)
                print(y + "-"+ m + dDigit )

                break

            else:
                #print("This is inside the else ")

                print("-".join(takeNewDate))
                
                break 


        except IndexError:
             pass
        
        except ValueError:
             pass
        
        