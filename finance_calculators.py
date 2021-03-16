import math
#print output outlining user calculations and get input from user
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment \t-to calculate the amount of interest you'll earn on your investment")
print("bond \t\t-to calculate the amount you'll have to pay on a home loan\n")

element = input("Do you want to work out an investment or bond? ")

#allow for all iterations of 'investment', 'bond', 'compound', 'simple'
invest = ["investment", "INVESTMENT", "Investment"]
bond = ["bond", "BOND", "Bond"]
valid_simple = ["simple", "Simple", "SIMPLE"] 
valid_compound = ["compound", "Compound", "COMPOUND"]

valid_elements = invest + bond

#check if user input was part of valid elements:
#then promt to investment/bond inputs and calculations
if element in valid_elements:
    if element in invest:
        invest_amount = float(input("Enter the investment amount: "))
        interest_rate = (float(input("Enter the interest rate (eg. if 8%, enter 8 without percent symbol): ")))/100
        years = float(input("How many years do you want to invest? "))
        interest = input("Do you want [simple] or [compound] interest? ")

        if interest in valid_simple:
            total = invest_amount*(1+interest_rate*years)
            total_round =  round(total, 2)
            print(f"Your investment will be worth R{total_round} after {years} years investing with simple interest")

        elif interest in valid_compound:
            total = invest_amount*math.pow((1+interest_rate), years)
            total_round = round(total, 2)
            print(f"Your investment will be worth R{total_round} after {years} years investing with compound interest")

    elif element in bond:
        present_value = float(input("Enter the present value of the house: "))
        interest_rate = (float(input("Enter the interest rate (eg. if 8%, enter 8 without percent symbol): ")))/100
        monthly_ir = interest_rate/12
        months = float(input("Enter the number of months you want to take to repay this bond (eg. 120 = 10 years): "))
        monthly_pay = (monthly_ir*present_value)/(1 - math.pow((1+monthly_ir), (-months)))
        monthly_pay_round = round(monthly_pay, 2)
        print(f"Your monthly payments to repay the bond in {months} months will be R{monthly_pay_round}")

else:
    print(f"The input you entered was not valid: \ninput entered: {element} \nvalid elements: {valid_elements}")
