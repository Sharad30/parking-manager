import random
import string
from .car import Car
from typing import List
from .parkinglot import ParkingLot


def create_cars(no_of_cars: int):
    """This method creates cars with random license numbers
    Args:
        no_of_cars (int): The number of cars to be created

    Returns:
        List[Car]: A list of cars
    """
    cars = []
    for _ in range(0, no_of_cars):
        random_license_no = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
        cars.append(Car(license_no=random_license_no))
    return cars


def random_park(cars: List[Car], parking_lot: ParkingLot):
    """This method parks the cars in the parking lot randomly
    Args:
        cars (List[Car]): The list of cars
        parking_lot (ParkingLot): The parking lot object

    Returns:
        list: A list containing the parking status.
        list: A list containing license number of non parked cars.
    """
    car_parking_status = []
    not_parked_cars = []
    for car in cars:
        parking_status = "Car not parked"
        total_occupied_spots = sum([1 if status == "Car parked" else 0 for status in car_parking_status])
        parking_full_condition = total_occupied_spots == parking_lot.parking_capacity
        if not parking_full_condition:
            while parking_status == "Car not parked":
                spot_no = random.randint(0, parking_lot.parking_capacity - 1)
                parking_status = car.park(parking_lot, spot_no)["status"]
        else:
            not_parked_cars.append(str(car))
        car_parking_status.append(parking_status)
    return car_parking_status, not_parked_cars
