# Modules
import amortization
import input as user_input

def main():
    debts_and_additional_contributions = user_input.main()
    amortization.main(debts_and_additional_contributions)

main()
