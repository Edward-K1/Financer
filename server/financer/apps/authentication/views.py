from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User

# Create your views here.
class RegisterCustomer(CreateAPIView):
    """
    Enable registration of `Customers`
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
