/*This program is handed for people with age is over or equal at 20*/

// Include header file for prototypes of scanf and printf
#include <stdio.h>

// Prototype of calcBmi function
float calcBmi(float h,float w);
float percentage(float i, float j);

// Main function - entry point
int main(){
    // Local variable declaration
    int underWeight=0, healthy=0, overWeight=0, obesity=0;
    int numPeople=0;
    float bmi;
    
    //Ask user for number of people
    printf("Enter the number of people: ");
    scanf("%d",&numPeople);
    
    //Declare array after asking the user for the number of people
    float height[numPeople];
    float weight[numPeople];

    //Loop for heights and weight of all people
    for(int i=0; i<numPeople; i++){
        // Ask user for height in cms
        printf("Enter the height in cms of person %d: ", i+1);
        scanf("%f",&height[i]);

        // Ask user for weight in kgs
        printf("Enter your weight in kgs: ");
        scanf("%f",&weight[i]);
    }

    //Loop to calculate and printf bmi of each person
    for(int i=0;i<numPeople;i++){
        // Call calcBmi function
        bmi=calcBmi(height[i],weight[i]);
         // Print result
        printf("the body mass index of person %i is %f kg/m^2\n",i+1, bmi);

        // Determine and print the BMI category for each person based on their BMI value
        if(bmi<18.5){
            printf("the person %i are underweight\n", i+1);
            underWeight+=1;
        }
        else if((bmi>=18.5)&&(bmi<=24.9)){
            printf("the person %i are healthy\n", i+1);
            healthy+=1;
        } 
        else if((bmi>=25)&&(bmi<=29.9)){
            printf("the person %i are overweight\n", i+1);
            overWeight+=1;
        }
        else if(bmi>=30){
            printf("the person %i are obesity\n", i+1);
            obesity+=1;
        }
    }    

//Print percent of every category from bmi
printf("The percentage of people with underweight is: %.2f\n", percentage(underWeight, numPeople));
printf("The percentage of people with healthy weight is %.2f\n", percentage(healthy, numPeople));
printf("The percentage of people with overweight is %.2f\n", percentage(overWeight, numPeople));
printf("The percentage of people with obesity is %.2f\n", percentage(obesity, numPeople));

}

// Implementation of calcBmi function
float calcBmi(float h,float w){
    float bmi;

    // Compute body mass index
    bmi=w/((h/100.0)*(h/100.0));
    return bmi;
}

float percentage(float i, float j){
    float percentage;

    percentage=(i/j)*100;
    return percentage;
}
