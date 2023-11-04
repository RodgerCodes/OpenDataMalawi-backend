from rest_framework import serializers
from .models import FileFormat, Field, Dataset


class FileFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileFormat
        fields = "__all__"


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = "__all__"
