#!/usr/bin/env python3

"""
    This is an NZ Tax Calculator, written in Python.

    Author: Erwin R. Pasia
    Email: erwinpasia@gmail.com
    Date: May 21, 2023

"""

def print_tax_banner():
    banner = """
    --------------------------------------------------------
    |       NZ Tax Rate Brackets as of 21 May, 2023        |  
    |             Author: Erwin R. Pasia                   |
    --------------------------------------------------------
    |        Income               |      Tax Rate          |
    --------------------------------------------------------
    | Tax 1: Up to $14,000.00     |       10.5%            |
    | Tax 2: Over $14,000.00      |       17.5%            |
    | Tax 3: Over $48,000.00      |       30.0%            |
    | Tax 4: Over $70,000.00      |       33.0%            |
    | Tax 5: Over $180,000.00     |       39.0%            |
    --------------------------------------------------------
    """
    print(banner)

# Call the function to display the tax banner
print_tax_banner()


def calculate_tax(income):
    if income <= 14000:
        tax = income * 0.105
        return income, tax, 0, 0, 0, 0, 0, 0, 0, 0
    elif 14000 < income <= 48000:
        income1 = 14000
        tax1 = income1 * 0.105
        income2 = income - income1
        tax2 = income2 * 0.175
        return income1, tax1, income2, tax2, 0, 0, 0, 0, 0, 0
    elif 48000 < income <= 70000:
        income1, tax1, income2, tax2, *_ = calculate_tax(48000)
        income3 = income - 48000
        tax3 = income3 * 0.3
        return income1, tax1, income2, tax2, income3, tax3, 0, 0, 0, 0
    elif 70000 < income <= 180000:
        income1, tax1, income2, tax2, income3, tax3, *_ = calculate_tax(70000)
        income4 = income - 70000
        tax4 = income4 * 0.33
        return income1, tax1, income2, tax2, income3, tax3, income4, tax4, 0, 0
    else:
        income1, tax1, income2, tax2, income3, tax3, income4, tax4, *_ = calculate_tax(180000)
        income5 = income - 180000
        tax5 = income5 * 0.39
        return income1, tax1, income2, tax2, income3, tax3, income4, tax4, income5, tax5

try:
    
    print("==========================================================================")
    #income = float(input("Enter your yearly income: "))
    income_input = input("Enter your yearly income: ")
    income_input = income_input.replace(",", "")  # Remove comma if present
    income = float(income_input) 
except ValueError:
    income = 0.0

# Handling invalid input for monthly deductions
try:
    #monthly_deductions = float(input("Enter your monthly deductions (i.e Kiwisaver or Superannuation): "))
    monthly_deductions_input = input("Enter your monthly deductions (i.e Kiwisaver or Superannuation): ")
    monthly_deductions_input = monthly_deductions_input.replace(",", "")  # Remove comma if present
    monthly_deductions = float(monthly_deductions_input)
except ValueError:
    monthly_deductions = 0.0

income1, tax1, income2, tax2, income3, tax3, income4, tax4, income5, tax5 = calculate_tax(income)

total_tax = tax1 + tax2 + tax3 + tax4 + tax5
net_income = income - total_tax

monthly_net_income = (net_income - (monthly_deductions * 12)) / 12
fortnightly_net_income = monthly_net_income / 2


print("==========================================================================")
print("Income 1: $", format(income1, ",.2f"))
print("Tax 1 @ 10.5%: $", format(tax1, ",.2f"))

if income > 14000:
    print("\nIncome 2: $", format(income2, ",.2f"))
    print("Tax 2 @ 17.5%: $", format(tax2, ",.2f"))

if income > 48000:
    print("\nIncome 3: $", format(income3, ",.2f"))
    print("Tax 3 @ 30%: $", format(tax3, ",.2f"))

if income > 70000:
    print("\nIncome 4: $", format(income4, ",.2f"))
    print("Tax 4 @ 33%: $", format(tax4, ",.2f"))

if income > 180000:
    print("\nIncome 5: $", format(income5, ",.2f"))
    print("Tax 5 @ 39%: $", format(tax5, ",.2f"))

print("============================================")
print("Total tax: $", format(total_tax, ",.2f"))
print("============================================")
print("Net income: $", format(net_income, ",.2f"))
print("============================================")
print("Monthly net income: $", format(monthly_net_income, ",.2f"))
print("============================================")
print("Fortnightly net income: $", format(fortnightly_net_income, ",.2f"))
print("============================================")
