from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from authentication.serializer import UserSerializer


class CreateUserView(viewsets.ModelViewSet):
    queryset = ""
    serializer_class = UserSerializer
