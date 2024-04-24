from unittest.mock import patch

from project import check_option, is_number, validate_date


def test_check_option():
    assert check_option("1") == 1
    assert check_option("5") == 5
    assert check_option("6") == 6
    assert check_option("0") == "Invalid number"
    assert check_option("8") == "Invalid number"
    assert check_option("50") == "Invalid number"
    assert check_option("5.5") == "Invalid option"
    assert check_option("-50") == "Invalid option"
    assert check_option("cat") == "Invalid option"
    assert check_option("Person") == "Invalid option"
    assert check_option("PERSON") == "Invalid option"
    assert check_option("Person-") == "Invalid option"


def test_is_number():
    assert is_number("5") == True
    assert is_number("10.50") == True
    assert is_number("dog") == False
    assert is_number("CAT") == False
    assert is_number("Dog10") == False


def test_validate_date():
    assert validate_date("1988-09-07") == True
    assert validate_date("1950-10-22") == True
    assert validate_date("1988/09/07") == False
    assert validate_date("1950/10/22") == False
