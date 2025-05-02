# Packages
import pytest
# Modules
from input import convert_to_float, convert_to_str, normalize_user_input, strip_characters_from_str, validate_input, validate_input_frequency, validate_input_numerical
# Constants
from constants import Constants

C = Constants()

class TestValidateInput:
    def test_convert_to_float(self):
        failing_tests = ["a", "!", "$", ".", ",", "%"]
        passing_tests = [
            0, 0.1, 0.01, 1, 1.1, 1.11, 11, 11.1, 11111.00, 1000000,
            "0", "0.1", "0.01", "1", "1.1", "1.11", "11", "11.1", "11,111.00", "1,000,000", "$1.00", "$1"
        ]

        for test in failing_tests:
            with pytest.raises(ValueError):
                convert_to_float(test) 

        for test in passing_tests:
            str_input = convert_to_str(test)
            cleaned_input = strip_characters_from_str(str_input, C.NUMERICAL_CHARACTERS)
            print(cleaned_input)
            assert float(cleaned_input) == convert_to_float(test)

    def test_convert_to_str(self):
        # NOTE: for casting to str to fail, you need a custom __str__
        # function in a class, because pretty much everything casts to str
        passing_tests = [
            (0, "0"),
            (100, "100"),
            (100.00, "100.0"),
            (-5, "-5"),
            ([1, 2], "[1, 2]"),
            ({ "A": 1 }, "{'A': 1}"),
            ("1", "1"),
            ("1,333", "1,333")
        ]

        for test in passing_tests:
            assert test[1] == convert_to_str(test[0])

    def test_normalize_user_input(self):
        passing_tests = [
            ("frequency", "MONTHLY", "monthly"),
            ("frequency", "Monthly", "monthly"),
            ("frequency", "monthly", "monthly"),
            ("frequency", "Bi-Weekly", "bi-weekly"),
            ("numerical", "$100", "100"),
            ("numerical", "$10,000", "10000"),
            ("numerical", "10%", "0.1"),
            ("numerical", "55.5%", "0.555")
        ]

        for test in passing_tests:
            assert normalize_user_input(test[0], test[1]) == test[2]

    def test_strip_characters_from_str(self):
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
			("$1", "1")
        ]

        for test in failing_tests:
            with pytest.raises(TypeError):
                strip_characters_from_str(test, C.NUMERICAL_CHARACTERS)

        for test in passing_tests:
            assert test[1] == strip_characters_from_str(test[0], C.NUMERICAL_CHARACTERS)

    def test_validate_input(self):
        failling_tests = [
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
            # ("numerical", "!"),
            # ("numerical", "$"),
            ("numerical", "."),
            # ("numerical", ","),
            # ("numerical", "%")
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

        for frequency in C.FREQUENCIES:
            passing_tests.append(("frequency", frequency))

        for test in failling_tests:
            normalized_user_input = normalize_user_input(test[0], test[1])
            assert not validate_input(test[0], normalized_user_input)

        for test in passing_tests:
            normalized_user_input = normalize_user_input(test[0], test[1])
            assert validate_input(test[0], normalized_user_input)

    def test_validate_input_frequency(self):
        failing_tests = ["bimonthly", "biweekly", "tacos", "month", "week", "bi-month", "bi-week", "year"]
        passing_tests = C.FREQUENCIES

        for test in failing_tests:
            assert not validate_input_frequency(test)

        for test in passing_tests:
            assert validate_input_frequency(test)

    def test_validate_input_numerical(self):
        failing_tests = ["a", "!", "$", ".", ",", "%"]
        passing_tests = [
            0, 0.1, 0.01, 1, 1.1, 1.11, 11, 11.1, 11111.00, 1000000,
            "0", "0.1", "0.01", "1", "1.1", "1.11", "11", "11.1", "11,111.00", "1,000,000", "$1.00", "$1"
        ]

        for test in failing_tests:
            assert not validate_input_numerical(test)

        for test in passing_tests:
            assert validate_input_numerical(test)

