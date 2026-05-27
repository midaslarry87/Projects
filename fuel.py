
while True:

    try:

        fuelGauge =  input("Fraction: ").split("/")

        x = fuelGauge[0]
        y = fuelGauge[1]


        fuelPercentage = int(x)/int(y) * 100

        if fuelPercentage == 100:
            print("F")
            break

        elif fuelPercentage == 0:
            print("E")
            break

        else:
        
            print(f"{fuelPercentage:.0f}%")
            break

    except ZeroDivisionError:

        pass

    except ValueError:

        pass

    except TypeError:
        
        pass   