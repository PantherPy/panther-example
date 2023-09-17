from panther import status
from panther.exceptions import APIException


class UsernameAlreadyExists(APIException):
    detail = 'Username Already Exists'
    status_code = status.HTTP_400_BAD_REQUEST
