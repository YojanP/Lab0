/*This program is handed for people with age is over or equal at 20*/

// Include header file for prototypes of scanf and printf
#include <stdio.h>

// Prototype of calcBmi function
float calcBmi(float h,float w);
float calcMinWeight(float h);
float calcMaxWeight(float h);

// Main function - entry point
int main(){
    // Local variable declaration
    float height;
    float weight;
    float bmi;

    // Ask user for height in cms
    printf("Enter your height in cms: ");
    scanf("%f",&height);

    // Ask user for weight in kgs
    printf("Enter your weight in kgs: ");
    scanf("%f",&weight);

    // Call calcBmi function
    bmi=calcBmi(height,weight);

    // Print result
    printf("Your body mass index is %f kg/m^2\n",bmi);

    if(bmi<18.5){
        printf("You are underweight\n");
        printf("Your ideal weight should be between %.2f and %.2f kgs\n", calcMinWeight(height), calcMaxWeight(height));
    }
    else if((bmi>=18.5)&&(bmi<=24.9)){
        printf("You are healthy");
    } 
    else if((bmi>=25)&&(bmi<=29.9)){
        printf("You are overweight\n");
        printf("Your ideal weight should be between %.2f and %.2f kgs\n", calcMinWeight(height), calcMaxWeight(height));
    }
    else if(bmi>=30){
        printf("You are obesity\n");
        printf("Your ideal weight should be between %.2f kgs and %.2f kgs\n", calcMinWeight(height), calcMaxWeight(height));
    }
}

// Implementation of calcBmi function
float calcBmi(float h,float w){
    float bmi;

    // Compute body mass index
    bmi=w/((h/100.0)*(h/100.0));
    return bmi;
}

//Implementation of calMinWeight
float calcMinWeight(float h){
    float minWeight;

    minWeight = 18.5*((h/100)*(h/100));
    return minWeight;
}

//Implementation of calMinWeight
float calcMaxWeight(float h){
    float maxWeight;

    maxWeight = 24.9*((h/100)*(h/100));
    return maxWeight;
}

