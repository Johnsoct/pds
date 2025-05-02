# PDS - Personal Debt Schedule

Python CLI tool taking your individual debts and monthly debt contribution as arguments to produce an expedited amortization schedule to calculate how fast you can pay off your debt given a specific amount of contributions each month.

## Motivation

Growing up, borrowing debt was the "thing to do" when you wanted to "own" something you could not afford, whether a car, computer, college, etc.; however, what everyone, who has more debt than they should reasonably have, fails to tell you is the weight it places on your mind... The constant reminder of the upcoming payment and the low balance of your checking account... I'm tired of that feeling, so I'm going to define a month-to-month schedule of how much money should go to a specific debt to pay off all my debt, besides my mortgage, as fast as possible.

## Definitions

* **Amortization** is the process of spreading out a loan or an asset's cost over a set period of time through regular payments. A portion of each payment covers part of the principal, the original amount borrowed, plus interest. It generally takes the form of a table.
* **Debt snowball**, a term coined by [Dave Ramsey](https://www.ramseysolutions.com/), references the effect that occurs when you start paying off your debts starting from the smallest to the largest debt. Technically, it refers to how the amount of money you can pay towards debt each month increases as you reduce the monthly payments from paid off debt.

## How an expedited amortization schedule works

Let's say you make $100,000/yr and have two loans, a vehicle loan and a mortgage. Here are the details for each loan, which are required to calculate the amortization of each loan.

| Loan | Principal | Interest Rate | Loan Term | Payment Frequency |
| --- | --- | --- | --- | ---|
| Vehicle | $15,000 | 6.73% | 60 months | monthly |
| Mortgage | $220,000 | 7.12% | 180 months | monthly |

The calculation for a loan's amortization schedule is:

$P = ((r(1+r)^n) / ((1+r)^n - 1)) * L$

**$P$**: monthly payment

**$r$**: monthly interest rate (annual interest rate / 12)

**$n$**: total number of payments

**$L$**: loan amount (principal)

So, for the standard amortization, for every payment period, we calculate the interest, principal portion, and then subtract principal portion from the current balance. We repeat this until the balance reaches zero.

With an expedited amortization, extra is paid towards the *principal* each period (or irregularly, but we're calculating via a monthly basis). This lowers the balance faster, which reduces total interest paid and the loan duration.

<!-- TODO: add a table exemplify a typical amortization table -->

# Development

## CLI inputs

### Loans

1. Loan amount
2. Interest rate
3. Original term length
4. Current balance

### Extra monthly contribution

1. Additional amount to contribute
1. Frequency of additional contributions

## Calculation(s)

1. Calculate the monthly payment normally
2. Apply the additional contribution directly to the balance

## Process

1. CLI Inputs for each loan
2. Determine the path to a debt snowball
3. Calculate the amortization of each loan
4. Apply the additional contribution

### Steps

#### Calculate the amortization of each loan

Since we're apply an additional contribution to a single loan per month, we need to calculate the amortizations one month at a time for all loans, apply the additional contribution, and then move on to the next month.

#### Apply the additional contribution

At the end of calculating a month's amortization for all loans, apply the defined additional contribution to the loan with the least balance (debt snowball).

If the balance < the additional contribution, apply the remainder to the next debt in line.

If the balance < the additional contribution and there isn't another debt in line, celebrate!!!
