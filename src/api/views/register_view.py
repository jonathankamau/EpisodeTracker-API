"""User Registration View."""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from api.models import UserProfile
from api.serializers import UserSerializer


class RegisterUser(viewsets.ViewSet):
    """
    Endpoint to register a user.
    """

    queryset = UserProfile.objects.all()

    def create(self, request):
        """
        Registration endpoint
        """
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
