#include <stdio.h>

void calculate_tax(float income, float *income1, float *tax1, float *income2, float *tax2, float *income3, float *tax3, float *income4, float *tax4, float *income5, float *tax5) {
    if (income <= 14000) {
        *income1 = income;
        *tax1 = income * 0.105;
        *income2 = 0;
        *tax2 = 0;
        *income3 = 0;
        *tax3 = 0;
        *income4 = 0;
        *tax4 = 0;
        *income5 = 0;
        *tax5 = 0;
    } else if (income > 14000 && income <= 48000) {
        *income1 = 14000;
        *tax1 = *income1 * 0.105;
        *income2 = income - *income1;
        *tax2 = *income2 * 0.175;
        *income3 = 0;
        *tax3 = 0;
        *income4 = 0;
        *tax4 = 0;
        *income5 = 0;
        *tax5 = 0;
    } else if (income > 48000 && income <= 70000) {
        calculate_tax(48000, income1, tax1, income2, tax2, income3, tax3, income4, tax4, income5, tax5);
        *income3 = income - 48000;
        *tax3 = *income3 * 0.3;
        *income4 = 0;
        *tax4 = 0;
        *income5 = 0;
        *tax5 = 0;
    } else if (income > 70000 && income <= 180000) {
        calculate_tax(70000, income1, tax1, income2, tax2, income3, tax3, income4, tax4, income5, tax5);
        *income4 = income - 70000;
        *tax4 = *income4 * 0.33;
        *income5 = 0;
        *tax5 = 0;
    } else {
        calculate_tax(180000, income1, tax1, income2, tax2, income3, tax3, income4, tax4, income5, tax5);
        *income5 = income - 180000;
        *tax5 = *income5 * 0.39;
    }
}

int main() {
    float income, income1, tax1, income2, tax2, income3, tax3, income4, tax4, income5, tax5;
    float total_tax, net_income, monthly_net_income, fortnightly_net_income;

    printf("Enter your income: ");
    scanf("%f", &income);

    calculate_tax(income, &income1, &tax1, &income2, &tax2, &income3, &tax3, &income4, &tax4, &income5, &tax5);

    total_tax = tax1 + tax2 + tax3 + tax4 + tax5;
    net_income = income - total_tax;
    monthly_net_income = net_income / 12;
    fortnightly_net_income = net_income / 24;

    printf("Income 1: $%.2f\n", income1);
    printf("Tax 1: $%.2f\n", tax1);

    if (income > 14000) {
        printf("Income 2: $%.2f\n", income2);
        printf("Tax 2: $%.2f\n", tax2);
    }

    if (income > 48000) {
        printf("Income 3: $%.2f\n", income3);
        printf("Tax 3: $%.2f\n", tax3);
    }

    if (income > 70000) {
        printf("Income 4: $%.2f\n", income4);
        printf("Tax 4: $%.2f\n", tax4);
    }

    if (income > 180000) {
        printf("Income 5: $%.2f\n", income5);
        printf("Tax 5: $%.2f\n", tax5);
    }

    printf("Total tax: $%.2f\n", total_tax);
    printf("Net income: $%.2f\n", net_income);
    printf("Monthly net income: $%.2f\n", monthly_net_income);
    printf("Fortnightly net income: $%.2f\n", fortnightly_net_income);

    return 0;
}

