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

    print("What is the current balance of the loan?")
    current_balance = collect_input("numerical")

    print("What is the interest rate of the loan?")
    interest_rate = collect_input("numerical")

    print("What was the original amount of the loan?")
    loan_amount = collect_input("numerical")

    print("What is the term length of the loan?")
    term_length = collect_input("numerical")

def collect_input(type):
    normalized_usr_input = normalize_user_input(type, input())

    if validate_input(type, normalized_usr_input):
        print(f"{normalized_usr_input} was not valid")
        # TODO: do something

    return normalized_usr_input 

def convert_to_float(input):
    try:
        str_input = convert_to_str(input)
        stripped_str_input = strip_characters_from_str(str_input, C.NUMERICAL_CHARACTERS)
        return float(stripped_str_input)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Could not convert {input!r} to float") from e

def convert_to_str(input):
    if isinstance(input, str):
        return input
    else:
        try:
            return str(input)
        except Exception as e:
            raise Exception(f"Could not convert {input!r} to string") from e

def normalize_user_input(type, input):
    normalized_user_input = input.lower()
    
    if type == "numerical":
        normalized_user_input = strip_characters_from_str(normalized_user_input, C.NUMERICAL_CHARACTERS)

        if normalized_user_input == "":
            normalized_user_input = "0"

        if "%" in input:
            normalized_user_input = normalized_user_input.replace("%", "")

            if normalized_user_input == "":
                normalized_user_input = "0"
            
            normalized_user_input = str(convert_to_float(normalized_user_input) / 100)

    return normalized_user_input

def strip_characters_from_str(input, characters):
    if isinstance(input, str):
        pattern = f"[{''.join(re.escape(c) for c in characters)}]"
        return re.sub(pattern, "", input)
    else:
        raise TypeError(f"{input!r} is not a string; cannot strip")

def validate_input_frequency(input):
    if input in C.FREQUENCIES:
        return True
    else:
        return False

def validate_input_numerical(input):
    # Stripped clean
    if input == "":
        print(f"{input!r} could not be converted to a decimal")
        return False

    try:
        convert_to_float(input)
        return True
    except (TypeError, ValueError):
        print(f"{input!r} could not be converted to a decimal")
        return False

# type = frequency, numerical
# frequency = constantsclass.FREQUENCIES
def validate_input(type, normalized_user_input):
    valid = True

    if type == "numerical":
        valid = validate_input_numerical(normalized_user_input)
    elif type == "frequency":
        valid = validate_input_frequency(normalized_user_input)

    return valid
    
def main():
    print("I'm going to ask you a series of questions about your debts and any additional contributions you want to make towards your monthly debt. Each debt will require the original loan amount, interest rate, term length, and the current balance.")

    collect_debt_information()

