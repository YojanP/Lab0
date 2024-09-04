""""This program is handed for people with age is over or equal at 20"""

# Function to calculate the Body Mass Index (BMI)
def calc_bmi(height, weight):
    bmi = weight / ((height / 100.0) ** 2)
    return bmi

# Main function - entry point
def main():

    # Ask user for number of people
    numPeople = int(input("Enter the number of people: "))

    height=[None]*numPeople
    weight=[None]*numPeople

    for i in range (0,numPeople):

        # Ask user for height in cms
        height[i] = float(input(f"Enter the height in cms of person {i+1}: "))

        # Ask user for weight in kgs
        weight[i] = float(input(f"Enter the weight in kgs of person {i+1}: "))

    for i in range (0,numPeople): 
        # Call calc_bmi function
        bmi = calc_bmi(height[i], weight[i])
        print(f"The body mass index of person {i+1} is {bmi:.2f} kg/m^2")

        # Evaluate the BMI status
        if bmi < 18.5:
            print(f"The person {i+1} are underweight")
        elif 18.5 <= bmi <= 24.9:
            print(f"The person {i+1} are healthy")
        elif 25 <= bmi <= 29.9:
            print(f"The person {i+1} are overweight")
        elif bmi >= 30:
            print(f"The person {i+1} are obesity")

# Execute the main function
main()


    