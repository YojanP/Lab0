""""This program is handed for people with age is over or equal at 20"""

# Function to calculate the Body Mass Index (BMI)
def calc_bmi(height, weight):
    bmi = weight / ((height / 100.0) ** 2)
    return bmi

#Function to calculate the minimun healtly weight
def calcMinWeight(height):
    minWeight = 18.5 * ((height/100)*(height/100))
    return minWeight

#Function to calculate the maximun healtly weight
def calcMaxWeight(height):
    maxWeight = 24.9 * ((height/100)*(height/100))
    return maxWeight
 
# Main function - entry point
def main():
    # Ask user for height in cms
    height = float(input("Enter your height in cms: "))

    # Ask user for weight in kgs
    weight = float(input("Enter your weight in kgs: "))

    # Call calc_bmi function
    bmi = calc_bmi(height, weight)

    # Print result
    print(f"Your body mass index is {bmi:.2f} kg/m^2")

    #Call calcMinWeight and calcMaxWeight
    minWeight = calcMinWeight(height)
    maxWeight = calcMaxWeight(height)
    # Evaluate the BMI status
    if bmi < 18.5:
        print("You are underweight")
        print(f"Your ideal weight should be between {minWeight: .2f} kgs and {maxWeight: .2f} kgs")
    elif 18.5 <= bmi <= 24.9:
        print("You are healthy")
    elif 25 <= bmi <= 29.9:
        print("You are overweight")
        print(f"Your ideal weight should be between {minWeight: .2f} kgs and {maxWeight: .2f} kgs")
    elif bmi >= 30:
        print("You are obesity")
        print(f"Your ideal weight should be between {minWeight: .2f} kgs and {maxWeight: .2f} kgs")

# Execute the main function
if __name__ == "__main__":
    main()
