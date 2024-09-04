""""This program is handed for people with age is over or equal at 20"""

# Function to calculate the Body Mass Index (BMI)
def calc_bmi(height, weight):
    bmi = weight / ((height / 100.0) ** 2)
    return bmi

#Function to calculate the percentaje of every category from bmi
def calc_percentage(i, j):
    percentage = (i/j)*100
    return percentage
    
# Main function - entry point
def main():
    # Ask user for number of people
    numPeople = int(input("Enter the number of people: "))

    height=[None]*numPeople
    weight=[None]*numPeople

    # Initialize counters for each BMI category
    underWeight = 0
    healthy = 0
    overWeight = 0
    obesity = 0

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
            underWeight = underWeight+1
        elif 18.5 <= bmi <= 24.9:
            print(f"The person {i+1} are healthy")
            healthy = healthy+1
        elif 25 <= bmi <= 29.9:
            print(f"The person {i+1} are overweight")
            overWeight = overWeight+1
        elif bmi >= 30:
            print(f"The person {i+1} are obesity")
            obesity = obesity+1

    #Call function percentaje for every category
    underWeightPercentage = calc_percentage(underWeight, numPeople)
    healthyPercentage = calc_percentage(healthy, numPeople)
    overWeightPercentage = calc_percentage(overWeight, numPeople)
    obesityPercentage = calc_percentage(obesity, numPeople)
    
    #Print percent of every category from bmi
    print(f"The percentage of people with underweight is: {underWeightPercentage:.2f}%\n")
    print(f"The percentage of people with healthy weight is {healthyPercentage:.2f}%\n")
    print(f"The percentage of people with overweight is {overWeightPercentage:.2f}%\n")
    print(f"The percentage of people with obesity is {obesityPercentage:.2f}%\n")
    

# Execute the main function
main()