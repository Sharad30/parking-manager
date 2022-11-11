from pydantic import BaseModel
from typing import Union, List, Optional


class ParkingLot(BaseModel):
    sq_footage: Union[int, tuple]
    parking_spots: Optional[List[int]]

    def __init__(
        self,
        sq_footage: Union[int, tuple],
        parking_spot_size: Union[int, tuple] = (8, 12),
    ):
        super().__init__(sq_footage=sq_footage)
        if isinstance(parking_spot_size, tuple):
            parking_spot_size = parking_spot_size[0] * parking_spot_size[1]
        if isinstance(sq_footage, tuple):
            self.sq_footage = sq_footage[0] * sq_footage[1]
        no_of_cars_parked = self.sq_footage // parking_spot_size
        self.parking_spots = [0] * no_of_cars_parked
