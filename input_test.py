# Packages
import pytest
import sys
# Modules
from input import *
# Constants
from constants import C 

class TestValidateInput:
    def test_collect_additional_contribution_information(self, capsys, monkeypatch):
        failing_tests = [
            ("bimonthly", "100"),
            ("biweekly", "100"),
            ("monthly", "abc"),
            ("weekly", "abc"),
        ]
        passing_tests = [(frequency, "100") for frequency in C.FREQUENCIES]
        recursively_passing_tests = [
            [("bimonthly", "bi-monthly"), ("abc", "100")],
            [("biweekly", "bi-weekly"), ("abc", "100")],
            [("month", "monthly"), ("abc", "100")],
            [("week", "weekly"), ("abc", "100")],
            [("year", "yearly"), ("abc", "100")],
        ]

        for test in failing_tests:
            tests = iter(test)
            monkeypatch.setattr("builtins.input", lambda _: next(tests))

            collect_additional_contribution_information(testing = True)

            # Prepare the stdout messages to assert against
            collect_input_stdout = f"was not valid"
            test_stdout = capsys.readouterr().out
            
            assert f"{collect_input_stdout}" in f"{test_stdout}"

        for test in passing_tests:
            tests = iter(test)

            monkeypatch.setattr("builtins.input", lambda _: next(tests))

            assert collect_additional_contribution_information() == (test[0], test[1])

        for test in recursively_passing_tests:
            tests = iter([*test[0], *test[1]])

            monkeypatch.setattr("builtins.input", lambda _: next(tests))

            assert collect_additional_contribution_information() == (test[0][1], test[1][1])

    def test_collect_input(self, capsys, monkeypatch):
        failing_tests = [
            ("confirmation", "", "abc"),
            ("confirmation", "", "noh"),
            ("numerical", "What is the current balance of the loan?", "abc"),
            ("numerical", "What is the interest rate of the loan?", "$12.00 cents"),
            ("numerical", "What was the original amount of the loan?", "-12"),
            ("numerical", "What is the term length of the loan?", "sixty months"),
        ]
        passing_tests = [
            ("confirmation", "", "yes"),
            ("confirmation", "", "y"),
            ("confirmation", "", "YES"),
            ("confirmation", "", "Yes"),
            ("confirmation", "", "no"),
            ("confirmation", "", "n"),
            ("confirmation", "", "NO"),
            ("confirmation", "", "No"),
            ("numerical", "What is the current balance of the loan?", "9,000"),
            ("numerical", "What is the interest rate of the loan?", "12"),
            ("numerical", "What was the original amount of the loan?", "12,000"),
            ("numerical", "What is the term length of the loan?", "60"),
        ]
        recursively_passing_tests = [
            ("confirmation", "", ["yah", "yes"]),
            ("confirmation", "", ["nah", "no"]),
            ("numerical", "What is the current balance of the loan?", ["abc", "9,000"]),
            ("numerical", "What is the interest rate of the loan?", ["$12.00 cents", "12"]),
            ("numerical", "What was the original amount of the loan?", ["-12", "12,000"]),
            ("numerical", "What is the term length of the loan?", ["sixty months", "60"]),
        ]

        for test in failing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test[2])

            collect_input(test[0], test[1], testing = True)

            # Prepare the stdout messages to assert against
            collect_input_stdout = f"{test[2]!r} was not valid"
            test_stdout = capsys.readouterr().out
            
            assert f"{collect_input_stdout}" in f"{test_stdout}"

        for test in passing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test[2])

            normalized_user_input = collect_input(test[0], test[1])

            assert normalized_user_input == normalize_user_input(
                test[2],
                C.get_disallowed_dangerous_characters_regex()
            )

        for test in recursively_passing_tests:
            tests = iter(test[2])

            monkeypatch.setattr("builtins.input", lambda _: next(tests))

            collect_input_output = collect_input(test[0], test[1])
            normalized_user_input = normalize_user_input(
                test[2][1],
                C.get_disallowed_dangerous_characters_regex(),
            )

            assert collect_input_output == normalized_user_input

    def test_confirm_additional_contribution_intent(self, capsys, monkeypatch):
        failing_tests = ["yess", "yers", "yeh", "nah", "nay", "noo"]
        passing_tests = [*C.CONFIRMATIONS]

        for test in failing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test)

            confirm_additional_contribution_intent(testing = True)
            
            # Prepare the stdout messages to assert against
            confirm_additional_contribution_stdout = f"{test!r} was not valid"
            test_stdout = capsys.readouterr().out
            
            assert f"{confirm_additional_contribution_stdout}" in f"{test_stdout}"

        for test in passing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test)
            
            if "y" in test:
                assert confirm_additional_contribution_intent()
            else:
                assert not confirm_additional_contribution_intent()

    def test_confirm_additional_debt_intent(self, capsys, monkeypatch):
        failing_tests = ["yess", "yers", "yeh", "nah", "nay", "noo"]
        passing_tests = [*C.CONFIRMATIONS]

        for test in failing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test)

            confirm_additional_debt_intent(testing = True)
            
            # Prepare the stdout messages to assert against
            confirm_additional_debt_intent_stdout = f"{test!r} was not valid"
            test_stdout = capsys.readouterr().out
            
            assert f"{confirm_additional_debt_intent_stdout}" in f"{test_stdout}"

        for test in passing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test)
            
            if "y" in test:
                assert confirm_additional_debt_intent()
            else:
                assert not confirm_additional_debt_intent()

    def test_confirm_additional_contribution_information(self, capsys, monkeypatch):
        additional_contribution_information = ("monthly", "$100.00")
        passing_tests = [*C.CONFIRMATIONS]

        for test in passing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test)

            confirm_additional_contribution_information(*additional_contribution_information)
            
            # Prepare the stdout messages to assert against
            confirm_additional_contribution_information_stdout = f"Frequency: {additional_contribution_information[0]}\nAmount: ${additional_contribution_information[1]}\n---------------------------------------\nDoes this information look correct?\n---------------------------------------\nIf 'NO', you'll be asked to enter the information again.\nIf 'YES', you'll move on to calculating your amortization schedule.\n"           
            test_stdout = capsys.readouterr().out
            
            assert f"{confirm_additional_contribution_information_stdout}" in f"{test_stdout}"

            if "y" in test:
                assert confirm_additional_contribution_information(*additional_contribution_information)

            else:
                assert not confirm_additional_contribution_information(*additional_contribution_information)

    def test_confirm_debt_information(self, capsys, monkeypatch):
        debt_information = ("10000.00", "12.5", "32000", "72")
        passing_tests = [*C.CONFIRMATIONS]

        for test in passing_tests:
            monkeypatch.setattr("builtins.input", lambda _: test)

            confirm_debt_information(*debt_information)
            
            # Prepare the stdout messages to assert against
            confirm_debt_information_stdout = f"Current balance: ${debt_information[0]}\nInterest rate: {debt_information[1]}%\nOriginal loan amount: ${debt_information[2]}\nTerm length: {debt_information[3]} months\n---------------------------------------\nDoes this information look correct?\n---------------------------------------\nIf 'NO', you'll be asked to enter the information again.\nIf 'YES', you'll move on to adding additional debts, if any.\n"           
            test_stdout = capsys.readouterr().out
            
            assert f"{confirm_debt_information_stdout}" in f"{test_stdout}"

            if "y" in test:
                assert confirm_additional_debt_intent()
            else:
                assert not confirm_additional_debt_intent()

    def test_format_currency(self):
        passing_tests = (
                [100, False, "100.00"],
                [100.00, False, "100.00"],
                [1200, False, "1,200.00"],
                [100.5, False, "100.50"],
        )

        for test in passing_tests:
            assert format_currency(test[0], test[1]) == test[2]

    def test_get_options(self):
        assert get_options("confirmation") == C.CONFIRMATIONS
        assert get_options("frequency") == C.FREQUENCIES
        assert get_options("unknown") == []

    def test_get_user_confirmation_comparison(self):
        false_tests = ["n", "N", "no", "NO", "No"]
        true_tests = ["y", "Y", "yes", "YES", "Yes"]

        for test in false_tests:
            assert not get_user_confirmation_comparison(
                normalize_user_input(test, C.get_disallowed_dangerous_characters_regex())
            )

        for test in true_tests:
            assert get_user_confirmation_comparison(
                normalize_user_input(test, C.get_disallowed_dangerous_characters_regex())
            )

    def test_is_float_positive(self):
        failing_tests = [-0.1, -2]
        passing_tests = [0.0, 1, 12.23]

        for test in failing_tests:
            assert not is_float_positive(test)

        for test in passing_tests:
            assert is_float_positive(test)

    def test_normalize_user_input(self):
        passing_tests = [
            ("frequency", "MONTHLY", "monthly"),
            ("frequency", "Monthly", "monthly"),
            ("frequency", "monthly", "monthly"),
            ("frequency", "Bi-Weekly", "bi-weekly"),
            ("numerical", "$100", "100"),
            ("numerical", "$10,000", "10000"),
            ("numerical", "10%", "10"),
            ("numerical", "55.5%", "55.5")
        ]

        for test in passing_tests:
            assert normalize_user_input(
                test[1], 
                C.get_disallowed_dangerous_characters_regex()
            ) == test[2]

    def test_strip_dangerous_characters_from_str(self):
        failing_tests = [
            0, 0.1, 0.01, 1, 1.1, 1.11, 11, 11.1, 11111.00, 1000000,
            { "a": 3 }, [1, 2, 3], (1, 2),
        ]
        passing_tests = [
            ("0", "0"),
			("0.1", "0.1"),
			("0.01", "0.01"),
			("1", "1"),
			("1.1", "1.1"),
			("1.11", "1.11"),
			("11", "11"),
			("11.1", "11.1"),
			("11,111.00", "11111.00"),
			("1,000,000", "1000000"),
			("$1.00", "1.00"),
			("$1", "1"),
            (";1", "1"),
            ("&&1", "1"),
            ("||1", "1"),
            ("|1", "1"),
            ("(1", "1"),
            (")1", "1"),
            ("`1", "1"),
            (">1", "1"),
            (">>1", "1"),
            ("<1", "1"),
            ("*1", "1"),
            ("?1", "1"),
            ("~1", "1"),
            ("$1", "1"),
            (",1", "1"),
            ("%1", "1"),
        ]

        for test in failing_tests:
            with pytest.raises(TypeError):
                strip_dangerous_characters_from_user_input(
                    C.get_disallowed_dangerous_characters_regex(),
                    test
                )

        for test in passing_tests:
            assert test[1] == strip_dangerous_characters_from_user_input(
                C.get_disallowed_dangerous_characters_regex(),
                test[0]
            )

    def test_validate_input(self):
        failling_tests = [
            ("confirmation", "yers"),
            ("confirmation", "yess"),
            ("confirmation", "nah"),
            ("confirmation", "nay"),
            ("frequency", "bimonthly"),
			("frequency", "biweekly"),
			("frequency", "tacos"),
			("frequency", "month"),
			("frequency", "week"),
			("frequency", "bi-month"),
			("frequency", "bi-week"),
			("frequency", "year"),
            ("frequency", "1234"),
            ("numerical", "a"), 
            ("numerical", "."),
        ]
        passing_tests = [
            ("frequency", "MONTHLY"),
            ("frequency", "Monthly"),
            ("frequency", "monthly"),
            ("frequency", "Bi-Weekly"),
            ("numerical", "$100"),
            ("numerical", "$10,000"),
            ("numerical", "10%"),
            ("numerical", "55.5%"),
            ("numerical", "0"),
            ("numerical", "0.1"),
			("numerical", "0.01"),
			("numerical", "1"),
			("numerical", "1.1"),
			("numerical", "1.11"),
			("numerical", "11"),
			("numerical", "11.1"),
			("numerical", "11"),
			("numerical", "111.00"),
			("numerical", "1,000,000"),
			("numerical", "$1.00"),
			("numerical", "$1"),
        ]

        for confirmation in C.CONFIRMATIONS:
            passing_tests.append(("confirmation", confirmation))

        for frequency in C.FREQUENCIES:
            passing_tests.append(("frequency", frequency))

        for test in failling_tests:
            normalized_user_input = normalize_user_input(test[1], C.get_disallowed_dangerous_characters_regex())
            pattern = None

            if test[0] == "frequency":
                pattern = C.FREQUENCIES
            else:
                pattern = C.CONFIRMATIONS

            assert not validate_input(test[0], normalized_user_input, pattern)

        for test in passing_tests:
            normalized_user_input = normalize_user_input(test[1], C.get_disallowed_dangerous_characters_regex())
            pattern = None

            if test[0] == "frequency":
                pattern = C.FREQUENCIES
            else:
                pattern = C.CONFIRMATIONS

            assert validate_input(test[0], normalized_user_input, pattern)

    def test_validate_input_option_in_options(self):
        failing_tests = ["yess", "yers", "nah", "nay"]
        passing_tests = C.CONFIRMATIONS

        for test in failing_tests:
            assert not validate_input_option_in_options(test, C.CONFIRMATIONS)

        for test in passing_tests:
            assert validate_input_option_in_options(test, C.CONFIRMATIONS)

    def test_validate_input_numerical(self):
        failing_tests = ["a", "!", "$", ".", ",", "%", "11,111.00", "1,000,000", "$1.00", "$1", "-12"]
        passing_tests = [
            0, 0.1, 0.01, 1, 1.1, 1.11, 11, 11.1, 11111.00, 1000000,
            "0", "0.1", "0.01", "1", "1.1", "1.11", "11", "11.1"
        ]

        for test in failing_tests:
            assert not validate_input_numerical(test)

        for test in passing_tests:
            assert validate_input_numerical(test)
