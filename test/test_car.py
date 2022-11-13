from parkingmanager import Car


def test_car_license_plate_property():
    car = Car(license_no="ABC-123")
    assert car.license_no == "ABC-123"


def test_car_str():
    car = Car(license_no="ABC-123")
    assert str(car) == "ABC-123"
