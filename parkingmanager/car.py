from pydantic import BaseModel, validator

from .parkinglot import ParkingLot
from .custom_errors import (
    NotAValidLicenseNoError,
    InvalidSpotNumberError,
    ParkingCapacityExceededError,
    SpotNotAvailableError,
)


class Car(BaseModel):
    """This class manages car related operations

    Attributes:
        license_no (str): The license number of car
    """

    license_no: str

    @validator("license_no")
    def value_must_equal_bar(cls, license_no):
        if len(license_no) != 7:
            raise NotAValidLicenseNoError(wrong_value=license_no)
        return license_no

    def __str__(self):
        return self.license_no

    def park(self, parking_lot: ParkingLot, spot_no: int):
        """This method parks the car in the parking lot

        Args:
            parking_lot (ParkingLot): The parking lot object
            spot_no (int): The spot number to park the car

        Returns:
            dict: A dictionary containing the parking `status`  and `error` if any.
        """
        if spot_no >= parking_lot.parking_capacity:
            try:
                raise (ParkingCapacityExceededError())
            except ParkingCapacityExceededError as error:
                return {"status": "Car not parked", "error": error.error_type}
        elif spot_no < 0:
            try:
                raise (InvalidSpotNumberError())
            except InvalidSpotNumberError as error:
                return {"status": "Car not parked", "error": error.error_type}
        elif parking_lot.parking_spots[spot_no] == 1:
            print(f"Car with license plate {self.license_no} not parked in spot {spot_no}")
            try:
                raise (SpotNotAvailableError())
            except SpotNotAvailableError as error:
                return {"status": "Car not parked", "error": error.error_type}
        else:
            print(f"Car with license plate {self.license_no} parked successfully in spot {spot_no}")
            parking_lot.parking_spots[spot_no] = self.license_no
            return {"status": "Car parked", "error": ""}
