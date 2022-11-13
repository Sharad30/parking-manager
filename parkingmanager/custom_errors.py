from pydantic import PydanticValueError


class NotAValidLicenseNoError(PydanticValueError):
    code = "not_a_valid_license_no"
    msg_template = 'value is not a 7 digit license number, got "{wrong_value}"'


class InvalidSpotError(Exception):
    def __init__(self):
        self.error_type = self.__class__.__name__

    def __str__(self):
        return self.error_type


class SpotNotAvailableError(Exception):
    def __init__(self):
        self.error_type = self.__class__.__name__

    def __str__(self):
        return self.error_type
