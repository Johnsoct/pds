# Packages
from tabulate import tabulate
import math

def calculate_amortization_schedule(debts_and_additional_contributions):
    additional_contribution_amount = debts_and_additional_contributions["additional_contribution_amount"]
    additional_contribution_frequency = debts_and_additional_contributions["additional_contribution_frequency"]
    debts = sort_debts(debts_and_additional_contributions["debts"])
    schedule = []

    # TODO: iterate through each month of all debts from the smallest to the largest current debt balance, add values to data as tuple
    for debt in debts:
    # TODO: calculate the monthly payment of each debt
    # TODO: calculate the monthly interest due of each debt

def calculate_monthly_contribution(monthly_payment, current_loan_amount, interest):
    amount_to_interest = current_loan_amount * (interest / 12)
    amount_to_principle = float(monthly_payment) - amount_to_interest

    return f"{amount_to_principle:.2f}", f"{amount_to_interest:.2f}"

def calculate_monthly_payment(original_loan_amount, interest, term_length_in_months):
    # Total payment = Loan amount x ((i * (1 + i)^n) / ((i + 1)^n -1))
    #
    # i = Monthly interest payment (interest rate / 12 months)
    # n = Number of payments (term length in months)

    interest_monthly = interest / 12
    formula_bottom = math.pow(interest_monthly + 1, term_length_in_months) - 1
    formula_top = interest_monthly * math.pow(1 + interest_monthly, term_length_in_months)

    return f"{original_loan_amount * (formula_top / formula_bottom):.2f}"

def display_amortization_schedule():
    data = [] # (monthly payment, interest due, principle due, new balance)

    print(tabulate(
        data, 
        headers = ["monthly payment", "interest due", "principle due", "new balance"],
        showindex = "always",
        tablefmt = "github",
    ))

def sort_debts(debts):
    # NOTE: sorts by the current balance
    ordered_debts = sorted(debts, key = lambda debt: debt[0])

    return ordered_debts

def main(debts_and_additional_contributions):
    print(debts_and_additional_contributions)

if __name__ == "__main__":
    main(dict())
