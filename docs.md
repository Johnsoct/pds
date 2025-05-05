# Logic: Expedited Amortization Schedule

## Notes

* All input will first be "normalized" and escaped before further processing

## Steps

1. Introduce the user to the CLI process
2. Collect information about user debts (loop)
    1. Collect the following debt information (loop): current balance, interest rate, original loan amount, term length
        1. Check if input is invalid; recursively collect input if not
            1. IF input type == numerical:
                1. TRY casting to float; return True
                1. EXCEPT return False
            2. IF input type == percentage:
                1. TRY casting to float && greater than 0; return True
                2. EXCEPT return False
    2. Display collected loan information to user
        1. Ask to confirm
            1. IF YES:
                1. Store data
                2. Continue
            2. IF NO:
                1. Reset state
                1. Recursively collect user input
    3. Ask if the user would like to enter another loan 
        1. IF YES; collect debt information
        2. IF NO; continue
3. Collect information about user's intended additional contribution(s)
    1. "Do you intend to contribute an additional amount towards your debt \[weekly, bi-weekly, monthly, bi-monthly, yearly]?"
        1. IF YES:
            1. Collect frequency information
                1. Check if input is invalid; recursively collect frequency information if not 
                    1. IF input == one of the frequency options ? return True : return False
            1. Collect contribution amount
                1. Validate input as a numerical type (check above); recursively collect amount if not
        2. IF NO; continue
4. Calculate amortization schedule
5. Write amortization schedule data to file
    1. Ask user if they want to save the amortization data in their ~/Downloads
        1. IF YES; write file
        2. IF NO; continue
5. Display amortization shedule
