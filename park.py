import json
import random
import string
from pathlib import Path
from typing import Union

from parkingmanager import Car, ParkingLot, upload_file_to_s3
from parkingmanager.park_utils import create_cars, random_park


def cars_park(no_of_cars: int):
    cars = create_cars(no_of_cars=no_of_cars)
    parking_lot = ParkingLot(sq_footage=(200, 10))
    _, not_parked_cars = random_park(cars=cars, parking_lot=parking_lot)
    print(f"Cars not parked due to full parking: {not_parked_cars}")
    return parking_lot


def save_vehicle_parking_details(filepath: Union[Path, str], parking_lot: ParkingLot):
    vehicle_spot_map = parking_lot.map_vehicle_spot()
    vehicle_spot_map = json.dumps(vehicle_spot_map, indent=4)
    with open(filepath, "w") as outfile:
        outfile.write(vehicle_spot_map)
    print(f"File {filepath} saved successfully")


if __name__ == "__main__":
    parking_lot = cars_park(no_of_cars=23)
    root_dir = Path("output")
    filename = "parking_details.json"
    filepath = root_dir / filename
    save_vehicle_parking_details(filepath=filepath, parking_lot=parking_lot)
    upload_file_to_s3(file_name=str(root_dir / filename), bucket="parking-manager")
