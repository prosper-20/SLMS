from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.models import Subject


class SubjectHomePage(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailPage(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


