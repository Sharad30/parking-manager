from parkingmanager import Car
from pydantic import ValidationError
from parkingmanager.custom_errors import NotAValidLicenseNoError


def test_car_license_number():
    car = Car(license_no="ABC-123")
    assert car.license_no == "ABC-123"


def test_car_str():
    car = Car(license_no="ABC-123")
    assert str(car) == "ABC-123"


def test_car_invalid_license_no():
    try:
        car = Car(license_no="ABC-1231")
    except ValidationError as e:
        assert e.errors()[0]["type"] == "value_error.not_a_valid_license_no"
