# Packages
import pytest
# Modules
from amortization import *

class TestAmortization:
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
