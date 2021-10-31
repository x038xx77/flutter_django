from django.shortcuts import redirect, render
import datetime
from django.contrib.auth.tokens import default_token_generator
from django.urls.base import reverse_lazy
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status, views

from rest_framework import status, views, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import email_user, is_auth_path
from rest_framework.views import APIView
from .serializers import UserSerializer


from django.contrib.auth import get_user_model

User = get_user_model()


class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser] # IsAdminUser, IsAuthenticated, AllowAny -all

    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
