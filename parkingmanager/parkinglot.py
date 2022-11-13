import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from pydantic import BaseModel
from rich.pretty import pprint


class ParkingLot(BaseModel):
    """This class manages parking related operations

    Attributes:
        sq_footage Union[int, Tuple[int, int]]: The parking lot size in sq.ft or (length, breadth) in feet.
        parking_spots (List[int]): The parking spots of the parking lot containing parking status of each car with `1` as `Car is parked` and `0` as `Car is not parked`.
        vehicle_spot_mapping (Dict[str, int]): The mapping of vehicle to spot number
    """

    sq_footage: Union[int, Tuple[int, int]]
    parking_spots: Optional[List[int]]
    vehicle_spot_mapping: Dict[str, int] = dict()

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
        parking_capacity = self.sq_footage // parking_spot_size
        self.parking_spots = [0] * parking_capacity

    def map_vehicle_spot(self, filepath: Union[str, Path]):
        """This method maps the vehicle to the spot number

        Returns:
            dict: A dictionary containing the vehicle and spot number
        """
        vehicle_spot_mapping = json.dumps(self.dict()["vehicle_spot_mapping"], indent=4)
        with open(filepath, "w") as outfile:
            outfile.write(vehicle_spot_mapping)
        pprint(f"File {filepath} saved successfully")
