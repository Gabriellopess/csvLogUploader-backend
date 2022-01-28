from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from csvFiles.models import CsvFiles
from csvFiles.serializer import CsvFilesSerializer
from rest_framework.views import APIView

from django.views.generic.edit import CreateView


# Create your views here.

class CsvFilesList(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = []

    queryset = CsvFiles.objects.all()
    serializer_class = CsvFilesSerializer


class CsvFilesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    queryset = CsvFiles.objects.all()
    serializer_class = CsvFilesSerializer
