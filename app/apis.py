from app.models import User
from app.serializers import SignupSerializer, LoginSerializer, ProfileSerializer, UpdateProfileSerializer

from panther import status
from panther.app import GenericAPI
from panther.request import Request
from panther.response import Response
from panther.authentications import JWTAuthentication


class SignupAPI(GenericAPI):
    input_model = SignupSerializer

    def post(self, request: Request):
        payload: SignupSerializer = request.validated_data
        user = User.insert_one(username=payload.username, password=payload.password)
        token = JWTAuthentication.login(user_id=user.id)
        return Response(data={'access_token': token}, status_code=status.HTTP_201_CREATED)


class LoginAPI(GenericAPI):
    input_model = LoginSerializer

    def post(self, request: Request):
        payload: SignupSerializer = request.validated_data
        token = JWTAuthentication.login(user_id=payload.user.id)
        return Response(data={'access_token': token}, status_code=status.HTTP_200_OK)


class ProfileAPI(GenericAPI):
    auth = True
    input_model = UpdateProfileSerializer
    output_model = ProfileSerializer

    def get(self, request: Request):
        return Response(data=request.user, status_code=status.HTTP_200_OK)

    def put(self, request: Request):
        payload: UpdateProfileSerializer = request.validated_data
        request.user.update(
            first_name=payload.first_name or request.user.first_name,
            last_name=payload.last_name or request.user.last_name,
        )
        return Response(data=request.user, status_code=status.HTTP_200_OK)
