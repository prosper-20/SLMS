from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView


class RegisterView(APIView):
    def post(self, request, format=None):
        user = UserRegistrationSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response({
        "email": user.data['email'],
        
        
}, status=status.HTTP_201_CREATED)

