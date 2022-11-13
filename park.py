import json
import random
import string
from pathlib import Path
from typing import Union, List

from parkingmanager import Car, ParkingLot, upload_file_to_s3
from parkingmanager.park_utils import create_cars, random_park


def cars_park(cars: List[Car]):
    """This method parks the cars in the parking lot randomly
    Args:
        cars (List[Car]): The list of cars

    Returns:
        ParkingLot: The parking lot object
    """
    parking_lot = ParkingLot(sq_footage=(200, 10))
    car_parking_status, not_parked_cars = random_park(cars=cars, parking_lot=parking_lot)
    print("----------------------------------------------------------------")
    print(f"Parking size: {parking_lot.sq_footage} sq.ft")
    print(f"Parking capacity: {parking_lot.parking_capacity}")
    print("----------------------------------------------------------------")
    print(f"Total cars to park: {len(cars)}")
    print(f"Total cars parked: {car_parking_status.count('Car parked')}")
    print(f"Total cars not parked due to full parking: {len(not_parked_cars)}")
    return parking_lot


if __name__ == "__main__":
    cars = create_cars(no_of_cars=23)
    parking_lot = cars_park(cars=cars)
    print("----------------------------------------------------------------")
    root_dir = Path("output")
    root_dir.mkdir(exist_ok=True)
    filename = "parking_details.json"
    filepath = root_dir / filename
    parking_lot.map_vehicle_spot(filepath=filepath)
    print("----------------------------------------------------------------")
    upload_file_to_s3(file_name=str(root_dir / filename), bucket="parking-manager")
