import hashlib

from panther.exceptions import AuthenticationException
from pydantic import BaseModel, Field, field_validator

from app.exceptions import UsernameAlreadyExists
from app.models import User


class SignupSerializer(BaseModel):
    username: str
    password: str = Field(min_length=4, max_length=8)

    @field_validator('username')
    def check_username(cls, username):
        if User.find_one(username=username):
            raise UsernameAlreadyExists
        return username

    @field_validator('password')
    def encrypt_password(cls, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()


class LoginSerializer(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def find_user(cls, username):
        if user := User.find_one(username=username):
            cls.user  = user
            return username
        raise AuthenticationException

    @field_validator('password')
    def check_password(cls, password):
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if cls.user.password != new_password:
            raise AuthenticationException
        return password


class ProfileSerializer(BaseModel):
    first_name: str
    last_name: str
    username: str


class UpdateProfileSerializer(BaseModel):
    first_name: str = None
    last_name: str = None
