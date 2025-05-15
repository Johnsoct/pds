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
