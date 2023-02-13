from main import validate_amount_payment, define_amount_hour, get_amount_hour, read_data_file
from constant.days_info import list_days
import pytest


def test_validate_valid_line():
    assert validate_amount_payment(
        "THOMAS=MO08:00-12:00,TU10:00-13:00,TH01:00-04:00,SA14:00-18:00,SU20:00-23:00",
        define_amount_hour(list_days), 1) == "The amount to pay : THOMAS is 345"


def test_validate_invalide_line():
    assert validate_amount_payment(
        "INVALID LINE",
        define_amount_hour(list_days), 1) == "The line number 1 is not valid for process"


@pytest.mark.parametrize(
    "info_payment, hour_amount, line, expected",
    [
        (
            "THOMAS=MO08:00-12:00,TU10:00-13:00,TH01:00-04:00,SA14:00-18:00,SU20:00-23:00",
            define_amount_hour(list_days),
            1,
            "The amount to pay : THOMAS is 345"
        ),
        (
            "INVALID LINE",
            define_amount_hour(list_days),
            1,
            "The line number 1 is not valid for process"
        ),
        (
            "JHON=MO10:00-12:00,TH12:00-14:00,FR07:00-11:00,SU20:00-21:00",
            define_amount_hour(list_days),
            1,
            "The amount to pay : JHON is 165"
        ),
        (
            "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00",
            define_amount_hour(list_days),
            1,
            "The amount to pay : RENE is 215"
        ),
        (
                "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
                define_amount_hour(list_days),
                1,
                "The amount to pay : ASTRID is 85"
        )
    ]
)
def test_validate_valid_multiple_line(info_payment, hour_amount, line, expected):
    assert validate_amount_payment(info_payment, hour_amount, line) == expected


def test_get_amount_hour_fail_attribute_error():
    assert get_amount_hour(None, None, None) == "Invalid values for defined amounts"


def test_open_file_success():
    result, _ = read_data_file('files/data.txt')
    assert result is True


def test_open_file_file_not_exists():
    result, _ = read_data_file('../files/data.txt')
    assert result is False