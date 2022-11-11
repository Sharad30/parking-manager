from parkingmanager import ParkingLot
from parkingmanager import Car
import random
import string


def test_parking_single():
    car = Car(license_no="ABC-123")
    parking_lot = ParkingLot(sq_footage=(200, 10))
    spot_no = random.randint(0, parking_lot.parking_capacity - 1)
    assert car.park(parking_lot, spot_no) == "Car parked"


def test_parking_multiple():
    cars = []
    no_of_cars = 3
    for _ in range(0, no_of_cars):
        random_license_no = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
        cars.append(Car(license_no=random_license_no))
    parking_lot = ParkingLot(sq_footage=(200, 10))
    car_parking_status = []
    for car in cars:
        parking_status = "Car not parked"
        while parking_status == "Car not parked":
            spot_no = random.randint(0, parking_lot.parking_capacity - 1)
            parking_status = car.park(parking_lot, spot_no)
        car_parking_status.append(parking_status)
    assert sum([1 if status == "Car parked" else 0 for status in car_parking_status]) == 3


def test_parking_multiple_full():
    cars = []
    no_of_cars = 23
    for _ in range(0, no_of_cars):
        random_license_no = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
        cars.append(Car(license_no=random_license_no))
    parking_lot = ParkingLot(sq_footage=(200, 10))
    car_parking_status = []
    not_parked_cars = []
    for car in cars:
        parking_status = "Car not parked"
        total_occupied_spots = sum([1 if status == "Car parked" else 0 for status in car_parking_status])
        parking_full_condition = total_occupied_spots == parking_lot.parking_capacity
        if not parking_full_condition:
            while parking_status == "Car not parked":
                spot_no = random.randint(0, parking_lot.parking_capacity - 1)
                parking_status = car.park(parking_lot, spot_no)
        else:
            not_parked_cars.append(car)
        car_parking_status.append(parking_status)
    assert (total_occupied_spots == no_of_cars - 3) and (len(not_parked_cars) == 3)
