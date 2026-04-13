def main():

    # calling both functions and assigning them to their variable

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # calculating the value 
    tip = dollars * percent

    # using the fstring format to print the result 
    print(f"leave ${tip:.2f}")

# Defining the function for the dollars_to_float
def dollars_to_float(d):
    # indexing and slicing the string from the input 
    rv = d[1:]
    # Change the string to float 
    mkInt = float(rv)
    # return the float value to the function to be use when it is called
    return mkInt

# Defining the function for the percent_to_float 
def percent_to_float(p):
    # Indexing and slicing the string value 
    rm = p[0:2]
    # converting the string into integer 
    fltChg = int(rm) / 100 
    # Assigning the float and making sure the float number 
    chn = float(fltChg)
    # return the float to the function 
    return chn


main()
