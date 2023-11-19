from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from Data_Library.services import AddDataSetService

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


class AddDataSet(APIView):
    """
    View for adding dataset
    """

    serializer = DataSetSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        instance = AddDataSetService(request.data).add_dataset()
        return Response(instance, status=instance["status"])
