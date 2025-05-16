# Packages
import pytest
# Modules
from amortization import *

class TestAmortization:
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

    def test_calculate_monthly_payment(self):
        passing_tests = [
            (30000, .03, 48, "664.03"),
        ]

        for test in passing_tests:
            assert calculate_monthly_payment(test[0], test[1], test[2]) == test[3]

    def test_calculate_monthly_contribution(self):
        monthly_payment = calculate_monthly_payment(30000, .03, 48)
        passing_tests = [
            (monthly_payment, 30000, .03, "589.03", "75.00"),
            (monthly_payment, 29410.97, .03, "590.50", "73.53"),
            (monthly_payment, 28820.47, .03, "591.98", "72.05"),
        ]

        for test in passing_tests:
            assert calculate_monthly_contribution(test[0], test[1], test[2]) == (test[3], test[4])
