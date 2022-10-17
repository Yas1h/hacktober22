#include <stdio.h>
#include <math.h>

int main(void)
{
    int choice;
    float p, r, t, si, ca;

    printf("What do you want to calculate?\n\n");
    printf("1. Simple interest\n");
    printf("2. Compound amount\n");
    printf("3. Exit\n");
    printf("\nEnter your choice: ");
    scanf("%d", &choice);

    switch (choice)
    {
        case 1:
            printf("Enter the principal amount: ");
            scanf("%f", &p);
            printf("Enter the rate of interest: ");
            scanf("%f", &r);
            printf("Enter the time period: ");
            scanf("%f", &t);
            si = (p * r * t) / 100;
            printf("Simple interest = %f", si);
            break;
        
        case 2:
            printf("Enter the principal amount: ");
            scanf("%f", &p);
            printf("Enter the rate of interest: ");
            scanf("%f", &r);
            printf("Enter the time period: ");
            scanf("%f", &t);
            ca = p * pow((1 + r / 100), t);
            printf("Compound Amount = %f", ca);
            break;
        
        case 3:
            exit(0);
        
        default:
            printf("Invalid choice!");
    }
    return 0;
}
