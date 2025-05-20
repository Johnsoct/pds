# Packages
from decimal import Decimal, ROUND_HALF_UP
# from tabulate import tabulate
import math

def calculate_amortization_schedule(debts_and_additional_contributions):
    additional_contribution_amount = debts_and_additional_contributions["additional_contribution_amount"]
    additional_contribution_frequency = debts_and_additional_contributions["additional_contribution_frequency"]
    debts = sort_debts(debts_and_additional_contributions["debts"])
    schedule = []

    # NOTE: Iterating through each debt, ordered by current balance, and applying the additional contribution to each payment. 
    # When the debt is paid off, the # of terms is recorded. 
    # When calculating the next debt, the additional contribution is not applied until the previously recorded # of terms is reached.
    # When this new debt is paid off, the terms from when the additional payment was added and until the debt was paid off are added to the recorded # of terms
    # Repeat...
    terms_until_additional_contributions = 0

    for index, debt in enumerate(debts):
        current_balance = debt[0]
        monthly_payment = calculate_monthly_payment(debt[3], debt[1], debt[2])

        schedule.append([])

        # Calculating each term
        while current_balance > 0:
            monthly_principle, monthly_interest = calculate_monthly_contribution(monthly_payment, debt[0], debt[1])
            print("monthly payment", monthly_payment)
            print("Monthly principle", monthly_principle)
            print("Monthly interest", monthly_interest)

            # Update current balance (avoid infinite loop)
            current_balance = calculate_new_balance(
                current_balance,
                monthly_principle,
                additional_contribution_amount,
                index,
                terms_until_additional_contributions,
            )

            schedule[index].append((
                index + 1,
                display_currency(monthly_principle),
                display_currency(monthly_interest),
                display_currency(current_balance), 
            ))
            terms_until_additional_contributions += 1

        return schedule

def calculate_monthly_contribution(monthly_payment, current_loan_amount, interest):
    amount_to_interest = current_loan_amount * (interest / Decimal(12))
    amount_to_principle = monthly_payment - amount_to_interest

    return amount_to_principle, amount_to_interest

def calculate_monthly_payment(original_loan_amount, interest, term_length_in_months):
    # Total payment = Loan amount x ((i * (1 + i)^n) / ((i + 1)^n -1))
    #
    # i = Monthly interest payment (interest rate / 12 months)
    # n = Number of payments (term length in months)

    interest_monthly = interest / Decimal(12)
    formula_bottom = Decimal(math.pow(interest_monthly + 1, term_length_in_months) - 1)
    formula_top = interest_monthly * Decimal(math.pow(1 + interest_monthly, term_length_in_months))

    return original_loan_amount * (formula_top / formula_bottom)

def calculate_new_balance(
    original_balance,
    monthly_principle,
    additional_contribution_amount = Decimal(0.0),
    current_index = 0,
    terms_until_additional_contributions = 0,
):
    new_balance = original_balance - monthly_principle

    if additional_contribution_amount > 0 and current_index >= terms_until_additional_contributions:
        new_balance -= additional_contribution_amount

    print("current balance", new_balance)

    return new_balance

def display_amortization_schedule():
    data = [] # (monthly payment, interest due, principle due, new balance)

    # print(tabulate(
    #     data, 
    #     headers = ["monthly payment", "interest due", "principle due", "new balance"],
    #     showindex = "always",
    #     tablefmt = "github",
    # ))

def display_currency(decimal):
    return float(decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

def sort_debts(debts):
    print(type(debts))
    # NOTE: sorts by the current balance
    ordered_debts = sorted(debts, key = lambda debt: debt[0])

    return ordered_debts

def main(debts_and_additional_contributions):
    print(debts_and_additional_contributions)

if __name__ == "__main__":
    main(dict())
