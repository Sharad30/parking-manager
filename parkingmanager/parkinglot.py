from typing import List, Optional, Union, Tuple

from pydantic import BaseModel


class ParkingLot(BaseModel):
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
        vehicle_spot_map = {}
        for i, license_no in enumerate(self.parking_spots):
            vehicle_spot_map[license_no] = i
        return vehicle_spot_map
