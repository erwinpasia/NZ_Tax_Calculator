#!/usr/bin/env python3

import time

"""
This is an NZ Tax Calculator, written in Python.

Author: Erwin R. Pasia
Email: erwinpasia@gmail.com
Date: May 21, 2023
Version: 2.0

==========
|Changes:|
==========
1. Moved the tax brackets to a constant list TAX_BRACKETS for better organization and easy modification in the future.
2. Refactored the calculate_tax function to use a loop instead of multiple if conditions, making the code more concise and easier to maintain.
3. Created a get_float_input function to handle repetitive input code for both income and monthly deductions.
4. Improved the formatting of output messages to display values with commas and two decimal places using f-strings.
5. Reorganized the code to follow PEP 8 style guidelines, including consistent indentation, spacing, and naming conventions.


"""

TAX_BRACKETS = [
    (14000, 0.105),
    (48000, 0.175),
    (70000, 0.3),
    (180000, 0.33),
    (float('inf'), 0.39)
]

def print_tax_banner():
    banner = """
    -----------------------------------------------------------------
    |            NZ Tax Rate Brackets as of 21 May, 2023            |  
    |                    Author: Erwin R. Pasia                     |
    -----------------------------------------------------------------
    |                Income               |      Tax Rate           |
    -----------------------------------------------------------------
    | Income_Bracket_1: Up to $14,000.00  |    Tax_1: 10.5%         |
    | Income_Bracket_2: Over $14,000.00   |    Tax_2: 17.5%         |
    | Income_Bracket_3: Over $48,000.00   |    Tax_3: 30.0%         |
    | Income_Bracket_4: Over $70,000.00   |    Tax_4: 33.0%         |
    | Income_Bracket_5: Over $180,000.00  |    Tax_5: 39.0%         |
    -----------------------------------------------------------------
    """
    print(banner)

def calculate_tax(income):
    taxes = []
    previous_limit = 0

    for limit, rate in TAX_BRACKETS:
        if income <= limit:
            taxable_amount = income - previous_limit
            tax = taxable_amount * rate
            taxes.append((taxable_amount, tax))
            break
        else:
            taxable_amount = limit - previous_limit
            tax = taxable_amount * rate
            taxes.append((taxable_amount, tax))
            previous_limit = limit

    return taxes

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).replace(',', ''))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Call the function to display the tax banner
print_tax_banner()

# Handling invalid input for income
income = get_float_input("Enter your New Yearly Salary Offer (income): $ ")

# Handling invalid input for Kiwisaver monthly deductions
monthly_deductions = get_float_input("Enter your Kiwisaver Percent Contribution (e.g 3,4,6,8, or 10): ") / 100
#print(monthly_deductions)
monthly_deductions_ks = "{:.2f}".format(income * monthly_deductions / 12) #set to two-decimal places only.
#print(monthly_deductions_ks)

# Handling invalid input for ACC monthly deductions
monthly_deductions_2 = get_float_input("Enter your ACC Percent Contribution (e.g 1): ") / 100
#print(monthly_deductions_2)
monthly_deductions_acc = "{:.2f}".format(income * monthly_deductions_2 / 12) #set to two-decimal places only.
#print(monthly_deductions_acc)

# Display the output
print("\nShow Me The Moneeeeey!!!")

# Delay for 3 seconds
time.sleep(2)

taxes = calculate_tax(income)
total_tax = sum(tax for _, tax in taxes)
net_income = income - total_tax

monthly_net_income = (net_income - (float(monthly_deductions_ks) + float(monthly_deductions_acc)) * 12) / 12  #converting from string to float.
fortnightly_net_income = monthly_net_income / 2
monthly_net_income_afterksacc = monthly_net_income * 12

print("\n==========================================================================")

for i, (taxable_amount, tax) in enumerate(taxes, start=1):
    print(f"Income_Bracket_{i}: ${taxable_amount:,.2f}")
    print(f"Tax_{i} @ {TAX_BRACKETS[i-1][1]*100:.1f}%: ${tax:,.2f}")
    print()

print("==========================================================================")
print(f"Total PAYE Tax: ${total_tax:,.2f}")
print("==========================================================================")
print(f"Yearly Net Income (BEFORE Kiwisaver & ACC deductions): ${net_income:,.2f}")
print("==========================================================================")
print("Kiwisaver Monthly Contribution Amount: $" + str(monthly_deductions_ks))  
print("==========================================================================")
print("ACC Monthly Contribution Amount: $" + str(monthly_deductions_acc))       
print("==========================================================================")
print(f"Yearly Net Income (AFTER Kiwisaver & ACC deductions): ${monthly_net_income_afterksacc:,.2f}")
print("==========================================================================")
print(f"\nMonthly Take-Home Pay: ${monthly_net_income:,.2f}")
print("\n==========================================================================")
print(f"\nFortnightly Take-Home Pay: ${fortnightly_net_income:,.2f}")

disclaimer_banner = '''
==========================================================================
|                                                                        |
|                              DISCLAIMER:                               |
|                    The calculations provided are                       |
|                  intended solely for informational                     |
|                  purposes and should be considered                     |
|                   as approximate estimations only.                     |
|                    Users are advised to exercise                       |
|                    caution and rely on their own                       |
|                        judgment when utilizing                         |
|                         the provided results.                          |
|                                                                        |
==========================================================================
'''

print(disclaimer_banner)
