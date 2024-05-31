def convert_F_to_C(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def convert_C_to_F(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

while True:
    print("Select conversion temperature:")
    print("A. Fahrenheit to Celsius")
    print("B. Celsius to Fahrenheit")
    print("C. Exit")

    choice = input("Enter your choice (A-C): ")

    if choice == 'A':
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = convert_F_to_C(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        break
    elif choice == 'B':
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = convert_C_to_F(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        break
    elif choice == 'C':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
