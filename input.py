# Packages
import re
# Constants
from constants import C 

additional_contribution_amount = 0
additional_contribution_frequency = 'monthly'
debts = [] # loan_amount, interest_rate, term_length, current_balance

def collect_debt_information():
    current_balance = collect_input("numerical", "What is the current balance of the loan?")
    interest_rate = collect_input("numerical", "What is the interest rate of the loan?")
    loan_amount = collect_input("numerical", "What was the original amount of the loan?")
    term_length = collect_input("numerical", "What is the term length of the loan?")

    return current_balance, interest_rate, loan_amount, term_length

def collect_input(type, prompt):
    user_input = input(prompt)
    normalized_user_input = normalize_user_input(user_input, C.get_disallowed_dangerous_characters_regex())

    if not validate_input(type, normalized_user_input, C.FREQUENCIES):
        print(f"{user_input} was not valid")
        collect_input(type, prompt)

    return normalized_user_input 

def introduce_user_to_process():
    print("I'm going to ask you a series of questions about your debts and any additional contributions you want to make towards your monthly debt. Each debt will require the original loan amount, interest rate, term length, and the current balance.")
    print("")
    print("When entering numerical values, such as dollars or percents, do not use special characters, such as $ or commas, and express percents as decimals, such as 3.25 instead of 0.0325")

def normalize_user_input(input, replace_pattern):
    if isinstance(input, str):
        return strip_dangerous_characters_from_user_input(replace_pattern, input.lower())
    else:
        raise TypeError(f"{input!r} is not a string; cannot normalize")

def strip_dangerous_characters_from_user_input(pattern, input):
    if isinstance(input, str):
        return re.sub(pattern, "", input)
    else:
        raise TypeError(f"{input!r} is not a string; cannot strip")

def validate_input_frequency(input, options):
    if input in options:
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

def validate_input(type, normalized_user_input, options):
    valid = True

    if type == "frequency":
        valid = validate_input_frequency(normalized_user_input, options)
    elif type == "numerical":
        valid = validate_input_numerical(normalized_user_input)
    elif type == "percentage":
        valid = validate_input_percentage(normalized_user_input)

    return valid
    
def main():
    introduce_user_to_process()
    loan1 = collect_debt_information()

    print(loan1)

if __name__ == "__main__":
    main()
