# Packages
import pytest
# Modules
from amortization import *

class TestAmortization:
    def test_calculate_amortization_schedule(self):
        passing_tests = [
            [
                # Input
               {
                    "additional_contribution_amount": 0,
                    "additional_contribution_frequency": "monthly",
                    "debts": [
                        (100, .1, 12, 1000),
                    ],
                },
                # Output
                [
                    # Debt schedule #1
                    [
                        # Payments
                        (1, 79.58, 8.33, 920.42),
                        (2, 80.25, 7.67, 840.17),
                        (3, 80.91, 7.00, 759.26),
                        (4, 81.59, 6.33, 677.67),
                        (5, 82.27, 5.65, 595.40),
                        (6, 82.95, 4.96, 512.45),
                        (7, 83.65, 4.27, 428.80),
                        (8, 84.34, 3.57, 344.46),
                        (9, 85.05, 2.87, 259.41),
                        (10, 85.75, 2.16, 173.66),
                        (11, 86.47, 1.45, 87.19),
                        (12, 87.19, 0.73, -0.00),
                    ],
                ],
            ]
        ]

        for test in passing_tests:
            assert calculate_amortization_schedule(test[0]) == test[1]

    def test_calculate_monthly_payment(self):
        passing_tests = [
            (30000, .03, 48, "664.03"),
            (1000, .1, 12, "87.92"),
        ]

        for test in passing_tests:
            assert calculate_monthly_payment(test[0], test[1], test[2]) == test[3]

    def test_calculate_monthly_contribution(self):
        monthly_payment = calculate_monthly_payment(30000, .03, 48)
        passing_tests = [
            {
                "parameters": [monthly_payment, 30000, .03],
                "result": ["589.03", "75.00"],
            },
            {
                "parameters": [monthly_payment, 29410.97, .03],
                "result": ["590.50", "73.53"],
            },
            {
                "parameters": [monthly_payment, 28820.47, .03],
                "result": ["591.98", "72.05"],
            },
            {
                "parameters": [87.92, 1000, .1],
                "result": ["79.58", "8.33"],
            },
        ]

        for test in passing_tests:
            params = test["parameters"]
            results = test["result"]
            assert calculate_monthly_contribution(params[0], params[1], params[2]) == (results[0], results[1])

    def test_calculate_new_balance(self):
        passing_tests = [
            # params: original balance, monthly principle, additional contribution amount, current index, terms until additional contributions
            {
                "params": [100, 10],
                "result": 90.0,
            },
            {
                "params": [100, 10, 10, 0, 0],
                "result": 80.0,
            },
            {
                "params": [100, 10, 10, 0, 1],
                "result": 90.0,
            },
            {
                "params": [100, 10, 10, 4, 1],
                "result": 80.0,
            },
        ]

        for test in passing_tests:
            assert calculate_new_balance(*test["params"]) == test["result"]

    def test_sort_debts(self):
        passing_tests = [
            {
                "additional_contribution_amount": 100,
                "additional_contribution_frequency": "monthly",
                "debts": [
                    ("12453.99", "12.4", "14523.45", "72", ),
                    ("500.00", "4.5", "1000.00", "60"),
                ],
            },
            {
                "additional_contribution_amount": 100,
                "additional_contribution_frequency": "monthly",
                "debts": [
                    ("7200.00", "8.99", "14000.00", "72"),
                    ("77500.00", "3.4", "134000.00", "84"),
                    ("6500.00", "2.41", "14000.00", "72"),
                    ("18000.00", "8.4", "24000.00", "72"),
                ],
            }
        ]

        for test in passing_tests:
            ordered_debts = sort_debts(test)

            for index, debt in enumerate(ordered_debts):
                if index == len(ordered_debts) - 1:
                    break

                assert debt[0] <= ordered_debts[index + 1][0]
