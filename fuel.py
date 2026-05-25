
fuelGauge =  input("Fraction: ").split("/")

print(fuelGauge)

x = fuelGauge[0]
y = fuelGauge[1]

print(x, y)

fuelPercentage = int(x)/int(y) * 100

print(f"{fuelPercentage:.0f}%")