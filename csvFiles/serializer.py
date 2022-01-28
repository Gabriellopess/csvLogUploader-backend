from rest_framework import serializers
from django.db import models
from csvFiles.models import CsvFiles

class CsvFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvFiles
        fields = '__all__'