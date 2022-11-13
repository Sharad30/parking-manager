from typing import List, Optional, Union, Tuple

from pydantic import BaseModel


class ParkingLot(BaseModel):
    """This class manages parking related operations

    Attributes:
        sq_footage Union[int, Tuple[int, int]]: The parking lot size in sq.ft or (length, breadth) in feet.
        parking_capacity (int): The parking capacity of the parking lot.
        parking_spots (List[int]): The parking spots of the parking lot containing parking status of each car with `1` as `Car is parked` and `0` as `Car is not parked`.
    """

    sq_footage: Union[int, Tuple[int, int]]
    parking_capacity: Optional[int]
    parking_spots: Optional[List[str]]

    def __init__(
        self,
        sq_footage: Union[int, Tuple[int, int]],
        parking_spot_size: Union[int, Tuple[int, int]] = (8, 12),
    ):
        super().__init__(sq_footage=sq_footage)
        if isinstance(parking_spot_size, tuple):
            parking_spot_size = parking_spot_size[0] * parking_spot_size[1]
        if isinstance(sq_footage, tuple):
            self.sq_footage = sq_footage[0] * sq_footage[1]
        self.parking_capacity = self.sq_footage // parking_spot_size
        self.parking_spots = [0] * self.parking_capacity

    def map_vehicle_spot(self):
        """This method maps the vehicle to the spot number

        Returns:
            dict: A dictionary containing the vehicle and spot number
        """
        vehicle_spot_map = {}
        for i, license_no in enumerate(self.parking_spots):
            vehicle_spot_map[license_no] = i
        return vehicle_spot_map
