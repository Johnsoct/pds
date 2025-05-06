# Logic: Expedited Amortization Schedule

## Notes

* All input will first be "normalized" and escaped before further processing

## Review

* By creating a pipeline for all input processes to follow, the functions I write to perform small actions along the pipeline RELY on having arguments which have been subject to other processes, such as how `get_user_confirmation_comparison` relies on `user_input_confirmation` (it's argument) to have been normalized through `collect_input`.
    * Without typing, I really don't like this, but with typing, this problem wouldn't be an issue at all, IMO.

## Steps

1. - [x] Introduce the user to the CLI process
2. - [x] Collect information about user debts (loop)
    1. - [x] Collect the following debt information (loop): current balance, interest rate, original loan amount, term length
        1. - [x] Check if input is invalid; recursively collect input if not
            1. - [x] IF input type == numerical:
                1. - [x] TRY casting to float; return True
                1. - [x] EXCEPT return False
    2. - [x] Display collected Loan information to user
        1. - [x] Ask to confirm
            1. - [x] IF YES:
                1. - [x] Store data
                2. - [x] Continue
            2. - [x] IF NO:
                1. - [x] Recursively collect user input
    3. - [x] Ask if the user would like to enter another loan 
        1. - [x] IF YES; collect debt information
        2. - [x] IF NO; continue
3. -  [x] Collect information about user's intended additional contribution(s)
    1. -  [x] "Do you intend to contribute an additional amount towards your debt \[weekly, bi-weekly, monthly, bi-monthly, yearly]?"
        1. -  [x] IF YES:
            1. -  [x] Collect frequency information
                1. -  [x] Check if input is invalid; recursively collect frequency information if not 
                    1. -  [x] IF input == one of the frequency options ? return True : return False
            1. -  [x] Collect contribution amount
                1. -  [x] Validate input as a numerical type (check above); recursively collect amount if not
        2. -  [x] IF NO; continue
4. - [ ] Calculate amortization schedule
5. - [ ] Write amortization schedule data to file
    1. - [ ] Ask user if they want to save the amortization data in their /Downloads
        1. - [ ] IF YES; write file
        2. - [ ] IF NO; continue
5. - [ ] Display amortization shedule
