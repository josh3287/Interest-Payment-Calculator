# Collect the necessary inputs: principal, APR, years
# Calculate the monthly payment

def main():
    print("Let's see how much you'll pay over time")
    print("")


    principal = float(input("Input total loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input amount of years: "))

    monthly_interest_rate = apr/ 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))


    print("Here's your monthly payment for this loan: " + str(monthly_payment))
main()