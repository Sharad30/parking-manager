import pytest
from parkingmanager import ParkingLot


def test_parking_spots_with_sq_footage_int():
    parking_lot = ParkingLot(sq_footage=2000)
    assert len(parking_lot.parking_spots) == 20


def test_parking_spots_with_sq_footage_tuple():
    parking_lot = ParkingLot(sq_footage=(200, 10))
    assert len(parking_lot.parking_spots) == 20
