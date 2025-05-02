# Packages
import re
# Constants
from constants import Constants

C = Constants()
additional_contribution_amount = 0
additional_contribution_frequency = 'monthly'
debts = [] # loan_amount, interest_rate, term_length, current_balance

def collect_debt_information():
    current_balance = None
    interest_rate = None
    loan_amount = None
    term_length = None

    current_balance = collect_input("numerical", "What is the current balance of the loan?")
    interest_rate = collect_input("numerical", "What is the interest rate of the loan?")
    loan_amount = collect_input("numerical", "What was the original amount of the loan?")
    term_length = collect_input("numerical", "What is the term length of the loan?")

    return current_balance, interest_rate, loan_amount, term_length

def collect_input(type, prompt):
    user_input = input(prompt)
    normalized_user_input = normalize_user_input(user_input)

    if not validate_input(type, normalized_user_input):
        print(f"{user_input} was not valid")
        collect_input(type, prompt)

    return normalized_user_input 

def normalize_user_input(input):
    return strip_dangerous_characters_from_user_input(input.lower())

def strip_dangerous_characters_from_user_input(input):
    if isinstance(input, str):
        pattern = f"[{''.join(re.escape(c) for c in C.DISALLOWED_DANGEROUS_CHARACTERS)}]"
        return re.sub(pattern, "", input)
    else:
        raise TypeError(f"{input!r} is not a string; cannot strip")

def validate_input_frequency(input):
    if input in C.FREQUENCIES:
        return True
    else:
        return False

def validate_input_numerical(input):
    try:
        float(input)
        return True
    except (TypeError, ValueError):
        print(f"{input!r} could not be converted to a decimal")
        return False

def validate_input_percentage(input):
    if float(input) >= 0:
        return True
    else:
        return False

# type = frequency, numerical, percentage
# frequency = constantsclass.FREQUENCIES
def validate_input(type, normalized_user_input):
    valid = True

    if type == "frequency":
        valid = validate_input_frequency(normalized_user_input)
    elif type == "numerical":
        valid = validate_input_numerical(normalized_user_input)
    elif type == "percentage":
        valid = validate_input_percentage(normalized_user_input)

    return valid
    
def main():
    print("I'm going to ask you a series of questions about your debts and any additional contributions you want to make towards your monthly debt. Each debt will require the original loan amount, interest rate, term length, and the current balance.")
    print("")
    print("When entering numerical values, such as dollars or percents, do not use special characters, such as $ or commas, and express percents as decimals, such as 3.25 instead of 0.0325")

    loan1 = collect_debt_information()

    print(loan1)

if __name__ == "__main__":
    main()
