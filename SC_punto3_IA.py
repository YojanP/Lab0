def calculate_bmi(height_cm, weight_kg):
    return weight_kg / ((height_cm / 100) ** 2)

def main():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))

    bmi = calculate_bmi(height, weight)
    print(f"Your body mass index is {bmi:.2f} kg/m^2")

if __name__ == "__main__":
    main()
