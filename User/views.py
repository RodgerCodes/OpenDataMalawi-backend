from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializer import UserSerializer


class RegisterAccount(APIView):
    """
    View for registering a new user
    """

    def post(self, request):
        try:
            user = User.objects.get(email=request.data["email"])
        except User.DoesNotExist:
            user = None

        if user is not None:
            return Response(
                {"message": "User with that account already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": " Your open data account has been successfully created"},
            status=status.HTTP_201_CREATED,
        )


# TODO add login route


class GetUserDetails(generics.RetrieveAPIView):
    """
    View for getting logged in user details
    """

    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class EditUserDetails(APIView):
    """
    View for editing user details
    """

    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        userInstance = User.objects.get(id=user.id)
        serializer = UserSerializer(
            instance=userInstance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Updated user details"}, status=status.HTTP_200_OK)
