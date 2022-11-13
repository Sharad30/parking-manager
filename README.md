# parking-manager

## Getting Started

1. Clone the repository

2. Install system packages
```
sudo apt install -y curl git python-dev gcc make gdb lcov libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev libncurses5-dev libreadline6-dev libsqlite3-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev libpq-dev
```

3. Install `asdf`
```
git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.10.2
cd
echo '. $HOME/.asdf/asdf.sh' >> .bashrc
echo '. $HOME/.asdf/completions/asdf.bash' >> .bashrc
```

4. Install `python3.9.6`
```
asdf plugin-add python
asdf install python 3.9.6
asdf global python 3.9.6
asdf reshim
```

5. Install poetry.
```
pip install poetry
asdf reshim
```

6. Install all dependencies: `poetry install`
7. [**Optional**] Integrating commitizen with pre-commit: `poetry run pre-commit install --hook-type commit-msg`

## Run main program
```
poetry run python park.py
```
The above command will do the following:
1. Create a list of `Car` objects with random `license_no`.
    ```
    cars = create_cars(no_of_cars=23)
    ```
2. Park cars in random parking spots.
    ```
    parking_lot = cars_park(cars=cars)
    ```
3. Save JSON object having vehicle, parking spot mapping.
    ```
    parking_lot.map_vehicle_spot(filepath=filepath)
    ```
4. Upload the JSON object file to S3 bucket (Make sure you have `aws cli` setup in your machine and configured to your `AWS` account with your credentials).
    ```
    upload_file_to_s3(file_name=str(root_dir / filename), bucket="parking-manager")
    ```

## Run tests
```
poetry run pytest test
```

## Error Codes

1. `NotAValidLicenseNoError`: Raised when `license_no` not equal to 7 digits.

2. `InvalidSpotNumberError`: Raised when `spot_no` < 0.
    ```
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    response = car.park(parking_lot, spot_no=-1)
    ```
        
3. `ParkingCapacityExceededError`: Raised when `spot_no` > `parking_capacity`.
    ```
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    response = car.park(parking_lot, spot_no=1000)
    ```

4. `SpotNotAvailableError`: Raised when the `spot_no` chosen already has a car parked in it.
    ```
    car = cars_config["car1"][0]
    parking_lot = ParkingLot(sq_footage=(200, 10))
    parking_lot.parking_spots[0] = 1
    response = car.park(parking_lot, spot_no=0)
    ```