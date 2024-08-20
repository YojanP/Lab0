/*This program is handed for people with age is over or equal at 20*/

// Include header file for prototypes of scanf and printf
#include <stdio.h>

// Prototype of calcBmi function
float calcBmi(float h,float w);

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
        printf("You are underweight");
    }
    else if((bmi>=18.5)&&(bmi<=24.9)){
        printf("You are healthy");
    } 
    else if((bmi>=25)&&(bmi<=29.9)){
        printf("You are overweight");
    }
    else if(bmi>=30){
        printf("You are obesity");
    }
}

// Implementation of calcBmi function
float calcBmi(float h,float w){
    float bmi;

    // Compute body mass index
    bmi=w/((h/100.0)*(h/100.0));
    return bmi;
}
