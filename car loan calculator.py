import math


def calculate_emi(principal, annual_rate, tenure_months):
    """Calculate Equated Monthly Installment (EMI)."""
    monthly_rate = annual_rate / (12 * 100)  # Convert annual rate to monthly and percentage to decimal
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / \
          (math.pow(1 + monthly_rate, tenure_months) - 1)
    return emi


def affordability_check(monthly_income, monthly_expenses, emi):
    """Check if the user can afford the EMI."""
    disposable_income = monthly_income - monthly_expenses
    return disposable_income >= emi


def main():
    print("Welcome to the Car Loan EMI and Affordability Calculator!\n")

    # User inputs
    car_price = float(input("Enter the car price: "))
    down_payment = float(input("Enter the down payment: "))
    loan_tenure_years = int(input("Enter the loan tenure (in years): "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    monthly_income = float(input("Enter your monthly income: "))
    monthly_expenses = float(input("Enter your monthly expenses: "))

    # Calculations
    loan_amount = car_price - down_payment
    tenure_months = loan_tenure_years * 12
    emi = calculate_emi(loan_amount, annual_interest_rate, tenure_months)
    total_payment = emi * tenure_months
    total_interest = total_payment - loan_amount

    # Affordability check
    affordable = affordability_check(monthly_income, monthly_expenses, emi)

    # Output results
    print("\n----- Loan Details -----")
    print(f"Loan Amount: ${loan_amount:.2f}")
    print(f"Monthly EMI: ${emi:.2f}")
    print(f"Total Payment (Principal + Interest): ${total_payment:.2f}")
    print(f"Total Interest Paid: ${total_interest:.2f}")

    print("\n----- Affordability Check -----")
    if affordable:
        print("Congratulations! You can afford this car loan.")
    else:
        print("Warning: This car loan exceeds your affordability. Consider revising your budget.")


if __name__ == "__main__":
    main()
