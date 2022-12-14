import random

import pytest

from parkingmanager import ParkingLot
from parkingmanager.park_utils import create_cars, random_park


@pytest.fixture
def cars_config():
    cars_config = {}
    for no_of_cars in [1, 3, 16, 23, 100]:
        cars = create_cars(no_of_cars=no_of_cars)
        cars_config[f"car{no_of_cars}"] = cars
    return cars_config


def test_parking_single(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    spot_no = random.randint(0, len(parking_lot.parking_spots) - 1)
    assert car.park(parking_lot, spot_no)["status"] == "Car parked"


def test_parking_multiple(cars_config):
    cars = cars_config["car3"]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    car_parking_status, _ = random_park(cars=cars, parking_lot=parking_lot)
    assert sum([1 if status == "Car parked" else 0 for status in car_parking_status]) == 3


def test_parking_multiple_full(cars_config):
    cars = cars_config["car23"]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    car_parking_status, not_parked_cars = random_park(cars=cars, parking_lot=parking_lot)
    assert (car_parking_status.count("Car parked") == 20) and (len(not_parked_cars) == 3)


def test_negative_parking_spot_no(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    response = car.park(parking_lot, spot_no=-1)
    assert response["status"] == "Car not parked" and response["error"] == "InvalidSpotNumberError"


def test_greater_than_capacity_parking_spot_no(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    response = car.park(parking_lot, spot_no=100)
    assert response["status"] == "Car not parked" and response["error"] == "ParkingCapacityExceededError"


def test_already_parked_parking_spot_no(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    parking_lot.parking_spots[0] = 1
    response = car.park(parking_lot, spot_no=0)
    assert response["status"] == "Car not parked" and response["error"] == "SpotNotAvailableError"


def test_parking_single_custom_sq_footage(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    spot_no = random.randint(0, len(parking_lot.parking_spots) - 1)
    assert car.park(parking_lot, spot_no)["status"] == "Car parked"


def test_parking_multiple_custom_sq_footage(cars_config):
    cars = cars_config["car3"]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    car_parking_status, _ = random_park(cars=cars, parking_lot=parking_lot)
    assert sum([1 if status == "Car parked" else 0 for status in car_parking_status]) == 3


def test_parking_multiple_full_custom_sq_footage(cars_config):
    cars = cars_config["car100"]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    car_parking_status, not_parked_cars = random_park(cars=cars, parking_lot=parking_lot)
    assert (car_parking_status.count("Car parked") == 52) and (len(not_parked_cars) == 48)


def test_negative_parking_spot_no_custom_sq_footage(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    response = car.park(parking_lot, spot_no=-1)
    assert response["status"] == "Car not parked" and response["error"] == "InvalidSpotNumberError"


def test_greater_than_capacity_parking_spot_no_custom_sq_footage(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    response = car.park(parking_lot, spot_no=100)
    assert response["status"] == "Car not parked" and response["error"] == "ParkingCapacityExceededError"


def test_already_parked_parking_spot_no_custom_sq_footage(cars_config):
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    parking_lot.parking_spots[0] = 1
    response = car.park(parking_lot, spot_no=0)
    assert response["status"] == "Car not parked" and response["error"] == "SpotNotAvailableError"


def test_park_randomly_unique_spot_for_each_car23(cars_config):
    cars = cars_config["car23"]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    _, _ = random_park(cars=cars, parking_lot=parking_lot)
    unique_parked_spots = set(parking_lot.vehicle_spot_mapping.values())
    assert len(unique_parked_spots) == 20


def test_park_randomly_unique_spot_for_each_car100_sq_footage_500(cars_config):
    cars = cars_config["car100"]
    parking_lot = ParkingLot(sq_footage=(500, 10))
    _, _ = random_park(cars=cars, parking_lot=parking_lot)
    unique_parked_spots = set(parking_lot.vehicle_spot_mapping.values())
    assert len(unique_parked_spots) == 52
