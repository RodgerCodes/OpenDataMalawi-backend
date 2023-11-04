from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Dataset, Field, FileFormat
from .serializer import DataSetSerializer, FieldSerializer, FileFormatSerializer


class GetFileFormat(generics.ListAPIView):
    """
    Get file formats
    """

    model = FileFormat
    serializer_class = FileFormatSerializer
    queryset = FileFormat.objects.all()


class GetFields(generics.ListAPIView):
    """
    Get datasets fields or categories
    """

    model = Field
    serializer_class = FieldSerializer
    queryset = Field.objects.all()
