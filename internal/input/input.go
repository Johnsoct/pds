package input

import (
	"fmt"
	"strconv"
)

// Types definitions
// Types definitions
// Types definitions
type (
	AdditionalContributionFrequency   string
	Dollars                           float32
	InterestRate                      float32
	NormalizedUserInput               string
	TermLength                        int
	AdditionalContributionAmount      = Dollars
	CurrentBalance                    = Dollars
	OriginalLoanAmount                = Dollars
	AdditionalContributionInformation struct {
		AdditionalContributionAmount    AdditionalContributionAmount
		AdditionalContributionFrequency AdditionalContributionFrequency
	}
	DebtInformation struct {
		CurrentBalance     CurrentBalance
		InterestRate       InterestRate
		OriginalLoanAmount OriginalLoanAmount
		TermLength         TermLength
	}
	State struct {
		AdditionalContributionInformation AdditionalContributionInformation
		Debts                             []DebtInformation
	}
)

var state = State{
	AdditionalContributionInformation: AdditionalContributionInformation{
		AdditionalContributionFrequency: "never",
		AdditionalContributionAmount:    0,
	},
	Debts: []DebtInformation{},
}

// Takes a string and converts it into a Decimal object.
//
// If error, returns the raw value attempted to convert.
func castToDecimal(str string) (float64, error) {
	f, error := strconv.ParseFloat(str, 64)

	if error != nil {
		fmt.Printf("\n%s could not be converted to a float\n", str)
		return 0, error
	}

	return f, error
}

// TEST:
func collectAdditionalContributionInformation(testing bool) (AdditionalContributionFrequency, AdditionalContributionAmount) {
	fmt.Println()

	additionalContributionFrequency := collectInput(
		"frequency",
		"How often do you want to contribute an additional amount to your debt?",
		testing,
	)
	additionalContributionAmount := collectInput(
		"numerical",
		"How much would you like to contribute every"+"additional_contribution_frequency?",
		testing,
	)

	return additionalContributionFrequency, additionalContributionAmount
}

// def collect_debt_information() -> DebtInformation:
//
//	print()
//	current_balance = collectInput(
//	    "numerical", "What is the current balance of the loan? ")
//	interest_rate = collectInput(
//	    "numerical", "What is the interest rate of the loan? ")
//	loan_amount = collectInput(
//	    "numerical", "What was the original amount of the loan? ")
//	term_length = collectInput(
//	    "numerical", "What is the term length of the loan? ")
//
//	return current_balance, interest_rate, loan_amount, term_length
//
// def confirm_additional_contribution_information(amount: Decimal, frequency: AdditionalContributionFrequency, testing=False) -> bool:
//
//	print()
//	display_additional_contribution_information((amount, frequency))
//	print("---------------------------------------")
//	print("Does this information look correct?")
//	print("---------------------------------------")
//	print("If 'NO', you'll be asked to enter the information again.")
//	print("If 'YES', you'll move on to calculating your amortization schedule.")
//
//	user_input_confirmation = collectInput("confirmation", testing=testing)
//
//	return get_user_confirmation_comparison(user_input_confirmation)
//
// def confirm_additional_contribution_intent(testing=False) -> bool:
//
//	print()
//	print(f"Do you intend to contribute an additional amount towards your debt every {
//	      C.FREQUENCIES}")
//	print("---------------------------------------")
//	print("If 'YES', I'll ask you how much and how often")
//	print("If 'NO', I'll continue to calculating your debt's amortization schedule")
//	print("---------------------------------------")
//
//	additional_contribution_confirmation = collectInput(
//	    "confirmation", testing=testing)
//
//	return get_user_confirmation_comparison(additional_contribution_confirmation)
//
// def confirm_additional_debt_intent(testing=False) -> bool:
//
//	print()
//	print("Would you like to enter another debt?")
//	print("---------------------------------------")
//	print("If 'NO', you'll move on towards getting your debt's amortization schedule.")
//	print("If 'YES', you'll be asked to enter another debt's information.")
//
//	user_input_confirmation = collectInput("confirmation", testing=testing)
//
//	return get_user_confirmation_comparison(user_input_confirmation)
//
// def confirm_debt_information(
//
//	debt_information: DebtInformation,
//	testing=False,
//
// ) -> bool:
//
//	print()
//	display_debt_information(debt_information)
//	print("---------------------------------------")
//	print("Does this information look correct?")
//	print("---------------------------------------")
//	print("If 'NO', you'll be asked to enter the information again.")
//	print("If 'YES', you'll move on to adding additional debts, if any.")
//
//	user_input_confirmation = collectInput("confirmation", testing=testing)
//
//	return get_user_confirmation_comparison(user_input_confirmation)
func collectInput(category string, prompt string, testing bool) NormalizedUserInput {
	options = get_options(type)
	user_input = input(prompt)
	user_input_normalized = normalize_user_input(
	    category,
	    user_input,
	    C.get_disallowed_dangerous_characters_regex()
	)

	if not validate_input(type, user_input_normalized, options):
	    print(f"{user_input!r} was not valid")

	    # NOTE: When testing failed cases, we want to avoid infinite recursion
	    if not testing:
	        return collectInput(type, prompt)
	else:
	    return user_input_normalized
}

// def display_additional_contribution_information(additional_contribution_information: AdditionalContributionInformation):
//     print()
//     print()
//     print()
//     print("Here is the additional contribution information we collected:\n")
//     print("---------------------------------------")
//     print("Here is the information you entered:\n")
//     print(f"Frequency: {additional_contribution_information[1]}")
//     print(f"Amount: {format_currency(additional_contribution_information[0])}")
//
//
// def display_debt_information(debt_information: DebtInformation):
//     print("Here is the information you entered:\n")
//     print(f"Current balance: {format_currency(debt_information[0])}")
//     print(f"Interest rate: {debt_information[1]}%")
//     print(f"Original loan amount: {format_currency(debt_information[2])}")
//     print(f"Term length: {debt_information[3]} months")
//
//
// def format_currency(value: Decimal) -> str:
//     rounded_decimal = value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
//     locale.setlocale(locale.LC_ALL, '')
//     return locale.currency(float(rounded_decimal), symbol=True, grouping=True)
//
//
// def get_options(type: str) -> (str, ...):
//     if type == "frequency":
//         return C.FREQUENCIES
//     elif type == "confirmation":
//         return C.CONFIRMATIONS
//     else:
//         return []
//
//
// def get_user_confirmation_comparison(user_input_confirmation: str) -> bool:
//     # WARN: do not call this before normalize_user_input() and validate_input()
//     # NOTE: I do not want to overcomplicated the C.CONFIRMATIONS value type
//     # because validate_input_option_in_options would get unnecessarily complicated
//     if user_input_confirmation and "y" in user_input_confirmation:
//         return True
//     else:
//         return False
//
//
// def introduce_user_to_process():
//     print("I'm going to ask you a series of questions about your debts and any additional contributions you want to make towards your monthly debt. Each debt will require the original loan amount, interest rate, term length, and the current balance.")
//     print("")
//     print("When entering numerical values, such as dollars or percents, do not use special characters, such as $ or commas, and express percents as decimals, such as 3.25 instead of 0.0325\n")
//
//
// def is_decimal_positive(decimal: Decimal) -> bool:
//     return not Decimal.is_signed(decimal)
//
//
// def normalize_user_input(type: str, input: str, replace_pattern: str) -> NormalizedUserInput:
//     if not isinstance(input, str):
//         raise TypeError
//
//     input_mutated = input.lower()
//
//     # 1. Strip of dangerous characters
//     input_mutated = strip_dangerous_characters_from_user_input(
//         replace_pattern, input_mutated)
//
//     # 2. Cast to appropriate type, if necessary
//     if type == "numerical":
//         input_mutated = cast_to_decimal(input_mutated)
//
//     return input_mutated
//
//
// def step_collect_additional_contribution() -> AdditionalContributionInformation | None:
//     additional_contribution_confirmation = confirm_additional_contribution_intent()
//
//     if additional_contribution_confirmation:
//         additional_contribution_information = collect_additional_contribution_information()
//         user_confirmation = confirm_additional_contribution_information(
//             *additional_contribution_information)
//
//         if user_confirmation:
//             display_additional_contribution_information(
//                 additional_contribution_information)
//
//             return additional_contribution_information
//         else:
//             return step_collect_additional_contribution()
//     else:
//         print()
//         print()
//         print()
//         print("Skipping additional contributions...")
//
//         return None
//
//
// def step_collect_debts() -> [DebtInformation, ...]:
//     debts = []
//     is_user_finished_submitting = False
//
//     while not is_user_finished_submitting:
//         debt_information = collect_debt_information()
//         user_confirmation = confirm_debt_information(debt_information)
//
//         if user_confirmation:
//             debts.append(debt_information)
//
//             user_confirmation = confirm_additional_debt_intent()
//
//             if user_confirmation:
//                 continue
//             else:
//                 is_user_finished_submitting = True
//         else:
//             # NOTE: Effectively, this is recursively calling collect_debt_information()
//             continue
//
//     print()
//     print()
//     print()
//     print("Here is the debt information we collected:\n")
//
//     for debt in debts:
//         print()
//         print(f"Debt #{debts.index(debt)}")
//         print("---------------------------------------")
//         display_debt_information(debt)
//
//     return debts
//
//
// def strip_dangerous_characters_from_user_input(pattern: str, input: str) -> str:
//     if isinstance(input, str):
//         return re.sub(pattern, "", input)
//     else:
//         raise TypeError(f"{input!r} is not a string; cannot strip")
//
//
// def validate_input_option_in_options(input: str, options: [str, ...]) -> bool:
//     if input in options:
//         return True
//     else:
//         return False
//
//
// def validate_input_numerical(decimal: Decimal) -> bool:
//     if is_decimal_positive(decimal):
//         return True
//     else:
//         print(f"{float(decimal)!r} was negative")
//         return False
//
//
// def validate_input(type: str, user_input_normalized: NormalizedUserInput, options: [str, ...]) -> bool:
//     valid = True
//
//     if user_input_normalized == None:
//         valid = False
//     elif type in ["confirmation", "frequency"]:
//         valid = validate_input_option_in_options(
//             user_input_normalized, options)
//     elif type == "numerical":
//         valid = validate_input_numerical(user_input_normalized)
//
//     return valid
//
//
// def write_to_tmp_file(data, directory="/tmp", filename="pds.json"):
//     f = open(f"{directory}/{filename}", 'w', encoding="utf-8")
//
//     json.dump(data, f)
//
//     f.close()
//
//
// func main () {
//     introduce_user_to_process()
//
//     debts = step_collect_debts()
//     additional_contribution = step_collect_additional_contribution()
//
//     state["debts"] = debts
//     if additional_contribution:
//         state["additional_contribution_information"] = (
//             additional_contribution[0], additional_contribution[1])
//
//     write_to_tmp_file(state, "/home/taylor/dev/pds")
//
//     return state
