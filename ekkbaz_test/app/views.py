from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from datetime import datetime

class RegisterView(APIView):

    authentication_classes, permission_classes = [], []

    """
    POST: Create a user with specific username, email, and password
    """
    def post(self, request, format=None):
        username, email, password = request.data.get('username'), request.data.get('email'), request.data.get('password')
        if username is None or email is None or password is None:
            return Response({"error": "Invalid information!"})
        user = User.objects.create_user(username, email, password)
        return Response({"output": "User created successfully!"})
    
    
class BusinessView(APIView):

    """
    GET: List all the business data of businesses that are within 2000 km
    """
    def get(self, request, format=None):
        businesses = BusinessData().getBusinesses()
        return Response({'businesses': businesses})
    