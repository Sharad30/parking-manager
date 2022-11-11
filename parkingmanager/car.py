from pydantic import BaseModel, PydanticValueError, validator

from .parkinglot import ParkingLot


class NotAValidLicenseNoError(PydanticValueError):
    code = "not_a_valid_license_no"
    msg_template = 'value is not a 7 digit license number, got "{wrong_value}"'


class Car(BaseModel):
    license_no: str

    @validator("license_no")
    def value_must_equal_bar(cls, license_no):
        if len(license_no) != 7:
            raise NotAValidLicenseNoError(wrong_value=license_no)
        return license_no

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def __repr__(self):
        return self.license_plate

    @property
    def license_plate(self):
        return self.license_no

    def park(self, parking_lot: ParkingLot, spot_no: int):
        if parking_lot.parking_spots[spot_no]:
            print(f"Car with license plate {self.license_plate} not parked in spot {spot_no}")
            return "Car not parked"
        else:
            print(f"Car with license plate {self.license_plate} parked successfully in spot {spot_no}")
            parking_lot.parking_spots[spot_no] = 1
            return "Car parked"
