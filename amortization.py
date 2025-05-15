# Packages
import math

def calculate_monthly_payment(original_loan_amount, interest, term_length_in_months):
    # Total payment = Loan amount x ((i * (1 + i)^n) / ((i + 1)^n -1))
    #
    # i = Monthly interest payment (interest rate / 12 months)
    # n = Number of payments (term length in months)

    interest_monthly = interest / 12
    formula_bottom = math.pow(interest_monthly + 1, term_length_in_months) - 1
    formula_top = interest_monthly * math.pow(1 + interest_monthly, term_length_in_months)

    return f"{original_loan_amount * (formula_top / formula_bottom):.2f}"


def main(debts_and_additional_contributions):
    print(debts_and_additional_contributions)

if __name__ == "__main__":
    main(dict())
