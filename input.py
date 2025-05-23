# Packages
import json
import locale
import re
# Constants
from constants import C 

state = {
    "additional_contribution_amount": "0",
    "additional_contribution_frequency": "monthly",
    "debts": [], # loan_amount, interest_rate, term_length, current_balance
}

def collect_additional_contribution_information(testing = False):
    print()

    additional_contribution_frequency = collect_input(
        "frequency",
        "How often do you want to contribute an additional amount to your debt? ",
        testing = testing
    )
    additional_contribution_amount = collect_input(
        "numerical",
        f"How much would you like to contribute every {additional_contribution_frequency}? ",
        testing = testing
    )

    return additional_contribution_amount, additional_contribution_frequency

def collect_debt_information():
    print()
    current_balance = collect_input("numerical", "What is the current balance of the loan? ")
    interest_rate = collect_input("numerical", "What is the interest rate of the loan? ")
    loan_amount = collect_input("numerical", "What was the original amount of the loan? ")
    term_length = collect_input("numerical", "What is the term length of the loan? ")

    return current_balance, interest_rate, loan_amount, term_length

def confirm_additional_contribution_information(amount, frequency, testing = False):
    print()
    display_additional_contribution_information((amount, frequency))
    print("---------------------------------------")
    print("Does this information look correct?")
    print("---------------------------------------")
    print("If 'NO', you'll be asked to enter the information again.")
    print("If 'YES', you'll move on to calculating your amortization schedule.")

    user_input_confirmation = collect_input("confirmation", testing = testing)

    return get_user_confirmation_comparison(user_input_confirmation)

def confirm_additional_contribution_intent(testing = False):
    print()
    print(f"Do you intend to contribute an additional amount towards your debt every {C.FREQUENCIES}")
    print("---------------------------------------")
    print("If 'YES', I'll ask you how much and how often")
    print("If 'NO', I'll continue to calculating your debt's amortization schedule")
    print("---------------------------------------")

    additional_contribution_confirmation = collect_input("confirmation", testing = testing)

    return get_user_confirmation_comparison(additional_contribution_confirmation)

def confirm_additional_debt_intent(testing = False):
    print()
    print("Would you like to enter another debt?")
    print("---------------------------------------")
    print("If 'NO', you'll move on towards getting your debt's amortization schedule.")
    print("If 'YES', you'll be asked to enter another debt's information.")

    user_input_confirmation = collect_input("confirmation", testing = testing)

    return get_user_confirmation_comparison(user_input_confirmation)

def confirm_debt_information(current_balance, interest_rate, loan_amount, term_length, testing = False):
    print()
    display_debt_information((current_balance, interest_rate, loan_amount, term_length))
    print("---------------------------------------")
    print("Does this information look correct?")
    print("---------------------------------------")
    print("If 'NO', you'll be asked to enter the information again.")
    print("If 'YES', you'll move on to adding additional debts, if any.")

    user_input_confirmation = collect_input("confirmation", testing = testing)

    return get_user_confirmation_comparison(user_input_confirmation)

def collect_input(type, prompt = "", testing = False):
    options = get_options(type)
    user_input = input(prompt)
    user_input_normalized = normalize_user_input(
        user_input,
        C.get_disallowed_dangerous_characters_regex()
    )

    if not validate_input(type, user_input_normalized, options):
        print(f"{user_input!r} was not valid")
        
        # NOTE: When testing failed cases, we want to avoid infinite recursion
        if not testing:
            return collect_input(type, prompt)
    else:
        return user_input_normalized 

def display_additional_contribution_information(additional_contribution_information):
    print()
    print()
    print()
    print("Here is the additional contribution information we collected:\n")
    print("---------------------------------------")
    print("Here is the information you entered:\n")
    print(f"Frequency: {additional_contribution_information[1]}")
    print(f"Amount: ${format_currency(additional_contribution_information[0])}")

def display_debt_information(debt_information):
    print("Here is the information you entered:\n")
    print(f"Current balance: ${format_currency(debt_information[0])}")
    print(f"Interest rate: {debt_information[1]}%")
    print(f"Original loan amount: ${format_currency(debt_information[2])}")
    print(f"Term length: {debt_information[3]} months")

def format_currency(string, include_sign = True):
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(float(string), symbol = include_sign, grouping = True)

def get_options(type):
    if type == "frequency":
        return C.FREQUENCIES
    elif type == "confirmation":
        return C.CONFIRMATIONS
    else:
        return []

def get_user_confirmation_comparison(user_input_confirmation):
    # WARN: do not call this before normalize_user_input() and validate_input()
    # NOTE: I do not want to overcomplicated the C.CONFIRMATIONS value type
    # because validate_input_option_in_options would get unnecessarily complicated
    if user_input_confirmation and "y" in user_input_confirmation:
        return True
    else:
        return False

def introduce_user_to_process():
    print("I'm going to ask you a series of questions about your debts and any additional contributions you want to make towards your monthly debt. Each debt will require the original loan amount, interest rate, term length, and the current balance.")
    print("")
    print("When entering numerical values, such as dollars or percents, do not use special characters, such as $ or commas, and express percents as decimals, such as 3.25 instead of 0.0325\n")

def is_float_positive(float):
    return float >= 0

def normalize_user_input(input, replace_pattern):
    if isinstance(input, str):
        return strip_dangerous_characters_from_user_input(replace_pattern, input.lower())
    else:
        raise TypeError(f"{input!r} is not a string; cannot normalize")

def step_collect_additional_contribution():
    additional_contribution_confirmation = confirm_additional_contribution_intent()

    if additional_contribution_confirmation:
        additional_contribution_information = collect_additional_contribution_information()
        user_confirmation = confirm_additional_contribution_information(*additional_contribution_information)

        if user_confirmation:
            display_additional_contribution_information(additional_contribution_information)

            return additional_contribution_information
        else:
            return step_collect_additional_contribution()
    else:
        print()
        print()
        print()
        print("Skipping additional contributions...")
        
        return None

def step_collect_debts():
    debts = []
    is_user_finished_submitting = False

    while not is_user_finished_submitting:
        debt_information = collect_debt_information()
        user_confirmation = confirm_debt_information(*debt_information)

        if user_confirmation:
            debts.append(debt_information)

            user_confirmation = confirm_additional_debt_intent()

            if user_confirmation:
                continue
            else:
                is_user_finished_submitting = True
        else: 
            # NOTE: Effectively, this is recursively calling collect_debt_information()
            continue

    print()
    print()
    print()
    print("Here is the debt information we collected:\n")

    for debt in debts:
        print()
        print(f"Debt #{debts.index(debt)}")
        print("---------------------------------------")
        display_debt_information(debt)

    return debts

def strip_dangerous_characters_from_user_input(pattern, input):
    if isinstance(input, str):
        return re.sub(pattern, "", input)
    else:
        raise TypeError(f"{input!r} is not a string; cannot strip")

def validate_input_option_in_options(input, options):
    if input in options:
        return True
    else:
        return False

def validate_input_numerical(input):
    try:
        if is_float_positive(float(input)):
            return True
        else:
            print(f"{float(input)!r} was negative")
            return False
    except:
        print(f"{input!r} could not be converted to a decimal")
        return False

def validate_input(type, user_input_normalized, options):
    valid = True

    if type in ["confirmation", "frequency"]:
        valid = validate_input_option_in_options(user_input_normalized, options)
    elif type == "numerical":
        valid = validate_input_numerical(user_input_normalized)

    return valid

def write_to_tmp_file(data, directory = "/tmp", filename = "pds.json"):
    f = open(f"{directory}/{filename}", 'w', encoding = "utf-8")

    json.dump(data, f)

    f.close()
    
def main():
    introduce_user_to_process()

    debts = step_collect_debts() 
    additional_contribution = step_collect_additional_contribution()

    state["additional_contribution_amount"] = additional_contribution[0]
    state["additional_contribution_frequency"] = additional_contribution[1]
    state["debts"] = debts
    write_to_tmp_file(state, "/home/taylor/dev/pds")

    print(debts)
    print(additional_contribution)

if __name__ == "__main__":
    main()
