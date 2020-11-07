def getTemp():
    try:
        temp = float(input("Gib eine Temperatur an:\n"))
        return temp
    except ValueError:
        print("Gib eine gültige Zahl an, plox.")
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
        opp = input("Welche Möglichkeit willst du wählen? \n(1) Celsius in Kelvin\n(2) Kelvin in Celsius\n(3) Celsius in Fahrenheit\n(4) Fahrenheit in Celsius\n(5) Kelvin in Fahrenheit\n(6) Fahrenheit in Kelvin\n")

        if opp == "1":
            temp = getTemp()
            print(f"{temp} Grad Celsius sind {str(CelsToKelvin(temp))} Kelvin")
            break
        if opp == "2":
            temp = getTemp()
            print(f"{temp} Kelvin sind {str(KelvinToCels(temp))} Grad Celsius")
            break
        if opp == "3":
            temp = getTemp()
            print(f"{temp} Grad Celsius sind {str(CelsToFahrenheit(temp))} Grad Fahrenheit")
            break
        if opp == "4":
            temp = getTemp()
            print(f"{temp} Grad Fahrenheit sind {str(FahrenheitToCels(temp))} Grad Celsius")
            break
        if opp == "5":
            temp = getTemp()
            print(f"{temp} Kelvin sind {str(KelvinToFahrenheit(temp))} Grad Fahrenheit")
            break
        if opp == "6":
            temp = getTemp()
            print(f"{temp} Grad Fahrenheit sind {str(FahrenheitToKelvin(temp))} Kelvin")
            break
        else:
            print(f"Möglichkeit {opp} existiert nicht. Bitte versuche es erneut.")






