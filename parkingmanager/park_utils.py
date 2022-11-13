import random
import string
from .car import Car


def create_cars(no_of_cars: int):
    cars = []
    for _ in range(0, no_of_cars):
        random_license_no = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))
        cars.append(Car(license_no=random_license_no))
    return cars


def random_park(cars, parking_lot):
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
