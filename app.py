def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("--- Temperature Converter Menu ---")
    print("1. Convert Celsius to Fahrenheit")
    choice = input("Enter your choice (1): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    else:
        print("Invalid choice. (Fahrenheit-to-Celsius coming soon!)")

if __name__ == "__main__":
    main()
