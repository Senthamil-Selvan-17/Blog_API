from django.shortcuts import render
from .serializers import SignupSerializer
from rest_framework import generics
from django.contrib.auth.models import User

# Create your views here.
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
