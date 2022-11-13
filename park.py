import json
import random
import string
from pathlib import Path
from typing import Union

from parkingmanager import Car, ParkingLot, upload_file_to_s3


def cars_park(no_of_cars: int):
    cars = []
    for _ in range(0, no_of_cars):
        random_license_no = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=7)
        )
        cars.append(Car(license_no=random_license_no))
    parking_lot = ParkingLot(sq_footage=(200, 10))
    car_parking_status = []
    not_parked_cars = []
    for car in cars:
        parking_status = "Car not parked"
        total_occupied_spots = sum(
            [1 if status == "Car parked" else 0 for status in car_parking_status]
        )
        parking_full_condition = total_occupied_spots == parking_lot.parking_capacity
        if not parking_full_condition:
            while parking_status == "Car not parked":
                spot_no = random.randint(0, parking_lot.parking_capacity - 1)
                parking_status = car.park(parking_lot, spot_no)
        else:
            not_parked_cars.append(car)
        car_parking_status.append(parking_status)
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
