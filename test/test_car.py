from parkingmanager import Car


def test_car_license_plate_property():
    car = Car(license_no="ABC-123")
    assert car.license_plate == "ABC-123"


def test_car_repr():
    car = Car(license_no="ABC-123")
    assert repr(car) == "ABC-123"


def test_car_str():
    car = Car(license_no="ABC-123")
    assert str(car) == "Car with license plate ABC-123"
