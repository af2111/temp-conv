def getTemp():
    try:
        temp = float(input("Provide a Temperature:\n"))
        return temp
    except ValueError:
        print("Provide a valid number, plox.")
        temp = getTemp()
        return temp
def CelsToKelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin
def KelvinToCels(kelvin):
    celsius = kelvin - 273.15
    return celsius
def CelsToFahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
def FahrenheitToCels(fahrenheit):
    celsius = fahrenheit - 32 * 5/9
    return celsius
def KelvinToFahrenheit(kelvin):
    fahrenheit = CelsToFahrenheit(KelvinToCels(kelvin))
    return fahrenheit
def FahrenheitToKelvin(fahrenheit):
    kelvin = CelsToKelvin(FahrenheitToCels(fahrenheit))
    return kelvin
if __name__ == "__main__":
    while True:
        opp = input("Which temperatures do you want to convert? \n(1) Celsius to Kelvin\n(2) Kelvin to Celsius\n(3) Celsius to Fahrenheit\n(4) Fahrenheit to Celsius\n(5) Kelvin to Fahrenheit\n(6) Fahrenheit to Kelvin\n")

        if opp == "1":
            temp = getTemp()
            print(f"{temp} ° Celsius are {str(CelsToKelvin(temp))} Kelvin")
            break
        if opp == "2":
            temp = getTemp()
            print(f"{temp} Kelvin are {str(KelvinToCels(temp))} ° Celsius")
            break
        if opp == "3":
            temp = getTemp()
            print(f"{temp} ° Celsius are {str(CelsToFahrenheit(temp))} ° Fahrenheit")
            break
        if opp == "4":
            temp = getTemp()
            print(f"{temp} ° Fahrenheit are {str(FahrenheitToCels(temp))} ° Celsius")
            break
        if opp == "5":
            temp = getTemp()
            print(f"{temp} Kelvin are {str(KelvinToFahrenheit(temp))} ° Fahrenheit")
            break
        if opp == "6":
            temp = getTemp()
            print(f"{temp} ° Fahrenheit are {str(FahrenheitToKelvin(temp))} Kelvin")
            break
        else:
            print(f"Conversion method {opp} doesn't exist. Please try again.")






